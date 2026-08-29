# ruff: noqa: B018, F401

import marimo

__generated_with = "0.23.16"
app = marimo.App(
    width="medium",
    app_title="Semana 3 · Módulos, librerías e importaciones",
)


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-03-objects-scientific-tools",
        notebook="02_modulos_librerias_e_importaciones",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Módulos y librerías: usar código que ya tiene un lugar

    Un programa no necesita definir desde cero cada operación. Python permite
    cargar módulos y utilizar los nombres que ofrecen: funciones, constantes,
    clases y otros objetos.

    En este cuaderno vas a:

    - distinguir módulo, paquete y librería;
    - interpretar qué hace `import`;
    - usar espacios de nombres y alias;
    - comparar una importación de módulo con una importación selectiva;
    - elegir una forma de importación que deje visible el origen de cada nombre.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Empieza por el origen de un nombre

    Compara estas expresiones:

    ```python
    sqrt(81)
    math.sqrt(81)
    ```

    Ambas podrían ser válidas en contextos distintos. ¿Cuál permite reconocer de
    inmediato de dónde viene `sqrt`? ¿Qué tendría que ocurrir antes para que cada
    expresión funcione?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    respuesta_inicial_modulos = mo.ui.text_area(
        label="¿Qué información aporta escribir math.sqrt?",
        placeholder="Relaciona el nombre math con el origen de la función sqrt.",
        rows=3,
        full_width=True,
    )
    respuesta_inicial_modulos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
            ## Organiza los términos antes de importar

            Un **módulo** es una unidad de código Python que define nombres
            reutilizables. Muchos módulos corresponden a un archivo `.py`, aunque
            también pueden implementarse de otras maneras.

            Un **paquete** organiza módulos relacionados bajo un nombre común. Una
            **librería** es un término más amplio: se refiere a código distribuido
            para resolver una familia de tareas y puede contener uno o varios
            paquetes y módulos.

            Estas palabras describen niveles distintos; no son tres sinónimos.
            """),
            mo.mermaid(r"""flowchart LR
                L["librería"] --> P["paquete"]
                P --> M1["módulo A"]
                P --> M2["módulo B"]
                M1 --> N1["funciones"]
                M1 --> N2["constantes"]"""),
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    NumPy y Pandas son librerías. Cuando escribimos `import numpy`, Python carga
    el módulo público llamado `numpy` y liga ese objeto al nombre `numpy` en el
    notebook.

    La biblioteca estándar ya viene con Python. Incluye módulos como `math`,
    `statistics`, `pathlib` y `datetime`. No se instalan por separado, pero sí se
    importan cuando queremos usar sus nombres.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interpreta `import` como una asignación de nombres

    Después de ejecutar:

    ```python
    import math
    ```

    el nombre `math` referencia un objeto módulo. La notación con punto del
    cuaderno anterior permite buscar objetos dentro de ese módulo:

    ```python
    math.pi
    math.sqrt(81)
    ```

    `pi` es un atributo con un número. `sqrt` es un atributo invocable: una
    función disponible dentro del espacio de nombres del módulo.
    """)
    return


@app.cell
def _():
    import math as _math

    evidencia_modulo = {
        "tipo": type(_math).__name__,
        "pi": _math.pi,
        "raíz": _math.sqrt(81),
        "sqrt es invocable": callable(_math.sqrt),
    }

    evidencia_modulo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Un **namespace** o espacio de nombres relaciona nombres con objetos. El módulo
    conserva su propio espacio de nombres; por eso `math.sqrt` y `math.ceil`
    pueden convivir con variables de nuestro notebook sin ocupar nombres sueltos.

    Esta forma es especialmente útil al aprender una librería: cada llamada deja
    visible su procedencia.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Usa un alias sin perder el origen

    Un alias cambia el nombre local con el que encontramos el módulo:

    ```python
    import statistics as st

    st.mean([8, 12, 10])
    ```

    El módulo no cambia. Solo ligamos el mismo objeto al nombre corto `st`. Los
    alias son útiles cuando existe una convención ampliamente reconocida, como
    `np` para NumPy y `pd` para Pandas, o cuando un nombre es demasiado largo.

    Un alias poco claro puede empeorar la lectura. No se trata de abreviar por
    abreviar, sino de conservar un nombre reconocible.
    """)
    return


@app.cell
def _():
    import statistics as st

    valores_alias = [8, 12, 10]
    media_alias = st.mean(valores_alias)
    mediana_alias = st.median(valores_alias)

    media_alias, mediana_alias
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Practica un namespace explícito

    Importa `math` con el alias `mt`. Utiliza dos atributos del módulo para
    obtener:

    - la raíz cuadrada de `81`;
    - el entero que resulta de redondear `4.2` hacia arriba.

    Las dos llamadas deben conservar visible el alias. No importes las funciones
    de manera selectiva en este ejercicio.
    """)
    return


