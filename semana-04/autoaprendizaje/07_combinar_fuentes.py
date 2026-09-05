# ruff: noqa: B018
import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Semana 4 · 07 Combinar fuentes")


@app.cell(hide_code=True)
def setup():
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    assets = Path(__file__).parent / "assets"
    feedback = load_feedback(
        mo, week="week-04-data-cleaning-wrangling", notebook="07_combinar_fuentes"
    )
    return Path, assets, feedback, mo, pd


@app.cell(hide_code=True)
def opening(mo):
    mo.md(r"""
    # 07 · Combinar fuentes con validación de cardinalidad

    En proyectos reales de salud, la información rara vez proviene de una sola tabla. Es habitual tener:
    - Una tabla central de participantes y visitas.
    - Tablas de catálogo o metadatos (ej. características de las sedes o centros de atención).
    - Lotes periódicos que llegan en archivos separados (ej. bitácoras diarias de llamadas de seguimiento).

    Para integrar estas fuentes utilizamos dos operaciones fundamentales:
    1. **Unión relacional (`pd.merge()`):** combina columnas de dos tablas a partir de una o más claves compartidas, validando la cardinalidad del cruce.
    2. **Concatenación o apilamiento (`pd.concat()`):** apila filas de tablas homogéneas que comparten las mismas variables.

    Al terminar esta unidad sabrás:
    - Ejecutar uniones relacionales seguras controlando tipo de unión (`how`), claves (`on`) y procedencia (`indicator=True`).
    - Validar la cardinalidad de la relación con `validate='many_to_one'` para prevenir explosiones cartesianas accidentales.
    - Apilar registros homogéneos con `pd.concat()` reindexando apropiadamente.
    """)
    return


@app.cell
def load_data(assets, pd):
    registros_union = pd.read_csv(assets / "pacientes_estudio.csv")
    registros_union["sede"] = registros_union["sede"].str.strip().str.lower()
    sedes_union = pd.read_csv(assets / "sedes_estudio.csv")

    {
        "Pacientes a enriquecer": len(registros_union),
        "Sedes disponibles en catálogo": len(sedes_union),
        "Variables en catálogo de sedes": sedes_union.columns.tolist(),
    }
    return registros_union, sedes_union


@app.cell(hide_code=True)
def cardinality_concept(mo):
    mo.md(r"""
    ---
    ## Unión relacional con validación de cardinalidad (`pd.merge`)

    Cuando unimos dos tablas en Pandas, es fundamental definir:
    - `on='columna_clave'`: la variable compartida sobre la cual se hace el emparejamiento.
    - `how='left'`: conserva **todas** las filas de la tabla izquierda (pacientes), trayendo datos de la derecha cuando haya coincidencia y completando con `NaN` si no existe la sede.
    - `validate='many_to_one'`: le ordena a Pandas comprobar que la clave en la tabla derecha sea estrictamente única. Si la tabla de sedes tuviera duplicados en su clave, Pandas arrojaría una excepción inmediata en vez de multiplicar filas en silencio.
    - `indicator=True`: añade la columna `_merge` indicando si el registro coincidió en `'both'`, solo en `'left_only'` o en `'right_only'`.

    Veamos un ejemplo ejecutable con las sedes del estudio:
    """)
    return


@app.cell
def merge_audit_demo(pd, registros_union, sedes_union):
    # Demostración de merge con validación e indicador de procedencia
    union_auditada = pd.merge(
        registros_union,
        sedes_union,
        on="sede",
        how="left",
        validate="many_to_one",
        indicator=True,
    )
    resumen_procedencia = union_auditada["_merge"].value_counts()

    {
        "Forma antes del merge": registros_union.shape,
        "Forma tras el merge (enriquecida)": union_auditada.shape,
        "Balance del indicador _merge": resumen_procedencia.to_dict(),
        "Muestra combinada": union_auditada[["codigo", "sede", "ciudad", "nivel_atencion", "_merge"]].head(3),
    }
    return resumen_procedencia, union_auditada


