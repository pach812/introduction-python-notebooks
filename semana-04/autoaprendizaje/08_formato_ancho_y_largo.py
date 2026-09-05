# ruff: noqa: B018
import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Semana 4 · 08 Formato ancho y largo")


@app.cell(hide_code=True)
def setup():
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    assets = Path(__file__).parent / "assets"
    feedback = load_feedback(
        mo, week="week-04-data-cleaning-wrangling", notebook="08_formato_ancho_y_largo"
    )
    return Path, assets, feedback, mo, pd


@app.cell(hide_code=True)
def opening(mo):
    mo.md(r"""
    # 08 · Reestructurar tablas: Formato Ancho y Formato Largo (*Tidy Data*)

    En recolección clínica es muy común registrar mediciones repetidas en **formato ancho (*wide format*)**: una columna por cada visita o momento en el tiempo (ej. `pas_inicial`, `pas_mes_1`, `pas_mes_3`).

    Sin embargo, los paquetes estadísticos modernos, las librerías de visualización (como Seaborn o Plotly) y los modelos de efectos mixtos exigen **formato largo (*long / tidy format*)**:
    - Cada variable debe formar una sola columna.
    - Cada observación o medición en el tiempo debe constituir una fila independiente.

    Pandas ofrece dos herramientas de reestructuración simétricas:
    1. **`pd.melt()`:** pasa de formato ancho a formato largo (*unpivot*).
    2. **`pd.pivot_table()`:** pasa de formato largo a matrices bidimensionales agregadas (*pivot*).

    Al terminar esta unidad sabrás:
    - Remodelar tablas de seguimiento longitudinal con `pd.melt()`.
    - Construir matrices de resumen estadístico con `pd.pivot_table()`.
    """)
    return


@app.cell
def load_data(assets, pd):
    presion_ancha = pd.read_csv(assets / "presion_ancha.csv")
    {
        "Pacientes en tabla ancha": len(presion_ancha),
        "Columnas observadas": presion_ancha.columns.tolist(),
        "Primeras 3 filas (formato ancho)": presion_ancha.head(3),
    }
    return (presion_ancha,)


@app.cell(hide_code=True)
def melt_concept(mo):
    mo.md(r"""
    ---
    ## De formato ancho a formato largo con `pd.melt()`

    La función `pd.melt()` "desenrolla" las columnas de mediciones repetidas:
    - `id_vars=[...]`: lista de columnas identificadoras fijas que **no** deben alterarse (ej. paciente, sede, sexo).
    - `value_vars=[...]`: lista de columnas que contienen las mediciones a colapsar en filas (ej. `['pas_inicial', 'pas_mes_1', 'pas_mes_3']`).
    - `var_name='nombre_variable'`: nombre de la nueva columna que almacenará qué medición se tomó.
    - `value_name='nombre_valor'`: nombre de la nueva columna que almacenará el valor numérico registrado.

    Veamos una demostración con un ejemplo compacto de dos pacientes:
    """)
    return


@app.cell
def ejemplo_melt_demostracion(pd):
    # Demostración pedagógica de melt con 2 pacientes y 2 momentos
    tabla_mini_ancha = pd.DataFrame({
        "codigo": ["HOR-001", "HOR-002"],
        "sede": ["Norte", "Sur"],
        "basal": [120, 135],
        "seguimiento": [115, 128],
    })

    tabla_mini_larga = pd.melt(
        tabla_mini_ancha,
        id_vars=["codigo", "sede"],
        value_vars=["basal", "seguimiento"],
        var_name="visita",
        value_name="presion",
    )

    {
        "Forma antes (ancho)": tabla_mini_ancha.shape,
        "Tabla original ancha": tabla_mini_ancha,
        "Forma después (largo)": tabla_mini_larga.shape,
        "Tabla resultante larga": tabla_mini_larga,
    }
    return tabla_mini_ancha, tabla_mini_larga


