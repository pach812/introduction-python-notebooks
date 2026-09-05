# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.24.0",
# ]
# ///

# ruff: noqa: B018
import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Semana 4 · 01 Leer archivos de texto")


@app.cell(hide_code=True)
def setup():
    from io import StringIO
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    assets = Path(__file__).parent / "assets"
    feedback = load_feedback(
        mo, week="week-04-data-cleaning-wrangling", notebook="01_leer_archivos_texto"
    )
    return StringIO, Path, assets, feedback, mo, pd


@app.cell(hide_code=True)
def opening(mo):
    mo.md(r"""
    # 01 · Leer archivos de texto con intención

    Bienvenido a la primera unidad de la **Semana 4**. Durante esta semana trabajaremos con los datos del **Estudio Horizonte**, un seguimiento clínico y epidemiológico multicéntrico ficticio en tres sedes (Norte, Sur y Centro). Recibiremos archivos de participantes, visitas presenciales, mediciones de presión arterial y llamadas de contacto.

    Un archivo de texto plano (`.csv`, `.tsv`, `.txt`) no es más que una secuencia continua de caracteres y bytes grabados en disco. **Pandas no "adivina" mágicamente la estructura**: cuando llamamos a `pd.read_csv()`, estamos ejecutando un analizador sintáctico (*parser*). Si no le declaramos con precisión las reglas de origen (delimitadores, cómo se codificó la ausencia, formatos de fechas o tipos de datos), Pandas tomará decisiones por defecto que pueden corromper silenciosamente los datos.

    Al terminar esta unidad sabrás:
    1. Configurar separadores estándar y no estándar (`sep`, `delimiter`).
    2. Declarar códigos personalizados de valores faltantes (`na_values`).
    3. Interpretar fechas automáticamente durante la ingesta (`parse_dates`, `dayfirst`).
    4. Cargar muestras selectivas de variables y filas (`usecols`, `nrows`, `skiprows`).
    5. Procesar archivos grandes por partes o bloques con `chunksize`.
    """)
    return


@app.cell(hide_code=True)
def pregunta_inicial(mo):
    mo.md(r"""
    ### Para pensar antes de empezar
    Antes de inspeccionar los datos, reflexiona: *Si abres un archivo delimitado en un editor y observas que las columnas están separadas por punto y coma `;` y que las ausencias están escritas como `"SIN_DATO"`, ¿qué ocurriría si ejecutas simplemente `pd.read_csv("archivo.csv")` con sus parámetros por defecto?*
    """)
    return


@app.cell(hide_code=True)
def como_interpreta_pandas(mo):
    mo.md(r"""
    ---
    ## Qué hace Pandas al abrir un archivo

    Cuando Pandas lee un archivo de texto delimitado, realiza cinco tareas críticas en milisegundos:
    1. **Tokenización:** divide las líneas según el delimitador especificado (`sep=','`, `sep=';'`, `sep='\t'`). Si el delimitador está mal configurado, toda la línea se leerá como una única columna gigantesca.
    2. **Encabezado e índices:** identifica los nombres de las variables (`header=0` usa la primera fila; `header=None` con `names=[...]` asigna nombres explícitos si el archivo no los trae).
    3. **Reconocimiento de nulos:** contrasta cada texto con los valores nulos estándar (`''`, `"NA"`, `"NaN"`, `"null"`) y con los adicionales que tú indiques en `na_values`.
    4. **Inferencia de tipos:** intenta convertir cadenas a enteros, números decimales o booleanos. Si encuentra un solo texto inesperado (como `"PENDIENTE"` en una columna de presión), forzará toda la columna al tipo genérico `object`.
    5. **Análisis de fechas:** si se declara `parse_dates`, transforma cadenas con fechas en objetos cronológicos precisos (`datetime64[ns]`), respetando si el día viene primero (`dayfirst=True` para formato latinoamericano/europeo `DD/MM/AAAA`).
    """)
    return


@app.cell
def inspect_raw_text(assets):
    # Inspeccionemos las primeras líneas crudas del archivo sin pasarlo aún por Pandas
    ruta_texto = assets / "pacientes_punto_y_coma.csv"
    with open(ruta_texto, "r", encoding="utf-8") as f:
        lineas_crudas = [f.readline().strip() for _ in range(5)]
    lineas_crudas
    return (ruta_texto,)


