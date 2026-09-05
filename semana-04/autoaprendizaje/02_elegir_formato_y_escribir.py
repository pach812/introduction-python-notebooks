# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///

# ruff: noqa: B018
import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Semana 4 · 02 Elegir formato y escribir")


@app.cell(hide_code=True)
def setup():
    from io import StringIO
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    assets = Path(__file__).parent / "assets"
    feedback = load_feedback(
        mo, week="week-04-data-cleaning-wrangling", notebook="02_elegir_formato_y_escribir"
    )
    return StringIO, Path, assets, feedback, mo, pd


@app.cell(hide_code=True)
def opening(mo):
    mo.md(r"""
    # 02 · Elegir formato y escribir con fidelidad de tipos

    En ciencia de datos, guardar una tabla no es simplemente volcar texto en un disco. Es elegir un **contrato de almacenamiento**. Cada formato tiene ventajas, compromisos y límites:

    | Formato | Estructura | Fidelidad de Tipos | Eficiencia en Espacio / I/O | Caso de uso principal |
    | :--- | :--- | :--- | :--- | :--- |
    | **CSV / TSV** | Texto plano delimitado | **Baja** (todo se serializa a texto; pierde datetimes, categorías) | Baja (sin comprimir, lectura lenta) | Intercambio universal simple entre herramientas heterogéneas |
    | **Parquet** | Binario columnar comprimido (Apache Arrow) | **Máxima** (preserva tipos exactos, nulos, metadatos y esquemas) | Sobresaliente (compresión Snappy/ZSTD, escaneo selectivo) | Almacenamiento analítico estándar en Big Data y Machine Learning |
    | **Excel (`.xlsx`)** | Libro comprimido XML con múltiples hojas | **Media** (interpreta tipos según configuración local de Excel) | Baja / Media (lento en archivos de más de 100.000 filas) | Reportes ejecutivos para usuarios finales no programadores |
    | **Pickle (`.pkl`)** | Binario específico de Python (objeto serializado) | **Alta** (preserva cualquier objeto de Python) | Rápido pero peligroso (inseguro ante código malicioso; no interoperable) | Almacenamiento temporal entre sesiones de Python |

    Al terminar esta unidad sabrás:
    1. Inspeccionar y extraer hojas individuales de libros Excel complejos con `pd.ExcelFile`.
    2. Comparar la preservación de esquemas entre CSV y Parquet.
    3. Validar ciclos completos de persistencia de ida y vuelta (*roundtrip*).
    """)
    return


@app.cell(hide_code=True)
def concept_schema_fidelity(mo):
    mo.md(r"""
    ---
    ## La trampa del CSV: pérdida silenciosa de tipos de datos

    Cuando guardas un DataFrame con columnas de fechas (`datetime64`), enteros con valores nulos (`Int64`) o variables categóricas en formato CSV, toda la información de tipo se disuelve en caracteres de texto plano. Al volver a abrirlo con `pd.read_csv()`:
    - Las fechas se convierten en cadenas de texto genéricas (`object`).
    - Los enteros con ausencias suelen forzarse a números decimales (`float64`).
    - Las categorías se revierten a texto libre.

    En contraste, **Apache Parquet** guarda los metadatos del esquema en el encabezado del archivo. Al recargarlo con `pd.read_parquet()`, los tipos regresan exactamente iguales sin necesidad de reconfiguración manual.

    Veamos la comparación en código:
    """)
    return


@app.cell
def parquet_vs_csv_demo(assets, pd):
    # Leemos la versión Parquet y la versión CSV para comparar tipos de datos recuperados
    df_parquet = pd.read_parquet(assets / "pacientes_estudio.parquet")
    df_csv = pd.read_csv(assets / "pacientes_estudio.csv")

    comparativa_tipos = pd.DataFrame(
        {
            "Tipo en Parquet": df_parquet.dtypes.astype(str),
            "Tipo en CSV (sin configurar)": df_csv.dtypes.astype(str),
            "¿Mantiene tipo exacto?": df_parquet.dtypes == df_csv.dtypes,
        }
    )
    {
        "Comparación de Tipos (muestra)": comparativa_tipos.loc[
            ["codigo", "fecha_visita", "visita_numero", "imc"]
        ]
    }
    return comparativa_tipos, df_csv, df_parquet


@app.cell(hide_code=True)
def excel_concept_explanation(mo):
    mo.md(r"""
    ---
    ## Trabajar con hojas de cálculo de Excel (`pd.ExcelFile`)

    En el ámbito clínico y administrativo es común recibir libros de cálculo con múltiples pestañas o metadatos de auditoría.

    Si ejecutas `pd.read_excel("archivo.xlsx")`, Pandas leerá únicamente la primera hoja por defecto.
    Para inspeccionar qué hojas contiene el archivo y elegir cuál cargar eficientemente:
    1. Abre el archivo con `excel = pd.ExcelFile(ruta)`.
    2. Consulta sus pestañas mediante el atributo `excel.sheet_names`.
    3. Carga la pestaña elegida con `pd.read_excel(excel, sheet_name="nombre_hoja")`.

    Veamos un ejemplo detallado cargando e inspeccionando las dos pestañas del libro del estudio:
    """)
    return


