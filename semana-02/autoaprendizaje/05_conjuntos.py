import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Conjuntos")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback
    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="05_conjuntos",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Conjuntos: pertenencia y valores únicos

    Imagina dos listados de códigos. En uno interesa saber cuántas veces aparece
    cada código; en el otro, únicamente cuáles códigos están presentes. Aunque
    ambos parten de los mismos valores, no necesitan conservar la misma información.

    En este cuaderno aprenderás a reconocer cuándo la ausencia de repeticiones es
    una ventaja, a comparar grupos mediante operaciones de conjuntos y a detectar
    cuándo esta estructura haría perder información importante.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Decide primero si una repetición aporta información

    Observa esta secuencia: `P01, P02, P01, P03`. Si representa cuatro visitas,
    las dos apariciones de `P01` importan. Si representa las personas que asistieron
    al menos una vez, basta con conservar `P01` una sola vez.

    Un **conjunto** es una colección mutable de elementos únicos. Sirve cuando la
    pregunta principal es “¿qué valores están presentes?” y no “¿en qué orden
    aparecieron?” ni “¿cuántas veces apareció cada uno?”.

    ```python
    grupos = {"A", "B", "C"}
    vacio = set()
    ```

    `{}` crea un diccionario vacío, no un conjunto; por eso usamos `set()`.
    Repetir un valor no crea otra posición: `set(["A", "B", "A"])` contiene
    únicamente `"A"` y `"B"`.

    Un conjunto no asigna posiciones a sus elementos, así que no se consulta por
    índice. Python puede mostrarlos en un orden determinado, pero ese orden no forma
    parte de la información que el conjunto garantiza.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    razon_inicial_conjuntos = mo.ui.text_area(
        label="¿Qué debería conservarse en este caso?",
        placeholder="Escoge un ejemplo —visitas o asistentes únicos— y explica si repetir P01 cambia la información.",
        rows=3,
        full_width=True,
    )
    razon_inicial_conjuntos
    return


@app.cell
def _():
    codigos_repetidos_demo = ["P01", "P02", "P01", "P03"]
    codigos_unicos_demo = set(codigos_repetidos_demo)
    aparece_p02 = "P02" in codigos_unicos_demo
    return aparece_p02, codigos_repetidos_demo, codigos_unicos_demo


@app.cell(hide_code=True)
def _(aparece_p02, codigos_unicos_demo, mo):
    mo.md(f"""
    ## 2. Comprueba presencia sin buscar una posición

    Al convertir la lista, Python produce `{codigos_unicos_demo}`. La expresión
    `"P02" in codigos_unicos_demo` pregunta si ese código pertenece al conjunto y
    responde `{aparece_p02}`. No necesitamos saber en qué posición estaría.

    La conversión conserva los códigos presentes, pero descarta una aparición de
    `P01`. Ese resultado es adecuado para identificar participantes únicos y sería
    inadecuado para contar visitas. Elegir una estructura también significa decidir
    qué información estamos dispuestos a dejar por fuera.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Cambia el conjunto según lo que sabes del problema

    Los conjuntos son mutables: podemos añadir o retirar elementos después de
    crearlos. En lugar de memorizar métodos aislados, relaciona cada operación con
    la decisión que representa:

    | Intención | Operación | Decisión importante |
    |---|---|---|
    | registrar un valor | `add(valor)` | si ya existe, el conjunto no lo repite |
    | incorporar varios valores | `update(coleccion)` | cada elemento se añade por separado |
    | retirar un valor obligatorio | `remove(valor)` | su ausencia produce `KeyError` |
    | retirar un valor opcional | `discard(valor)` | su ausencia no detiene el programa |
    | retirar algún elemento | `pop()` | no podemos escogerlo por posición |
    | vaciar la colección | `clear()` | se eliminan todos los elementos |
    | trabajar sin alterar la fuente | `copy()` | se crea otro conjunto |

    La diferencia entre `remove` y `discard` no es solo de sintaxis. Si un código
    debía existir, `remove` permite detectar que algo no coincide con lo esperado.
    Si su ausencia es una posibilidad normal, `discard` evita tratarla como error.
    """)
    return


