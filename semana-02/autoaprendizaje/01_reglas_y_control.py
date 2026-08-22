import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Reglas y control")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="01_reglas_y_control",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Semana 2 · Del problema a una decisión en Python

    En la semana anterior trabajaste con valores, tipos, nombres y expresiones.
    Ahora usarás esas expresiones para decidir qué instrucciones ejecuta un programa.

    En este cuaderno pasarás de una regla expresada con palabras a un programa que
    elige un camino. Para hacerlo, describirás procedimientos con pseudocódigo,
    convertirás preguntas en valores booleanos y construirás decisiones con `if`,
    `elif` y `else`.

    Al final podrás seguir el recorrido de un caso, comprobar qué ocurre alrededor
    de un límite y explicar por qué el orden de las condiciones cambia algunos
    resultados.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Separa la información, la pregunta y la respuesta

    Considera esta regla ficticia:

    > Los registros de personas con 60 años o más requieren seguimiento.

    | Pregunta | Decisión para este ejemplo |
    |---|---|
    | ¿Qué información entra? | La edad como número entero |
    | ¿Qué se necesita preguntar? | ¿La edad es mayor o igual que 60? |
    | ¿Qué ocurre si se cumple? | Asignar `"seguimiento"` |
    | ¿Qué ocurre si no se cumple? | Asignar `"general"` |
    | ¿Qué debe salir? | La clasificación asignada |

    Antes de programar hay que precisar qué dato llega, qué pregunta permite tomar
    la decisión y qué resultado corresponde a cada respuesta. Esta separación evita
    escribir código para una regla todavía ambigua. La sintaxis viene después.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Formula una regla antes de mirar su código

    Piensa en una decisión cotidiana o académica que tenga dos resultados posibles:
    por ejemplo, determinar si una entrega está dentro del plazo. ¿Cuál sería el
    dato de entrada, qué pregunta podría responderse con sí o no y cuáles serían
    los dos resultados?

    Escribe una primera versión. No se califica; servirá para comparar el lenguaje
    cotidiano con la estructura del programa.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    regla_inicial = mo.ui.text_area(
        label="Describe la entrada, la pregunta y los dos resultados de tu regla.",
        placeholder="Entra... \nPreguntamos si... \nCuando se cumple... \nEn caso contrario...",
        rows=4,
        full_width=True,
    )
    regla_inicial
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ordena el procedimiento antes de traducirlo a Python

    El pseudocódigo es una descripción ordenada que una persona puede revisar antes
    de convertirla en un lenguaje de programación. No se ejecuta y no tiene una
    sintaxis universal.

    ```text
    ENTRADA
      edad

    PROCESO
      SI edad es mayor o igual que 60
        asignar "seguimiento"
      DE LO CONTRARIO
        asignar "general"

    SALIDA
      clasificación asignada
    ```

    Su función es aclarar entradas, pasos, casos y salida. El ejemplo permite seguir
    una decisión completa: recibe la edad, formula una pregunta que admite dos
    respuestas, asigna una clasificación para cada una y entrega el resultado. No
    consiste en traducir palabra por palabra a Python.

    **No-ejemplo:** `procesar los datos y dar el resultado`. Esa frase no dice qué
    entra, qué regla se aplica ni qué resultado se espera; por tanto, no permite
    implementar o comprobar el procedimiento.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Comprueba si otra persona podría seguir tus pasos

    - ¿Están identificadas todas las entradas?
    - ¿Cada pregunta puede responderse como verdadera o falsa?
    - ¿Existe una acción para cada caso relevante?
    - ¿La salida permite saber qué decidió el procedimiento?

    Si alguna respuesta no está clara, todavía conviene ajustar la regla. Estas
    preguntas permiten encontrar ambigüedades antes de que se conviertan en errores
    de código.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Convierte una pregunta en `True` o `False`

    Para elegir un camino, Python necesita una expresión cuyo resultado sea
    `True` o `False`. Estos dos valores pertenecen al tipo `bool` y se llaman
    **booleanos**.

    | Operador | Pregunta | Ejemplo |
    |---|---|---|
    | `==` | ¿es igual? | `grupo == "A"` |
    | `!=` | ¿es diferente? | `estado != "cerrado"` |
    | `<` / `<=` | ¿es menor?, ¿incluye el límite? | `medicion <= 10` |
    | `>` / `>=` | ¿es mayor?, ¿incluye el límite? | `edad >= 60` |

    > `=` asigna un valor
    >
    > `==` (dos iguales) compara dos valores.

    Confundirlos cambia la forma y el significado de la instrucción. También vale
    la pena mirar los límites: `edad > 60` excluye el 60, mientras que
    `edad >= 60` lo incluye.
    """)
    return


@app.cell
def _():
    edad_comparacion = 60
    seguimiento_comparacion = edad_comparacion >= 60
    grupos_iguales = "A" == "B"
    return grupos_iguales, seguimiento_comparacion


@app.cell(hide_code=True)
def _(grupos_iguales, mo, seguimiento_comparacion):
    mo.md(f"""
    Python evaluó dos expresiones:

    - `60 >= 60` → `{seguimiento_comparacion}`
    - `"A" == "B"` → `{grupos_iguales}`

    En el primer caso, el valor que está justo en el límite queda incluido. En el
    segundo, los textos son distintos. Las comparaciones producen valores de tipo
    `bool`; una estructura condicional usa ese resultado para decidir qué bloque
    ejecutar.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Expresa con código una frontera inclusiva

    Una medición pertenece al rango esperado cuando vale 10 o más. Construye una
    comparación entre `medicion_comparacion` y el límite. La expresión debe seguir
    funcionando si después cambiamos la medición; por eso no escribas directamente
    `True`.
    """)
    return


@app.cell
def _(feedback):
    medicion_comparacion = 10
    # Compara medicion_comparacion con el límite indicado en la consigna.
    resultado_comparacion = None
    feedback.exercise("comparacion", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejecuta un bloque solo cuando se cumple la condición

    ```python
    if condicion:
        instruccion_del_bloque
    ```

    La instrucción `if` conecta una condición con un bloque de código. Python evalúa
    la condición: si obtiene `True`, ejecuta el bloque indentado; si obtiene
    `False`, lo omite. Después continúa con la siguiente instrucción que vuelva al
    margen anterior.

    La indentación —los espacios al comienzo de la línea— no es decoración: define
    qué instrucciones pertenecen a la decisión. Una instrucción que vuelve al
    margen queda fuera del bloque y se ejecuta después del `if`.
    """)
    return


