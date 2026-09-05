# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///

# ruff: noqa: B018
import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Semana 4 · 05 Corregir etiquetas, tipos y duplicados")


@app.cell(hide_code=True)
def setup():
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    assets = Path(__file__).parent / "assets"
    feedback = load_feedback(
        mo,
        week="week-04-data-cleaning-wrangling",
        notebook="05_corregir_etiquetas_tipos_duplicados",
    )
    return Path, assets, feedback, mo, pd


@app.cell(hide_code=True)
def opening(mo):
    mo.md(r"""
    # 05 · Corregir etiquetas, tipos de datos y duplicados

    Los datos del mundo real rara vez llegan limpios y homogéneos. Cuando múltiples centros u operadores digitan información de forma descentralizada, aparecen inconsistencias comunes:
    - Espacios accidentales al inicio o final de las cadenas (`" Norte "` vs `"Norte"`).
    - Variaciones de mayúsculas y minúsculas (`"SUR"` vs `"Sur"` vs `"sur"`).
    - Identificadores o números de visita almacenados como números decimales (`1.0`) o texto genérico en lugar de enteros o cadenas estrictas.
    - Observaciones duplicadas que violan el principio de unicidad de la clave primaria.

    Al terminar esta unidad sabrás:
    - Utilizar el accesor `.str` de Pandas (`strip()`, `title()`, `replace()`).
    - Convertir columnas a tipos con soporte de nulos (`string`, `Int64`).
    - Identificar y resolver duplicados con `.drop_duplicates(subset=..., keep=...)`.
    """)
    return


@app.cell
def load_data(assets, pd):
    registros_crudos = pd.read_csv(assets / "pacientes_estudio.csv")
    {
        "Sedes observadas en crudo": registros_crudos["sede"].unique().tolist(),
        "Tipo inferido para codigo": str(registros_crudos["codigo"].dtype),
        "Tipo inferido para numero_visitas": str(registros_crudos["numero_visitas"].dtype),
        "Filas duplicadas en codigo": int(registros_crudos.duplicated(subset=["codigo"]).sum()),
    }
    return (registros_crudos,)


@app.cell(hide_code=True)
def string_methods_concept(mo):
    mo.md(r"""
    ---
    ## El accesor `.str` y la conversión de tipos en Pandas

    Pandas ofrece un conjunto completo de operaciones vectorizadas de texto mediante el accesor `.str`:
    - `.str.strip()`: retira espacios en blanco al inicio y al final.
    - `.str.title()`: convierte a formato tipo título (primera letra de cada palabra en mayúscula: `"norte"` $\rightarrow$ `"Norte"`).
    - `.str.lower()` y `.str.upper()`: normalizan a minúsculas o mayúsculas completas.
    - `.str.replace(patron, reemplazo, regex=True)`: limpia caracteres no deseados con expresiones regulares.

    Además, los métodos `.astype("string")` y `.astype("Int64")` aplican los tipos modernos de Pandas, que admiten valores ausentes sin degradar enteros a decimales `float64`.

    Veamos una demostración práctica con las sedes y códigos:
    """)
    return


@app.cell
def string_demo(registros_crudos):
    # Demostración de limpieza de texto y casteo de tipos
    sede_limpia = registros_crudos["sede"].str.strip().str.title()
    codigo_estricto = registros_crudos["codigo"].astype("string")
    visitas_enteras = registros_crudos["numero_visitas"].astype("Int64")

    {
        "Sedes antes de limpiar": registros_crudos["sede"].unique().tolist(),
        "Sedes tras strip() y title()": sede_limpia.unique().tolist(),
        "Tipo de codigo resultante": str(codigo_estricto.dtype),
        "Tipo de numero_visitas resultante": str(visitas_enteras.dtype),
    }
    return codigo_estricto, sede_limpia, visitas_enteras


