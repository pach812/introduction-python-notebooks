# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///

# ruff: noqa: B018
import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Semana 4 · 06 Transformar variables")


@app.cell(hide_code=True)
def setup():
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    assets = Path(__file__).parent / "assets"
    feedback = load_feedback(
        mo, week="week-04-data-cleaning-wrangling", notebook="06_transformar_variables"
    )
    return Path, assets, feedback, mo, pd


@app.cell(hide_code=True)
def opening(mo):
    mo.md(r"""
    # 06 · Transformar y derivar variables con justificación

    La ingeniería de variables (*feature engineering*) en estudios de salud y bioestadística no consiste en aplicar funciones al azar. Cada transformación debe responder a una justificación clínica o metodológica:
    1. **Banderas de alerta (*outlier tagging*):** marcar observaciones cuyos valores escapan a límites biológicos razonables (ej. edades mayores a 110 años o menores de edad en cohortes adultas) para revisión por el equipo médico, en lugar de borrarlas silenciosamente.
    2. **Discretización en categorías (*binning*):** convertir variables numéricas continuas (como edad, presión arterial o IMC) en estratos clínicos estandarizados mediante `pd.cut()` y `pd.qcut()`.

    Al terminar esta unidad sabrás:
    - Crear columnas booleanas de alerta basadas en rangos de plausibilidad.
    - Configurar `pd.cut()` con puntos de corte (`bins`) y nombres de grupo (`labels`).
    - Entender la diferencia entre intervalos cerrados por derecha o izquierda.
    """)
    return


@app.cell
def load_data(assets, pd):
    tabla_base = pd.read_csv(assets / "pacientes_estudio.csv")
    {
        "Rango de edad observado": (float(tabla_base["edad"].min()), float(tabla_base["edad"].max())),
        "Rango de IMC observado": (float(tabla_base["imc"].min()), float(tabla_base["imc"].max())),
        "Rango de sistólica": (float(tabla_base["lectura_sistolica"].min()), float(tabla_base["lectura_sistolica"].max())),
    }
    return (tabla_base,)


@app.cell(hide_code=True)
def outlier_masking_concept(mo):
    mo.md(r"""
    ---
    ## Señalización de valores atípicos mediante banderas booleanas

    Cuando un valor viola el rango de plausibilidad biológica (por ejemplo, un error tipográfico donde se digitó una edad de 145 años o una presión de 30 mmHg incompatible con la vida), **la mejor práctica no es borrar la fila entera**, sino crear una columna booleana indicadora.

    Esto permite que los análisis posteriores puedan filtrar o estratificar fácilmente los datos dudosos sin perder la pista del paciente.

    Para construir una bandera de alerta combinando condiciones:
    $$\text{condicion} = (\text{serie} < \text{limite\_inferior}) \mid (\text{serie} > \text{limite\_superior})$$

    Veamos un ejemplo ejecutable marcando presiones sistólicas fuera de rango:
    """)
    return


@app.cell
def ejemplo_marcado_anomalias(pd, tabla_base):
    # Demostración: marcamos presiones fuera de rango plausible (80 a 200 mmHg)
    muestra_demo = tabla_base.copy()
    cond_anomala = (muestra_demo["lectura_sistolica"] < 80) | (muestra_demo["lectura_sistolica"] > 200)

    muestra_demo["sistolica_para_revisar"] = cond_anomala

    {
        "Casos marcados para revisión médica": int(muestra_demo["sistolica_para_revisar"].sum()),
        "Detalle de casos identificados": muestra_demo.loc[
            muestra_demo["sistolica_para_revisar"], ["codigo", "sede", "lectura_sistolica", "sistolica_para_revisar"]
        ],
    }
    return cond_anomala, muestra_demo


