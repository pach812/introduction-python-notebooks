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
    # Incidente 1 · El identificador no coincide con el registro

    El lote llegó como `"  Horizonte_A-01  "`, pero el registro espera
    `"horizonte_a-01"`.

    Conserven el texto recibido. Recuperen primero las dos operaciones que
    necesitan, comprueben que se pueden llamar y produzcan el identificador
    normalizado en un nombre nuevo.
    """)
    return


@app.cell
def process_one_object_workspace():
    identificador_fuente_c01 = "  Horizonte_A-01  "

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
    # Decisión 2 · Abrir herramientas sin ocultar su origen

    El equipo utilizará NumPy para operar sobre las lecturas y Pandas para
    conservar sus etiquetas. Importen ambas librerías con los alias acordados.

    Construyan un array de prueba con `[72, 68]` y obtengan su tipo, forma y
    `dtype` desde el objeto. En la revisión deben poder señalar qué parte de cada
    expresión conserva visible el origen de la herramienta.
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
    # Decisión 3 · Preparar el lote completo para operar en conjunto

    Las seis lecturas crudas del lote son `[72, 68, 75, 80, 71, 77]`.
    Conviértanlas en un array de tipo `float`.

    Obtengan desde el objeto su forma, cantidad de dimensiones y `dtype`. Estos
    resultados serán la evidencia de que el lote quedó listo sin escribir sus
    propiedades manualmente.
    """)
    return


@app.cell
def numpy_creation_workspace(np):
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
    # Consecuencia 4 · Todas las lecturas requieren el mismo ajuste

    El protocolo técnico solicita multiplicar todas las lecturas del lote A por
    `1.05`. Apliquen el ajuste al array completo, sin escribir un ciclo.

    Conserven la fuente y produzcan dos evidencias: que entrada y salida tienen
    la misma forma y que el array fuente no fue reemplazado por el resultado.
    """)
    return


@app.cell
def numpy_vectorization_workspace(np):
    lecturas_lote_b_c03b = np.array([72.0, 68.0, 75.0, 80.0, 71.0, 77.0])

    lecturas_ajustadas_c03b = None
    misma_forma_c03b = None
    fuente_conservada_c03b = None

    {
        "fuente": lecturas_lote_b_c03b,
        "ajuste": lecturas_ajustadas_c03b,
        "¿misma forma?": misma_forma_c03b,
        "¿fuente conservada?": fuente_conservada_c03b,
    }
    return


@app.cell(hide_code=True)
def numpy_indexing_prompt(mo):
    mo.md(r"""
    # Incidente 5 · La bitácora señala posiciones, no participantes

    Una bitácora provisional pide revisar posiciones del lote ajustado. Obtengan:

    - el tercer valor como escalar;
    - los tres valores centrales como array;
    - una lectura sí y una no, empezando en la primera posición.

    Antes de ejecutar, indiquen qué posiciones esperan conservar. Al final,
    expliquen qué información todavía falta para saber a quién pertenece cada
    valor.
    """)
    return


@app.cell
def numpy_indexing_workspace(np):
    lecturas_ordenadas_c03c = np.array(
        [75.6, 71.4, 78.75, 84.0, 74.55, 80.85]
    )

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
    # Decisión 6 · Convertir una regla en una selección verificable

    El estudio revisará las lecturas ajustadas mayores o iguales a `78`.

    A partir de la lista cruda del lote A, construyan el array, apliquen el factor
    `1.05`, produzcan la máscara y seleccionen los valores. Conserven la máscara
    como evidencia: no basta con mostrar únicamente el resultado final.
    """)
    return


