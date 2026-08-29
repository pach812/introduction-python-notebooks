# ruff: noqa: B018

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 3 · Series de Pandas")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-03-objects-scientific-tools",
        notebook="04_pandas_series",
    )
    return feedback, mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Series: valores que conservan sus etiquetas

    Un array unidimensional conserva valores y posiciones. Una `Series` de
    Pandas agrega una pieza decisiva: un índice que identifica cada observación.

    En este cuaderno aprenderás a:

    - construir una `Series` con valores, índice y nombre;
    - distinguir etiqueta de posición;
    - seleccionar con `loc` e `iloc`;
    - filtrar sin perder las etiquetas;
    - comprender por qué las operaciones entre Series se alinean por índice.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pregunta qué debe permanecer unido

    Tenemos tres observaciones:

    ```text
    P01 → 8
    P02 → 12
    P03 → 9
    ```

    Si ordenamos los valores o añadimos otra fuente de información, ¿qué riesgo
    aparece si conservamos solo `[8, 12, 9]`? Escribe qué función cumplen los
    códigos y por qué no son simplemente otra lista de datos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    respuesta_inicial_series = mo.ui.text_area(
        label="¿Qué relación protegen las etiquetas?",
        placeholder="Explica qué podría perderse si valores y códigos se separan.",
        rows=4,
        full_width=True,
    )
    respuesta_inicial_series
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
            ## Define una estructura unidimensional etiquetada

            Una **Series** es un objeto unidimensional de Pandas que relaciona
            cada valor con una etiqueta de índice. También puede tener un nombre
            que describa qué representan sus valores.

            Sus partes principales son:

            - `values`: los datos;
            - `index`: las etiquetas que identifican posiciones;
            - `name`: el significado de la variable;
            - `dtype`: la representación de los valores.
            """),
            mo.mermaid(r"""flowchart LR
                S["Series: visitas"] --> I["index: P01, P02, P03"]
                S --> V["values: 8, 12, 9"]
                S --> D["dtype: int64"]
                I --> R["cada etiqueta permanece ligada a su valor"]
                V --> R"""),
        ],
        gap=1,
    )
    return


@app.cell
def _(pd):
    visitas_demo_series = pd.Series(
        [8, 12, 9],
        index=["P01", "P02", "P03"],
        name="visitas",
    )

    visitas_demo_series
    return


@app.cell
def _(visitas_demo_series):
    informacion_demo_series = {
        "tipo": type(visitas_demo_series).__name__,
        "shape": visitas_demo_series.shape,
        "dtype": str(visitas_demo_series.dtype),
        "name": visitas_demo_series.name,
        "index": visitas_demo_series.index.tolist(),
    }

    informacion_demo_series
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Una `Series` se parece a un array porque es unidimensional y permite
    operaciones vectorizadas. No obstante, su índice participa en la selección y
    en la alineación de operaciones.

    El índice no tiene que ser texto, pero debe identificar de manera coherente
    las observaciones. Si no lo indicamos, Pandas crea etiquetas numéricas
    consecutivas. Esas etiquetas pueden coincidir visualmente con posiciones, pero
    siguen siendo conceptos distintos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Construye una Series y conserva su significado

    Crea `serie_visitas` con los valores y códigos preparados. Asigna el nombre
    `"visitas"`. Después recupera ese nombre desde el atributo correspondiente y
    guárdalo en `nombre_serie`.

    El Coach revisará el tipo del objeto, sus valores, su índice y su nombre.
    """)
    return


@app.cell
def _(feedback, pd):
    valores_visitas = [8, 12, 9]
    codigos_visitas = ["P01", "P02", "P03"]

    # TU TURNO: crea la Series etiquetada y consulta su nombre.
    serie_visitas = None
    nombre_serie = None

    feedback.exercise("series_creacion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Separa etiqueta y posición

    Pandas ofrece dos indexadores con intenciones diferentes:

    - `loc` selecciona mediante **etiquetas**;
    - `iloc` selecciona mediante **posiciones enteras**.

    ```python
    visitas.loc["P02"]
    visitas.iloc[1]
    ```

    En esta Series ambas expresiones llegan al valor `12`, pero no formulan la
    misma solicitud. Una pide la observación identificada como P02; la otra pide
    la segunda posición disponible.
    """)
    return


@app.cell
def _(visitas_demo_series):
    seleccion_demo_series = {
        "por etiqueta": visitas_demo_series.loc["P02"],
        "por posición": visitas_demo_series.iloc[1],
        "etiquetas P01 a P02": visitas_demo_series.loc["P01":"P02"],
        "posiciones 0 a 1": visitas_demo_series.iloc[0:2],
    }

    seleccion_demo_series
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hay una diferencia de frontera que vale la pena observar:

    - un corte con `loc["P01":"P02"]` incluye la etiqueta final;
    - un corte con `iloc[0:2]` excluye la posición final, como los cortes de
      Python y NumPy.

    Si una etiqueta no existe, `loc` puede producir un `KeyError`. Ese error no
    significa que la Series esté dañada: indica que la etiqueta solicitada no
    pertenece a su índice.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Llega al mismo valor por dos rutas

    Usa la Series preparada para seleccionar la observación P02 mediante su
    etiqueta y mediante su posición. Guarda los dos escalares por separado.

    El objetivo no es ahorrar una línea: es demostrar que puedes expresar qué
    clase de referencia estás utilizando.
    """)
    return


