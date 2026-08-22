import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Listas")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="02_listas",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Listas: valores que conservan su lugar

    Usamos una lista cuando necesitamos reunir varios valores sin perder el orden
    en que aparecen. Una agenda de turnos, una serie de mediciones o una fila de
    archivos pendientes son buenos ejemplos: cada elemento ocupa un lugar y la
    colección puede cambiar con el tiempo.

    En este cuaderno vamos a mirar tres ideas con cuidado:

    - qué información conserva una lista;
    - qué ocurre cuando añadimos, retiramos o reordenamos sus elementos;
    - por qué dos nombres pueden mostrar los cambios de una misma lista.

    Al final resolverás un caso nuevo y explicarás, con tus propias palabras, por
    qué una lista es una representación adecuada.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Antes de leer la definición: ¿qué necesitamos conservar?

    Considera estas tres observaciones tomadas en momentos diferentes:

    ```text
    Temperatura 21/Ago/2026

    6:06 = 20
    12:20 = 30
    22:00 = 21
    ```

    Mira las tres observaciones y responde:

    1. ¿Importa el orden en que ocurrieron?
    2. ¿Debe conservarse que el valor `8` apareció dos veces?
    3. ¿Podría añadirse otra observación después?

    Escribe una respuesta breve en el espacio siguiente. No buscamos una definición
    técnica todavía: interesa identificar qué información no debería perderse.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    respuesta_inicial_listas = mo.ui.text_area(
        label="¿Qué debería conservar una colección para representar estas observaciones?",
        placeholder="Escribe qué pasaría con el orden, la repetición del 8 y una posible observación nueva.",
        rows=3,
        full_width=True,
    )
    respuesta_inicial_listas
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. ¿Qué es una lista?

    Una **lista** es un tipo de dato de Python que reúne varios elementos en una
    secuencia. Es **ordenada** porque cada elemento conserva una posición y es
    **mutable** porque podemos cambiar su contenido después de crearla.

    Cada parte de la definición aporta algo:

    | Término | Significado observable |
    |---|---|
    | tipo de dato de Python | podemos usarlo sin instalar ni importar una biblioteca |
    | secuencia | cada elemento ocupa una posición |
    | ordenada | cambiar el orden puede cambiar el significado |
    | mutable | la misma lista puede recibir, perder o reemplazar elementos |
    | elementos | puede contener números, textos, booleanos u otros objetos |

    Se escribe entre corchetes y sus elementos se separan con comas:

    ```python
    mediciones = [8, 8, 12]
    nombres = ["Ana", "Luis"]
    pendientes = []
    ```

    Los valores repetidos no desaparecen: cada aparición ocupa su propia posición.
    Python permite mezclar tipos dentro de una lista, aunque en muchos problemas es
    más claro reunir valores que cumplen una función parecida.
    """)
    return


@app.cell
def _():
    mediciones_definicion = [8, 8, 12]
    tipo_mediciones = type(mediciones_definicion)
    cantidad_mediciones = len(mediciones_definicion)
    tipo_mediciones, cantidad_mediciones
    return cantidad_mediciones, tipo_mediciones


@app.cell(hide_code=True)
def _(cantidad_mediciones, mo, tipo_mediciones):
    mo.md(rf"""
    Python informa que el objeto es `{tipo_mediciones}` y que contiene
    `{
        cantidad_mediciones
    }` elementos. La longitud cuenta posiciones, no valores
    diferentes: los dos `8` ocupan lugares distintos y ambos forman parte de la
    información.

    {
        mo.mermaid('''flowchart LR
        N[nombre: mediciones] --> L[lista]
        L --> P0[posición 0: 8]
        L --> P1[posición 1: 8]
        L --> P2[posición 2: 12]''')
    }
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Aclaremos los límites de la definición

    - No es “un grupo de valores sin orden”: sus posiciones importan.
    - No elimina automáticamente repeticiones.
    - No relaciona atributos con nombres como `"edad"` o `"grupo"`.
    - No es inmutable: sus elementos pueden cambiar.

    Más adelante compararemos las listas con otras estructuras. Por ahora, quédate
    con cuatro propiedades: una lista conserva posiciones, orden y repeticiones, y
    permite cambiar su contenido.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Ubicar un elemento sin cambiar la lista

    Python numera desde cero. Los índices negativos cuentan desde el final:

    ```text
    elemento      "P01"    "P02"    "P03"    "P04"
    índice           0         1         2         3
    índice neg.     -4        -3        -2        -1
    ```

    Un índice permite consultar una posición. Un **corte** —también llamado
    *slice*— toma varias posiciones y produce una lista nueva con ese tramo.
    """)
    return


@app.cell
def _():
    codigos_acceso = ["P01", "P02", "P03", "P04"]
    primer_codigo = codigos_acceso[0]
    ultimo_codigo = codigos_acceso[-1]
    codigos_centrales = codigos_acceso[1:3]
    primeros_tres = codigos_acceso[:3]
    return codigos_centrales, primer_codigo, primeros_tres, ultimo_codigo


@app.cell(hide_code=True)
def _(codigos_centrales, mo, primer_codigo, primeros_tres, ultimo_codigo):
    mo.md(f"""
    | Expresión | Resultado | Interpretación |
    |---|---|---|
    | `[0]` | `{primer_codigo}` | primer elemento |
    | `[-1]` | `{ultimo_codigo}` | último elemento |
    | `[1:3]` | `{codigos_centrales}` | desde 1 hasta antes de 3 |
    | `[:3]` | `{primeros_tres}` | desde el comienzo hasta antes de 3 |

    En un corte, la posición final no se incluye. Por ejemplo, `[1:3]` toma las
    posiciones 1 y 2. Pedir un índice inexistente produce `IndexError`; un corte
    que supera el final simplemente se detiene donde termina la lista.

    Operaciones de consulta frecuentes:

    - `len(lista)`: cantidad de elementos;
    - `valor in lista`: responde si el valor está presente;
    - `lista.count(valor)`: cantidad de apariciones;
    - `lista.index(valor)`: primera posición del valor.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Cambiar el contenido: eso es mutabilidad

    Cuando modificamos una lista, el mismo objeto queda con un contenido diferente.
    A ese cambio lo llamamos **mutación**. En lugar de memorizar métodos aislados,
    relaciona cada uno con la decisión que necesitas tomar:

    | Intención | Método | Pregunta que debes resolver |
    |---|---|---|
    | añadir al final | `append(valor)` | ¿es un elemento o varios? |
    | añadir varios | `extend(coleccion)` | ¿debo incorporar cada elemento? |
    | añadir en una posición | `insert(i, valor)` | ¿qué posición debe ocupar? |
    | retirar por valor | `remove(valor)` | ¿sé cuál valor sale? |
    | retirar por posición | `pop(i)` | ¿conozco el lugar y necesito guardar lo retirado? |
    | ordenar la misma lista | `sort()` | ¿quiero cambiar el orden de esta lista? |
    | invertir la misma lista | `reverse()` | ¿quiero que el orden inverso reemplace al actual? |

    Ojo con una diferencia que suele pasar inadvertida: `append(["A", "B"])`
    añade una lista completa como un solo elemento; `extend(["A", "B"])` añade
    `"A"` y `"B"` como dos elementos separados. Para escoger, imagina primero
    cómo debería verse el resultado.
    """)
    return


@app.cell
def _():
    agenda_ejemplo = ["Laura", "Mateo"]
    estados_agenda = [("inicio", agenda_ejemplo.copy())]
    agenda_ejemplo.append("Sara")
    estados_agenda.append(("append", agenda_ejemplo.copy()))
    agenda_ejemplo.insert(1, "Diana")
    estados_agenda.append(("insert", agenda_ejemplo.copy()))
    persona_atendida = agenda_ejemplo.pop(0)
    estados_agenda.append(("pop", agenda_ejemplo.copy()))
    return estados_agenda, persona_atendida


@app.cell(hide_code=True)
def _(estados_agenda, mo, persona_atendida):
    mo.md(f"""
    ### Sigamos los cambios de una agenda

    Cada línea muestra la operación que acaba de ocurrir y el contenido de la
    agenda después de esa operación:

    1. `{estados_agenda[0]}`
    2. `{estados_agenda[1]}`
    3. `{estados_agenda[2]}`
    4. `{estados_agenda[3]}`

    Busca dos momentos: cuándo Diana cambia de posición y cuándo una persona deja
    de aparecer. `pop(0)` retiró a `{persona_atendida}` y además devolvió ese nombre,
    por eso podemos guardarlo en otra variable. Esta lectura paso a paso se llama
    **traza** y sirve para localizar el primer cambio que no coincide con lo esperado.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Antes de ejecutar: ¿qué listas cambiarán?

    Lee el código línea por línea. `grupos_alias` se crea mediante una asignación;
    `grupos_copia`, mediante `copy()`. Después se añade un valor desde cada nombre.

    ```python
    grupos_base = ["A", "B"]
    grupos_alias = grupos_base
    grupos_copia = grupos_base.copy()

    grupos_alias.append("C")
    grupos_copia.append("D")
    ```

    Antes de comprobar el resultado, reemplaza los tres valores iniciales por las
    listas que crees que mostrará cada nombre al finalizar. Empieza por una pregunta:
    ¿cuántas listas distintas se crearon realmente?

    La revisión automática comparará únicamente las tres listas. Después tendrás
    un espacio para explicar por qué dos nombres terminan mostrando el mismo cambio.
    """)
    return


@app.cell
def _(feedback):
    # Escribe cómo crees que quedará cada nombre al finalizar el código anterior.
    resultado_esperado_base = "PENDIENTE"
    resultado_esperado_alias = None
    resultado_esperado_copia = None
    feedback.exercise("listas_traza", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_alias = mo.ui.text_area(
        label="Explica lo que ocurrió",
        placeholder="¿Cuántas listas se crearon? ¿Por qué grupos_base y grupos_alias terminaron con el mismo contenido?",
        rows=3,
        full_width=True,
    )
    explicacion_alias
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ### Compara tu explicación con este modelo

    {
        mo.mermaid('''flowchart LR
        B[nombre: grupos_base] --> L[lista compartida: A, B, C]
        A[nombre: grupos_alias] --> L
        C[nombre: grupos_copia] --> LC[lista independiente: A, B, D]''')
    }

    Cuando una asignación crea otro nombre para la misma lista, decimos que ese
    nombre es un **alias**. `grupos_base` y `grupos_alias` son alias del mismo
    objeto; `copy()` sí produce otra lista. Esta diferencia permite anticipar qué
    nombres mostrarán una mutación.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Decidir entre cambiar una lista y crear otra

    Algunas operaciones modifican el objeto y suelen devolver `None`:

    ```python
    lista.append(valor)
    lista.sort()
    lista.reverse()
    ```

    Otras expresiones producen una lista nueva:

    ```python
    ampliada = lista + [valor]
    ordenada = sorted(lista)
    copia = lista.copy()
    tramo = lista[1:3]
    ```

    Por eso `resultado = lista.sort()` deja `resultado` en `None`: `sort()` ordena
    la lista existente, pero no devuelve una lista nueva. En un cuaderno reactivo
    como marimo, crear un resultado nuevo también ayuda a ver con claridad qué
    valor utiliza cada celda.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Elige cómo representar los cambios de una agenda

    La agenda inicial es `['Laura', 'Mateo', 'Sara']`. Después ocurren estos
    eventos:

    - Diana requiere atención prioritaria y debe ocupar la primera posición.
    - Mateo cancela su turno.
    - Pablo e Inés se incorporan al final en ese orden.
    - Se atiende y retira la primera persona.

    Trabaja sobre una copia para que `agenda_base` permanezca igual. Representa los
    cuatro eventos en el orden en que ocurrieron; no escribas directamente la lista
    final. Al terminar:

    - `persona_atendida_turno` debe guardar el nombre de quien salió primero;
    - `agenda_final` debe conservar, en orden, a las personas que siguen esperando.

    Aquí debes escoger las operaciones. Pregúntate en qué evento conoces una
    posición, en cuál conoces un valor y en cuál necesitas añadir varios elementos.
    """)
    return


