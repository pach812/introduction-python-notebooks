import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Comprensiones")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="09_comprensiones",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Comprensiones: expresar un recorrido en una sola construcción

    Ya sabemos crear una colección vacía, recorrer datos y añadir un resultado en
    cada vuelta. Cuando ese patrón es breve y regular, Python permite expresarlo
    mediante una **comprensión**.

    La meta no es escribir menos líneas a cualquier costo. Vamos a reconocer el
    recorrido que sigue existiendo dentro de la forma compacta, separar la parte
    que transforma de la que filtra y decidir cuándo un ciclo explícito comunica
    mejor la intención.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Reconocer el mismo proceso en dos escrituras

    ```python
    cuadrados = []
    for numero in [1, 2, 3]:
        cuadrados.append(numero ** 2)

    cuadrados = [numero ** 2 for numero in [1, 2, 3]]
    ```

    Las dos versiones crean `[1, 4, 9]`. En la primera podemos seguir tres acciones:
    preparar una lista vacía, tomar cada número y añadir su cuadrado. La segunda
    conserva el recorrido y la transformación, pero los reúne entre corchetes.

    Esa construcción se llama **comprensión de lista**. Para leerla, ubica sus
    partes antes de intentar memorizar el orden:

    ```text
    expresión que produce la salida | for nombre in colección | condición opcional
             numero ** 2              for numero in numeros       if ...
    ```

    Aunque la expresión de salida aparece primero en la escritura, piensa la
    ejecución así: “para cada número de la colección, produce su cuadrado”. Una
    comprensión crea una colección nueva; no va modificando la colección recorrida.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    comparacion_inicial_comprensiones = mo.ui.text_area(
        label="Compara las dos versiones",
        placeholder="¿Qué acciones del ciclo siguen presentes en la comprensión? Este texto no se califica.",
        rows=3,
        full_width=True,
    )
    comparacion_inicial_comprensiones
    return


@app.cell
def _():
    numeros_demo_comp = [1, 2, 3, 4, 5, 6]
    cuadrados_pares_demo = [
        numero_comp_demo ** 2
        for numero_comp_demo in numeros_demo_comp
        if numero_comp_demo % 2 == 0
    ]
    return cuadrados_pares_demo, numeros_demo_comp


@app.cell(hide_code=True)
def _(cuadrados_pares_demo, mo):
    mo.md(rf"""
    ## 2. Separar la transformación del filtro

    El ejemplo produce `{cuadrados_pares_demo}`. Reconstruyamos una vuelta antes de
    mirar el resultado completo. Cuando el número es `3`, la condición
    `3 % 2 == 0` es falsa y no se añade nada. Cuando es `4`, la condición es
    verdadera y la expresión de salida calcula `4 ** 2`.

    En una comprensión con filtro, el orden mental es:

    1. tomar un elemento;
    2. comprobar la condición;
    3. si la cumple, aplicar la expresión y añadir el resultado a la colección nueva.

    {
        mo.mermaid('''flowchart LR
        A[Tomar elemento] --> B{{¿Cumple la condición?}}
        B -->|no| E[Pasar al siguiente]
        B -->|sí| C[Aplicar la expresión]
        C --> D[Añadir el resultado]
        D --> E''')
    }

    La condición **filtra**: decide qué elementos continúan. La expresión de salida
    **transforma**: decide qué valor se guarda. Sin `if`, todos los elementos llegan
    a la transformación.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Elegir qué colección queremos construir

    ```python
    longitudes = {texto: len(texto) for texto in ["sol", "marimo"]}
    iniciales = {texto[0] for texto in ["Ana", "Andrés", "Beatriz"]}
    ```

    Los delimitadores y la expresión de salida indican qué colección se construye:

    - `[expresion for ...]` crea una lista y conserva el orden y las repeticiones;
    - `{clave: valor for ...}` crea un diccionario y relaciona cada clave con un valor;
    - `{expresion for ...}` crea un conjunto y conserva valores únicos.

    En `longitudes`, cada vuelta produce una pareja como `"sol": 3`. En
    `iniciales`, Ana y Andrés producen la misma letra; el conjunto conserva una
    sola `"A"`.

    Los paréntesis marcan un límite importante: `(x for x in datos)` no crea una
    tupla, sino un **generador**, tema que está fuera de esta unidad. Si necesitas
    una tupla, puedes convertir una comprensión de lista con
    `tuple([x for x in datos])`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Reconocer cuándo la forma compacta deja de ayudar

    Una comprensión funciona bien cuando puede leerse como una transformación
    breve, con un filtro opcional. Observa este contraejemplo:

    ```python
    # Difícil de revisar: demasiadas decisiones juntas
    [transformar(x) if condicion_a(x) else otra(x) for x in datos if condicion_b(x)]
    ```

    Aquí una sola línea contiene dos transformaciones, una decisión entre ellas y
    un filtro adicional. Para entenderla hay que desarmarla mentalmente. Un bucle
    resulta más claro cuando hay varias ramas, actualizaciones diferentes, manejo
    de errores o pasos que necesitan nombres y comentarios.

    Menos líneas no significa automáticamente más claridad. La pregunta útil es:
    “¿puedo explicar esta comprensión como un recorrido, una transformación y, a
    lo sumo, un filtro breve?”.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Construye una comprensión identificando sus tres partes

    Crea `longitudes_pares` con la longitud de cada palabra cuya cantidad de letras
    sea par. No escribas manualmente la lista resultante.

    Antes de completar la línea, señala mentalmente:

    - la colección que vas a recorrer;
    - la condición que permite pasar una palabra;
    - el valor que guardarás cuando la condición se cumpla.

    El Coach revisará el resultado producido por el código.
    """)
    return


@app.cell
def _(feedback):
    palabras_fuente = ["sol", "luna", "mar", "datos"]
    # Construye la lista mediante una comprensión con transformación y filtro.
    longitudes_pares = None
    feedback.exercise("comprensiones_lectura", locals())
    return (longitudes_pares,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Transfiere el patrón a una comprensión de diccionario

    Crea `mediciones_por_id` como diccionario que relacione cada id con su medición,
    pero solo para valores mayores o iguales a 10. Usa una comprensión de
    diccionario y conserva los valores numéricos.

    Esta vez cada elemento que supera el filtro debe producir una pareja. Decide
    cuál expresión será la clave, cuál será el valor y dónde ubicarás la condición.
    El registro con medición igual a 10 permite comprobar si incluiste el límite.
    """)
    return


@app.cell
def _(feedback):
    registros_comp = [
        {"id": "C01", "medicion": 8},
        {"id": "C02", "medicion": 10},
        {"id": "C03", "medicion": 14},
    ]
    # Construye el diccionario mediante una comprensión y conserva el límite.
    mediciones_por_id = None
    feedback.exercise("comprensiones_transferencia", locals())
    return (mediciones_por_id,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cierre: decide si conviene una comprensión

    Explica con tus palabras cómo leerías una comprensión con filtro, aunque la
    expresión de salida aparezca al comienzo. Distingue qué parte recorre, cuál
    filtra y cuál transforma.

    Después propone un caso en el que preferirías un bucle explícito. Justifica la
    elección por la claridad del proceso, no solamente por la cantidad de líneas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    resumen_comprensiones = mo.ui.text_area(
        label="¿Comprensión o bucle explícito?",
        placeholder="Explica cómo lees la comprensión y cuándo escogerías cada forma. Este texto no se califica.",
        rows=5,
        full_width=True,
    )
    resumen_comprensiones
    return


if __name__ == "__main__":
    app.run()
