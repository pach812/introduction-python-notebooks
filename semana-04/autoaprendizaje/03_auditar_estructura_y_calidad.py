# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///

# ruff: noqa: B018
import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Semana 4 · 03 Auditar estructura y calidad")


@app.cell(hide_code=True)
def setup():
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    assets = Path(__file__).parent / "assets"
    feedback = load_feedback(
        mo, week="week-04-data-cleaning-wrangling", notebook="03_auditar_estructura_y_calidad"
    )
    return Path, assets, feedback, mo, pd


@app.cell(hide_code=True)
def opening(mo):
    mo.md(r"""
    # 03 · Auditar estructura y calidad antes de modificar datos

    Una de las reglas de oro de la ingeniería de datos en salud es: **nunca limpies ni modifiques un dataset sin antes haber auditado y documentado rigurosamente su estado inicial**.

    Limpiar a ciegas aplicando funciones apresuradas destruye evidencia, oculta sesgos y puede distorsionar las conclusiones epidemiológicas. Una auditoría formal produce un diagnóstico objetivo distinguiendo cuatro dimensiones:

    1. **Estructura:** dimensiones (filas $\times$ columnas), nombres exactos de variables y tipos inferidos.
    2. **Completitud:** cuantificación de valores ausentes por variable y por observación.
    3. **Consistencia de dominios:** frecuencias de categorías, presencia de espacios invisibles (`" norte "`) o mayúsculas discordantes (`"SUR"` vs `"Sur"`).
    4. **Unicidad y plausibilidad biológica:** verificación de claves primarias (¿hay pacientes duplicados?) y detección de valores fuera de rango fisiológico (ej. edad de 145 años).

    Al terminar esta unidad sabrás:
    - Aplicar `.info()`, `.describe(include='all')`, `.isna().sum()` y `.value_counts(dropna=False)`.
    - Cruzar un DataFrame contra un diccionario oficial de datos.
    - Construir filtros booleanos combinados para aislar filas que requieren revisión clínica.
    """)
    return


@app.cell
def load_datasets(assets, pd):
    # Cargamos el dataset clínico y su diccionario normativo oficial
    registros = pd.read_csv(assets / "pacientes_estudio.csv")
    diccionario = pd.read_csv(assets / "diccionario_datos.csv")
    {"Forma de registros": registros.shape, "Variables en diccionario": len(diccionario)}
    return diccionario, registros


@app.cell(hide_code=True)
def dictionary_inspection(mo):
    mo.md(r"""
    ---
    ## El Diccionario de Datos como estándar normativo

    El diccionario de datos define qué se espera de cada columna:
    - El tipo de dato previsto (`string`, `float64`, `int64`, `datetime`).
    - El rango admisible o los valores categóricos válidos.
    - Si la variable admite o prohíbe valores nulos.

    Inspeccionemos las especificaciones normativas del Estudio Horizonte:
    """)
    return


@app.cell
def view_dictionary(diccionario):
    # Mostramos el diccionario de datos de Estudio Horizonte
    diccionario[["variable", "tipo_esperado", "rango_o_valores", "admite_nulos"]]
    return


@app.cell(hide_code=True)
def explicacion_herramientas_diagnostico(mo):
    mo.md(r"""
    ---
    ## Herramientas de diagnóstico de Pandas

    Veamos cómo inspeccionar sistemáticamente la calidad con ejemplos concretos:
    1. `registros.isna().sum()`: produce una Series con el número exacto de nulos en cada variable.
    2. `registros.isna().mean() * 100`: calcula el porcentaje exacto de ausencia relativa.
    3. `registros["sede"].value_counts(dropna=False)`: revela categorías válidas, variantes con problemas de digitación y posibles nulos.
    4. `registros.duplicated(subset=["codigo"], keep=False)`: marca **todas** las apariciones de un identificador duplicado para comparar ambas filas.
    """)
    return


@app.cell
def inspection_demo(registros):
    duplicados_codigo = registros[registros.duplicated(subset=["codigo"], keep=False)]
    resumen_sedes = registros["sede"].value_counts(dropna=False)
    porcentaje_nulos = (registros.isna().mean() * 100).round(1)

    {
        "Conteo total de nulos en la tabla": int(registros.isna().sum().sum()),
        "Variables con mayor % de ausencia": porcentaje_nulos[porcentaje_nulos > 0].to_dict(),
        "Distribución de sedes recibidas (en crudo)": resumen_sedes.to_dict(),
        "Filas con código repetido para comparar": duplicados_codigo[["codigo", "fecha_visita", "sede", "edad"]],
    }
    return duplicados_codigo, porcentaje_nulos, resumen_sedes