@app.cell
def ejemplo_inspeccion_excel(assets, pd):
    # Inspección de un libro de Excel con pd.ExcelFile
    ruta_excel = assets / "paquete_estudio.xlsx"
    lector_excel = pd.ExcelFile(ruta_excel)

    # Listar hojas disponibles
    nombres_hojas = lector_excel.sheet_names

    # Cargar selectivamente cada hoja
    muestra_pacientes = pd.read_excel(lector_excel, sheet_name="pacientes").head(2)
    muestra_sedes = pd.read_excel(lector_excel, sheet_name="sedes")

    {
        "Hojas encontradas en el libro": nombres_hojas,
        "Vista preliminar hoja 'pacientes' (2 filas)": muestra_pacientes[["codigo", "sede", "lectura_sistolica"]],
        "Vista completa hoja 'sedes'": muestra_sedes,
    }
    return lector_excel, muestra_pacientes, muestra_sedes, nombres_hojas, ruta_excel


@app.cell(hide_code=True)
def practice_one_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 1 · Inspeccionar y extraer una hoja de Excel

    **Consigna:**
    A partir de `ruta_excel`:
    1. Obtén la lista con los nombres de todas las hojas disponibles y guárdala en `hojas_disponibles` (debe ser una lista de cadenas de texto).
    2. Carga la hoja llamada exactamente `"sedes"` en la variable `tabla_sedes_excel`.

    *Verificación esperada:* `hojas_disponibles` debe contener `['pacientes', 'sedes']` y `tabla_sedes_excel` debe tener las 3 sedes del estudio.
    """)
    return


@app.cell
def practice_one(feedback, pd, ruta_excel):
    # TU TURNO: define hojas_disponibles y tabla_sedes_excel
    hojas_disponibles = None
    tabla_sedes_excel = None
    feedback.exercise("inspeccionar_libro_excel", locals())
    return hojas_disponibles, tabla_sedes_excel


@app.cell(hide_code=True)
def roundtrip_concept(mo):
    mo.md(r"""
    ---
    ## El ciclo de ida y vuelta (*roundtrip*)

    Llamamos **roundtrip** al ciclo completo de:
    $$\text{DataFrame en Memoria} \xrightarrow{\text{guardar}} \text{Disco} \xrightarrow{\text{cargar}} \text{DataFrame Recuperado}$$

    Un formato de alta fidelidad garantiza que:
    $$\text{DataFrame Recuperado.equals(DataFrame Original)} == \text{True}$$

    Comparemos qué sucede con el ciclo roundtrip en CSV frente a Parquet:
    """)
    return


@app.cell
def roundtrip_demo(assets, pd):
    # Demostración del ciclo roundtrip
    fuente_roundtrip = pd.read_csv(assets / "pacientes_estudio.csv")
    fuente_roundtrip["fecha_visita"] = pd.to_datetime(fuente_roundtrip["fecha_visita"])

    import tempfile
    with tempfile.TemporaryDirectory() as _dir_temporal:
        _ruta_temp_csv = Path(_dir_temporal) / "prueba.csv"
        _ruta_temp_parquet = Path(_dir_temporal) / "prueba.parquet"

        # Roundtrip en CSV
        fuente_roundtrip.to_csv(_ruta_temp_csv, index=False)
        _recuperado_csv = pd.read_csv(_ruta_temp_csv)

        # Roundtrip en Parquet
        fuente_roundtrip.to_parquet(_ruta_temp_parquet, index=False)
        _recuperado_parquet = pd.read_parquet(_ruta_temp_parquet)

        resultado_roundtrip = {
            "CSV conserva datetime original": str(_recuperado_csv["fecha_visita"].dtype) == "datetime64[ns]",
            "Parquet conserva datetime original": str(_recuperado_parquet["fecha_visita"].dtype) == "datetime64[ns]",
            "¿Parquet es idéntico a la fuente (equals)?": bool(_recuperado_parquet.equals(fuente_roundtrip)),
        }

    resultado_roundtrip
    return fuente_roundtrip, resultado_roundtrip


@app.cell(hide_code=True)
def practice_two_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 2 · Validar persistencia exacta con Parquet

    **Consigna:**
    A partir de `fuente_roundtrip`:
    1. Exporta la tabla a un archivo temporal Parquet (usa `ruta_temporal_parquet = assets / "temporal_pacientes.parquet"` con `to_parquet(..., index=False)`).
    2. Vuelve a cargar ese archivo en la variable `recuperado_parquet` con `pd.read_parquet(...)`.
    3. Evalúa si el DataFrame recuperado es idéntico al original usando `fuente_roundtrip.equals(recuperado_parquet)` y asigna el resultado booleano a `es_identico`.

    *Verificación esperada:* `recuperado_parquet` debe ser un DataFrame y `es_identico` debe ser `True`.
    """)
    return


@app.cell
def practice_two(assets, feedback, fuente_roundtrip, pd):
    # TU TURNO: ejecuta el ciclo roundtrip y asigna el resultado
    recuperado_parquet = None
    es_identico = None
    feedback.exercise("validar_roundtrip_parquet", locals())
    return es_identico, recuperado_parquet


@app.cell(hide_code=True)
def reflection_unit_2(mo):
    cierre_unidad_2 = mo.ui.text_area(
        label="Para cerrar: criterio de selección de formato",
        placeholder="Imagina que debes transferir 50 millones de registros de visitas clínicas a un clúster de cómputo en la nube. ¿Qué formato eliges y cuáles son tus dos razones técnicas?",
        rows=3,
        full_width=True,
    )
    cierre_unidad_2
    return


@app.cell(hide_code=True)
def closing_unit_2(mo):
    mo.md(r"""
    ### Conclusión y siguiente paso
    Has comprobado por qué Parquet es el estándar de oro para el almacenamiento intermedio en ciencia de datos. En la **Unidad 03** iniciaremos la fase de auditoría: antes de corregir o transformar cualquier dato, aprenderemos a diagnosticar su calidad, detectar valores atípicos y cuantificar faltantes sin alterarlos.
    """)
    return


if __name__ == "__main__":
    app.run()
