# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = [
#     "marimo==0.24.0",
#     "numpy==2.5.2",
#     "pandas==3.0.5",
# ]
# ///

# ruff: noqa: B018, F841

import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="full",
    app_title="Semana 3 · Workbook en vivo",
    layout_file="layouts/lesson.slides.json",
    css_file="../../assets/ces-theme.css",
)


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def process_one_object_prompt(mo):
    mo.md(r"""
    # Los métodos limpian el texto sin cambiar la fuente
    ## Problema 01

    El lote llegó como `"  Horizonte_A-01  "`, pero el registro espera
    `"horizonte_a-01"`.

    El equipo necesita entregar el identificador normalizado sin alterar el texto
    que llegó de la fuente. Decida cómo usar la interfaz del objeto para producir
    `"horizonte_a-01"`. Guarde los métodos en nombres separados y use
    `callable(...)` para comprobar que Python puede ejecutarlos.
    """)
    return


@app.cell
def process_one_object_workspace():
    identificador_fuente_c01 = "  Horizonte_A-01  "

    # TU TURNO: recupere los métodos y llámelos para crear el resultado.
    metodo_limpieza_c01 = None
    metodo_minusculas_c01 = None
    operaciones_invocables_c01 = None
    identificador_limpio_c01 = None

    {
        "fuente": identificador_fuente_c01,
        "método 1": metodo_limpieza_c01,
        "método 2": metodo_minusculas_c01,
        "¿se pueden llamar?": operaciones_invocables_c01,
        "resultado": identificador_limpio_c01,
    }
    return


@app.cell(hide_code=True)
def process_one_import_prompt(mo):
    mo.md(r"""
    # Demostración guiada · La biblioteca estándar resuelve tareas comunes

    Acompañe la demostración del docente con `math.ceil(...)`, `stats.mean(...)`
    y `random.choice(...)`. Por ahora no hay un problema que entregar: NumPy y
    Pandas aparecerán cuando empecemos a trabajar con arrays y tablas.
    """)
    return


@app.cell
def process_one_import_workspace(mo):
    import math
    import random
    import statistics as stats

    minutos_sesion_c02 = 137
    lecturas_prueba_c02 = [72, 68, 75]
    random.seed(2026)

    mo.ui.table(
        {
            "horas completas necesarias": math.ceil(minutos_sesion_c02 / 60),
            "promedio de prueba": stats.mean(lecturas_prueba_c02),
            "selección reproducible": random.choice(["P01", "P02", "P03"]),
        }
    )
    return


@app.cell(hide_code=True)
def scientific_tools_imports():
    import numpy as np
    import pandas as pd

    return np, pd


@app.cell(hide_code=True)
def numpy_creation_prompt(mo):
    mo.md(r"""
    # `shape`, `ndim` y `dtype` describen el array
    ## Problema 02

    El nuevo lote contiene `[72, 68, 75, 80, 71, 77]`. El ajuste posterior puede
    producir decimales. Queremos confirmar que las seis lecturas quedaron en una
    sola dimensión y que el array puede guardar valores decimales.

    Vamos a crear el array con `dtype=float`. Después revisaremos `shape`, `ndim`
    y `dtype`: esas tres salidas muestran cómo quedó organizado.
    """)
    return


@app.cell
def numpy_creation_workspace():
    lecturas_lote_a_c03a = [72, 68, 75, 80, 71, 77]

    array_lote_a_c03a = None
    forma_c03a = None
    dimensiones_c03a = None
    dtype_c03a = None

    {
        "fuente": lecturas_lote_a_c03a,
        "array": array_lote_a_c03a,
        "shape": forma_c03a,
        "ndim": dimensiones_c03a,
        "dtype": dtype_c03a,
    }
    return


@app.cell(hide_code=True)
def numpy_vectorization_prompt(mo):
    mo.md(r"""
    # La fuente y el resultado permanecen separados
    ## Problema 03

    Una simulación del estudio usa un factor de `1.05`, pero después tendremos que
    comparar las lecturas crudas con las ajustadas. Calcule el nuevo lote con una
    sola expresión sobre el array. Compare las formas de entrada y salida, y use
    `np.array_equal(...)` para revisar que la fuente siga intacta.
    """)
    return