@app.cell
def _():
    medicion_if = 22
    mensaje_if = "sin alerta"
    if medicion_if >= 20:
        mensaje_if = "revisar medición"
    salida_if = mensaje_if
    return (salida_if,)


@app.cell(hide_code=True)
def _(mo, salida_if):
    mo.callout(
        f"Como 22 es mayor o igual que 20, Python entró al bloque y el mensaje quedó en: {salida_if}.",
        kind="info",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Asigna una respuesta a cada uno de dos caminos

    ```python
    if edad >= 60:
        clasificacion = "seguimiento"
    else:
        clasificacion = "general"
    ```

    Cuando la regla tiene dos resultados excluyentes, `else` reúne todos los casos
    en los que la condición del `if` fue falsa. No lleva una condición propia y
    solo una de las dos ramas se ejecuta.

    Para seguir —o **trazar**— el programa con `edad = 45`, podemos anotar una
    decisión por paso:

    | Paso | Estado |
    |---|---|
    | Evaluar | `45 >= 60` produce `False` |
    | Elegir | Se omite `if` y se entra a `else` |
    | Asignar | `clasificacion = "general"` |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Traduce una regla de dos caminos

    ```text
    ENTRADA: edad_regla
    SI edad_regla es 60 o más: asignar "seguimiento"
    DE LO CONTRARIO: asignar "general"
    SALIDA: clasificacion_regla
    ```

    Sustituye el valor pendiente por una estructura `if` / `else`. Mantén primero
    `edad_regla = 60`: este caso permite comprobar si la frontera está incluida.
    Después prueba también con `59` y `61` y observa qué rama se ejecuta.
    """)
    return


@app.cell
def _(feedback):
    edad_regla = 60
    # Reemplaza la asignación pendiente por la decisión descrita arriba.
    clasificacion_regla = "PENDIENTE"
    feedback.exercise("regla_edad", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_regla_edad = mo.ui.text_area(
        label="¿Qué muestran juntos los casos 59, 60 y 61?",
        placeholder="El caso 60 permite comprobar... mientras 59 y 61...",
        rows=3,
        full_width=True,
    )
    explicacion_regla_edad
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ordena tres o más caminos con `elif`

    Python evalúa las ramas de arriba hacia abajo y se detiene en la primera
    condición verdadera.

    ```python
    if medicion < 10:
        categoria = "baja"
    elif medicion < 20:
        categoria = "esperada"
    else:
        categoria = "alta"
    ```

    Si Python llega al `elif`, ya sabe que la medición no es menor que 10: la rama
    anterior fue falsa. Por eso no es necesario repetir el límite inferior. El
    orden de las ramas también comunica cómo dividimos los rangos.
    """)
    return


