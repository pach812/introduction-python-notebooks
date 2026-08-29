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
    # Proceso 1 · Normalizar el identificador del lote

    El lote llegó identificado como `"  LOTE_A  "`.

    Conserven el texto original y produzcan `"lote_a"` en un nombre nuevo.
    Recuperen primero los métodos que necesitan y después llámenlos.
    """)
    return


@app.cell
def process_one_object_workspace():
    identificador_fuente_c01 = "  LOTE_A  "

    metodo_limpieza_c01 = None
    metodo_minusculas_c01 = None
    identificador_limpio_c01 = None

    {
        "fuente": identificador_fuente_c01,
        "método 1": metodo_limpieza_c01,
        "método 2": metodo_minusculas_c01,
        "resultado": identificador_limpio_c01,
    }
    return


@app.cell(hide_code=True)
def process_one_import_prompt(mo):
    mo.md(r"""
    # Proceso 1 · Abrir las herramientas científicas

    Después de importar NumPy como `np` y Pandas como `pd`, construyan un array
    con `[72, 68, 75, 80]`. Obtengan su tipo, su forma y el `dtype` directamente
    desde los objetos correspondientes.
    """)
    return


@app.cell
def process_one_import_workspace():
    import numpy as np
    import pandas as pd

    array_importado_c02 = None
    tipo_array_c02 = None
    forma_array_c02 = None
    dtype_array_c02 = None

    {
        "array": array_importado_c02,
        "tipo": tipo_array_c02,
        "shape": forma_array_c02,
        "dtype": dtype_array_c02,
    }
    return np, pd


@app.cell(hide_code=True)
def numpy_creation_prompt(mo):
    mo.md(r"""
    # Proceso 2 · Construir el array del lote A

    Conviertan `[72, 68, 75, 80]` en un array de tipo `float`.

    Obtengan desde el objeto su forma, cantidad de dimensiones y `dtype`.
    """)
    return


@app.cell
def numpy_creation_workspace(np):
    lecturas_lote_a_c03a = [72, 68, 75, 80]

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
    # Proceso 2 · Ajustar el lote B

    Apliquen el factor técnico `1.05` al array completo, sin escribir un ciclo.

    Conserven la fuente y comprueben que entrada y salida tienen la misma forma.
    """)
    return


@app.cell
def numpy_vectorization_workspace(np):
    lecturas_lote_b_c03b = np.array([64.0, 71.0, 69.0, 76.0])

    lecturas_ajustadas_c03b = None
    misma_forma_c03b = None

    {
        "fuente": lecturas_lote_b_c03b,
        "ajuste": lecturas_ajustadas_c03b,
        "¿misma forma?": misma_forma_c03b,
    }
    return


@app.cell(hide_code=True)
def numpy_indexing_prompt(mo):
    mo.md(r"""
    # Proceso 3 · Localizar lecturas dentro del lote

    Del array `[68, 72, 71, 75, 73, 80]`, obtengan:

    - el tercer valor como escalar;
    - los tres valores centrales como array;
    - los valores de las posiciones pares con un corte con paso.
    """)
    return


@app.cell
def numpy_indexing_workspace(np):
    lecturas_ordenadas_c03c = np.array([68, 72, 71, 75, 73, 80])

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
    # Proceso 3 · Seleccionar lecturas para revisión

    El lote C contiene `[70, 76, 73, 81, 75]`.

    Constrúyanlo como array de tipo `float`, apliquen el factor `1.05` y conserven
    las lecturas ajustadas mayores o iguales a `78`. La lista fuente no cambia.
    """)
    return


@app.cell
def numpy_mask_workspace(np):
    lecturas_fuente_c03d = [70, 76, 73, 81, 75]

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
    # Proceso 3 · Resumir dos capturas

    La matriz representa tres participantes en filas y dos capturas en columnas.

    Calculen un promedio por participante, un promedio por captura y el valor
    máximo de toda la matriz.
    """)
    return


@app.cell
def numpy_aggregation_workspace(np):
    matriz_capturas_c03e = np.array(
        [
            [72.0, 74.0],
            [68.0, 71.0],
            [75.0, 80.0],
        ]
    )

    promedio_participante_c03e = None
    promedio_captura_c03e = None
    maximo_global_c03e = None

    {
        "por participante": promedio_participante_c03e,
        "por captura": promedio_captura_c03e,
        "máximo": maximo_global_c03e,
    }
    return


@app.cell(hide_code=True)
def pandas_series_creation_prompt(mo):
    mo.md(r"""
    # Proceso 4 · Volver a unir códigos y lecturas

    Construyan una Series con los cuatro valores del lote A, los códigos P01–P04
    y el nombre `"lectura_tecnica"`.

    Recuperen después el nombre y el índice desde el objeto.
    """)
    return