@app.cell
def _(feedback):
    # TU TURNO: importa math como mt y usa su namespace.

    raiz_modulo = None
    techo_modulo = None

    feedback.exercise("modulos_namespace", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Compara la importación selectiva

    También podemos traer un nombre concreto al namespace del notebook:

    ```python
    from statistics import mean

    mean([8, 12, 10])
    ```

    Esta forma es compacta, pero el origen de `mean` ya no aparece en la llamada.
    Además, una variable posterior con el mismo nombre podría ocultar la función.

    ```python
    mean = 10
    # mean([8, 12, 10]) ya no puede llamar la función
    ```

    La importación selectiva no es incorrecta. Conviene usarla cuando el origen es
    claro, el nombre es específico y el riesgo de colisión es pequeño.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Elige una forma según la tarea

    | Forma | Qué nombre aparece | Cuándo resulta clara |
    |---|---|---|
    | `import math` | `math` | cuando queremos mantener visible el módulo |
    | `import numpy as np` | `np` | cuando existe un alias convencional |
    | `from math import sqrt` | `sqrt` | cuando usamos pocos nombres muy específicos |
    | `from math import *` | muchos nombres | se evita porque oculta el origen |

    El asterisco incorpora muchos nombres sin mostrarlos en la instrucción. Esa
    ambigüedad dificulta leer, depurar y mantener el programa.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Resuelve una necesidad nueva con la biblioteca estándar

    En una actividad participan 23 personas. Cada grupo admite máximo 5. Calcula
    cuántos grupos completos debemos preparar para que nadie quede por fuera.

    Usa el módulo `math` mediante un namespace explícito. El resultado debe ser un
    entero y debe contemplar el grupo adicional cuando la división no es exacta.
    """)
    return


@app.cell
def _(feedback):
    import math

    personas_actividad = 23
    capacidad_por_grupo = 5

    # TU TURNO: usa una operación de math para calcular la capacidad necesaria.
    cantidad_grupos = None

    feedback.exercise("modulos_transferencia", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lee un import que encuentres en otro programa

    Cuando revises código desconocido, pregunta en este orden:

    1. ¿qué nombre queda disponible después del import?
    2. ¿ese nombre representa un módulo o un objeto seleccionado?
    3. ¿qué parte de la llamada muestra su procedencia?
    4. ¿hay una variable que podría ocultar ese nombre más adelante?

    Esta lectura será útil en el siguiente notebook. Allí `import numpy as np`
    prepara el namespace desde el cual construiremos arrays.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explica la decisión de importación

    Imagina que encuentras `np.array(...)` en un notebook. Explica qué objeto
    representa `np`, qué busca el punto y por qué ese nombre corto no impide
    reconocer la librería de origen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    cierre_modulos = mo.ui.text_area(
        label="¿Cómo interpretarías np.array(...) paso a paso?",
        placeholder="Relaciona alias, módulo, atributo y llamada.",
        rows=4,
        full_width=True,
    )
    cierre_modulos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lo que conviene conservar

    - Un módulo reúne nombres reutilizables en su propio namespace.
    - Un paquete organiza módulos; una librería puede reunir varios paquetes y
      módulos para una familia de tareas.
    - `import` liga un objeto o nombre al namespace del notebook.
    - La notación con punto mantiene visible la procedencia de una operación.
    - Los alias ayudan cuando son reconocibles; las importaciones con asterisco
      dificultan saber de dónde viene cada nombre.
    """)
    return


if __name__ == "__main__":
    app.run()
