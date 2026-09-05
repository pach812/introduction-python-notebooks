# ruff: noqa: B018
import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Semana 4 · 09 Integrar flujo reproducible")


@app.cell(hide_code=True)
def setup():
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    assets = Path(__file__).parent / "assets"
    feedback = load_feedback(
        mo, week="week-04-data-cleaning-wrangling", notebook="09_integrar_flujo"
    )
    return Path, assets, feedback, mo, pd


@app.cell(hide_code=True)
def opening(mo):
    mo.md(r"""
    # 09 · Integrar un flujo de preparación reproducible de punta a punta

    Has llegado a la unidad culminante de la Semana 4. En la práctica profesional, la preparación de datos nunca consiste en pasos aislados ejecutados a mano: **se diseña como un pipeline reproducible y auditable**.

    Un flujo de preparación de grado científico debe garantizar:
    1. **Inmutabilidad de la fuente:** los archivos originales nunca se sobreescriben.
    2. **Secuencia lógica sin pérdidas ocultas:** normalización de texto $\rightarrow$ marcado de anomalías $\rightarrow$ imputación con bandera $\rightarrow$ resolución de duplicados $\rightarrow$ cruce relacional.
    3. **Reporte de control (*scorecard*):** un resumen objetivo de métricas de calidad que certifique que los datos están listos para el modelado bioestadístico.

    Al terminar esta unidad sabrás:
    - Construir una tubería de transformación limpia de extremo a extremo.
    - Generar un diccionario formal de auditoría y control de calidad.
    """)
    return


@app.cell
def load_sources(assets, pd):
    fuente_integracion = pd.read_csv(assets / "pacientes_estudio.csv")
    sedes_integracion = pd.read_csv(assets / "sedes_estudio.csv")
    {
        "Pacientes crudos iniciales": len(fuente_integracion),
        "Sedes de referencia": len(sedes_integracion),
    }
    return fuente_integracion, sedes_integracion


@app.cell(hide_code=True)
def pipeline_architecture_concept(mo):
    mo.md(r"""
    ---
    ## Diseño de una función de preparación modular

    La mejor forma de garantizar reproducibilidad es encapsular la secuencia de transformaciones en una función pura o en una secuencia documentada paso a paso.

    Veamos una demostración con un lote piloto reducido para ilustrar cómo cada paso refina la tabla:
    """)
    return


@app.cell
def ejemplo_mini_pipeline(pd):
    # Demostración conceptual: preparación secuencial sobre una muestra piloto
    muestra_cruda = pd.DataFrame({
        "codigo": ["P1", "P2", "P1"],
        "sede_cruda": [" norte ", "SUR", "norte"],
        "valor": [25.0, None, 25.0],
    })

    # Paso 1: Copia de trabajo
    df_proc = muestra_cruda.copy()

    # Paso 2: Normalización de texto
    df_proc["sede_limpia"] = df_proc["sede_cruda"].str.strip().str.title()

    # Paso 3: Bandera booleana de auditoría
    df_proc["valor_imputado"] = df_proc["valor"].isna()

    # Paso 4: Imputación con mediana
    mediana = df_proc["valor"].median()
    df_proc["valor"] = df_proc["valor"].fillna(mediana)

    # Paso 5: Deduplicación de clave
    df_final_demo = df_proc.drop_duplicates(subset=["codigo"], keep="first")

    {
        "Filas crudas iniciales": len(muestra_cruda),
        "Filas tras procesar y deduplicar": len(df_final_demo),
        "Valores nulos remanentes": int(df_final_demo["valor"].isna().sum()),
        "Resultado limpio": df_final_demo[["codigo", "sede_limpia", "valor", "valor_imputado"]],
    }
    return df_final_demo, df_proc, mediana, muestra_cruda