@app.cell
def numpy_vectorization_workspace(np):
    lecturas_lote_a_c03b = np.array([72.0, 68.0, 75.0, 80.0, 71.0, 77.0])

    lecturas_ajustadas_c03b = None
    misma_forma_c03b = None
    fuente_conservada_c03b = None

    {
        "fuente": lecturas_lote_a_c03b,
        "ajuste": lecturas_ajustadas_c03b,
        "¿misma forma?": misma_forma_c03b,
        "¿fuente conservada?": fuente_conservada_c03b,
    }
    return


@app.cell(hide_code=True)
def numpy_indexing_prompt(mo):
    mo.md(r"""
    # Seleccionar con índices y cortes
    ## Problema 04

    Una bitácora antigua solo dice: “tercera lectura”, “tres lecturas centrales”
    y “una lectura sí y una no desde el inicio”. Traduzca esas referencias a
    selecciones sobre el array. Antes de ejecutar, anticipe qué posiciones deben
    aparecer; después, explique qué información no puede recuperarse únicamente
    con posiciones.
    """)
    return


@app.cell
def numpy_indexing_workspace(np):
    lecturas_ordenadas_c03c = np.array([75.6, 71.4, 78.75, 84.0, 74.55, 80.85])

    tercer_valor_c03c = None
    region_central_c03c = None
    posiciones_pares_c03c = None

    {
        "tercer valor": tercer_valor_c03c,
        "región central": region_central_c03c,
        "posiciones pares": posiciones_pares_c03c,
    }
    return


@app.cell(hide_code=True)
def numpy_mask_prompt(mo):
    mo.md(r"""
    # Seleccionar valores con una máscara
    ## Problema 05

    Para este lote, una lectura ajustada entra a revisión desde `78`, inclusive.
    Primero preparemos los datos y apliquemos el factor `1.05`. Guarde la comparación
    `mediciones_ajustadas_c03 >= 78` en una variable: así podremos ver la decisión
    `True` o `False` correspondiente a cada lectura. Use esa máscara para obtener
    la selección final y conserve la lista original para compararla.
    """)
    return


@app.cell
def numpy_mask_workspace():
    lecturas_fuente_c03d = [72, 68, 75, 80, 71, 77]

    array_lote_c_c03d = None
    lecturas_ajustadas_c03d = None
    mascara_revision_c03d = None
    lecturas_revision_c03d = None

    {
        "fuente": lecturas_fuente_c03d,
        "array": array_lote_c_c03d,
        "ajuste": lecturas_ajustadas_c03d,
        "máscara": mascara_revision_c03d,
        "selección": lecturas_revision_c03d,
    }
    return


@app.cell(hide_code=True)
def numpy_aggregation_prompt(mo):
    mo.md(r"""
    # El eje depende de la respuesta que queremos conservar
    ## Problema 06

    La matriz representa seis participantes en filas y dos capturas en columnas.

    El equipo necesita tres respuestas: el promedio de cada participante, el
    promedio de cada captura y el máximo global. Antes de elegir un eje, anticipe
    cuántos valores debería tener cada respuesta. Use después las salidas para
    comprobar que la dimensión adecuada permaneció.
    """)
    return


@app.cell
def numpy_aggregation_workspace(np):
    matriz_capturas_c03e = np.array(
        [
            [72.0, 74.0],
            [68.0, 69.0],
            [75.0, 76.0],
            [80.0, 79.0],
            [71.0, 72.0],
            [77.0, 78.0],
        ]
    )

    promedio_participante_c03e = None
    promedio_visita_c03e = None
    maximo_global_c03e = None

    {
        "por participante": promedio_participante_c03e,
        "por captura": promedio_visita_c03e,
        "máximo": maximo_global_c03e,
    }
    return


@app.cell(hide_code=True)
def pandas_series_creation_prompt(mo):
    mo.md(r"""
    # Crear una Series con etiquetas
    ## Problema 07

    El equipo recibió por separado seis valores ajustados y seis códigos. Necesita
    un objeto que preserve su correspondencia aunque después cambie el orden de
    presentación. Cree una Series llamada `"lectura_ajustada"`. Al final, consulte
    `.index` y `.name` para revisar que los códigos y el nombre sí quedaron dentro
    del objeto.
    """)
    return


@app.cell
def pandas_series_creation_workspace():
    valores_c04a = [75.6, 71.4, 78.75, 84.0, 74.55, 80.85]
    codigos_c04a = ["P01", "P02", "P03", "P04", "P05", "P06"]

    lecturas_etiquetadas_c04a = None
    nombre_c04a = None
    indice_c04a = None

    {
        "Series": lecturas_etiquetadas_c04a,
        "nombre": nombre_c04a,
        "índice": indice_c04a,
    }
    return


