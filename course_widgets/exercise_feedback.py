"""Retroalimentación persistente para ejercicios escritos en celdas de Marimo.

Los criterios viven fuera del notebook. Cada celda editable solo necesita terminar
con ``feedback.exercise("id", locals())`` para evaluar su estado y mostrar el coach.
"""

from __future__ import annotations

import re
import tomllib
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from importlib.machinery import SourcelessFileLoader
from importlib.util import module_from_spec, spec_from_loader
from numbers import Real
from pathlib import Path
from types import MappingProxyType
from typing import Any

import anywidget
import traitlets


@dataclass(frozen=True)
class PredicateSpec:
    """Descripción declarativa y segura de una comprobación."""

    kind: str
    name: str | None = None
    value: object = None
    minimum: int | None = None
    expected_type: str | None = None
    cases: tuple[Mapping[str, object], ...] = ()


@dataclass(frozen=True)
class Criterion:
    """Un aspecto observable de la respuesta esperada."""

    label: str
    predicate: Callable[[Mapping[str, object]], bool]
    success: str
    guidance: str


@dataclass(frozen=True)
class FeedbackContent:
    """Contenido y contrato de validación de un ejercicio."""

    title: str
    hints: tuple[str, ...] = ()
    required: tuple[str, ...] = ()
    criteria: tuple[Criterion, ...] = ()
    pending: PredicateSpec | None = None


@dataclass(frozen=True)
class CheckResult:
    """Resultado breve, serializable y visible de un criterio."""

    label: str
    passed: bool
    message: str

    def as_dict(self) -> dict[str, str | bool]:
        return {"label": self.label, "passed": self.passed, "message": self.message}


@dataclass(frozen=True)
class NameSnapshot:
    """Valores disponibles y nombres ausentes después de ejecutar una celda."""

    values: Mapping[str, object]
    missing: tuple[str, ...] = ()


@dataclass(frozen=True)
class ExerciseAttempt:
    """Estado de un intento listo para mostrarse en el coach."""

    status: str
    summary: str
    checks: tuple[CheckResult, ...] = ()
    error: str | None = None

    def as_state(self) -> dict[str, object]:
        return {
            "status": self.status,
            "summary": self.summary,
            "checks": [result.as_dict() for result in self.checks],
            "error": self.error,
        }


def criterion(
    label: str,
    predicate: Callable[[Mapping[str, object]], bool],
    *,
    success: str,
    guidance: str,
) -> Criterion:
    """Construye un criterio Python para compatibilidad con notebooks anteriores."""

    return Criterion(label, predicate, success, guidance)


def check(
    label: str,
    condition: bool | Callable[[], bool],
    *,
    success: str,
    guidance: str,
) -> CheckResult:
    """Construye una comprobación simple y recuperable."""

    try:
        passed = bool(condition() if callable(condition) else condition)
    except (AttributeError, IndexError, KeyError, TypeError, ValueError):
        passed = False
    return CheckResult(label, passed, success if passed else guidance)


def capture_names(
    namespace: Mapping[str, object],
    *,
    required: Sequence[str],
    trigger: object | None = None,
) -> NameSnapshot:
    """Captura los nombres solicitados sin referenciarlos directamente."""

    del trigger
    names = tuple(required)
    if not names or any(
        not isinstance(name, str) or not name.strip() for name in names
    ):
        raise ValueError("required debe contener nombres de variables no vacíos.")
    if len(set(names)) != len(names):
        raise ValueError("required no debe repetir nombres.")
    missing = tuple(name for name in names if name not in namespace)
    values = {name: namespace[name] for name in names if name in namespace}
    return NameSnapshot(MappingProxyType(values), missing)