@app.cell
def _(feedback, pd):
    serie_seleccion_base = pd.Series(
        [8, 12, 9],
        index=["P01", "P02", "P03"],
        name="visitas",
    )

    # TU TURNO: selecciona P02 por etiqueta y la segunda posición con iloc.
    valor_por_etiqueta = None
    valor_por_posicion = None

    feedback.exercise("series_seleccion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Filtra y conserva el índice

    Comparar una Series produce otra Series booleana con el mismo índice:

    ```python
    visitas >= 10
    ```

    Al usar esa máscara sobre la Series original, Pandas conserva los valores que
    cumplen la condición y también sus etiquetas. La salida sigue explicando a
    qué observación corresponde cada resultado.
    """)
    return


@app.cell
def _(visitas_demo_series):
    mascara_demo_series = visitas_demo_series >= 10
    filtro_demo_series = visitas_demo_series[mascara_demo_series]

    {
        "máscara": mascara_demo_series,
        "resultado": filtro_demo_series,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La máscara y los datos están alineados por índice. Si construyes una máscara
    externa con etiquetas diferentes, Pandas intentará relacionarlas y puede
    advertir que la selección no es válida.

    Para una primera práctica, crea la máscara directamente desde la Series que
    vas a filtrar. Así queda visible que cada decisión proviene del mismo objeto.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conserva valores y códigos después del filtro

    Filtra las observaciones que alcanzan o superan `10`. El resultado debe ser
    una `Series`, no una lista ni un array, porque necesitamos conservar los
    códigos de las observaciones elegidas.
    """)
    return


@app.cell
def _(feedback, pd):
    serie_filtro_base = pd.Series(
        [7, 12, 9, 15, 11],
        index=["P01", "P02", "P03", "P04", "P05"],
        name="medicion",
    )

    # TU TURNO: construye la condición y filtra la Series.
    serie_alertas = None

    feedback.exercise("series_filtro", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Observa la alineación antes de sumar

    La diferencia más importante frente a un array aparece al operar entre dos
    Series. Pandas relaciona valores por sus etiquetas, no por la posición visual.

    ```python
    base = pd.Series([1, 2, 3], index=["A", "B", "C"])
    adicional = pd.Series([30, 10, 20], index=["C", "A", "B"])
    base + adicional
    ```

    La etiqueta A relaciona `1` con `10`; B relaciona `2` con `20`; C relaciona
    `3` con `30`. El orden distinto no rompe esa correspondencia.
    """)
    return


@app.cell
def _(pd):
    base_alineacion_demo = pd.Series([1, 2, 3], index=["A", "B", "C"])
    adicional_alineacion_demo = pd.Series([30, 10, 20], index=["C", "A", "B"])
    total_alineacion_demo = base_alineacion_demo + adicional_alineacion_demo

    total_alineacion_demo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Si una etiqueta aparece solo en una de las Series, no existe un par directo
    para realizar la operación. Pandas suele representar ese resultado como un
    valor faltante. No inventa automáticamente un cero porque esa decisión depende
    del significado de los datos.

    Alinear por etiquetas protege relaciones, pero también exige revisar índices
    antes de combinar fuentes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Transfiere la alineación a dos Series desordenadas

    Suma las dos Series preparadas sin extraer sus valores ni reorganizarlas
    manualmente. Deja que Pandas relacione A, B y C mediante el índice.

    Antes de ejecutar, escribe en papel qué suma corresponde a cada etiqueta.
    """)
    return


@app.cell
def _(feedback, pd):
    serie_base_alineacion = pd.Series([1, 2, 3], index=["A", "B", "C"])
    serie_adicional_alineacion = pd.Series(
        [30, 10, 20], index=["C", "A", "B"]
    )

    # TU TURNO: suma las Series conservando la alineación por índice.
    total_alineado = None

    feedback.exercise("series_alineacion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Decide cuándo una Series aporta algo

    Una lista puede bastar cuando el orden contiene toda la información necesaria.
    Un array aporta forma, `dtype` y operaciones numéricas vectorizadas. Una
    Series resulta especialmente útil cuando cada valor necesita una etiqueta y
    esas etiquetas deben sobrevivir a selecciones u operaciones.

    La estructura adecuada no es la más compleja. Es la que conserva las
    relaciones que el problema necesita.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explica el papel del índice

    Describe una situación en la que dos Series puedan tener los mismos valores
    en órdenes diferentes. Explica cómo el índice evita combinar observaciones
    equivocadas y qué revisarías si aparece un valor faltante después de operar.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    cierre_series = mo.ui.text_area(
        label="¿Qué protege el índice de una Series?",
        placeholder="Relaciona etiquetas, selección, alineación y valores faltantes.",
        rows=4,
        full_width=True,
    )
    cierre_series
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lo que conviene conservar

    - Una Series relaciona valores unidimensionales con etiquetas de índice.
    - `loc` selecciona etiquetas; `iloc` selecciona posiciones.
    - Un filtro conserva los valores elegidos y sus etiquetas.
    - Las operaciones entre Series se alinean por índice.
    - Una etiqueta ausente no se reemplaza automáticamente: primero debemos
      interpretar qué significa esa ausencia.

    El siguiente cuaderno reúne varias Series en una estructura bidimensional: el
    `DataFrame`.
    """)
    return


if __name__ == "__main__":
    app.run()
