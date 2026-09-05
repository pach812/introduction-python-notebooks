# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///

# ruff: noqa: B018
import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Semana 4 · 04 Tratar datos faltantes")


@app.cell(hide_code=True)
def setup():
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    assets = Path(__file__).parent / "assets"
    feedback = load_feedback(
        mo, week="week-04-data-cleaning-wrangling", notebook="04_tratar_datos_faltantes"
    )
    return Path, assets, feedback, mo, pd


@app.cell(hide_code=True)
def opening(mo):
    mo.md(r"""
    # 04 · Tratar datos faltantes con rigor científico

    En investigación clínica y epidemiológica, los valores faltantes (*missing data*) no son un simple inconveniente estético: **son información sobre el proceso de recolección**. Un dato puede faltar porque:
    - El paciente no asistió a la toma de muestra.
    - El sensor falló o arrojó un error de calibración.
    - La pregunta no aplicaba para el participante.

    Existen dos caminos fundamentales para abordar la ausencia:
    1. **Descarte controlado (*filtering / dropping*):** eliminar observaciones incompletas cuando el análisis exige estrictamente el caso completo.
    2. **Imputación con trazabilidad (*imputation with flags*):** rellenar el valor con una estimación estadística (mediana, media, valor previo) pero **marcando siempre una columna booleana que documente qué registros fueron alterados**.

    Al terminar esta unidad sabrás:
    - Aplicar `.dropna()` de forma quirúrgica con `subset=[...]` y `how=...`.
    - Comparar la pérdida de muestra entre el descarte ciego y el descarte enfocado.
    - Imputar valores numéricos mediante `.fillna()` conservando trazabilidad auditable.
    """)
    return


@app.cell
def load_data(assets, pd):
    registros_faltantes = pd.read_csv(assets / "pacientes_estudio.csv")
    {
        "Total observaciones": len(registros_faltantes),
        "Faltantes en lectura_sistolica": int(registros_faltantes["lectura_sistolica"].isna().sum()),
        "Faltantes en imc": int(registros_faltantes["imc"].isna().sum()),
    }
    return (registros_faltantes,)


@app.cell(hide_code=True)
def dropping_concept(mo):
    mo.md(r"""
    ---
    ## Descarte selectivo frente a descarte masivo

    Ejecutar `df.dropna()` sin parámetros elimina cualquier fila que tenga **al menos un valor nulo en cualquier columna**. En bases de datos con muchas variables, esto puede destruir más del 50% de la muestra de forma innecesaria.

    Pandas permite controlar el descarte mediante parámetros clave:
    - `subset=['col1', 'col2']`: restringe la evaluación únicamente a las variables indispensables para el modelo analítico.
    - `how='any'` (por defecto): descarta la fila si falta cualquiera de las variables del `subset`.
    - `how='all'`: descarta la fila solo si **todas** las variables del `subset` están ausentes.
    - `thresh=k`: conserva filas que tengan al menos $k$ valores no nulos.

    Veamos la diferencia en código ejecutable:
    """)
    return


@app.cell
def dropping_example(registros_faltantes):
    # Comparación entre descarte ciego y descarte selectivo
    descarte_masivo = registros_faltantes.dropna()
    descarte_solo_sistolica = registros_faltantes.dropna(subset=["lectura_sistolica"])
    descarte_mediciones = registros_faltantes.dropna(subset=["lectura_sistolica", "imc"])

    {
        "Total inicial de pacientes": len(registros_faltantes),
        "Filas tras dropna() ciego (todas las cols)": len(descarte_masivo),
        "Filas descartando solo si falta sistólica": len(descarte_solo_sistolica),
        "Filas descartando si falta sistólica o IMC": len(descarte_mediciones),
    }
    return (
        descarte_masivo,
        descarte_mediciones,
        descarte_solo_sistolica,
    )


