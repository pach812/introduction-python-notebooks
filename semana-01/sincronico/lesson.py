# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = ["marimo==0.23.16"]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(
    width="full",
    app_title="Semana 1 · Workbook en vivo",
    layout_file="layouts/lesson.slides.json",
    css_file="../../assets/ces-theme.css",
)


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def cover(mo):
    mo.md(r"""
    # Fundamentos de Python para análisis de datos
    ## Semana 1: workbook de la sesión
    <p class="ces-meta">Universidad CES</p>
    """)
    return


@app.cell(hide_code=True)
def workbook_route(mo):
    mo.md(r"""
    # Cómo trabajaremos aquí

    En cada ejercicio encontrarás:

    1. una respuesta inicial o una hipótesis;
    2. una celda editable marcada con `# TU TURNO`;
    3. una comprobación que cambia con tu código;
    4. una explicación breve y un reintento.

    Conserva tus respuestas: serán la evidencia de lo que observaste durante la sesión.
    """)
    return


@app.cell(hide_code=True)
def section_project(mo):
    mo.md(r"""
    # Proyecto y reactividad
    ## Ubicar · registrar · modificar · explicar
    """)
    return


@app.cell(hide_code=True)
def project_prompt(mo):
    mo.md(r"""
    # Comprueba tu espacio de trabajo

    En la terminal:

    ```sh
    pwd
    ls
    ```

    Criterio: puedes indicar la carpeta del proyecto, reconocer el archivo del cuaderno y mostrar una actualización entre dos celdas.
    """)
    return


@app.cell
def project_evidence():
    # TU TURNO: reemplaza los textos y cambia 10 por otro número.
    ruta_proyecto_w1 = "PENDIENTE"
    archivo_cuaderno_w1 = "PENDIENTE"
    base_reactiva_w1 = 10
    return archivo_cuaderno_w1, base_reactiva_w1, ruta_proyecto_w1


@app.cell
def project_reactivity(base_reactiva_w1):
    # Esta celda depende de base_reactiva_w1, definida en la celda anterior.
    resultado_reactivo_w1 = base_reactiva_w1 * 2
    return (resultado_reactivo_w1,)


@app.cell(hide_code=True)
def project_check(
    archivo_cuaderno_w1,
    base_reactiva_w1,
    mo,
    resultado_reactivo_w1,
    ruta_proyecto_w1,
):
    _path_ready = ruta_proyecto_w1.strip().upper() != "PENDIENTE"
    _file_ready = (
        archivo_cuaderno_w1.strip().upper() != "PENDIENTE"
        and archivo_cuaderno_w1.strip().endswith(".py")
    )
    _reactivity_ready = (
        isinstance(base_reactiva_w1, (int, float))
        and base_reactiva_w1 != 10
        and resultado_reactivo_w1 == base_reactiva_w1 * 2
    )

    if not _path_ready or not _file_ready:
        _message = "Registra la ruta observada y un archivo cuyo nombre termine en .py."
        _kind = "info"
    elif not _reactivity_ready:
        _message = "Cambia el valor de base_reactiva_w1 y vuelve a observar la celda dependiente."
        _kind = "warn"
    else:
        _message = f"Criterio alcanzado: la celda dependiente muestra {resultado_reactivo_w1}."
        _kind = "success"

    mo.callout(_message, kind=_kind)
    return


@app.cell
def project_explanation():
    # TU TURNO: explica qué cambió y por qué Marimo actualizó la otra celda.
    explicacion_proyecto_w1 = "PENDIENTE"
    return (explicacion_proyecto_w1,)


@app.cell(hide_code=True)
def project_completion(explicacion_proyecto_w1, mo):
    _text = explicacion_proyecto_w1.strip().lower()
    _ready = len(_text) >= 25 and ("depend" in _text or "celda" in _text)
    mo.callout(
        "La explicación relaciona las dos celdas y completa el ejercicio."
        if _ready
        else "Añade una explicación que relacione la celda que define el valor con la celda que lo utiliza.",
        kind="success" if _ready else "info",
    )
    return


@app.cell(hide_code=True)
def project_hint(mo):
    mo.accordion(
        {
            "Pista 1 · ubicación": "La ruta es la respuesta que observas después de ejecutar pwd.",
            "Pista 2 · reactividad": "Edita únicamente el número de la primera celda y observa qué salida cambia sin redefinir la variable.",
        }
    )
    return


@app.cell(hide_code=True)
def section_types(mo):
    mo.md(r"""
    # Valores y tipos
    ## Predecir · ejecutar · comparar · explicar
    """)
    return