@app.cell(hide_code=True)
def practice_one_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 1 · Convertir el seguimiento de presión a formato largo

    **Consigna:**
    A partir de `presion_ancha`:
    1. Aplica `pd.melt()` para reestructurar las tres mediciones temporales.
    2. Identificadores que se mantienen: `id_vars=["codigo", "sede", "sexo_reportado"]`.
    3. Mediciones a transformar: `value_vars=["pas_inicial", "pas_mes_1", "pas_mes_3"]`.
    4. Nombre de la columna de momento: `var_name="tiempo"`.
    5. Nombre de la columna de valor: `value_name="pas"`.
    6. Asigna el resultado a `presion_larga`.

    *Verificación esperada:* Como hay 12 pacientes y 3 momentos, `presion_larga` debe tener exactamente $12 \times 3 = 36$ filas y 5 columnas.
    """)
    return


@app.cell
def practice_one(feedback, pd, presion_ancha):
    # TU TURNO: transforma presion_ancha a formato largo con pd.melt
    presion_larga = None
    feedback.exercise("convertir_a_formato_largo", locals())
    return (presion_larga,)


@app.cell(hide_code=True)
def pivot_table_concept(mo):
    mo.md(r"""
    ---
    ## Agregación bidimensional con `pd.pivot_table()`

    Una vez los datos están en formato largo, `pd.pivot_table()` permite generar reportes agregados estructurados en filas y columnas cruzadas:
    - `index='columna_filas'`: variable categórica que definirá las filas (ej. la sede).
    - `columns='columna_encabezados'`: variable que definirá las columnas (ej. el momento de medición).
    - `values='columna_valores'`: variable numérica sobre la cual se calculará el resumen (ej. la presión sistólica `pas`).
    - `aggfunc='mean'` (o `'median'`, `'count'`, etc.): función de agregación estadística.

    Veamos un ejemplo ejecutable sobre la tabla larga pequeña construida arriba:
    """)
    return


@app.cell
def ejemplo_pivot_table_demostracion(pd, tabla_mini_larga):
    # Demostración de pivot_table
    resumen_pivote = pd.pivot_table(
        tabla_mini_larga,
        index="sede",
        columns="visita",
        values="presion",
        aggfunc="mean",
    )
    {
        "Resumen matricial generado con pivot_table": resumen_pivote,
        "Filas del pivote": resumen_pivote.index.tolist(),
        "Columnas del pivote": resumen_pivote.columns.tolist(),
    }
    return (resumen_pivote,)


@app.cell(hide_code=True)
def practice_two_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 2 · Matriz de presión media por sede y tiempo

    **Consigna:**
    A partir de `presion_larga` (creada en la Práctica 1):
    1. Construye una tabla pivote que resuma la **presión arterial media** por sede y momento de seguimiento.
    2. En las filas: `"sede"`.
    3. En las columnas: `"tiempo"`.
    4. En los valores numéricos: `"pas"`.
    5. Función de agregación: `'mean'`.
    6. Redondea los resultados a 1 decimal con `.round(1)`.
    7. Asigna el resultado a `presion_media_sede_tiempo`.

    *Verificación esperada:* `presion_media_sede_tiempo` debe ser una matriz de 3 filas (sedes) por 3 columnas (momentos).
    """)
    return


@app.cell
def practice_two(feedback, pd, presion_larga):
    # TU TURNO: construye la tabla pivote de medias por sede y tiempo
    presion_media_sede_tiempo = None
    feedback.exercise("resumir_con_pivot_table", locals())
    return (presion_media_sede_tiempo,)


@app.cell(hide_code=True)
def reflection_unit_8(mo):
    cierre_unidad_8 = mo.ui.text_area(
        label="Para cerrar: ¿cuándo usar cada formato?",
        placeholder="Si vas a graficar la evolución de la presión en el tiempo usando una curva por paciente con Seaborn, ¿por qué es indispensable tener los datos en formato largo en vez de ancho?",
        rows=3,
        full_width=True,
    )
    cierre_unidad_8
    return


@app.cell(hide_code=True)
def closing_unit_8(mo):
    mo.md(r"""
    ### Conclusión y siguiente paso
    Has dominado la reestructuración bidireccional entre formato ancho y formato largo. En la **Unidad 09** integraremos todas las técnicas de la semana en un flujo de preparación reproducible de punta a punta, auditado con un reporte formal de calidad (*scorecard*).
    """)
    return


if __name__ == "__main__":
    app.run()