@app.cell(hide_code=True)
def practice_one_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 1 · Auditoría de completitud y categorías

    **Consigna:**
    A partir de `registros`:
    1. Calcula el conteo de valores faltantes por cada columna y guárdalo en `faltantes_por_variable` (usa `.isna().sum()`).
    2. Calcula la frecuencia de aparición de cada sede observada, incluyendo ausencias si las hubiera, y guárdala en `frecuencia_sedes` (usa `.value_counts(dropna=False)`).

    *Nota importante:* No modifiques las etiquetas ni apliques filtros; la auditoría debe reflejar fielmente la evidencia recibida.
    """)
    return


@app.cell
def practice_one(feedback, registros):
    # TU TURNO: define faltantes_por_variable y frecuencia_sedes
    faltantes_por_variable = None
    frecuencia_sedes = None
    feedback.exercise("auditar_completitud_categorias", locals())
    return faltantes_por_variable, frecuencia_sedes


@app.cell(hide_code=True)
def finding_anomalies_concept(mo):
    mo.md(r"""
    ---
    ## Aislamiento de anomalías con máscaras booleanas compuestas

    En auditoría de datos, en lugar de eliminar observaciones sospechosas, creamos un **subconjunto de hallazgos para revisión humana**.

    Para evaluar múltiples señales de alerta utilizamos operadores lógicos vectorizados:
    - Operador O (`|`): se cumple si al menos una condición es verdadera.
    - Operador Y (`&`): se cumple si ambas condiciones son verdaderas simultáneamente.
    - Negación (`~`): invierte la condición booleana.
    - Pertenencia (`.isin([...])`): verifica si el valor pertenece a una lista de permitidos.

    *Regla sintáctica fundamental:* Cada condición individual debe ir siempre entre paréntesis: `(condición_1) | (condición_2)`.

    Veamos un ejemplo ejecutable donde aislamos pacientes con lecturas extremas de presión o IMC:
    """)
    return


@app.cell
def ejemplo_mascaras_combinadas(registros):
    # Ejemplo: detectamos mediciones hemodinámicas o antropométricas atípicas
    # Condición A: Presión sistólica fuera de rango plausible (menor a 80 o mayor a 190 mmHg)
    cond_presion = (registros["lectura_sistolica"] < 80) | (registros["lectura_sistolica"] > 190)

    # Condición B: IMC fuera de rango clínico (menor a 16 o mayor a 45)
    cond_imc = (registros["imc"] < 16) | (registros["imc"] > 45)

    # Combinamos ambas condiciones con | (se activa si ocurre cualquiera de las dos)
    alerta_mediciones = cond_presion | cond_imc

    # Filtramos la tabla para inspeccionar los casos
    casos_alerta = registros.loc[alerta_mediciones, ["codigo", "sede", "lectura_sistolica", "imc"]]

    {
        "Total pacientes con presión atípica": int(cond_presion.sum()),
        "Total pacientes con IMC atípico": int(cond_imc.sum()),
        "Total filas bajo alerta combinada (|)": int(alerta_mediciones.sum()),
        "Detalle de casos detectados": casos_alerta,
    }
    return alerta_mediciones, casos_alerta, cond_imc, cond_presion


@app.cell(hide_code=True)
def practice_two_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 2 · Localizar registros que requieren revisión clínica

    **Consigna:**
    Construye la variable `filas_para_revisar` filtrando de `registros` todas las filas que cumplan **al menos una** de las siguientes anomalías:
    1. Son filas duplicadas completas (usa `registros.duplicated(keep=False)` para conservar todas las apariciones).
    2. Tienen una edad biológicamente fuera de rango: edad menor a 18 o mayor a 110 años.
    3. Tienen una sede que no coincide exactamente con `'Norte'`, `'Sur'` o `'Centro'`.

    *Verificación esperada:* `filas_para_revisar` debe ser un DataFrame con exactamente 5 registros que ilustran estas tres situaciones.
    """)
    return


@app.cell
def practice_two(feedback, registros):
    # TU TURNO: combina las tres condiciones con | y filtra registros
    filas_para_revisar = None
    feedback.exercise("localizar_hallazgos_calidad", locals())
    return (filas_para_revisar,)


@app.cell(hide_code=True)
def reflection_unit_3(mo):
    cierre_unidad_3 = mo.ui.text_area(
        label="Para cerrar: tu diagnóstico clínico",
        placeholder="Observa las 5 filas identificadas: ¿Por qué en un ensayo clínico es un error gravísimo eliminar automáticamente el registro con edad=145 en lugar de reportarlo al centro de investigación?",
        rows=3,
        full_width=True,
    )
    cierre_unidad_3
    return


@app.cell(hide_code=True)
def closing_unit_3(mo):
    mo.md(r"""
    ### Conclusión y siguiente paso
    Ahora cuentas con un informe riguroso de calidad. En la **Unidad 04** abordaremos el tratamiento científico de los valores faltantes: cuándo es válido descartar observaciones y cómo imputar con trazabilidad.
    """)
    return


if __name__ == "__main__":
    app.run()
