# ruff: noqa: B018

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 3 · DataFrames de Pandas")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import pandas as pd

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-03-objects-scientific-tools",
        notebook="05_pandas_dataframes",
    )
    return feedback, mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # DataFrames: filas y columnas con significado

    Una `Series` representa una variable etiquetada. Un `DataFrame` reúne varias
    variables en una tabla donde tanto las filas como las columnas pueden tener
    etiquetas.

    En este cuaderno aprenderás a:

    - construir e inspeccionar un DataFrame pequeño;
    - distinguir una columna de una tabla de una sola columna;
    - seleccionar mediante etiquetas y posiciones;
    - filtrar filas con condiciones booleanas;
    - crear una columna derivada sobre una copia;
    - elegir entre lista, array, Series y DataFrame según la información que debe
      conservarse.

    Los registros utilizados son sintéticos. Las reglas sirven para practicar
    operaciones de datos y no representan decisiones clínicas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Identifica qué representa cada dirección

    Imagina una tabla con tres personas y estas columnas:

    ```text
    codigo | edad | grupo
    ```

    ¿Qué representa una fila completa? ¿Qué representa una columna completa? ¿Por
    qué sería problemático guardar las edades, los códigos y los grupos en listas
    separadas sin una estructura que mantenga su correspondencia?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    respuesta_inicial_dataframe = mo.ui.text_area(
        label="¿Qué relación protege una tabla?",
        placeholder=(
            "Explica qué significa recorrer una fila y qué significa recorrer "
            "una columna."
        ),
        rows=4,
        full_width=True,
    )
    respuesta_inicial_dataframe
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
            ## Define una estructura bidimensional etiquetada

            Un **DataFrame** es un objeto tabular bidimensional de Pandas. Cada
            columna tiene un nombre, un `dtype` y valores alineados con el índice
            de las filas.

            Una forma útil de leerlo es:

            - cada fila representa una observación o registro;
            - cada columna representa una variable;
            - el índice identifica las filas;
            - las etiquetas de columna identifican las variables.
            """),
            mo.mermaid(r"""flowchart LR
                D["DataFrame"] --> F["filas: observaciones"]
                D --> C["columnas: variables"]
                D --> I["índice: etiquetas de fila"]
                C --> S1["Series: código"]
                C --> S2["Series: edad"]
                C --> S3["Series: grupo"]"""),
        ],
        gap=1,
    )
    return


@app.cell
def _(pd):
    tabla_demo_dataframe = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03"],
            "edad": [34, 51, 42],
            "grupo": ["A", "B", "A"],
        }
    )

    tabla_demo_dataframe
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    El constructor recibió un diccionario. Cada clave se convirtió en una
    columna y cada lista aportó sus valores. Las listas deben tener la misma
    longitud para que cada posición pueda formar una fila coherente.

    Pandas creó un índice numérico porque no proporcionamos otro. Ese índice no
    reemplaza la columna `codigo`: cumple la función interna de etiquetar filas,
    mientras `codigo` sigue siendo una variable del problema.
    """)
    return


@app.cell
def _(tabla_demo_dataframe):
    inspeccion_demo_dataframe = {
        "tipo": type(tabla_demo_dataframe).__name__,
        "shape": tabla_demo_dataframe.shape,
        "columnas": tabla_demo_dataframe.columns.tolist(),
        "índice": tabla_demo_dataframe.index.tolist(),
        "tipos": tabla_demo_dataframe.dtypes.astype(str).to_dict(),
    }

    inspeccion_demo_dataframe
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Antes de transformar una tabla conviene inspeccionarla:

    - `shape` informa cuántas filas y columnas hay;
    - `columns` muestra las etiquetas de las variables;
    - `dtypes` muestra el tipo almacenado en cada columna;
    - `head()` permite observar las primeras filas.

    Estos atributos y métodos responden preguntas distintas. `shape` no revela
    los nombres; `columns` no revela los tipos; `head()` no garantiza que hayamos
    visto todos los casos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Construye una tabla desde columnas relacionadas

    El diccionario `datos_participantes` ya contiene tres columnas de la misma
    longitud. Conviértelo en un DataFrame llamado `tabla_participantes`.

    No reorganices ni copies manualmente las filas. Deja que el constructor
    preserve la correspondencia por posición del diccionario.
    """)
    return


@app.cell
def _(feedback, pd):
    datos_participantes = {
        "codigo": ["P01", "P02", "P03"],
        "edad": [34, 51, 42],
        "grupo": ["A", "B", "A"],
    }

    # TU TURNO: construye el DataFrame con las tres columnas.
    tabla_participantes = None

    feedback.exercise("dataframe_creacion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Distingue una columna de una tabla

    Los corchetes permiten seleccionar columnas, pero la forma de escribirlos
    cambia el tipo de salida:

    ```python
    tabla["edad"]      # Series
    tabla[["edad"]]    # DataFrame de una columna
    ```

    La primera expresión selecciona una variable unidimensional. La segunda
    selecciona una lista de columnas —aunque la lista tenga un solo nombre— y
    conserva la estructura bidimensional.
    """)
    return