@app.cell(hide_code=True)
def types_prompt(mo):
    mo.md(r"""
    # Responde antes de ejecutar

    Escribe el nombre del tipo que esperas para cada valor:

    ```python
    8
    8.0
    "8"
    ```

    Criterio: quedan registradas tres respuestas iniciales y una explicación que distingue valor y tipo.
    """)
    return


@app.cell
def type_initial_answers():
    # TU TURNO: reemplaza PENDIENTE por int, float o str.
    respuesta_8_w1 = "PENDIENTE"
    respuesta_8_decimal_w1 = "PENDIENTE"
    respuesta_8_texto_w1 = "PENDIENTE"
    return respuesta_8_decimal_w1, respuesta_8_texto_w1, respuesta_8_w1


@app.cell(hide_code=True)
def initial_answers_check(
    mo,
    respuesta_8_decimal_w1,
    respuesta_8_texto_w1,
    respuesta_8_w1,
):
    _initial_answers = [
        respuesta_8_w1.strip().lower(),
        respuesta_8_decimal_w1.strip().lower(),
        respuesta_8_texto_w1.strip().lower(),
    ]
    _ready = all(_answer in {"int", "float", "str"} for _answer in _initial_answers)
    mo.callout(
        "Las tres respuestas iniciales están registradas. Ahora ejecuta la comprobación."
        if _ready
        else "Completa las tres respuestas antes de ejecutar type.",
        kind="success" if _ready else "info",
    )
    return


@app.cell
def type_observation():
    # Ejecuta esta celda después de registrar tus respuestas iniciales.
    tipo_8_w1 = type(8).__name__
    tipo_8_decimal_w1 = type(8.0).__name__
    tipo_8_texto_w1 = type("8").__name__
    return tipo_8_decimal_w1, tipo_8_texto_w1, tipo_8_w1


@app.cell(hide_code=True)
def type_comparison(
    mo,
    respuesta_8_decimal_w1,
    respuesta_8_texto_w1,
    respuesta_8_w1,
    tipo_8_decimal_w1,
    tipo_8_texto_w1,
    tipo_8_w1,
):
    _rows = [
        {"valor": "8", "respuesta inicial": respuesta_8_w1, "observación": tipo_8_w1},
        {"valor": "8.0", "respuesta inicial": respuesta_8_decimal_w1, "observación": tipo_8_decimal_w1},
        {"valor": '"8"', "respuesta inicial": respuesta_8_texto_w1, "observación": tipo_8_texto_w1},
    ]
    _all_match = all(
        _row["respuesta inicial"].strip().lower() == _row["observación"] for _row in _rows
    )
    mo.vstack(
        [
            mo.ui.table(_rows, selection=None),
            mo.callout(
                "Las respuestas iniciales coinciden con las tres observaciones."
                if _all_match
                else "Compara cada respuesta inicial con la observación y localiza la discrepancia.",
                kind="success" if _all_match else "warn",
            ),
        ],
        gap=1,
    )
    return


@app.cell
def type_explanation():
    # TU TURNO: usa las palabras valor y tipo en tu explicación.
    explicacion_tipos_w1 = "PENDIENTE"
    return (explicacion_tipos_w1,)


@app.cell(hide_code=True)
def types_completion(explicacion_tipos_w1, mo):
    _text = explicacion_tipos_w1.strip().lower()
    _ready = len(_text) >= 25 and "valor" in _text and "tipo" in _text
    mo.callout(
        "La explicación distingue valor y tipo; conserva esta versión."
        if _ready
        else "Explica la diferencia observada usando las palabras valor y tipo.",
        kind="success" if _ready else "info",
    )
    return


@app.cell(hide_code=True)
def types_hint(mo):
    mo.accordion(
        {
            "Pista 1 · forma": "Compara el punto decimal y las comillas antes de volver a predecir.",
            "Pista 2 · significado": "El valor es lo evaluado; el tipo describe la clase de objeto y las operaciones disponibles.",
        }
    )
    return


@app.cell(hide_code=True)
def section_debug(mo):
    mo.md(r"""
    # Leer y corregir un error
    ## Mensaje · hipótesis · cambio · reintento
    """)
    return


@app.cell(hide_code=True)
def debug_prompt(mo):
    mo.md(r"""
    # Un error previsto

    La celda de trabajo comienza en un estado seguro. Sustituye `"SIN_INTENTO"` por esta expresión y ejecútala:

    ```python
    cantidad_depurar_w1 + incremento_depurar_w1
    ```

    Lee la última línea del error. Después registra una hipótesis, cambia un solo operando y vuelve a ejecutar.

    Criterio: identificas el error, haces compatibles los operandos y explicas la nueva salida.
    """)
    return