def evaluate_snapshot(
    snapshot: NameSnapshot,
    *,
    criteria: Sequence[Criterion] = (),
    pending_when: Callable[[Mapping[str, object]], bool] | None = None,
) -> ExerciseAttempt:
    """Evalúa un conjunto seguro de valores y produce feedback pedagógico."""

    if snapshot.missing:
        joined = ", ".join(snapshot.missing)
        noun = "la variable" if len(snapshot.missing) == 1 else "las variables"
        return ExerciseAttempt(
            "error",
            f"No encuentro {noun} que necesita este ejercicio.",
            error=f"NameError: revisa el nombre o define {joined} en esta celda.",
        )
    readonly_values = MappingProxyType(dict(snapshot.values))
    if pending_when is not None:
        try:
            is_pending = bool(pending_when(readonly_values))
        except (AttributeError, IndexError, KeyError, TypeError, ValueError):
            is_pending = False
        if is_pending:
            return ExerciseAttempt(
                "pending",
                "La celda está lista. Escribe tu respuesta y vuelve a ejecutarla.",
            )
    results: list[CheckResult] = []
    for item in criteria:
        try:
            passed = bool(item.predicate(readonly_values))
        except Exception:
            passed = False
        results.append(
            CheckResult(item.label, passed, item.success if passed else item.guidance)
        )
    passed_count = sum(result.passed for result in results)
    total_count = len(results)
    if total_count and passed_count == total_count:
        return ExerciseAttempt(
            "complete",
            f"Listo: alcanzaste los {total_count} criterios del ejercicio.",
            tuple(results),
        )
    if total_count:
        remaining = total_count - passed_count
        noun = "criterio" if remaining == 1 else "criterios"
        return ExerciseAttempt(
            "review",
            f"Hay {remaining} {noun} por revisar.",
            tuple(results),
        )
    return ExerciseAttempt("complete", "La celda se ejecutó sin problemas.")


def evaluate_names(
    namespace: Mapping[str, object],
    *,
    required: Sequence[str],
    criteria: Sequence[Criterion] = (),
    pending_when: Callable[[Mapping[str, object]], bool] | None = None,
    trigger: object | None = None,
) -> ExerciseAttempt:
    """Atajo para capturar y evaluar los nombres de una celda de Marimo."""

    snapshot = capture_names(namespace, required=required, trigger=trigger)
    return evaluate_snapshot(snapshot, criteria=criteria, pending_when=pending_when)


class FeedbackCoach(anywidget.AnyWidget):
    """Panel persistente de resultados y pistas para una celda Python real."""

    _esm = Path(__file__).with_name("assets").joinpath("exercise_feedback.js")
    _css = Path(__file__).with_name("assets").joinpath("exercise_feedback.css")

    title = traitlets.Unicode("Revisión del ejercicio").tag(sync=True)
    hints = traitlets.List(trait=traitlets.Unicode()).tag(sync=True)
    status = traitlets.Unicode("pending").tag(sync=True)
    summary = traitlets.Unicode().tag(sync=True)
    checks = traitlets.List(trait=traitlets.Dict()).tag(sync=True)
    error = traitlets.Unicode(allow_none=True, default_value=None).tag(sync=True)
    value = traitlets.Dict().tag(sync=True)

    def __init__(
        self,
        *,
        content: FeedbackContent,
        attempt: ExerciseAttempt,
        interaction: Mapping[str, object] | None = None,
    ) -> None:
        if not isinstance(content, FeedbackContent):
            raise TypeError("content debe ser un FeedbackContent.")
        if not isinstance(attempt, ExerciseAttempt):
            raise TypeError("attempt debe ser un ExerciseAttempt.")
        current_interaction: dict[str, object] = {"hints_shown": 0}
        current_interaction.update(interaction or {})
        hints_shown = current_interaction.get("hints_shown", 0)
        if not isinstance(hints_shown, int) or isinstance(hints_shown, bool):
            raise ValueError("hints_shown debe ser un número entero.")
        current_interaction["hints_shown"] = min(
            max(hints_shown, 0), len(content.hints)
        )
        super().__init__(
            title=content.title,
            hints=list(content.hints),
            value=current_interaction,
            **attempt.as_state(),
        )

    def update_attempt(self, attempt: ExerciseAttempt) -> None:
        """Actualiza el mismo modelo sin reiniciar las pistas reveladas."""

        if not isinstance(attempt, ExerciseAttempt):
            raise TypeError("attempt debe ser un ExerciseAttempt.")
        with self.hold_trait_notifications():
            self.status = attempt.status
            self.summary = attempt.summary
            self.checks = [result.as_dict() for result in attempt.checks]
            self.error = attempt.error


@dataclass(frozen=True)
class ExerciseRuntime:
    """Objetos persistentes que pertenecen a un ejercicio."""

    content: FeedbackContent
    coach: FeedbackCoach
    widget: Any


