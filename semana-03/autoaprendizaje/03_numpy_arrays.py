# ruff: noqa: B018

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 3 · Arrays NumPy")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-03-objects-scientific-tools",
        notebook="03_numpy_arrays",
    )
    return feedback, mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # NumPy: valores organizados para operar en conjunto

    Las listas permiten reunir objetos variados. Cuando la tarea es numérica,
    suele ser más útil representar muchos valores en una estructura que conozca
    su forma y pueda aplicar la misma operación a todas sus posiciones.

    NumPy ofrece el objeto `ndarray`, que llamaremos **array**. En este cuaderno
    aprenderás a:

    - construir e inspeccionar arrays;
    - interpretar `shape`, `ndim` y `dtype`;
    - aplicar operaciones elemento a elemento;
    - seleccionar con índices, cortes y máscaras;
    - reconocer filas, columnas y ejes en una matriz pequeña.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Anticipa una diferencia importante

    ¿Qué crees que devolverá cada expresión?

    ```python
    [2, 4, 6] * 2
    np.array([2, 4, 6]) * 2
    ```

    Escribe los dos resultados esperados. No basta con decir que serán
    diferentes: explica qué significado tiene `* 2` para cada tipo de objeto.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    respuesta_inicial_numpy = mo.ui.text_area(
        label="¿Qué hará la lista y qué hará el array?",
        placeholder=(
            "Escribe ambos resultados y una razón basada en el tipo del objeto."
        ),
        rows=4,
        full_width=True,
    )
    respuesta_inicial_numpy
    return


@app.cell
def _(np):
    lista_contraste_numpy = [2, 4, 6]
    array_contraste_numpy = np.array([2, 4, 6])

    {
        "lista * 2": lista_contraste_numpy * 2,
        "array * 2": array_contraste_numpy * 2,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La lista interpreta `* 2` como repetición de la secuencia. El array interpreta
    la misma sintaxis como multiplicación numérica elemento a elemento.

    Este contraste muestra por qué importa conocer el tipo: una expresión no
    tiene significado aislada del objeto que la recibe. NumPy no convierte una
    lista en “una lista más rápida”; introduce otro tipo con otro conjunto de
    reglas y operaciones.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
            ## Define el objeto central: `ndarray`

            Un `ndarray` es un objeto de NumPy que organiza valores en una forma
            rectangular de una o más dimensiones. Sus posiciones comparten un
            `dtype`, es decir, una representación de dato común.

            Tres atributos permiten orientarnos:

            - `shape`: tamaño de cada dimensión;
            - `ndim`: cantidad de dimensiones;
            - `dtype`: tipo utilizado para almacenar los valores.
            """),
            mo.mermaid(r"""flowchart LR
                A["array [8, 12, 9]"] --> S["shape: (3,)"]
                A --> N["ndim: 1"]
                A --> D["dtype: int64"]"""),
        ],
        gap=1,
    )
    return


@app.cell
def _(np):
    array_inspeccion_numpy = np.array([8, 12, 9])
    informacion_array_numpy = {
        "tipo": type(array_inspeccion_numpy).__name__,
        "shape": array_inspeccion_numpy.shape,
        "ndim": array_inspeccion_numpy.ndim,
        "dtype": str(array_inspeccion_numpy.dtype),
    }

    informacion_array_numpy
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La forma `(3,)` describe una dimensión con tres posiciones. La coma pertenece
    a la representación de una tupla de un solo elemento; no indica una segunda
    dimensión vacía.

    `dtype` no es exactamente lo mismo que `type`. `type` identifica el objeto
    completo como `ndarray`; `dtype` describe cómo se almacenan sus elementos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Construye un array con una intención explícita

    Convierte la lista de mediciones en un array NumPy. Declara `dtype=float`
    para que la representación numérica sea explícita.

    Conserva el orden de los cuatro valores. Al ejecutar, el Coach revisará el
    tipo del objeto, su forma, su `dtype` y sus valores.
    """)
    return