@app.cell
def _():
    medicion_ramas = 10
    if medicion_ramas < 10:
        categoria_ramas = "baja"
    elif medicion_ramas < 20:
        categoria_ramas = "esperada"
    else:
        categoria_ramas = "alta"
    return (categoria_ramas,)


@app.cell(hide_code=True)
def _(categoria_ramas, mo):
    mo.callout(
        f"Con 10 se omite la primera rama y se obtiene: {categoria_ramas}.",
        kind="info",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Detecta una rama que nunca alcanza a ejecutarse

    ```python
    if puntaje >= 60:
        nivel = "suficiente"
    elif puntaje >= 90:
        nivel = "destacado"
    else:
        nivel = "por revisar"
    ```

    Sigamos `puntaje = 95`: `95 >= 60` produce `True`, así que Python asigna
    `"suficiente"` y deja de revisar ramas. Nunca alcanza la pregunta `95 >= 90`.
    El programa termina sin error de sintaxis, pero no representa la intención.

    Cuando varias condiciones pueden ser verdaderas para el mismo valor, la más
    específica debe aparecer antes que la más amplia.
    """)
    return


@app.cell
def _(feedback):
    puntaje_orden = 95
    # Reordena las ramas para que 95 se clasifique como "destacado".
    if puntaje_orden >= 60:
        nivel_orden = "suficiente"
    elif puntaje_orden >= 90:
        nivel_orden = "destacado"
    else:
        nivel_orden = "por revisar"
    feedback.exercise("orden_ramas", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_orden_ramas = mo.ui.text_area(
        label="¿Por qué el orden original impedía llegar a la categoría 'destacado'?",
        placeholder="Python evaluaba primero... y por eso...",
        rows=3,
        full_width=True,
    )
    explicacion_orden_ramas
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Combina preguntas sin perder legibilidad

    Algunas decisiones dependen de más de una pregunta booleana. Los operadores
    lógicos permiten combinarlas:

    - `A and B`: ambas condiciones deben ser verdaderas.
    - `A or B`: al menos una debe ser verdadera.
    - `not A`: invierte el booleano de `A`.

    ```python
    requiere_revision = medicion >= 20 and autorizacion
    prioridad = edad >= 60 or medicion >= 20
    registro_abierto = not cerrado
    ```

    Por ejemplo, la primera expresión solo es verdadera cuando la medición alcanza
    el límite **y** existe autorización. Si una condición compuesta resulta difícil
    de explicar, divídela en nombres booleanos más pequeños. La legibilidad también
    ayuda a comprobar qué parte produjo un resultado inesperado.
    """)
    return