@app.cell
def _(feedback):
    agenda_base = ["Laura", "Mateo", "Sara"]
    # Crea una copia de trabajo y representa los cuatro eventos en orden.
    agenda_final = "PENDIENTE"
    persona_atendida_turno = None
    feedback.exercise("listas_operaciones", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_agenda = mo.ui.text_area(
        label="Explica una de tus decisiones",
        placeholder="Elige uno de los eventos y explica por qué usaste una operación por posición o por valor.",
        rows=3,
        full_width=True,
    )
    explicacion_agenda
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Encuentra la causa de tres resultados inesperados

    El programa debería conservar `etiquetas_base`, añadir `"archivo"` y
    `"revisión"` como elementos separados y producir otra lista ordenada. Esta fue
    la primera versión:

    ```python
    etiquetas_trabajo = etiquetas_base
    etiquetas_trabajo.append(["archivo", "revisión"])
    etiquetas_ordenadas = etiquetas_trabajo.sort()
    ```

    Al ejecutarla aparecen tres síntomas:

    1. la lista original también cambia;
    2. las dos etiquetas nuevas quedan dentro de una lista anidada;
    3. `etiquetas_ordenadas` queda en `None`.

    Corrige el código, pero hazlo una causa a la vez. Para cada síntoma, identifica
    primero la línea que podría producirlo y luego cambia únicamente esa decisión.
    """)
    return


@app.cell
def _(feedback):
    etiquetas_base = ["control", "seguimiento", "urgente"]
    # Corrige las tres causas y conserva la lista original.
    etiquetas_trabajo = "PENDIENTE"
    etiquetas_ordenadas = None
    feedback.exercise("listas_depuracion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_depuracion = mo.ui.text_area(
        label="Registra cómo encontraste las causas",
        placeholder="Relaciona cada síntoma con la línea que lo produjo. ¿Cuál corrección hiciste primero y por qué?",
        rows=4,
        full_width=True,
    )
    explicacion_depuracion
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Decidir si una lista es la representación adecuada

    Una lista es una buena elección cuando:

    - el orden tiene significado;
    - las repeticiones deben conservarse;
    - se consulta por posición o se recorren los elementos;
    - la colección puede crecer, reducirse o reordenarse.

    No es la mejor elección cuando:

    - solo interesan valores únicos;
    - cada atributo necesita una clave como `"edad"`;
    - las posiciones deben permanecer fijas;
    - una modificación accidental debería ser imposible.

    Vale la pena cambiar la pregunta. En lugar de “¿puedo resolverlo con una
    lista?”, pregunta “¿qué información conservará la lista y qué información
    dejará por fuera?”.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Reto final: organiza la recepción de muestras

    `muestras_recepcion` registra llegadas en orden. `M01` aparece dos veces porque
    representa dos entregas diferentes; la repetición no debe eliminarse.

    ```python
    muestras_recepcion = ["M01", "M02", "M01", "M03"]
    ```

    A partir de esa lista, prepara tres resultados:

    1. `lote_despacho`: las dos primeras llegadas;
    2. `cola_pendiente`: el resto de la cola, con `M99` insertada como prioridad;
    3. `apariciones_m01`: cuántas entregas de `M01` constan en la recepción.

    Conserva intacta la lista original. Usa posiciones, cortes y operaciones de
    lista; no uses ciclos ni comprensiones, que se estudiarán después.

    Cuando el código funcione, explica qué dato concreto se perdería si las dos
    apariciones de `M01` se conservaran como una sola. Explica también por qué no
    basta con que `M99` esté presente: su posición comunica que debe procesarse antes.
    """)
    return