@app.cell(hide_code=True)
def practice_one_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 1 · Señalizar edades fuera de rango de plausibilidad

    **Consigna:**
    A partir de `tabla_base`:
    1. Crea una copia de trabajo con `.copy()`.
    2. Crea una nueva columna booleana llamada `"edad_para_revisar"`.
    3. Asigna `True` a aquellos registros cuya edad sea **menor a 18** o **mayor a 110** años, y `False` al resto.
    4. Guarda la tabla resultante en `tabla_con_revision`.

    *Verificación esperada:* `tabla_con_revision` debe tener 50 filas, 11 columnas y exactamente 1 fila con `"edad_para_revisar" == True` (el paciente con 145 años).
    """)
    return


@app.cell
def practice_one(feedback, tabla_base):
    # TU TURNO: crea tabla_con_revision con la bandera booleana edad_para_revisar
    tabla_con_revision = None
    feedback.exercise("marcar_valores_fuera_dominio", locals())
    return (tabla_con_revision,)


@app.cell(hide_code=True)
def discretization_concept(mo):
    mo.md(r"""
    ---
    ## Discretización en estratos clínicos con `pd.cut`

    La función `pd.cut()` convierte una variable cuantitativa continua en una variable categórica ordinal según intervalos (*bins*):
    - `bins=[b0, b1, b2, ...]`: define los límites de los intervalos. Un valor $x$ caerá en el primer intervalo si $b_0 < x \le b_1$.
    - `labels=['Etiqueta1', 'Etiqueta2', ...]`: asigna nombres legibles a cada intervalo. La lista debe tener exactamente un elemento menos que `bins`.
    - `right=True` (por defecto): los intervalos son cerrados por la derecha $(b_0, b_1]$.

    Veamos un ejemplo ejecutable clasificando el IMC en categorías según estándares nutricionales:
    """)
    return


@app.cell
def cut_demo(pd, tabla_base):
    # Ejemplo de pd.cut sobre el IMC
    limites_imc = [0, 24.9, 29.9, 100]
    etiquetas_imc = ["Normal", "Sobrepeso", "Obesidad"]

    categoria_imc = pd.cut(
        tabla_base["imc"],
        bins=limites_imc,
        labels=etiquetas_imc,
        right=True,
    )
    {
        "Frecuencia por categoría de IMC": categoria_imc.value_counts(dropna=False).to_dict(),
        "Muestra de participantes clasificados": pd.DataFrame(
            {"imc": tabla_base["imc"], "categoria_imc": categoria_imc}
        ).head(4),
    }
    return categoria_imc, etiquetas_imc, limites_imc


@app.cell(hide_code=True)
def practice_two_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 2 · Estratificación etaria con `pd.cut`

    **Consigna:**
    A partir de `tabla_con_revision` (producida en la Práctica 1):
    1. Agrega una nueva columna llamada `"grupo_edad"` usando `pd.cut()`.
    2. Límites de corte: `[0, 39, 59, 150]`.
    3. Etiquetas correspondientes: `["Joven", "Adulto", "Adulto Mayor"]`.
    4. Asigna el DataFrame resultante a `tabla_con_grupo_edad`.

    *Interpretación clínica:*
    - `Joven`: $(0, 39]$ años.
    - `Adulto`: $(39, 59]$ años.
    - `Adulto Mayor`: $(59, 150]$ años.

    *Verificación esperada:* `tabla_con_grupo_edad` debe tener 50 filas, 12 columnas y la columna `"grupo_edad"` clasificada sin generar valores nulos en edades válidas.
    """)
    return


@app.cell
def practice_two(feedback, pd, tabla_con_revision):
    # TU TURNO: añade grupo_edad con pd.cut
    tabla_con_grupo_edad = None
    feedback.exercise("crear_intervalos_edad", locals())
    return (tabla_con_grupo_edad,)


@app.cell(hide_code=True)
def reflection_unit_6(mo):
    cierre_unidad_6 = mo.ui.text_area(
        label="Para cerrar: comparar formas de agrupar",
        placeholder="Explica con tus palabras: ¿En qué se diferencia pd.cut() (que usa límites preestablecidos) de pd.qcut() (que divide en cuantiles de igual tamaño)? ¿Cuál usarías para percentiles de crecimiento?",
        rows=3,
        full_width=True,
    )
    cierre_unidad_6
    return


@app.cell
def closing_unit_6(mo):
    mo.md(r"""
    ### Conclusión y siguiente paso
    Has dominado la creación de variables derivadas con sustento metodológico. En la **Unidad 07** abordaremos la integración de fuentes heterogéneas: cruzando pacientes con sedes mediante `pd.merge()` y apilando jornadas operativas mediante `pd.concat()`.
    """)
    return


if __name__ == "__main__":
    app.run()