@app.cell
def numpy_mask_workspace(np):
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
    # Decisión 7 · Resumir sin confundir participantes y capturas

    La matriz representa seis participantes en filas y dos capturas en columnas.

    Antes de programar, determinen cuántos valores debería producir cada resumen.
    Luego calculen un promedio por participante, un promedio por captura y el
    valor máximo de toda la matriz. Usen la forma de los resultados para comprobar
    que eligieron el eje correcto.
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
    # Incidente 8 · Una selección de posiciones perdió la identidad

    Los valores ajustados deben volver a quedar unidos a los códigos P01–P06.
    Construyan una Series llamada `"lectura_ajustada"` con ambos componentes.

    Recuperen el nombre y el índice desde el objeto. La salida debe permitir
    comprobar que hay exactamente una etiqueta por lectura.
    """)
    return


@app.cell
def pandas_series_creation_workspace(pd):
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
    # Comprobación 9 · La etiqueta debe resistir un cambio de orden

    La Series preparada llega en el orden P04, P01, P06, P03, P02, P05.

    Seleccionen P03 por etiqueta y la tercera posición con `iloc`. Luego obtengan
    P01, P03 y P05 mediante una lista de etiquetas.

    Comparen los dos primeros resultados: esta vez no coinciden. Expliquen cuál
    solicitud conserva la identidad y cuál depende del orden actual.
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
    # Decisión 10 · Reunir variables que describen la misma observación

    El equipo necesita leer en cada fila el código, la lectura cruda y el estado
    de revisión. Comprueben primero que las columnas del diccionario tienen la
    misma longitud, conviértanlo en un DataFrame y obtengan su forma.

    La tabla es válida si conserva seis observaciones y tres variables alineadas.
    """)
    return


@app.cell
def pandas_dataframe_creation_workspace(pd):
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
    # Verificación 11 · Elegir evidencia antes de seguir

    Antes de transformar la tabla, respondan con código:

    - ¿tiene seis filas y tres columnas?;
    - ¿qué variable quedó representada como booleana?;
    - ¿qué aspecto tienen las dos primeras observaciones?

    Elijan atributos o métodos que reaccionen si los datos cambian. No escriban
    las respuestas manualmente.
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
    # Decisión 12 · La siguiente tarea exige conservar una tabla

    Primero recuperen `codigo` como Series para observar una sola variable.
    Después preparen dos entregas que deben seguir siendo DataFrames:

    - una tabla de una columna con `codigo`;
    - una tabla con `codigo` y `lectura`.

    Comprueben los tipos. Decidan qué forma usarían si otra persona espera una
    tabla, incluso cuando solo contiene una variable.
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
    # Comprobación 13 · Identidad y posición responden preguntas distintas

    La tabla está indexada por código, pero su orden fue alterado.

    Usen `loc` para obtener P02 y P03 con `codigo` y `lectura`. Después usen
    `iloc` para obtener las dos primeras filas y las dos primeras columnas.
    Comparen las salidas y expliquen cuál podría cambiar si alguien reordena la
    tabla otra vez.
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
    # Decisión 14 · La coordinación necesita una cola de revisión

    La cola debe incluir únicamente registros marcados para revisión cuya lectura
    cruda sea mayor o igual a `75`.

    Construyan y conserven por separado las dos condiciones y la máscara
    combinada. Después seleccionen `codigo` y `lectura`. La máscara debe permitir
    explicar por qué cada fila entró o quedó fuera.
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
    # Consecuencia 15 · La entrega necesita mostrar el ajuste

    Trabajen sobre una copia del lote completo y creen `lectura_ajustada`
    aplicando el factor `1.05` a `lectura`.

    Produzcan evidencia de dos cosas: la correspondencia fila a fila se conserva
    y la tabla fuente mantiene sus columnas originales.
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
    # Transferencia final · Llegó el lote B

    Este lote no conserva el orden ni los valores del ejemplo:

    ```python
    {
        "codigo": ["P12", "P09", "P14", "P11", "P10"],
        "lectura": [74, 82, 69, 78, 76],
        "requiere_revision": [True, False, True, True, True],
    }
    ```

    Construyan una entrega que:

    - conserve intacta la fuente;
    - añada `lectura_ajustada` con el factor `1.05`;
    - incluya registros marcados y con lectura ajustada de al menos `80`;
    - muestre `codigo`, `lectura` y `lectura_ajustada`;
    - quede ordenada de mayor a menor por la lectura ajustada.

    Decidan la secuencia de operaciones. Al comparar soluciones deberán justificar
    dónde aplicaron la condición y cómo comprobaron que la fuente no cambió.
    """)
    return


@app.cell
def final_transfer_workspace():
    # TU TURNO: construyan aquí la solución completa.
    ...
    return


if __name__ == "__main__":
    app.run()