@dataclass(frozen=True)
class FeedbackSession:
    """Sesión compartida que revisa y muestra todos los ejercicios del notebook."""

    mo: Any
    runtimes: Mapping[str, ExerciseRuntime]

    @classmethod
    def create(
        cls,
        mo: Any,
        contents: Mapping[str, FeedbackContent],
    ) -> FeedbackSession:
        if not contents:
            raise ValueError("La sesión necesita al menos un ejercicio.")
        runtimes: dict[str, ExerciseRuntime] = {}
        for exercise_id, content in contents.items():
            initial = ExerciseAttempt(
                "pending",
                "La celda está lista. Escribe tu respuesta y ejecútala.",
            )
            coach = FeedbackCoach(content=content, attempt=initial)
            widget = mo.ui.anywidget(coach)
            runtimes[exercise_id] = ExerciseRuntime(content, coach, widget)
        return cls(mo, MappingProxyType(runtimes))

    @property
    def contents(self) -> Mapping[str, FeedbackContent]:
        return MappingProxyType(
            {key: runtime.content for key, runtime in self.runtimes.items()}
        )

    def content(self, exercise_id: str) -> FeedbackContent:
        try:
            return self.runtimes[exercise_id].content
        except KeyError as error:
            raise KeyError(f"Ejercicio no configurado: {exercise_id!r}.") from error

    def evaluate(
        self,
        exercise_id: str,
        namespace: Mapping[str, object],
        *,
        required: Sequence[str] | None = None,
        criteria: Sequence[Criterion] | None = None,
        pending_when: Callable[[Mapping[str, object]], bool] | None = None,
        trigger: object | None = None,
    ) -> ExerciseAttempt:
        """Evalúa configuración externa o argumentos de compatibilidad."""

        content = self.content(exercise_id)
        configured_required = content.required if required is None else tuple(required)
        configured_criteria = content.criteria if criteria is None else tuple(criteria)
        configured_pending = pending_when
        if configured_pending is None and content.pending is not None:
            configured_pending = _predicate_for(content.pending)
        return evaluate_names(
            namespace,
            required=configured_required,
            criteria=configured_criteria,
            pending_when=configured_pending,
            trigger=trigger,
        )

    def exercise(
        self,
        exercise_id: str,
        namespace: Mapping[str, object],
    ) -> Any:
        """Evalúa y muestra el coach persistente desde la propia celda editable."""

        runtime = self.runtimes.get(exercise_id)
        if runtime is None:
            self.content(exercise_id)
            raise AssertionError("unreachable")
        attempt = self.evaluate(exercise_id, namespace)
        runtime.coach.update_attempt(attempt)
        return runtime.widget

    def panel(self, exercise_id: str, attempt: ExerciseAttempt) -> Any:
        """Compatibilidad: actualiza y devuelve el widget persistente."""

        runtime = self.runtimes.get(exercise_id)
        if runtime is None:
            self.content(exercise_id)
            raise AssertionError("unreachable")
        runtime.coach.update_attempt(attempt)
        return runtime.widget

    def sync(self, coaches: Mapping[str, Any]) -> None:
        """Compatibilidad: el estado ya vive en los widgets persistentes."""

        unknown = set(coaches).difference(self.runtimes)
        if unknown:
            self.content(sorted(unknown)[0])


# Nombre anterior conservado para no romper materiales todavía no migrados.
FeedbackTools = FeedbackSession


_TYPE_MAP: Mapping[str, type] = MappingProxyType(
    {
        "bool": bool,
        "dict": dict,
        "float": float,
        "int": int,
        "list": list,
        "set": set,
        "str": str,
        "tuple": tuple,
    }
)
_ALLOWED_KINDS = {
    "all_items_type",
    "all_required_none",
    "call_cases",
    "equals",
    "length_at_least",
    "length_equals",
    "mapping_equals",
    "never",
    "not_none",
    "numeric_items",
    "sequence_equals",
    "set_equals",
    "type_is",
}


def _normalize_sequence(value: object) -> object:
    if isinstance(value, (list, tuple)):
        return [_normalize_sequence(item) for item in value]
    return value