@app.cell
def _():
    categorias_demo = {"A", "B"}
    categorias_editadas = categorias_demo.copy()
    categorias_editadas.add("C")
    categorias_editadas.discard("Z")
    return categorias_demo, categorias_editadas


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Formula la pregunta antes de escoger la operación

    Cuando tenemos dos grupos, cada operación responde una pregunta distinta:

    | Expresión | Pregunta |
    |---|---|
    | `a | b` o `a.union(b)` | ¿qué aparece en al menos uno? |
    | `a & b` o `a.intersection(b)` | ¿qué aparece en ambos? |
    | `a - b` o `a.difference(b)` | ¿qué aparece en `a` pero no en `b`? |
    | `a ^ b` | ¿qué aparece en uno solo? |
    | `a <= b` | ¿todos los elementos de `a` están en `b`? |

    La resta merece atención: `a - b` empieza por `a` y retira lo que también está
    en `b`. Por eso cambiar el orden puede cambiar el resultado. Estas expresiones
    construyen conjuntos nuevos y dejan intactos los originales.

    Existen versiones que modifican el conjunto, como `intersection_update`, pero
    no las necesitamos todavía. Primero conviene hacer visible qué valores entran
    en cada comparación y cuál conjunto permanece como fuente.
    """)
    return


@app.cell
def _():
    sede_norte = {"P01", "P02", "P03"}
    sede_centro = {"P02", "P03", "P04"}
    en_ambas_sedes = sede_norte & sede_centro
    solo_norte = sede_norte - sede_centro
    en_alguna_sede = sede_norte | sede_centro
    return en_alguna_sede, en_ambas_sedes, sede_centro, sede_norte, solo_norte


@app.cell(hide_code=True)
def _(en_alguna_sede, en_ambas_sedes, mo, solo_norte):
    mo.md(f"""
    Lee los resultados como respuestas, no como símbolos aislados:

    - ¿quién aparece en ambas sedes? `{en_ambas_sedes}`;
    - ¿quién aparece en Norte pero no en Centro? `{solo_norte}`;
    - ¿quién aparece en al menos una sede? `{en_alguna_sede}`.

    Python puede cambiar el orden en que muestra esos valores sin cambiar ninguna
    de las tres respuestas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Separa lo compartido, lo exclusivo y el total

    Los conjuntos `ids_control` e `ids_seguimiento` reúnen identificadores de dos
    grupos. Construye tres respuestas sin modificar los conjuntos originales:

    1. `comunes`: identificadores presentes en ambos grupos;
    2. `solo_seguimiento`: identificadores que aparecen en seguimiento y no en control;
    3. `todos_los_ids`: cada identificador presente en al menos uno de los grupos.

    Antes de escribir operadores, formula en palabras la pregunta de cada resultado.
    En la diferencia, revisa cuál conjunto debe quedar a la izquierda.
    """)
    return


@app.cell
def _(feedback):
    ids_control = {"A01", "A02", "A03"}
    ids_seguimiento = {"A02", "A03", "A04", "A05"}
    # Calcula la intersección, la diferencia dirigida y la unión.
    comunes = None
    solo_seguimiento = None
    todos_los_ids = None
    feedback.exercise("conjuntos_operaciones", locals())
    return comunes, solo_seguimiento, todos_los_ids


@app.cell(hide_code=True)
def _(mo):
    explicacion_operaciones_conjuntos = mo.ui.text_area(
        label="Explica la operación en la que el orden sí importa",
        placeholder="¿Por qué seguimiento menos control responde una pregunta diferente de control menos seguimiento?",
        rows=3,
        full_width=True,
    )
    explicacion_operaciones_conjuntos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Reconoce lo que un conjunto conserva y lo que descarta

    Un conjunto representa bien valores únicos, preguntas de pertenencia y
    comparaciones entre grupos. No representa bien una fila, un historial, un
    conteo de repeticiones ni un registro con atributos identificados por nombre.

    Hay otro límite técnico: sus elementos deben ser **inmutables**, es decir, no
    deben cambiar internamente mientras pertenecen al conjunto. Números, textos y
    tuplas simples pueden ser elementos; una lista no. Intentar `{[1, 2]}` produce
    `TypeError`.

    Este límite permite que Python localice cada elemento de manera consistente.
    No significa que el conjunto completo sea inmutable: todavía podemos usar
    `add`, `remove` o `discard` para cambiar qué elementos contiene.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Decide si una persona cubre todos los requisitos

    `competencias_requeridas` contiene lo necesario para una actividad y
    `competencias_persona` contiene lo que una persona ya tiene.

    Calcula primero `competencias_faltantes`: lo requerido que todavía no está
    disponible. A partir de ese resultado, construye `cumple_requisitos` como un
    booleano. Será `True` únicamente cuando no falte ninguna competencia.

    La decisión debe derivarse del conjunto faltante; no escribas el booleano a
    mano para este caso particular.
    """)
    return


@app.cell
def _(feedback):
    competencias_requeridas = {"python", "terminal", "marimo"}
    competencias_persona = {"python", "marimo"}
    # Deriva los faltantes y la decisión booleana a partir de los conjuntos.
    competencias_faltantes = None
    cumple_requisitos = None
    feedback.exercise("conjuntos_transferencia", locals())
    return competencias_faltantes, cumple_requisitos


@app.cell(hide_code=True)
def _(mo):
    explicacion_cobertura_conjuntos = mo.ui.text_area(
        label="Relaciona el conjunto faltante con la decisión",
        placeholder="Explica por qué un conjunto vacío permitiría concluir que se cumplen todos los requisitos.",
        rows=3,
        full_width=True,
    )
    explicacion_cobertura_conjuntos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cierre: explica cuándo la unicidad ayuda y cuándo perjudica

    Redacta una explicación breve para una persona que debe escoger entre lista y
    conjunto. Incluye un caso en el que eliminar repeticiones sea útil y otro en el
    que cambie el significado de los datos. Relaciona también `remove` y `discard`
    con la decisión de tratar una ausencia como error o como posibilidad prevista.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    resumen_conjuntos = mo.ui.text_area(
        label="Mi explicación de los conjuntos",
        placeholder="Escribe qué conservan, qué descartan y una situación en la que los escogerías.",
        rows=5,
        full_width=True,
    )
    resumen_conjuntos
    return


if __name__ == "__main__":
    app.run()