@app.cell(hide_code=True)
def practice_one_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 1 · Normalizar texto y tipos de columnas clave

    **Consigna:**
    A partir de `registros_crudos`, crea el DataFrame `registros_normalizados` aplicando:
    1. Una copia de la tabla original con `.copy()`.
    2. La normalización de la columna `"sede"`: retira espacios en blanco con `.str.strip()` y aplica formato de título con `.str.title()`.
    3. El casteo explícito de `"codigo"` al tipo `"string"`.
    4. El casteo de `"numero_visitas"` al tipo entero con soporte de nulos `"Int64"`.

    *Verificación esperada:* En `registros_normalizados`, las únicas sedes observadas deben ser exactamente `['Norte', 'Sur', 'Centro']`.
    """)
    return


@app.cell
def practice_one(feedback, registros_crudos):
    # TU TURNO: crea registros_normalizados con las transformaciones requeridas
    registros_normalizados = None
    feedback.exercise("normalizar_etiquetas_tipos", locals())
    return (registros_normalizados,)


@app.cell(hide_code=True)
def duplicates_concept(mo):
    mo.md(r"""
    ---
    ## Detección y resolución de duplicados en claves primarias

    En una tabla donde cada fila debe representar a un paciente único, dos filas con el mismo identificador (`codigo`) constituyen una violación de integridad relacional.

    Pandas ofrece dos herramientas complementarias:
    1. `.duplicated(subset=['codigo'], keep=...)`:
       - `keep='first'` (por defecto): marca como `True` todas las repeticiones excepto la primera.
       - `keep='last'`: marca como `True` todas las repeticiones excepto la última.
       - `keep=False`: marca como `True` **todas** las apariciones repetidas para poder compararlas antes de decidir.
    2. `.drop_duplicates(subset=['codigo'], keep='first')`:
       - Conserva la primera ocurrencia y elimina las réplicas posteriores.

    Veamos un ejemplo inspeccionando las filas repetidas antes de deduplicar:
    """)
    return


@app.cell
def duplicates_demo(registros_crudos):
    # Inspección de duplicados antes de remover
    filas_con_codigo_repetido = registros_crudos[
        registros_crudos.duplicated(subset=["codigo"], keep=False)
    ]
    tabla_deduplicada_demo = registros_crudos.drop_duplicates(subset=["codigo"], keep="first")

    {
        "Total filas antes": len(registros_crudos),
        "Filas duplicadas encontradas": len(filas_con_codigo_repetido),
        "Total filas tras deduplicar": len(tabla_deduplicada_demo),
        "¿La clave 'codigo' es ahora única?": bool(tabla_deduplicada_demo["codigo"].is_unique),
        "Detalle de las filas que estaban repetidas": filas_con_codigo_repetido[["codigo", "fecha_visita", "sede"]],
    }
    return filas_con_codigo_repetido, tabla_deduplicada_demo


@app.cell(hide_code=True)
def practice_two_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 2 · Resolver la duplicación de clave primaria

    **Consigna:**
    A partir de `registros_normalizados` (producido en la Práctica 1):
    1. Elimina las observaciones que repitan el `"codigo"`, conservando la primera aparición (`keep='first'`).
    2. Asigna la tabla limpia resultante a la variable `registros_sin_duplicados`.

    *Verificación esperada:* `registros_sin_duplicados` debe tener exactamente 49 filas y su columna `"codigo"` debe ser completamente única (`is_unique == True`).
    """)
    return


@app.cell
def practice_two(feedback, registros_normalizados):
    # TU TURNO: define registros_sin_duplicados con drop_duplicates(subset=['codigo'], keep='first')
    registros_sin_duplicados = None
    feedback.exercise("resolver_duplicados", locals())
    return (registros_sin_duplicados,)


@app.cell(hide_code=True)
def reflection_unit_5(mo):
    cierre_unidad_5 = mo.ui.text_area(
        label="Para cerrar: duplicados en claves primarias",
        placeholder="Si descubres que un paciente tiene dos registros con distinta fecha de visita, ¿por qué keep='first' requiere ser una decisión explícita y documentada en el protocolo de investigación?",
        rows=3,
        full_width=True,
    )
    cierre_unidad_5
    return


@app.cell(hide_code=True)
def closing_unit_5(mo):
    mo.md(r"""
    ### Conclusión y siguiente paso
    Has consolidado la consistencia de tipos, textos y unicidad. En la **Unidad 06** aprenderemos a transformar variables continuas: detectando valores atípicos mediante banderas booleanas y construyendo grupos etarios mediante discretización controlada (`pd.cut`).
    """)
    return


if __name__ == "__main__":
    app.run()
