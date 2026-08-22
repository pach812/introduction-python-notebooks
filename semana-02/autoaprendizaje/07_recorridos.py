import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Recorridos")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="07_recorridos",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Recorridos y Ciclos: procesar un elemento a la vez

    Una colección puede contener muchos elementos, pero con frecuencia aplicamos
    la misma pregunta o transformación a cada uno: revisar una medición, contar un
    caso, sumar un valor o conservar solo algunos registros.

    En este cuaderno seguirás un `for` vuelta por vuelta, construirás resultados
    parciales con acumuladores y distinguirás ese recorrido de un `while`. La meta
    no es repetir código de memoria, sino poder explicar qué cambia en cada vuelta
    y por qué el ciclo termina.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## 1. Sigue un `for` vuelta por vuelta

    ```python
    for medicion in [8, 10, 21]:
        print(medicion)
    ```

    | Vuelta | `medicion` | Acción |
    |---:|---:|---|
    | 1 | 8 | imprime 8 |
    | 2 | 10 | imprime 10 |
    | 3 | 21 | imprime 21 |
    | fin | — | continúa después del bloque |

    Cada ejecución del bloque se llama una **iteración** o vuelta. En cada una,
    `medicion` recibe un solo elemento de la lista. Ese nombre no representa la
    colección completa: primero vale `8`, después `10` y finalmente `21`.

    La indentación marca el bloque que se repite. Cuando ya no quedan elementos,
    Python sale del ciclo y continúa con la siguiente línea no indentada.

    {
        mo.mermaid('''flowchart LR
        A[Tomar siguiente elemento] --> B[Asignarlo al nombre del for]
        B --> C[Ejecutar bloque indentado]
        C --> D{¿Quedan elementos?}
        D -->|Sí| A
        D -->|No| E[Continuar después del ciclo]''')
    }
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_inicial_recorridos = mo.ui.text_area(
        label="Sigue una vuelta con tus palabras",
        placeholder="Escoge 8, 10 o 21. ¿Qué valor recibe medicion y qué línea se ejecuta durante esa vuelta?",
        rows=3,
        full_width=True,
    )
    explicacion_inicial_recorridos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Conserva memoria entre una vuelta y la siguiente

    A veces no basta con mirar cada elemento: necesitamos recordar lo construido
    hasta ese momento. Un **acumulador** es una variable que conserva ese resultado
    parcial entre vueltas.

    Su valor inicial debe representar “todavía no hemos procesado nada”. Después,
    cada iteración lo actualiza según el producto que queremos construir:

    | Objetivo | Inicio | Actualización |
    |---|---|---|
    | contar | `0` | sumar `1` |
    | sumar | `0` | sumar el valor |
    | filtrar | `[]` | `append` cuando cumple |
    | categorías únicas | `set()` | `add` |
    | frecuencias | `{}` | actualizar una clave |

    Por ejemplo, una suma comienza en `0` porque todavía no se ha añadido ningún
    valor; un filtro comienza en `[]` porque todavía no se ha conservado ningún
    elemento. El acumulador se crea antes del ciclo. Si se reinicia dentro de cada
    vuelta, el proceso borra su propia memoria y solo conserva el último paso.
    """)
    return


@app.cell
def _():
    valores_traza = [8, 16, 5, 20]
    suma_altos_demo = 0
    traza_altos_demo = []
    for valor_traza_demo in valores_traza:
        if valor_traza_demo >= 15:
            suma_altos_demo = suma_altos_demo + valor_traza_demo
        traza_altos_demo.append((valor_traza_demo, suma_altos_demo))
    return suma_altos_demo, traza_altos_demo


@app.cell(hide_code=True)
def _(mo, suma_altos_demo, traza_altos_demo):
    mo.md(f"""
    ## 3. Usa una traza para localizar el primer cambio inesperado

    La lista `{traza_altos_demo}` registra parejas con la forma
    `(elemento, suma_parcial)`. Al pasar por `8`, la condición no se cumple y la
    suma continúa en cero. `16` sí cambia el acumulador; `5` lo deja igual y `20`
    vuelve a cambiarlo. El resultado final es `{suma_altos_demo}`.

    Ese registro paso a paso se llama **traza**. Si el resultado final no coincide
    con lo esperado, busca la primera pareja incorrecta. Así puedes distinguir si
    el problema está en el valor inicial, en la condición o en la actualización,
    sin revisar todo el ciclo al mismo tiempo.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Reconstruye cómo crece un conteo

    Recorre `numeros_traza` y cuenta cuántos números pares has encontrado. Después
    de cada vuelta, añade a `traza_conteo` una tupla con la forma
    `(numero, conteo_parcial)`.

    El registro debe incluir también las vueltas en las que el número es impar y
    el conteo no cambia. Para organizar el código, identifica primero:

    1. qué valor inicial representa que todavía no has encontrado pares;
    2. qué colección vacía recibirá la traza;
    3. qué condición cambia el conteo;
    4. en qué momento de cada vuelta debes registrar el estado parcial.
    """)
    return


@app.cell
def _(feedback):
    numeros_traza = [2, 5, 8, 11]
    # Construye el conteo y registra su estado después de cada vuelta.
    conteo_pares = None
    traza_conteo = None
    feedback.exercise("recorridos_traza", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_traza_recorridos = mo.ui.text_area(
        label="Explica dónde registraste la traza",
        placeholder="¿Por qué la pareja debe añadirse después de decidir si el número actual cambia el conteo?",
        rows=3,
        full_width=True,
    )
    explicacion_traza_recorridos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Usa `range` solo cuando la posición forme parte del problema

    `range(3)` produce `0`, `1` y `2`: el límite final no se incluye. Es útil cuando
    interesa una cantidad de vueltas o necesitamos trabajar explícitamente con las
    posiciones. Si solo queremos leer los elementos, suele ser más claro evitar el
    índice:

    ```python
    for registro in registros:       # preferido si solo necesito el elemento
        ...

    for posicion in range(len(registros)):  # si la posición es parte del problema
        ...
    ```

    La segunda forma no es incorrecta, pero añade una operación y otro nombre. La
    posición se justifica cuando necesitamos modificar un lugar, comparar elementos
    vecinos o conservar el número de la vuelta; no por costumbre.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## 5. Diseña un `while` que avance hacia su final

    Un `for` toma elementos de una colección disponible. Un `while` repite un bloque
    mientras una condición continúe siendo verdadera; resulta útil cuando el número
    de vueltas no se conoce de antemano.

    ```python
    saldo = 5
    while saldo > 0:
        saldo = saldo - 1
    ```

    En el ejemplo, `saldo` empieza en `5`, la condición pregunta si todavía es mayor
    que cero y la actualización resta uno. Estas tres piezas —estado inicial,
    condición y actualización— permiten explicar tanto la repetición como su final.
    Si la actualización no acerca la condición a `False`, el ciclo puede continuar
    indefinidamente.

    {
        mo.mermaid('''flowchart LR
        I[Estado inicial] --> C{¿Condición verdadera?}
        C -->|Sí| B[Ejecutar bloque]
        B --> U[Actualizar estado]
        U --> C
        C -->|No| F[Finalizar]''')
    }

    `break` permite terminar un ciclo desde el bloque y `continue` pasa directamente
    a la siguiente vuelta. Son herramientas útiles, aunque primero conviene buscar
    una condición y una actualización que hagan visible el recorrido completo.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## Filtra registros y resume sus mediciones en un solo recorrido

    Recorre `registros_recorrido` una sola vez. Cuando la medición sea mayor o igual
    a `10`, conserva el identificador en `ids_validos` y suma esa medición en
    `total_valido`.

    Necesitas dos acumuladores porque estás construyendo dos resultados distintos:
    una lista que conserva el orden de los identificadores y un total numérico. Los
    dos deben actualizarse dentro de la misma condición. No modifiques
    `registros_recorrido`.

    Antes de escribir el ciclo, identifica qué valor inicial corresponde a cada
    acumulador y qué ocurre exactamente con el registro cuyo valor es `10`.
    """)
    return