@app.cell
def debug_hypothesis():
    # TU TURNO: registra tu hipótesis después de leer el error y antes de corregir.
    hipotesis_error_w1 = "PENDIENTE"
    return (hipotesis_error_w1,)


@app.cell
def debug_workspace():
    cantidad_depurar_w1 = "8"
    incremento_depurar_w1 = 2

    # TU TURNO 1: reemplaza "SIN_INTENTO" por la expresión indicada y observa el error.
    # TU TURNO 2: cambia un solo operando para representar tu intención y reintenta.
    resultado_depurar_w1 = "SIN_INTENTO"
    return cantidad_depurar_w1, incremento_depurar_w1, resultado_depurar_w1


@app.cell(hide_code=True)
def debug_status(
    cantidad_depurar_w1,
    incremento_depurar_w1,
    mo,
    resultado_depurar_w1,
):
    _attempted = resultado_depurar_w1 != "SIN_INTENTO"
    _compatible = type(cantidad_depurar_w1) is type(incremento_depurar_w1)
    if not _attempted:
        _message = "Aún no hay un reintento correcto. Sigue la secuencia indicada en la consigna."
        _kind = "info"
    elif not _compatible:
        _message = "Revisa si ambos operandos representan el mismo tipo de operación."
        _kind = "warn"
    else:
        _message = f"El reintento se ejecutó y produjo {resultado_depurar_w1}."
        _kind = "success"
    mo.callout(_message, kind=_kind)
    return


@app.cell
def debug_explanation():
    # TU TURNO: explica qué cambiaste y por qué la nueva salida apoya tu hipótesis.
    explicacion_error_w1 = "PENDIENTE"
    return (explicacion_error_w1,)


@app.cell(hide_code=True)
def debug_completion(
    cantidad_depurar_w1,
    explicacion_error_w1,
    hipotesis_error_w1,
    incremento_depurar_w1,
    mo,
    resultado_depurar_w1,
):
    _hypothesis = hipotesis_error_w1.strip().lower()
    _explanation = explicacion_error_w1.strip()
    _diagnosed = "typeerror" in _hypothesis and "str" in _hypothesis and "int" in _hypothesis
    _recovered = (
        resultado_depurar_w1 != "SIN_INTENTO"
        and type(cantidad_depurar_w1) is type(incremento_depurar_w1)
    )
    _explained = len(_explanation) >= 30
    _complete = _diagnosed and _recovered and _explained
    mo.callout(
        "Diagnóstico, corrección y explicación completos. Conserva este reintento."
        if _complete
        else "Para cerrar: nombra TypeError, identifica str e int, corrige un operando y explica la nueva salida.",
        kind="success" if _complete else "info",
    )
    return


@app.cell(hide_code=True)
def debug_hint(mo):
    mo.accordion(
        {
            "Pista 1 · leer": "Empieza por la última línea y compara los tipos que aparecen en el mensaje.",
            "Pista 2 · decidir": "Decide si tu intención es sumar números o unir textos antes de cambiar un operando.",
            "Pista 3 · reintentar": "Cambia una sola cosa; una corrección útil permite explicar qué produjo el nuevo resultado.",
        }
    )
    return


@app.cell(hide_code=True)
def exit_prompt(mo):
    mo.md(r"""
    # Evidencia de salida

    Completa tres frases con lo que observaste hoy. No copies una definición: describe una relación o una acción comprobable.
    """)
    return


@app.cell
def exit_ticket():
    # TU TURNO: reemplaza cada texto pendiente.
    salida_codigo_w1 = "El código y la salida se relacionan porque PENDIENTE"
    salida_tipo_w1 = "Un valor y su tipo se distinguen porque PENDIENTE"
    salida_error_w1 = "Cuando aparece un error, comienzo por PENDIENTE"
    return salida_codigo_w1, salida_error_w1, salida_tipo_w1


@app.cell(hide_code=True)
def exit_feedback(mo, salida_codigo_w1, salida_error_w1, salida_tipo_w1):
    _responses = [salida_codigo_w1, salida_tipo_w1, salida_error_w1]
    _complete = all("pendiente" not in _response.lower() and len(_response) >= 35 for _response in _responses)
    mo.callout(
        "Las tres evidencias están registradas. Guarda el workbook."
        if _complete
        else "Completa las tres frases con una relación o una acción que hayas comprobado.",
        kind="success" if _complete else "info",
    )
    return


@app.cell(hide_code=True)
def closing(mo):
    mo.md(r"""
    # Predijiste, ejecutaste y corregiste
    ## Guarda este workbook como evidencia de la sesión
    """)
    return


if __name__ == "__main__":
    app.run()