@app.cell(hide_code=True)
def practice_one_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 1 · Construir la tabla preparada de pacientes

    **Consigna:**
    A partir de `fuente_integracion`, crea la variable `tabla_preparada` ejecutando exactamente los siguientes 5 pasos en orden:

    1. **Copia:** parte de una copia independiente con `fuente_integracion.copy()`.
    2. **Normalización de sede:** transforma la columna `"sede"` aplicando `.str.strip().str.title()`.
    3. **Marca de plausibilidad:** crea la columna booleana `"edad_para_revisar"`, que debe valer `True` para edades $< 18$ o $> 110$ años, y `False` en caso contrario.
    4. **Imputación con auditoría:**
       - Crea la columna booleana `"imc_faltaba"` con `tabla_preparada["imc"].isna()`.
       - Imputa los valores ausentes de `"imc"` con la mediana calculada sobre los valores válidos.
    5. **Deduplicación de clave primaria:** elimina filas con `"codigo"` repetido conservando la primera aparición (`keep='first'`).

    *Verificación esperada:* `tabla_preparada` debe tener exactamente 49 filas (se elimina el duplicado de `HOR-005`) y 12 columnas.
    """)
    return


@app.cell
def practice_one(feedback, fuente_integracion):
    # TU TURNO: construye tabla_preparada siguiendo los 5 pasos
    tabla_preparada = None
    feedback.exercise("construir_tabla_preparada", locals())
    return (tabla_preparada,)


@app.cell(hide_code=True)
def scorecard_concept(mo):
    mo.md(r"""
    ---
    ## Enriquecimiento relacional y *Scorecard* de calidad

    El paso de cierre de un pipeline de ingeniería de datos es emitir un **informe de control objetivo** que certifique el estado de la entrega.

    Un diccionario de control (*scorecard*) reúne métricas críticas:
    - Total de observaciones entregadas.
    - Certificación de clave primaria única (`tabla['codigo'].is_unique`).
    - Número de discrepancias en cruces relacionales (ej. filas con `_merge == 'left_only'`).
    - Conteo de observaciones marcadas para revisión clínica (`edad_para_revisar.sum()`).
    - Conteo de observaciones imputadas sintéticamente (`imc_faltaba.sum()`).

    Veamos una demostración con el lote piloto preparado antes:
    """)
    return


@app.cell
def ejemplo_construccion_scorecard(df_final_demo):
    # Demostración: construcción programática de un scorecard
    scorecard_demo = {
        "filas_totales": len(df_final_demo),
        "claves_unicas": bool(df_final_demo["codigo"].is_unique),
        "total_imputados": int(df_final_demo["valor_imputado"].sum()),
    }
    scorecard_demo
    return (scorecard_demo,)


@app.cell(hide_code=True)
def practice_two_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 2 · Enriquecimiento relacional y scorecard final

    **Consigna:**
    A partir de `tabla_preparada` (creada en la Práctica 1) y `sedes_integracion`:

    1. **Unión relacional:** une ambas tablas en `tabla_final` mediante `pd.merge()`:
       - Clave: `on='sede'`.
       - Tipo: `how='left'`.
       - Validación: `validate='many_to_one'`.
       - Indicador: `indicator=True`.

    2. **Diccionario de control:** construye la variable `control_final` como un diccionario con exactamente estas claves y valores:
       - `'filas'`: total de filas de `tabla_final` (`len(tabla_final)`).
       - `'codigos_unicos'`: booleano de si `'codigo'` es único (`tabla_final['codigo'].is_unique`).
       - `'sedes_sin_coincidencia'`: número entero de filas donde `_merge == 'left_only'`.
       - `'edades_para_revisar'`: número entero de casos donde `"edad_para_revisar"` es `True`.
       - `'imc_completados'`: número entero de casos donde `"imc_faltaba"` es `True`.

    *Verificación esperada:* `tabla_final` debe tener 49 filas y 15 columnas; `control_final` debe reflejar la certificación completa del estudio.
    """)
    return


@app.cell
def practice_two(feedback, pd, sedes_integracion, tabla_preparada):
    # TU TURNO: crea tabla_final y control_final
    tabla_final = None
    control_final = None
    feedback.exercise("entregar_pipeline_auditado", locals())
    return control_final, tabla_final


@app.cell
def final_scorecard_view(control_final):
    if isinstance(control_final, dict):
        vista_control = {
            "Total pacientes en cohorte": control_final.get("filas"),
            "¿Clave primaria íntegra y única?": control_final.get("codigos_unicos"),
            "Sedes no reconocidas en catálogo": control_final.get("sedes_sin_coincidencia"),
            "Pacientes remitidos a revisión médica (edad)": control_final.get("edades_para_revisar"),
            "Valores de IMC imputados con trazabilidad": control_final.get("imc_completados"),
        }
    else:
        vista_control = "El scorecard se mostrará automáticamente cuando completes control_final."
    vista_control
    return (vista_control,)


@app.cell(hide_code=True)
def reflection_unit_9(mo):
    cierre_unidad_9 = mo.ui.text_area(
        label="Para cerrar: el valor de un flujo documentado",
        placeholder="Imagina que dentro de un año la cohorte del Estudio Horizonte duplica su tamaño. ¿Qué ventajas tiene haber diseñado este pipeline como código reproducible en lugar de haber limpiado los datos manualmente en Excel?",
        rows=3,
        full_width=True,
    )
    cierre_unidad_9
    return


@app.cell(hide_code=True)
def closing_unit_9(mo):
    mo.md(r"""
    ### ¡Felicitaciones! Has completado la Semana 4
    Has construido un flujo completo de ingestión, auditoría, limpieza, transformación e integración relacional siguiendo los más altos estándares de calidad analítica y reproducibilidad.
    """)
    return


if __name__ == "__main__":
    app.run()