@app.cell(hide_code=True)
def pandas_series_selection_prompt(mo):
    mo.md(r"""
    # Seleccionar por etiqueta y por posición
    ## Problema 08

    La Series preparada llega en el orden P04, P01, P06, P03, P02, P05.

    La Series llega en el orden P04, P01, P06, P03, P02, P05. El equipo pide la
    lectura de P03, la observación situada actualmente en tercer lugar y el grupo
    P01–P03–P05. Busque cada resultado y compare cuál permanecería estable ante
    un nuevo reordenamiento.
    """)
    return


@app.cell
def pandas_series_selection_workspace(pd):
    lecturas_c04b = pd.Series(
        [84.0, 75.6, 80.85, 78.75, 71.4, 74.55],
        index=["P04", "P01", "P06", "P03", "P02", "P05"],
        name="lectura_ajustada",
    )

    p03_por_etiqueta_c04b = None
    tercera_posicion_c04b = None
    participantes_clave_c04b = None

    {
        "P03": p03_por_etiqueta_c04b,
        "tercera posición": tercera_posicion_c04b,
        "participantes clave": participantes_clave_c04b,
    }
    return


@app.cell(hide_code=True)
def pandas_dataframe_creation_prompt(mo):
    mo.md(r"""
    # Construir un DataFrame desde un diccionario
    ## Problema 09

    Las columnas llegaron dentro de un diccionario. Antes de producir la tabla de
    entrega, revise si todas describen la misma cantidad de observaciones. Si las
    longitudes coinciden, construya el DataFrame y consulte `.shape` para confirmar
    cuántas observaciones y variables quedaron en la tabla.
    """)
    return


@app.cell
def pandas_dataframe_creation_workspace():
    datos_c04c = {
        "codigo": ["P01", "P02", "P03", "P04", "P05", "P06"],
        "lectura": [72, 68, 75, 80, 71, 77],
        "requiere_revision": [False, True, True, False, True, True],
    }

    tabla_c04c = None
    forma_c04c = None

    {
        "tabla": tabla_c04c,
        "shape": forma_c04c,
    }
    return


@app.cell(hide_code=True)
def pandas_inspection_prompt(mo):
    mo.md(r"""
    # Revisar la forma, los tipos y las primeras filas
    ## Problema 10

    Antes de continuar, queremos saber cuántas filas y columnas tiene la tabla,
    cuál variable es booleana y cómo se ven las dos primeras observaciones.
    Responda con `.shape`, `.dtypes` y `.head(2)` para que las salidas se actualicen
    si la tabla cambia.
    """)
    return


@app.cell
def pandas_inspection_workspace(pd):
    tabla_c04d = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03", "P04", "P05", "P06"],
            "lectura": [72, 68, 75, 80, 71, 77],
            "requiere_revision": [False, True, True, False, True, True],
        }
    )

    forma_c04d = None
    columnas_c04d = None
    tipos_c04d = None
    primeras_filas_c04d = None

    {
        "shape": forma_c04d,
        "columnas": columnas_c04d,
        "tipos": tipos_c04d,
        "primeras filas": primeras_filas_c04d,
    }
    return


@app.cell(hide_code=True)
def pandas_columns_prompt(mo):
    mo.md(r"""
    # Seleccionar una columna como Series o DataFrame
    ## Problema 11

    Una herramienta acepta una Series; otra exige siempre una tabla de dos
    dimensiones. A partir del mismo DataFrame, seleccione `codigo` en ambos
    formatos y cree además una tabla con `codigo` y `lectura`. Compare el tipo y
    la forma de las tres salidas antes de decidir cuál usaría en cada caso.
    """)
    return


@app.cell
def pandas_columns_workspace(pd):
    tabla_c04e = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03"],
            "lectura": [72, 68, 75],
            "lote": ["A", "A", "A"],
        }
    )

    codigos_series_c04e = None
    codigos_dataframe_c04e = None
    codigo_lectura_c04e = None

    {
        "Series": codigos_series_c04e,
        "DataFrame de una columna": codigos_dataframe_c04e,
        "DataFrame de dos columnas": codigo_lectura_c04e,
    }
    return


@app.cell(hide_code=True)
def pandas_loc_iloc_prompt(mo):
    mo.md(r"""
    # Seleccionar filas y columnas con `loc` e `iloc`
    ## Problema 12

    La tabla está indexada por código, pero su orden fue alterado.

    La tabla está indexada por código, pero su orden fue alterado. El equipo
    necesita las variables `codigo` y `lectura` de P02 y P03 y, por separado, una
    revisión visual de las dos primeras filas y columnas actuales.
    Hagamos ambas selecciones y revisemos cuál cambiaría con un nuevo orden.
    """)
    return