@app.cell(hide_code=True)
def explicacion_lectura_parametrizada(mo):
    mo.md(r"""
    ### Ejemplo 1 · Cargar indicando separador, fechas y nulos

    Observa las líneas crudas arriba:
    - Las columnas están separadas por punto y coma (`;`).
    - Las fechas tienen el formato `DD/MM/AAAA` (ej. `29/03/2026`).
    - Los identificadores clínicos (`codigo`) y las sedes (`sede`) deben ser tratados explícitamente como cadenas de texto (`string`), no como objetos genéricos.
    - Los valores ausentes están codificados como `"SIN_DATO"`.

    A continuación ejecutamos una lectura rigurosa declarando cada una de estas decisiones:
    """)
    return


@app.cell
def ejemplo_lectura_completa(pd, ruta_texto):
    # Lectura con parámetros explícitos
    df_ejemplo = pd.read_csv(
        ruta_texto,
        sep=";",
        na_values=["SIN_DATO", "DESCONOCIDO", "-99"],
        parse_dates=["fecha_visita"],
        dayfirst=True,
        dtype={"codigo": "string", "sede": "string"},
    )
    {
        "Forma (filas, cols)": df_ejemplo.shape,
        "Tipo de fecha_visita": str(df_ejemplo["fecha_visita"].dtype),
        "Valores nulos detectados en IMC": int(df_ejemplo["imc"].isna().sum()),
        "Primeras 3 filas": df_ejemplo[["codigo", "fecha_visita", "sede", "imc"]].head(3),
    }
    return (df_ejemplo,)


@app.cell(hide_code=True)
def explicacion_error_separador(mo):
    mo.md(r"""
    ### Qué pasa si olvidamos indicar el separador

    Veamos qué ocurre si ejecutamos `pd.read_csv(ruta_texto)` sin indicar `sep=";"`:
    """)
    return


@app.cell
def demostracion_omision_separador(pd, ruta_texto):
    # Lectura ingenua sin declarar el separador real
    df_fallido = pd.read_csv(ruta_texto)
    {
        "Forma obtenida": df_fallido.shape,
        "Nombre de la columna (toda la línea pegada)": df_fallido.columns[0][:60] + "...",
        "Tipo de dato": str(df_fallido.dtypes.iloc[0]),
    }
    return (df_fallido,)


@app.cell(hide_code=True)
def practice_one_prompt(mo):
    mo.md(r"""
    ---
    ## Práctica 1 · Carga parametrizada del archivo completo

    **Consigna:**
    Carga el archivo `ruta_texto` en la variable `tabla_texto`.
    1. Delimitador: `;`.
    2. Valores nulos adicionales: `"SIN_DATO"`.
    3. Conversión de fecha: columna `"fecha_visita"`, con día primero (`dayfirst=True`).
    4. Tipos explícitos: `"codigo"` y `"sede"` como `"string"`.

    *Verificación esperada:* Un DataFrame de exactamente 50 filas y 10 columnas, con fecha reconocida como `datetime64` y ausencias reconocidas.
    """)
    return


@app.cell
def practice_one(feedback, pd, ruta_texto):
    # TU TURNO: define tabla_texto con la llamada parametrizada
    tabla_texto = None
    feedback.exercise("cargar_texto_parametrizado", locals())
    return (tabla_texto,)


@app.cell(hide_code=True)
def partial_read_concept_markdown(mo):
    mo.md(r"""
    ---
    ## Lecturas selectivas: cargar solo lo que necesitas

    En proyectos de salud o investigación epidemiológica con tablas de cientos de columnas o millones de registros, **cargar todo el archivo por defecto es ineficiente y puede desbordar la memoria RAM**.

    Pandas ofrece tres mecanismos complementarios para leer selectivamente:

    1. **Selección por lista de columnas (`usecols=['col1', 'col2']`)**:
       Descarta en tiempo de lectura las columnas no deseadas, ahorrando tiempo y memoria.
    2. **Selección dinámica con funciones (`usecols=callable`)**:
       Puedes pasar una función `lambda` que devuelva `True` para los nombres de columna que deseas conservar.
    3. **Lectura por fragmentos de filas (`nrows` y `skiprows`)**:
       - `nrows=N`: lee únicamente las primeras $N$ observaciones (ideal para una vista preliminar).
       - `skiprows=range(1, k)`: salta las primeras $k-1$ filas de datos pero **conserva la fila 0 de encabezados**.

    Veamos estos tres patrones en acción con ejemplos ejecutables:
    """)
    return