@app.cell
def _(feedback, np):
    mediciones_base_numpy = [72, 68, 75, 80]

    # TU TURNO: construye un array de tipo float a partir de la lista.
    mediciones_array = None

    feedback.exercise("numpy_creacion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Opera sobre todas las posiciones

    Una operación **vectorizada** expresa una transformación sobre el array
    completo. NumPy aplica la operación correspondiente sin que escribamos un
    ciclo `for` explícito.

    ```python
    valores = np.array([10.0, 12.0, 15.0])
    valores * 1.5
    ```

    El resultado es otro array. Cada posición conserva su correspondencia con la
    posición original. El array de entrada no cambia por esa expresión.
    """)
    return


@app.cell
def _(np):
    base_vectorizada_numpy = np.array([10.0, 12.0, 15.0])
    resultado_vectorizado_numpy = base_vectorizada_numpy * 1.5

    {
        "entrada": base_vectorizada_numpy,
        "resultado": resultado_vectorizado_numpy,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La vectorización no significa que cualquier forma pueda combinarse con otra.
    Las dimensiones deben ser compatibles. Un número puede aplicarse a todas las
    posiciones; dos arrays del mismo tamaño pueden operar posición por posición.

    Más adelante estudiarás reglas más amplias de compatibilidad. Por ahora,
    comprueba siempre `shape` antes de relacionar dos arrays.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Aplica una transformación sin construir un ciclo

    Multiplica cada valor de `mediciones_vector_numpy` por el factor preparado.
    La salida debe seguir siendo un array y la entrada debe conservarse.
    """)
    return


@app.cell
def _(feedback, np):
    mediciones_vector_numpy = np.array([10.0, 12.0, 15.0])
    factor_numpy = 1.5

    # TU TURNO: aplica el factor al array completo.
    mediciones_escaladas = None

    feedback.exercise("numpy_vectorizacion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Selecciona posiciones y fragmentos

    En una dimensión, la indexación se parece a la de las listas:

    ```python
    valores[0]      # primera posición
    valores[-1]     # última posición
    valores[1:4]    # desde 1 hasta antes de 4
    ```

    El índice selecciona una posición y suele devolver un escalar. Un corte
    selecciona una región y devuelve otro array. El extremo derecho del corte no
    se incluye.
    """)
    return


@app.cell
def _(np):
    array_cortes_numpy = np.array([5, 8, 12, 9, 15])
    evidencia_cortes_numpy = {
        "primero": array_cortes_numpy[0],
        "último": array_cortes_numpy[-1],
        "posiciones 1 a 3": array_cortes_numpy[1:4],
    }

    evidencia_cortes_numpy
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Convierte una condición en una máscara

    Comparar un array con un límite produce un array booleano de la misma forma:

    ```python
    valores >= 10
    ```

    Cada `True` o `False` responde la pregunta para una posición. Esa máscara
    puede usarse después para seleccionar los valores correspondientes:

    ```python
    valores[valores >= 10]
    ```

    La máscara no contiene los datos seleccionados. Contiene decisiones alineadas
    con ellos.
    """)
    return


@app.cell
def _(np):
    valores_mascara_numpy = np.array([7, 12, 9, 15, 11])
    mascara_demo_numpy = valores_mascara_numpy >= 10
    seleccion_demo_numpy = valores_mascara_numpy[mascara_demo_numpy]

    {
        "valores": valores_mascara_numpy,
        "máscara": mascara_demo_numpy,
        "selección": seleccion_demo_numpy,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Construye y usa una máscara

    Identifica las mediciones que alcanzan o superan el límite `10`. Guarda la
    máscara y úsala para construir un array nuevo con los valores seleccionados.

    Ojo con la frontera: el valor `10` debe quedar incluido aunque no aparezca en
    la lista actual. La comparación debe expresar correctamente esa regla.
    """)
    return


@app.cell
def _(feedback, np):
    valores_filtro_numpy = np.array([7, 12, 9, 15, 11])

    # TU TURNO: construye la máscara para valores de 10 o más y aplícala.
    mascara_seleccion = None
    valores_seleccionados = None

    feedback.exercise("numpy_seleccion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Resume sin perder de vista qué se está reduciendo

    Métodos como `sum`, `mean`, `min` y `max` reducen varios valores a un resumen.
    En un array de una dimensión, una llamada sin argumentos resume todo el
    vector:

    ```python
    valores.mean()
    ```

    En dos dimensiones aparece una decisión adicional: el **eje**. El eje indica
    qué dimensión se recorre para producir el resumen.
    """)
    return