@app.cell
def pandas_series_creation_workspace(pd):
    valores_c04a = [72, 68, 75, 80]
    codigos_c04a = ["P01", "P02", "P03", "P04"]

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
    # Proceso 4 · Seleccionar por identidad o posición

    Seleccionen P03 por etiqueta, la tercera posición con `iloc` y el tramo desde
    P02 hasta P04 con `loc`.

    Los dos primeros resultados coinciden, pero representan solicitudes distintas.
    """)
    return


@app.cell
def pandas_series_selection_workspace(pd):
    lecturas_c04b = pd.Series(
        [72, 68, 75, 80],
        index=["P01", "P02", "P03", "P04"],
        name="lectura_tecnica",
    )

    p03_por_etiqueta_c04b = None
    tercera_posicion_c04b = None
    tramo_etiquetas_c04b = None

    {
        "P03": p03_por_etiqueta_c04b,
        "tercera posición": tercera_posicion_c04b,
        "P02 a P04": tramo_etiquetas_c04b,
    }
    return


@app.cell(hide_code=True)
def pandas_dataframe_creation_prompt(mo):
    mo.md(r"""
    # Proceso 5 · Construir la primera tabla

    Conviertan el diccionario preparado en un DataFrame y obtengan su forma desde
    el objeto. Las tres columnas deben conservar su correspondencia por fila.
    """)
    return


@app.cell
def pandas_dataframe_creation_workspace(pd):
    datos_c04c = {
        "codigo": ["P01", "P02", "P03"],
        "lectura": [72, 68, 75],
        "lote": ["A", "A", "A"],
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
    # Proceso 5 · Obtener evidencia sobre la tabla

    Obtengan la forma, los nombres de las columnas, sus tipos y las dos primeras
    filas. Todos los resultados deben provenir del DataFrame.
    """)
    return


@app.cell
def pandas_inspection_workspace(pd):
    tabla_c04d = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03"],
            "lectura": [72, 68, 75],
            "requiere_revision": [False, False, True],
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
    # Proceso 5 · Elegir el tipo de salida

    Produzcan `codigo` como Series, `codigo` como DataFrame de una columna y
    `codigo` junto con `lectura` como DataFrame.
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
    # Proceso 5 · Seleccionar en dos dimensiones

    Usen `loc` para obtener P02 y P03 con `codigo` y `lectura`. Después usen
    `iloc` para obtener las dos primeras filas y las dos primeras columnas.
    """)
    return


@app.cell
def pandas_loc_iloc_workspace(pd):
    tabla_c04f = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03", "P04"],
            "lectura": [72, 68, 75, 80],
            "lote": ["A", "A", "A", "A"],
        },
        index=["P01", "P02", "P03", "P04"],
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
    # Proceso 5 · Coordinar dos condiciones

    Seleccionen las filas con `lectura >= 75` y `requiere_revision == True`.
    Conserven únicamente `codigo` y `lectura`.
    """)
    return


@app.cell
def pandas_filter_workspace(pd):
    tabla_c04g = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03", "P04"],
            "lectura": [72, 68, 75, 80],
            "requiere_revision": [False, False, True, True],
        }
    )

    mascara_c04g = None
    seleccion_c04g = None

    {
        "máscara": mascara_c04g,
        "selección": seleccion_c04g,
    }
    return


@app.cell(hide_code=True)
def pandas_derived_prompt(mo):
    mo.md(r"""
    # Proceso 5 · Añadir la lectura ajustada

    Trabajen sobre una copia y creen `lectura_ajustada` aplicando el factor
    `1.05`. La tabla fuente debe conservar sus columnas originales.
    """)
    return


@app.cell
def pandas_derived_workspace(pd):
    tabla_fuente_c04h = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03"],
            "lectura": [72, 68, 75],
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
    # Reto final · Construir la entrega completa

    Partan de estos datos:

    ```python
    {
        "codigo": ["P01", "P02", "P03", "P04"],
        "lectura": [72, 68, 75, 80],
        "requiere_revision": [False, False, True, True],
    }
    ```

    Construyan el DataFrame, trabajen sobre una copia, creen
    `lectura_ajustada`, filtren las filas marcadas con lectura mínima de `75` y
    entreguen `codigo`, `lectura` y `lectura_ajustada`.
    """)
    return


@app.cell
def final_transfer_workspace():
    # TU TURNO: construyan aquí la solución completa.
    ...
    return


if __name__ == "__main__":
    app.run()