def _compare_value(kind: str, actual: object, expected: object) -> bool:
    if kind == "sequence_equals":
        return (
            isinstance(actual, (list, tuple))
            and _normalize_sequence(actual) == _normalize_sequence(expected)
        )
    if kind == "set_equals":
        return isinstance(actual, (set, frozenset)) and actual == set(expected)
    if kind == "mapping_equals":
        return isinstance(actual, Mapping) and dict(actual) == expected
    return actual == expected


def _predicate_for(spec: PredicateSpec) -> Callable[[Mapping[str, object]], bool]:
    def predicate(values: Mapping[str, object]) -> bool:
        if spec.kind == "all_required_none":
            return bool(values) and all(value is None for value in values.values())
        if spec.kind == "never":
            return False
        if spec.name is None:
            return False
        actual = values.get(spec.name)
        if spec.kind == "not_none":
            return actual is not None
        if spec.kind in {
            "equals",
            "mapping_equals",
            "sequence_equals",
            "set_equals",
        }:
            return _compare_value(spec.kind, actual, spec.value)
        if spec.kind == "type_is":
            if spec.expected_type == "number":
                return isinstance(actual, Real) and not isinstance(actual, bool)
            expected = _TYPE_MAP[spec.expected_type]
            return type(actual) is expected
        if spec.kind == "length_at_least":
            return len(actual) >= spec.minimum
        if spec.kind == "length_equals":
            return len(actual) == spec.minimum
        if spec.kind == "numeric_items":
            items = list(actual)
            return len(items) >= spec.minimum and all(
                isinstance(item, Real) and not isinstance(item, bool)
                for item in items[: spec.minimum]
            )
        if spec.kind == "all_items_type":
            expected = _TYPE_MAP[spec.expected_type]
            return all(type(item) is expected for item in actual)
        if spec.kind == "call_cases":
            if not callable(actual):
                return False
            for case in spec.cases:
                args = case.get("args", [])
                kwargs = case.get("kwargs", {})
                expected = case.get("expected")
                comparison = case.get("comparison", "equals")
                if not _compare_value(comparison, actual(*args, **kwargs), expected):
                    return False
            return True
        return False

    return predicate


def _require_text(config: Mapping[str, object], key: str, context: str) -> str:
    value = config.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{context} necesita {key} con texto.")
    return value.strip()


def _spec_from_config(config: object, context: str) -> PredicateSpec:
    if not isinstance(config, Mapping):
        raise ValueError(f"{context} debe ser una tabla TOML.")
    kind = config.get("kind")
    if kind not in _ALLOWED_KINDS:
        raise ValueError(f"Tipo de comprobación no permitido en {context}: {kind!r}.")
    name = config.get("name")
    if name is not None and (not isinstance(name, str) or not name.strip()):
        raise ValueError(f"name inválido en {context}.")
    expected_type = config.get("expected_type")
    if kind in {"type_is", "all_items_type"}:
        allowed_types = set(_TYPE_MAP)
        if kind == "type_is":
            allowed_types.add("number")
        if expected_type not in allowed_types:
            raise ValueError(f"expected_type inválido en {context}: {expected_type!r}.")
    minimum = config.get("minimum")
    if kind in {"length_at_least", "length_equals", "numeric_items"}:
        lower_bound = 1 if kind == "numeric_items" else 0
        if (
            not isinstance(minimum, int)
            or isinstance(minimum, bool)
            or minimum < lower_bound
        ):
            raise ValueError(f"minimum inválido en {context}.")
    cases = config.get("cases", [])
    if kind == "call_cases":
        if not isinstance(cases, list) or not cases:
            raise ValueError(f"{context} necesita una lista no vacía de cases.")
        for case in cases:
            if not isinstance(case, Mapping):
                raise ValueError(f"Cada case de {context} debe ser una tabla.")
            if not isinstance(case.get("args", []), list):
                raise ValueError(f"args de {context} debe ser una lista.")
            if not isinstance(case.get("kwargs", {}), Mapping):
                raise ValueError(f"kwargs de {context} debe ser una tabla.")
            comparison = case.get("comparison", "equals")
            if comparison not in {
                "equals",
                "mapping_equals",
                "sequence_equals",
                "set_equals",
            }:
                raise ValueError(f"comparison inválido en {context}: {comparison!r}.")
    return PredicateSpec(
        kind=kind,
        name=name.strip() if isinstance(name, str) else None,
        value=config.get("value"),
        minimum=minimum,
        expected_type=expected_type,
        cases=tuple(MappingProxyType(dict(case)) for case in cases),
    )