@app.cell
def _(np):
    matriz_demo_numpy = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
        ]
    )
    resumen_matriz_numpy = {
        "shape": matriz_demo_numpy.shape,
        "segunda fila": matriz_demo_numpy[1, :],
        "segunda columna": matriz_demo_numpy[:, 1],
        "media por fila": matriz_demo_numpy.mean(axis=1),
        "media por columna": matriz_demo_numpy.mean(axis=0),
    }

    resumen_matriz_numpy
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En `matriz[filas, columnas]`, la primera parte selecciona filas y la segunda
    selecciona columnas. Los dos puntos significan “conservar todas las
    posiciones de esta dimensión”.

    Para los resúmenes:

    - `axis=0` recorre las filas y deja un resultado por columna;
    - `axis=1` recorre las columnas y deja un resultado por fila.

    Conviene verificar la forma del resultado en lugar de memorizar una frase
    aislada sobre los ejes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Transfiere la selección a una matriz

    Extrae la segunda columna completa de la matriz preparada. Después calcula un
    promedio por cada fila.

    Antes de ejecutar, anticipa la forma de cada resultado: ambos deben tener tres
    posiciones, pero representan recorridos distintos sobre la matriz.
    """)
    return


@app.cell
def _(feedback, np):
    matriz_ejercicio_numpy = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
        ]
    )

    # TU TURNO: selecciona la segunda columna y calcula la media por fila.
    segunda_columna = None
    promedios_por_fila = None

    feedback.exercise("numpy_matriz", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reconoce dos límites frecuentes

    **Combinar condiciones.** Con arrays se usan `&` y `|`, colocando cada
    comparación entre paréntesis:

    ```python
    (valores >= 10) & (valores <= 15)
    ```

    `and` y `or` esperan una sola verdad y no pueden decidir automáticamente qué
    hacer con un array completo de booleanos.

    **Combinar formas.** Dos arrays pueden contener números válidos y aun así no
    ser compatibles. Antes de operar, revisa `shape` y formula qué posiciones
    deberían corresponderse.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explica el cambio de representación

    Describe una situación en la que preferirías un array a una lista. Incluye en
    tu respuesta qué aporta `shape`, qué informa `dtype` y qué significa aplicar
    una operación vectorizada.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    cierre_numpy = mo.ui.text_area(
        label="¿Qué problema representa mejor un array?",
        placeholder=(
            "Explica la estructura, la operación y la evidencia que revisarías."
        ),
        rows=4,
        full_width=True,
    )
    cierre_numpy
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lo que conviene conservar

    - Un `ndarray` organiza valores mediante dimensiones y un `dtype` común.
    - `shape`, `ndim` y `dtype` describen aspectos distintos del objeto.
    - Las operaciones vectorizadas actúan sobre posiciones correspondientes.
    - Una máscara booleana contiene decisiones y permite seleccionar valores.
    - En dos dimensiones se seleccionan filas y columnas; los ejes determinan qué
      dimensión se reduce en un resumen.

    El siguiente cuaderno añade etiquetas a una estructura unidimensional mediante
    una `Series` de Pandas.
    """)
    return


if __name__ == "__main__":
    app.run()