@app.cell
def ejemplo_lectura_selectiva(pd, ruta_texto):
    # Ejemplo A: Selección directa con lista de nombres y límite de 3 filas
    muestra_columnas = pd.read_csv(
        ruta_texto,
        sep=";",
        usecols=["codigo", "sede", "lectura_sistolica"],
        nrows=3,
    )

    # Ejemplo B: Selección dinámica con función (ej. columnas que contienen 'visita' o 'codigo')
    muestra_dinamica = pd.read_csv(
        ruta_texto,
        sep=";",
        usecols=lambda col: "visita" in col or col == "codigo",
        nrows=3,
    )

    # Ejemplo C: Muestreo de observaciones intermedias usando skiprows
    # Saltamos las filas de datos 1 a 20 para leer las observaciones 21 a 23
    muestra_intermedia = pd.read_csv(
        ruta_texto,
        sep=";",
        skiprows=range(1, 21),
        nrows=3,
    )

    {
        "Muestra A (usecols lista)": muestra_columnas,
        "Muestra B (usecols función)": muestra_dinamica,
        "Muestra C (skiprows filas 21-23)": muestra_intermedia[["codigo", "fecha_visita", "sede"]],
    }
    return muestra_columnas, muestra_dinamica, muestra_intermedia


@app.cell(hide_code=True)
def practice_two_prompt(mo):
    mo.md(r"""
    ## Práctica 2 · Construir una vista reducida de inspección

    **Consigna:**
    Carga desde `ruta_texto` únicamente las primeras **5 filas** y solo estas **4 columnas**:
    `["codigo", "fecha_visita", "sede", "lectura_sistolica"]`.
    Asigna el resultado a `vista_inicial`. Mantén las mismas reglas de separador (`;`), faltantes (`"SIN_DATO"`) y fecha (`parse_dates=["fecha_visita"]`).
    """)
    return


@app.cell
def practice_two(feedback, pd, ruta_texto):
    # TU TURNO: carga la vista reducida usando usecols y nrows
    vista_inicial = None
    feedback.exercise("cargar_vista_inicial", locals())
    return (vista_inicial,)


@app.cell(hide_code=True)
def concepto_lectura_bloques(mo):
    mo.md(r"""
    ---
    ## Leer archivos muy grandes por partes (`chunksize`)

    Cuando un archivo de texto supera la capacidad de la memoria RAM (por ejemplo, registros de urgencias de todo un país), no podemos usar `pd.read_csv()` directamente.

    El parámetro `chunksize=N` devuelve un **iterador** que divide el archivo en bloques de $N$ filas. Podemos recorrerlos con un bucle `for`, calcular resúmenes parciales en cada bloque y luego combinarlos.

    Veamos cómo contar los pacientes por sede procesando el archivo en bloques pequeños de 15 filas:
    """)
    return


@app.cell
def chunking_example(pd, ruta_texto):
    # Procesamiento por bloques de 15 registros
    conteo_acumulado = pd.Series(dtype="int64")

    for trozo in pd.read_csv(ruta_texto, sep=";", chunksize=15):
        # En cada iteración 'trozo' es un DataFrame de máximo 15 filas
        conteo_parcial = trozo["sede"].str.strip().str.title().value_counts()
        conteo_acumulado = conteo_acumulado.add(conteo_parcial, fill_value=0)

    conteo_acumulado = conteo_acumulado.astype(int)
    {
        "Conteo acumulado por bloques": conteo_acumulado.to_dict(),
        "Total pacientes procesados": int(conteo_acumulado.sum()),
    }
    return (conteo_acumulado,)


@app.cell(hide_code=True)
def reflexion_final(mo):
    cierre_unidad_1 = mo.ui.text_area(
        label="Para cerrar: una regla con tus palabras",
        placeholder="Explica con tus palabras: ¿Por qué en un estudio clínico es crítico especificar na_values=['SIN_DATO', '-99'] en lugar de dejar que Pandas lo lea como texto?",
        rows=3,
        full_width=True,
    )
    cierre_unidad_1
    return


@app.cell(hide_code=True)
def closing_unit_1(mo):
    mo.md(r"""
    ### Conclusión y siguiente paso
    Has dominado la interpretación controlada de archivos delimitados de texto y las técnicas de lectura selectiva y por bloques. En la **Unidad 02** analizaremos qué ocurre cuando necesitamos exportar y compartir tablas en formatos binarios modernos como **Parquet** o intercambiables como **Excel**, evaluando la fidelidad de tipos y el ciclo de ida y vuelta (*roundtrip*).
    """)
    return


if __name__ == "__main__":
    app.run()