@app.cell
def _(feedback):
    muestras_recepcion = ["M01", "M02", "M01", "M03"]
    # Construye los tres resultados sin modificar muestras_recepcion.
    lote_despacho = "PENDIENTE"
    cola_pendiente = None
    apariciones_m01 = None
    feedback.exercise("listas_transferencia", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_transferencia = mo.ui.text_area(
        label="Explica por qué una lista funciona en este caso",
        placeholder="¿Qué se perdería si M01 apareciera una sola vez? ¿Qué comunica la primera posición de M99?",
        rows=4,
        full_width=True,
    )
    explicacion_transferencia
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cierre: explica la idea con tus palabras

    Redacta una explicación breve para alguien que todavía no ha trabajado con
    listas. Incluye estas ideas sin convertirlas en una enumeración de definiciones:

    - qué conserva una lista;
    - qué significa que sea mutable;
    - por qué un alias y una copia reaccionan de manera diferente;
    - un caso en el que perder el orden o una repetición cambiaría la información.

    Si tu explicación depende de “porque así es la sintaxis”, vuelve al ejemplo de
    la agenda o al diagrama de alias y describe qué cambió paso a paso.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    resumen_listas = mo.ui.text_area(
        label="Mi explicación de las listas",
        placeholder="Escribe aquí tu explicación final. Este texto no se califica.",
        rows=6,
        full_width=True,
    )
    resumen_listas
    return


if __name__ == "__main__":
    app.run()