@app.cell
def _(tabla_demo_dataframe):
    columna_edad_demo = tabla_demo_dataframe["edad"]
    tabla_edad_demo = tabla_demo_dataframe[["edad"]]

    {
        "tipo con un corchete": type(columna_edad_demo).__name__,
        "shape con un corchete": columna_edad_demo.shape,
        "tipo con doble corchete": type(tabla_edad_demo).__name__,
        "shape con doble corchete": tabla_edad_demo.shape,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La elección depende de lo que necesitas después. Si vas a operar con una sola
    variable, una Series suele ser adecuada. Si otra función espera una tabla o
    necesitas conservar varias columnas, conviene mantener un DataFrame.

    No hay una opción universalmente superior: el tipo de salida forma parte del
    contrato de la operación.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Selecciona por etiquetas con `loc`

    En un DataFrame, `loc` recibe primero una selección de filas y después una
    selección de columnas:

    ```python
    tabla.loc[filas, columnas]
    ```

    Para conservar todas las filas y elegir dos columnas por nombre:

    ```python
    tabla.loc[:, ["codigo", "edad"]]
    ```

    Los dos puntos conservan todas las etiquetas de fila. La lista mantiene la
    salida como DataFrame y también define el orden de las columnas.
    """)
    return


@app.cell
def _(tabla_demo_dataframe):
    seleccion_loc_demo = tabla_demo_dataframe.loc[:, ["codigo", "edad"]]
    seleccion_iloc_demo = tabla_demo_dataframe.iloc[0:2, 0:2]

    {
        "loc por etiquetas": seleccion_loc_demo,
        "iloc por posiciones": seleccion_iloc_demo,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `iloc` usa posiciones enteras en ambos ejes. `iloc[0:2, 0:2]` selecciona las
    primeras dos filas y las primeras dos columnas; los extremos derechos no se
    incluyen.

    Usa `loc` cuando el significado está expresado en las etiquetas. Usa `iloc`
    cuando la posición es realmente parte de la tarea. Elegir `iloc` solo porque
    parece más corto puede volver frágil el código si cambia el orden de columnas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conserva todas las filas y dos variables

    A partir de la tabla preparada, construye `tabla_identificacion` con las
    columnas `codigo` y `edad`, en ese orden. Usa `loc` para que la selección
    exprese los nombres de las variables.

    La salida debe seguir siendo un DataFrame de tres filas y dos columnas.
    """)
    return


@app.cell
def _(feedback, pd):
    tabla_seleccion_base = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03"],
            "edad": [34, 51, 42],
            "grupo": ["A", "B", "A"],
        }
    )

    # TU TURNO: selecciona todas las filas y las columnas codigo y edad.
    tabla_identificacion = None

    feedback.exercise("dataframe_seleccion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Filtra filas mediante una condición alineada

    Comparar una columna produce una Series booleana con el mismo índice de la
    tabla. Podemos combinar condiciones y utilizar el resultado para seleccionar
    filas:

    ```python
    condicion = tabla["consentimiento"] & tabla["formulario"]
    tabla[condicion]
    ```

    `&` expresa que ambas condiciones deben ser verdaderas. Cada comparación debe
    ir entre paréntesis cuando incluye operadores como `==`, `>=` o `<=`.
    """)
    return


@app.cell
def _(pd):
    tabla_reglas_demo = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03"],
            "consentimiento": [True, False, True],
            "formulario": [True, True, True],
        }
    )
    condicion_demo_dataframe = (
        tabla_reglas_demo["consentimiento"]
        & tabla_reglas_demo["formulario"]
    )
    filas_demo_dataframe = tabla_reglas_demo[condicion_demo_dataframe]

    filas_demo_dataframe
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    El filtro devuelve otra tabla con las mismas columnas y solo las filas donde
    la máscara contiene `True`. El índice original se conserva; Pandas no vuelve
    a numerar automáticamente las filas porque esas etiquetas pueden tener
    significado para operaciones posteriores.

    Si necesitas una lista de códigos, selecciona después la columna y llama
    `.tolist()`. De ese modo cada paso mantiene un resultado con una intención
    clara.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Filtra una regla compuesta y extrae sus códigos

    Construye una condición donde `consentimiento` y `formulario` sean verdaderos.
    Úsala para crear `tabla_continuan`. Después extrae los códigos de esa subtabla
    como una lista llamada `codigos_continuan`.
    """)
    return