@app.cell(hide_code=True)
def practice_one_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 1 · Enriquecer pacientes con información de sedes

    **Consigna:**
    A partir de `registros_union` y `sedes_union`:
    1. Ejecuta una unión relacional izquierda (`how='left'`) sobre la clave `"sede"`.
    2. Valida que la relación sea de muchos a uno (`validate='many_to_one'`).
    3. Habilita el indicador de procedencia (`indicator=True`).
    4. Asigna la tabla combinada a la variable `registros_enriquecidos`.

    *Verificación esperada:* `registros_enriquecidos` debe tener exactamente 50 filas y 13 columnas (las 10 de pacientes + 2 de sedes + 1 de `_merge`).
    """)
    return


@app.cell
def practice_one(feedback, pd, registros_union, sedes_union):
    # TU TURNO: realiza el merge entre registros_union y sedes_union
    registros_enriquecidos = None
    feedback.exercise("unir_con_validacion", locals())
    return (registros_enriquecidos,)


@app.cell(hide_code=True)
def concat_concept(mo):
    mo.md(r"""
    ---
    ## Apilar registros homogéneos con `pd.concat`

    Cuando recopilamos datos en lotes secuenciales (por ejemplo, los contactos telefónicos registrados en el Día 1 y los del Día 2), no necesitamos cruzar por claves sino **apilar verticalmente** las tablas.

    Aspectos clave de `pd.concat()`:
    - Recibe una lista de DataFrames: `pd.concat([tabla_1, tabla_2, ...])`.
    - Por defecto apila sobre el eje de filas (`axis=0`).
    - **`ignore_index=True`:** regenera un índice numérico continuo $(0, 1, 2, \dots, N-1)$. Si se omite, los índices originales se repetirán, causando ambigüedades al indexar con `.loc`.

    Veamos un ejemplo ejecutable comparando dos turnos de recolección:
    """)
    return


@app.cell
def ejemplo_concatenacion(pd):
    # Demostración de concatenación vertical
    turno_manana = pd.DataFrame({
        "codigo": ["HOR-001", "HOR-002"],
        "operador": ["Op_A", "Op_B"],
        "minutos_llamada": [12, 8],
    })
    turno_tarde = pd.DataFrame({
        "codigo": ["HOR-003", "HOR-004"],
        "operador": ["Op_A", "Op_C"],
        "minutos_llamada": [15, 6],
    })

    # Apilamos ambos turnos ignorando índices originales
    contactos_dia_completo = pd.concat([turno_manana, turno_tarde], ignore_index=True)

    {
        "Filas turno mañana": len(turno_manana),
        "Filas turno tarde": len(turno_tarde),
        "Total tras concatenar": len(contactos_dia_completo),
        "Tabla apilada resultante": contactos_dia_completo,
    }
    return contactos_dia_completo, turno_manana, turno_tarde


@app.cell(hide_code=True)
def practice_two_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 2 · Apilar jornadas de contacto operativo

    **Consigna:**
    En la carpeta `assets` se encuentran dos archivos con el registro de llamadas de seguimiento:
    `contactos_dia_1.csv` (4 filas) y `contactos_dia_2.csv` (4 filas).

    1. Cárgalos en memoria usando `pd.read_csv()`.
    2. Apílalos verticalmente en una sola tabla llamada `contactos_totales` utilizando `pd.concat()`.
    3. Asegúrate de regenerar el índice con `ignore_index=True`.

    *Verificación esperada:* `contactos_totales` debe tener exactamente 8 filas y 4 columnas.
    """)
    return


@app.cell
def practice_two(assets, feedback, pd):
    contactos_dia_1 = pd.read_csv(assets / "contactos_dia_1.csv")
    contactos_dia_2 = pd.read_csv(assets / "contactos_dia_2.csv")

    # TU TURNO: apila los dos DataFrames con pd.concat(..., ignore_index=True)
    contactos_totales = None
    feedback.exercise("concatenar_jornadas", locals())
    return contactos_dia_1, contactos_dia_2, contactos_totales


@app.cell(hide_code=True)
def reflection_unit_7(mo):
    cierre_unidad_7 = mo.ui.text_area(
        label="Para cerrar: el cuidado con las claves",
        placeholder="¿Qué riesgo metodológico existe al hacer un pd.merge sin validar la cardinalidad si la tabla de la derecha tiene filas duplicadas en la columna de enlace?",
        rows=3,
        full_width=True,
    )
    cierre_unidad_7
    return


@app.cell(hide_code=True)
def closing_unit_7(mo):
    mo.md(r"""
    ### Conclusión y siguiente paso
    Has integrado fuentes relacionales con validación estricta y apilado lotes operativos. En la **Unidad 08** nos enfocaremos en la reestructuración de tablas: alternando entre el formato ancho (para ingreso visual de datos) y el formato largo o *tidy* (para análisis longitudinal y modelos estadísticos).
    """)
    return


if __name__ == "__main__":
    app.run()