@app.cell
def _():
    medicion_compuesta = 22
    autorizacion_compuesta = True
    resultado_compuesto = medicion_compuesta >= 20 and autorizacion_compuesta
    return (resultado_compuesto,)


@app.cell(hide_code=True)
def _(mo, resultado_compuesto):
    mo.md(f"""
    Con una medición de 22 y autorización verdadera, el resultado es
    `{resultado_compuesto}`. Cambia la autorización a `False`, ejecuta de nuevo y
    observa qué parte de la condición deja de cumplirse.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Prueba la decisión donde es más probable que falle

    | Situación | Primera revisión |
    |---|---|
    | `SyntaxError` cerca de `if` | Dos puntos y forma de la comparación |
    | `IndentationError` | Margen de las instrucciones del bloque |
    | Se usó `=` en la pregunta | Diferenciar asignación de `==` |
    | Una categoría nunca aparece | Orden y solapamiento de ramas |
    | El código corre, pero clasifica mal | Comparar la salida con el pseudocódigo |

    No todos los casos aportan la misma información. Para un límite situado en 20,
    prueba al menos `19`, `20` y `21`. Los valores inmediatamente alrededor de la
    frontera muestran si elegiste `<`, `<=`, `>` o `>=` de acuerdo con la regla.
    Estos casos se conocen como **casos límite**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Integra autorización, rangos y orden de prioridad

    ```text
    ENTRADAS: medicion_triage, autorizacion_triage
    SI no existe autorización: asignar "no procesar"
    SI NO, SI la medición es menor de 10: asignar "baja"
    SI NO, SI la medición es menor de 20: asignar "esperada"
    DE LO CONTRARIO: asignar "alta"
    SALIDA: resultado_triage
    ```

    Implementa la regla respetando el orden del pseudocódigo. La autorización debe
    revisarse primero porque una autorización falsa conduce a `"no procesar"` sin
    importar el valor de la medición.

    Conserva inicialmente `10` y `True`; después prueba `9`, `20` y una autorización
    falsa. En cada caso identifica cuál fue la primera condición verdadera.
    """)
    return


@app.cell
def _(feedback):
    medicion_triage = 10
    autorizacion_triage = True
    # Reemplaza la asignación pendiente por las ramas descritas en el pseudocódigo.
    resultado_triage = "PENDIENTE"
    feedback.exercise("triage", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_triage = mo.ui.text_area(
        label="¿Por qué conviene comprobar la autorización antes que los rangos?",
        placeholder="Si la autorización es falsa... por eso la primera pregunta...",
        rows=3,
        full_width=True,
    )
    explicacion_triage
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reconstruye el camino de una decisión

    Sin releer todavía, explica con tus palabras cómo pasarías de una regla escrita
    a un programa comprobable. Incluye estas cuatro ideas en una explicación
    conectada:

    1. ¿Qué aporta el pseudocódigo antes de escribir Python?
    2. ¿Qué diferencia existe entre una condición y el bloque que controla?
    3. ¿Por qué Python se detiene en el primer `if` o `elif` verdadero?
    4. ¿Qué tres valores probarías para una frontera situada en 20?

    Si alguna parte todavía resulta imprecisa, vuelve a esa sección, cambia un valor
    y sigue la nueva traza. El objetivo es justificar el camino del programa, no
    memorizar palabras reservadas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    resumen_control = mo.ui.text_area(
        label="Explica cómo diseñas y compruebas una decisión en Python.",
        placeholder="Primero aclaro... Después convierto... Para comprobar...",
        rows=6,
        full_width=True,
    )
    resumen_control
    return


if __name__ == "__main__":
    app.run()