def _criterion_from_config(
    exercise_id: str,
    index: int,
    config: object,
) -> Criterion:
    context = f"criterio {index} de {exercise_id!r}"
    if not isinstance(config, Mapping):
        raise ValueError(f"El {context} debe ser una tabla TOML.")
    spec = _spec_from_config(config, context)
    label = _require_text(config, "label", context)
    success = _require_text(config, "success", context)
    guidance = _require_text(config, "guidance", context)
    return criterion(
        label,
        _predicate_for(spec),
        success=success,
        guidance=guidance,
    )


def _content_from_section(exercise_id: str, section: object) -> FeedbackContent:
    if not isinstance(section, Mapping):
        raise ValueError(f"El bloque {exercise_id!r} debe ser una tabla TOML.")
    title = _require_text(section, "title", f"ejercicio {exercise_id!r}")
    hints = section.get("hints", [])
    if not isinstance(hints, list) or any(
        not isinstance(hint, str) or not hint.strip() for hint in hints
    ):
        raise ValueError(
            f"Las hints de {exercise_id!r} deben ser una lista de textos no vacíos."
        )
    validation = section.get("validation", {})
    if not isinstance(validation, Mapping):
        raise ValueError(f"validation de {exercise_id!r} debe ser una tabla TOML.")
    required = validation.get("required", [])
    if not isinstance(required, list) or any(
        not isinstance(name, str) or not name.strip() for name in required
    ):
        raise ValueError(
            f"required de {exercise_id!r} debe ser una lista de nombres no vacíos."
        )
    if len(set(required)) != len(required):
        raise ValueError(f"required de {exercise_id!r} no debe repetir nombres.")
    pending_config = validation.get("pending")
    legacy_pending = validation.get("pending_when")
    if pending_config is not None and legacy_pending is not None:
        raise ValueError(f"{exercise_id!r} no puede declarar dos reglas pending.")
    if pending_config is not None:
        pending = _spec_from_config(pending_config, f"pending de {exercise_id!r}")
    elif legacy_pending == "all_required_none":
        pending = PredicateSpec("all_required_none")
    elif legacy_pending is None:
        pending = PredicateSpec("all_required_none") if required else None
    elif legacy_pending == "never":
        pending = None
    else:
        raise ValueError(f"pending_when no reconocido en {exercise_id!r}.")
    raw_criteria = validation.get("criteria", [])
    if not isinstance(raw_criteria, list):
        raise ValueError(f"criteria de {exercise_id!r} debe ser una lista TOML.")
    criteria = tuple(
        _criterion_from_config(exercise_id, index, item)
        for index, item in enumerate(raw_criteria, start=1)
    )
    return FeedbackContent(
        title,
        tuple(hint.strip() for hint in hints),
        tuple(name.strip() for name in required),
        criteria,
        pending,
    )


def load_feedback_content(path: str | Path, exercise_id: str) -> FeedbackContent:
    """Carga un ejercicio desde un TOML semanal o desde el formato anterior."""

    with Path(path).open("rb") as content_file:
        document = tomllib.load(content_file)
    sections = document.get("exercises", document)
    try:
        section = sections[exercise_id]
    except KeyError as error:
        available = ", ".join(sorted(sections)) or "ninguno"
        raise KeyError(
            f"No existe el ejercicio {exercise_id!r}. Bloques: {available}."
        ) from error
    return _content_from_section(exercise_id, section)