@app.cell
def _(feedback):
    registros_recorrido = [
        {"id": "R01", "medicion": 8},
        {"id": "R02", "medicion": 10},
        {"id": "R03", "medicion": 15},
    ]
    # Filtra los identificadores y acumula las mediciones en el mismo recorrido.
    ids_validos = None
    total_valido = None
    feedback.exercise("recorridos_transferencia", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    explicacion_transferencia_recorridos = mo.ui.text_area(
        label="Explica cómo coordinaste los dos acumuladores",
        placeholder="¿Por qué ambos cambian bajo la misma condición y qué información conserva cada uno?",
        rows=3,
        full_width=True,
    )
    explicacion_transferencia_recorridos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cierre: explica cómo sabes que un recorrido está bien construido

    Escribe una explicación que conecte estas ideas:

    - qué valor representa el nombre definido por un `for` durante una vuelta;
    - por qué un acumulador se crea antes del ciclo y se actualiza dentro;
    - cómo una traza permite localizar el primer estado incorrecto;
    - qué relación deben tener el estado, la condición y la actualización de un
      `while` para que el ciclo termine.

    Incluye también un ejemplo en el que usarías `range` porque la posición aporta
    información y otro en el que recorrerías directamente los elementos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    resumen_recorridos = mo.ui.text_area(
        label="Mi explicación de un recorrido",
        placeholder="Explica cómo cambia el estado vuelta por vuelta y cómo compruebas que el ciclo puede terminar.",
        rows=6,
        full_width=True,
    )
    resumen_recorridos
    return


if __name__ == "__main__":
    app.run()
