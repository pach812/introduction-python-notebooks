import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Comparar estructuras")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="06_comparar_estructuras",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Elegir una estructura de datos

    Una estructura de datos no es solo una forma distinta de escribir valores.
    Cada una conserva cierta información, facilita algunas preguntas y deja otras
    por fuera. Por eso la elección comienza en el problema, no en la sintaxis.

    En este cuaderno reunirás listas, tuplas, diccionarios y conjuntos. Al final
    podrás justificar una elección hablando de orden, cambios, claves, repeticiones
    y pertenencia, en lugar de responder solamente “porque se escribe así”.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Antes de comparar: ¿qué pregunta debe responder la colección?

    Los códigos `P01, P02, P01` pueden representar un historial, un grupo de
    personas únicas o un conteo por persona. Los valores son los mismos, pero la
    pregunta cambia qué información necesitamos conservar.

    Escribe una primera elección para uno de esos tres propósitos. No hace falta
    acertar de inmediato; retomaremos la respuesta después de comparar las cuatro
    estructuras.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    eleccion_inicial_estructuras = mo.ui.text_area(
        label="Escoge una representación inicial",
        placeholder="Elige historial, personas únicas o conteo por persona. ¿Qué estructura usarías y qué conservaría?",
        rows=3,
        full_width=True,
    )
    eleccion_inicial_estructuras
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Compara la información que conserva cada estructura

    | Propiedad | Lista | Tupla | Diccionario | Conjunto |
    |---|:---:|:---:|:---:|:---:|
    | Reúne varios valores | Sí | Sí | Sí | Sí |
    | Conserva orden de inserción | Sí | Sí | Sí | No usar como garantía |
    | Acceso por índice | Sí | Sí | No | No |
    | Acceso por clave | No | No | Sí | No |
    | Permite duplicados | Sí | Sí | Claves no; valores sí | No |
    | Puede cambiar | Sí | No sus posiciones | Sí | Sí |
    | Pregunta de pertenencia | elementos | elementos | claves | elementos |

    La tabla no pretende decir que una estructura sea mejor que las demás. Sirve
    para relacionar una necesidad con una propiedad observable.

    Ojo con una palabra que puede confundir: **ordenado** no significa
    automáticamente **clasificado**. Una lista `[3, 1, 2]` conserva ese orden como
    secuencia, aunque sus números no estén organizados de menor a mayor.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## 2. Haz preguntas antes de escoger

    Empieza por la información que debe poder recuperarse. Este recorrido ayuda a
    organizar la decisión:

    {
        mo.mermaid('''flowchart TD
        A{¿Cada dato necesita<br/>un nombre o clave?}
        A -->|Sí| D[Diccionario]
        A -->|No| B{¿Solo importan valores<br/>únicos y pertenencia?}
        B -->|Sí| S[Conjunto]
        B -->|No| C{¿La secuencia<br/>debe poder cambiar?}
        C -->|Sí| L[Lista]
        C -->|No| T[Tupla]''')
    }

    Este árbol es una primera aproximación, no una ley. Un problema real puede
    necesitar varias propiedades a la vez. Por ejemplo, una lista de diccionarios
    representa varios registros en secuencia y cada diccionario conserva sus
    atributos con nombre.
    """)
    return


@app.cell
def _():
    registros_combinados = [
        {"id": "P01", "grupo": "A", "mediciones": (8, 10)},
        {"id": "P02", "grupo": "B", "mediciones": (12, 14)},
    ]
    grupos_combinados = {registro["grupo"] for registro in registros_combinados}
    return grupos_combinados, registros_combinados


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Observa cómo cambia la respuesta al cambiar la representación

    Considera los códigos `P01, P02, P01`:

    - una **lista** conserva las tres apariciones y su orden;
    - una **tupla** conserva lo mismo, pero señala que la secuencia no se editará;
    - un **conjunto** conserva únicamente `P01` y `P02`;
    - un **diccionario** podría conservar frecuencias: `{"P01": 2, "P02": 1}`.

    Ninguna salida es universalmente mejor. La lista responde por el historial; la
    tupla, por una secuencia que se declara estable; el conjunto, por presencia; y
    el diccionario, por la frecuencia asociada con cada código.

    Aquí aparece el criterio central: una elección es adecuada si conserva la
    información necesaria para responder la pregunta. Si convertimos el historial
    en conjunto, por ejemplo, ya no podremos reconstruir ni el orden ni las dos
    apariciones de `P01`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Prioriza una representación clara antes de optimizar

    Un conjunto expresa con claridad una pregunta de pertenencia; un diccionario,
    una consulta por clave. Esa relación entre problema y representación importa
    antes que afirmaciones generales como “esta estructura siempre es más rápida”.

    La velocidad depende de la operación, el tamaño de los datos y la forma de uso.
    Primero aclara la entrada, la salida y la información que no puede perderse.
    Si más adelante el rendimiento importa, la optimización se sustenta con
    mediciones reales, no con una regla memorizada.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Justifica cuatro elecciones de representación

    Para cada situación, asigna el nombre del tipo apropiado: `"lista"`, `"tupla"`,
    `"diccionario"` o `"conjunto"`.

    1. `tipo_historial`: visitas en el orden ocurrido, incluidos duplicados.
    2. `tipo_coordenada`: latitud y longitud que no se editarán por posición.
    3. `tipo_registro`: edad, grupo y sede consultados por nombre.
    4. `tipo_categorias`: categorías presentes sin repeticiones.

    Antes de escribir cada nombre, subraya mentalmente la propiedad decisiva:
    orden y repeticiones, posiciones estables, claves o unicidad. El Coach revisará
    el código; después podrás dejar por escrito la razón de tus elecciones.
    """)
    return


@app.cell
def _(feedback):
    # Escribe el tipo que conserva la propiedad decisiva en cada situación.
    tipo_historial = None
    tipo_coordenada = None
    tipo_registro = None
    tipo_categorias = None
    feedback.exercise("elegir_estructuras", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    justificacion_estructuras = mo.ui.text_area(
        label="Justifica dos de tus elecciones",
        placeholder="Escoge dos situaciones y explica qué información necesita cada una y qué propiedad de la estructura la conserva.",
        rows=4,
        full_width=True,
    )
    justificacion_estructuras
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cierre: construye tu propio criterio de elección

    Antes de elegir una estructura, formula estas preguntas sobre el problema:

    - ¿importan el orden o las repeticiones?
    - ¿la colección debe cambiar después de crearla?
    - ¿cada valor se consulta por posición o por un nombre?
    - ¿solo interesa saber si un valor está presente?

    Vuelve a tu elección inicial y revísala con estas preguntas. Si la mantienes,
    explica por qué. Si la cambias, identifica qué información habías pasado por
    alto. El siguiente cuaderno mostrará cómo procesar estas estructuras elemento
    por elemento sin cambiar lo que representan.
    """)
    return


if __name__ == "__main__":
    app.run()