@app.cell
def pandas_loc_iloc_workspace(pd):
    tabla_c04f = pd.DataFrame(
        {
            "codigo": ["P04", "P01", "P06", "P03", "P02", "P05"],
            "lectura": [80, 72, 77, 75, 68, 71],
            "lote": ["A", "A", "A", "A", "A", "A"],
        },
        index=["P04", "P01", "P06", "P03", "P02", "P05"],
    )

    seleccion_loc_c04f = None
    seleccion_iloc_c04f = None

    {
        "loc": seleccion_loc_c04f,
        "iloc": seleccion_iloc_c04f,
    }
    return


@app.cell(hide_code=True)
def pandas_filter_prompt(mo):
    mo.md(r"""
    # Combinar dos condiciones en un filtro
    ## Problema 13

    La cola debe contener únicamente participantes que cumplen ambas reglas:

    - `lectura` es mayor o igual a `75`;
    - `requiere_revision` es verdadero.

    Guarde primero cada condición en una variable y luego combínelas con `&`.
    Mostrar las dos condiciones y la máscara final nos permite revisar por qué
    cada fila entró o quedó fuera. Use la máscara para seleccionar `codigo` y
    `lectura`.
    """)
    return


@app.cell
def pandas_filter_workspace(pd):
    tabla_c04g = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03", "P04", "P05", "P06"],
            "lectura": [72, 68, 75, 80, 71, 77],
            "requiere_revision": [False, True, True, False, True, True],
        }
    )

    condicion_lectura_c04g = None
    condicion_marcacion_c04g = None
    mascara_c04g = None
    seleccion_c04g = None

    {
        "condición de lectura": condicion_lectura_c04g,
        "condición de marcación": condicion_marcacion_c04g,
        "máscara combinada": mascara_c04g,
        "selección": seleccion_c04g,
    }
    return


@app.cell(hide_code=True)
def pandas_derived_prompt(mo):
    mo.md(r"""
    # Crear una columna sin cambiar la tabla original
    ## Problema 14

    La entrega debe mostrar juntas la lectura original y la ajustada, pero la tabla
    recibida debe quedar intacta. Haga una copia, cree allí `lectura_ajustada`
    usando el factor `1.05` y compare `.columns` en ambas tablas para revisar dónde
    quedó la nueva variable.
    """)
    return


@app.cell
def pandas_derived_workspace(pd):
    tabla_fuente_c04h = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03", "P04", "P05", "P06"],
            "lectura": [72, 68, 75, 80, 71, 77],
        }
    )

    tabla_copia_c04h = None
    columnas_fuente_c04h = None
    columnas_copia_c04h = None

    {
        "fuente": tabla_fuente_c04h,
        "copia": tabla_copia_c04h,
        "columnas fuente": columnas_fuente_c04h,
        "columnas copia": columnas_copia_c04h,
    }
    return


@app.cell(hide_code=True)
def final_transfer_prompt(mo):
    mo.md(r"""
    # Integrar el proceso con un lote nuevo
    ## Problema 15

    El lote B cambia códigos, orden y valores. Necesitamos una copia con el ajuste
    `1.05`, un filtro que combine la marcación existente con un límite de `80`
    sobre la lectura ajustada y una tabla final ordenada de mayor a menor.

    Organice la solución con las ideas que trabajamos durante la sesión. Al final,
    muestre la tabla original junto con el resultado para comprobar que la fuente
    no cambió.
    """)
    return


@app.cell
def final_transfer_workspace(pd):
    datos_fuente_c04 = {
        "codigo": ["P12", "P09", "P14", "P11", "P10"],
        "lectura": [74, 82, 69, 78, 76],
        "requiere_revision": [True, False, True, True, True],
    }

    tabla_fuente_c04 = pd.DataFrame(datos_fuente_c04)

    # TU TURNO: construya aquí la solución completa.
    tabla_trabajo_c04 = None
    mascara_final_c04 = None
    tabla_revision_c04 = None

    {
        "fuente": tabla_fuente_c04,
        "copia de trabajo": tabla_trabajo_c04,
        "máscara": mascara_final_c04,
        "entrega": tabla_revision_c04,
    }
    return


if __name__ == "__main__":
    app.run()