def _contents_for_notebook(
    document: Mapping[str, object],
    *,
    week: str,
    notebook: str,
) -> Mapping[str, FeedbackContent]:
    if document.get("schema_version") != 1:
        raise ValueError("El feedback semanal necesita schema_version = 1.")
    if document.get("week") != week:
        raise ValueError(f"El bundle no corresponde a la semana {week!r}.")
    notebooks = document.get("notebooks")
    exercises = document.get("exercises")
    if not isinstance(notebooks, Mapping) or not isinstance(exercises, Mapping):
        raise ValueError("El feedback semanal necesita tablas notebooks y exercises.")
    try:
        notebook_config = notebooks[notebook]
    except KeyError as error:
        raise KeyError(f"Notebook no configurado: {notebook!r}.") from error
    if not isinstance(notebook_config, Mapping):
        raise ValueError(f"La configuración de {notebook!r} debe ser una tabla.")
    ids = notebook_config.get("exercises")
    if (
        not isinstance(ids, list)
        or not ids
        or any(not isinstance(item, str) or not item.strip() for item in ids)
    ):
        raise ValueError(f"{notebook!r} necesita una lista de ejercicios.")
    if len(set(ids)) != len(ids):
        raise ValueError(f"{notebook!r} no debe repetir ejercicios.")
    contents: dict[str, FeedbackContent] = {}
    for exercise_id in ids:
        if exercise_id not in exercises:
            raise KeyError(f"Ejercicio no definido en la semana: {exercise_id!r}.")
        contents[exercise_id] = _content_from_section(
            exercise_id, exercises[exercise_id]
        )
    return MappingProxyType(contents)


def _safe_week_name(week: str) -> str:
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", week):
        raise ValueError("week debe usar minúsculas, números, guiones o guion bajo.")
    return week.replace("-", "_")


def _load_sourceless_bundle(path: Path) -> Mapping[str, object]:
    module_name = f"_course_feedback_{path.stem}"
    loader = SourcelessFileLoader(module_name, str(path))
    spec = spec_from_loader(module_name, loader)
    if spec is None:
        raise ImportError(f"No se pudo preparar el bundle {path}.")
    module = module_from_spec(spec)
    loader.exec_module(module)
    document = module.load()
    if not isinstance(document, Mapping):
        raise ValueError(f"El bundle {path} no contiene una configuración válida.")
    return document


def _resolve_week_document(
    week: str,
    source: str | Path | Mapping[str, object] | None,
) -> Mapping[str, object]:
    if isinstance(source, Mapping):
        return source
    if source is not None:
        source_path = Path(source)
        if source_path.suffix == ".pyc":
            return _load_sourceless_bundle(source_path)
        with source_path.open("rb") as content_file:
            return tomllib.load(content_file)
    root = Path(__file__).resolve().parents[1]
    private_toml = root / "materials/v2/instructor/feedback" / f"{week}.toml"
    if private_toml.is_file():
        with private_toml.open("rb") as content_file:
            return tomllib.load(content_file)
    bundle_name = f"{_safe_week_name(week)}.pyc"
    candidates = (
        root / "course_feedback/bundles" / bundle_name,
        Path.cwd() / "course_feedback/bundles" / bundle_name,
    )
    for candidate in candidates:
        if candidate.is_file():
            return _load_sourceless_bundle(candidate)
    raise FileNotFoundError(
        f"No encuentro la configuración privada ni el bundle de {week!r}."
    )


def load_feedback(
    mo: Any,
    *,
    week: str,
    notebook: str,
    source: str | Path | Mapping[str, object] | None = None,
) -> FeedbackSession:
    """Carga una sola configuración semanal y prepara el notebook indicado."""

    document = _resolve_week_document(week, source)
    contents = _contents_for_notebook(document, week=week, notebook=notebook)
    return FeedbackSession.create(mo, contents)


def setup_feedback(
    mo: Any,
    path: str | Path,
    exercise_ids: Sequence[str],
) -> FeedbackSession:
    """Compatibilidad con el setup basado en un TOML junto al notebook."""

    ids = tuple(exercise_ids)
    if not ids or any(
        not isinstance(exercise_id, str) or not exercise_id.strip()
        for exercise_id in ids
    ):
        raise ValueError("exercise_ids debe contener identificadores no vacíos.")
    if len(set(ids)) != len(ids):
        raise ValueError("exercise_ids no debe repetir identificadores.")
    contents = {
        exercise_id: load_feedback_content(path, exercise_id) for exercise_id in ids
    }
    return FeedbackSession.create(mo, contents)


def display_coach(mo: Any, coach: FeedbackCoach) -> Any:
    """Envuelve un coach aislado según la API de Marimo."""

    return mo.ui.anywidget(coach)