@app.cell(hide_code=True)
def practice_one_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 1 · Seleccionar casos completos para protocolo hemodinámico

    **Consigna:**
    A partir de `registros_faltantes`, crea el DataFrame `casos_completos_mediciones` eliminando únicamente las observaciones donde falte **al menos una** de las siguientes variables clínicas:
    - `"lectura_sistolica"`
    - `"imc"`

    *Verificación esperada:* `casos_completos_mediciones` debe conservar exactamente 48 pacientes (descartando las 2 filas con nulos en estas dos mediciones).
    """)
    return


@app.cell
def practice_one(feedback, registros_faltantes):
    # TU TURNO: define casos_completos_mediciones usando dropna con subset
    casos_completos_mediciones = None
    feedback.exercise("seleccionar_casos_completos", locals())
    return (casos_completos_mediciones,)


@app.cell(hide_code=True)
def imputation_traceability_concept(mo):
    mo.md(r"""
    ---
    ## Imputación científica: conservar la trazabilidad

    Cuando descartar observaciones sesgaría el estudio o reduciría la potencia estadística, podemos imputar los valores faltantes (por ejemplo, con la **mediana**, que es robusta ante valores atípicos).

    **Regla metodológica de oro:**
    > *Nunca imputes una variable sobre la columna original sin crear antes una columna de auditoría.*

    El protocolo reproducible consta de 3 pasos:
    1. **Crear una copia de trabajo:** `df_limpio = df.copy()`.
    2. **Registrar la bandera de auditoría booleana:** `df_limpio['var_faltaba'] = df_limpio['var'].isna()`.
    3. **Reemplazar la ausencia:** `df_limpio['var'] = df_limpio['var'].fillna(valor_imputacion)`.

    Veamos una demostración completa con la presión sistólica:
    """)
    return


@app.cell
def imputation_demo(registros_faltantes):
    # Demostración del flujo con trazabilidad
    copia_demo = registros_faltantes.copy()

    # 1. Bandera booleana antes de imputar
    copia_demo["sistolica_faltaba"] = copia_demo["lectura_sistolica"].isna()

    # 2. Imputación con la mediana
    mediana_sistolica = copia_demo["lectura_sistolica"].median()
    copia_demo["lectura_sistolica"] = copia_demo["lectura_sistolica"].fillna(mediana_sistolica)

    {
        "Mediana calculada para sistólica": float(mediana_sistolica),
        "Nulos remanentes en sistólica": int(copia_demo["lectura_sistolica"].isna().sum()),
        "Total de valores imputados (bandera True)": int(copia_demo["sistolica_faltaba"].sum()),
        "Muestra de filas imputadas": copia_demo.loc[
            copia_demo["sistolica_faltaba"], ["codigo", "sede", "lectura_sistolica", "sistolica_faltaba"]
        ],
    }
    return copia_demo, mediana_sistolica


@app.cell(hide_code=True)
def practice_two_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 2 · Imputar IMC con bandera de auditoría

    **Consigna:**
    A partir de `registros_faltantes`:
    1. Crea una copia independiente llamada `tabla_imc_completado` con `.copy()`.
    2. Crea en esa tabla una nueva columna booleana llamada `"imc_faltaba"` que valga `True` si `"imc"` es nulo y `False` si ya tenía dato.
    3. Calcula la mediana de `"imc"` sobre los datos no nulos.
    4. Rellena los valores ausentes de `"imc"` con dicha mediana usando `.fillna(...)`.

    *Verificación esperada:* `tabla_imc_completado` debe tener 50 filas, 11 columnas, 0 nulos en `"imc"`, y exactamente 1 fila con `"imc_faltaba" == True`.
    """)
    return


@app.cell
def practice_two(feedback, registros_faltantes):
    # TU TURNO: implementa la copia, la bandera booleana imc_faltaba y la imputación con la mediana
    tabla_imc_completado = None
    feedback.exercise("completar_con_trazabilidad", locals())
    return (tabla_imc_completado,)


@app.cell(hide_code=True)
def reflection_unit_4(mo):
    cierre_unidad_4 = mo.ui.text_area(
        label="Para cerrar: trazabilidad ante una auditoría",
        placeholder="Si un auditor clínico te pregunta: '¿Cuáles pacientes recibieron un valor sintético de IMC?', ¿cómo te permite responder de inmediato la columna imc_faltaba?",
        rows=3,
        full_width=True,
    )
    cierre_unidad_4
    return


@app.cell(hide_code=True)
def closing_unit_4(mo):
    mo.md(r"""
    ### Conclusión y siguiente paso
    Has aprendido a tratar datos faltantes con transparencia metodológica. En la **Unidad 05** abordaremos la limpieza de texto, la corrección de etiquetas categóricas, el casteo a tipos específicos y la resolución de duplicados en claves primarias.
    """)
    return


if __name__ == "__main__":
    app.run()