@app.cell
def _(feedback, pd):
    tabla_filtro_base = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03", "P04"],
            "consentimiento": [True, False, True, True],
            "formulario": [True, True, True, False],
        }
    )

    # TU TURNO: combina las condiciones, filtra y extrae los códigos.
    tabla_continuan = None
    codigos_continuan = None

    feedback.exercise("dataframe_filtro", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Crea información derivada sin alterar la fuente

    Una columna derivada expresa una transformación de variables existentes. Por
    ejemplo, si `formulario` es booleano, podemos construir una decisión nueva:

    ```python
    copia["requiere_revision"] = ~copia["formulario"]
    ```

    `~` invierte cada booleano de la Series. Trabajar sobre una copia permite
    conservar la tabla fuente y comparar antes y después. Esta precaución será
    esencial cuando estudiemos limpieza de datos.
    """)
    return


@app.cell
def _(pd):
    tabla_derivada_fuente = pd.DataFrame(
        {
            "codigo": ["P01", "P02"],
            "formulario": [True, False],
        }
    )
    tabla_derivada_demo = tabla_derivada_fuente.copy()
    tabla_derivada_demo["requiere_revision"] = ~tabla_derivada_demo["formulario"]

    {
        "fuente": tabla_derivada_fuente,
        "copia": tabla_derivada_demo,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Transfiere el recorrido completo a una tabla nueva

    Trabaja sobre una copia de `tabla_transferencia_fuente`. Agrega la columna
    booleana `requiere_revision`, que será verdadera cuando el formulario esté
    incompleto. Después extrae los códigos correspondientes.

    Guarda también las columnas de la tabla fuente para comprobar que no fue
    modificada. La solución debe dejar tres evidencias: copia enriquecida, códigos
    elegidos y fuente conservada.
    """)
    return


@app.cell
def _(feedback, pd):
    tabla_transferencia_fuente = pd.DataFrame(
        {
            "codigo": ["P01", "P02", "P03"],
            "edad": [34, 51, 42],
            "consentimiento": [True, True, False],
            "formulario": [True, False, True],
        }
    )

    # TU TURNO: copia, deriva requiere_revision y extrae los códigos.
    tabla_seguimiento = None
    codigos_revision = None
    columnas_fuente = None

    feedback.exercise("dataframe_transferencia", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Elige la estructura que conserva lo necesario

    | Estructura | Conserva especialmente | Es adecuada cuando… |
    |---|---|---|
    | lista | orden y mutabilidad | reunimos una secuencia general de objetos |
    | ndarray | forma y `dtype` | operamos por posiciones |
    | Series | valores e índice | una variable necesita etiquetas alineadas |
    | DataFrame | filas, columnas e índice | reunimos varias variables |

    Convertir una estructura en otra puede perder información. Pasar una Series a
    lista elimina su índice; extraer `.values` de un DataFrame elimina las
    etiquetas de columnas. Haz la conversión solo cuando esa pérdida sea
    deliberada.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explica una selección completa

    Describe con tus propias palabras qué ocurre en esta expresión:

    ```python
    tabla.loc[tabla["edad"] >= 40, ["codigo", "edad"]]
    ```

    Separa la explicación en tres partes: construcción de la condición, selección
    de filas y selección de columnas. Indica también qué tipo de objeto esperas
    como resultado.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    cierre_dataframe = mo.ui.text_area(
        label="¿Cómo leerías la expresión de selección?",
        placeholder="Explica condición, filas, columnas y tipo de salida.",
        rows=5,
        full_width=True,
    )
    cierre_dataframe
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lo que conviene conservar

    - Un DataFrame relaciona filas observacionales con columnas que representan
      variables.
    - `shape`, `columns`, `dtypes` y `head()` responden preguntas diferentes.
    - Seleccionar una columna produce una Series; seleccionar una lista de
      columnas conserva un DataFrame.
    - `loc` trabaja con etiquetas y `iloc` con posiciones.
    - Una máscara selecciona filas alineadas con el índice.
    - Crear columnas sobre una copia permite conservar una fuente para comparar.

    Con estos objetos ya puedes leer y construir estructuras científicas pequeñas.
    La siguiente semana utilizará esta base para cargar, inspeccionar y preparar
    datos sin mezclar todavía esas decisiones con la definición de los objetos.
    """)
    return


if __name__ == "__main__":
    app.run()
