import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Funciones")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="08_funciones",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Funciones: darle un nombre a un proceso

    Hay procesos que necesitamos repetir con datos diferentes: convertir una
    temperatura, clasificar una medición o resumir un grupo de registros. Copiar
    las mismas líneas cada vez funciona por un rato, pero hace más difícil saber
    qué cambia y qué debería permanecer igual.

    Una función permite reunir ese proceso bajo un nombre y declarar qué
    información necesita para trabajar. En este cuaderno seguiremos una llamada
    paso a paso, distinguiremos `return` de `print` y construiremos una función
    cuyas entradas y salida puedan entenderse desde fuera.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Antes de escribir `def`: ¿qué debería permanecer estable?

    Imagina que debes convertir varias temperaturas de Celsius a Fahrenheit.
    La fórmula no cambia; lo que cambia en cada conversión es la temperatura de
    entrada.

    Describe el proceso como si se lo entregaras a otra persona: ¿qué dato recibe,
    qué operación realiza y qué resultado debe entregar? Todavía no hace falta
    escribir código.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    idea_inicial_funciones = mo.ui.text_area(
        label="Describe el proceso de conversión",
        placeholder="Entrada..., proceso..., salida... Este texto no se califica.",
        rows=3,
        full_width=True,
    )
    idea_inicial_funciones
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Acordar el proceso antes de implementarlo

    ```text
    entrada: temperatura en grados Celsius
    proceso: multiplicar por 9/5 y sumar 32
    salida: temperatura equivalente en Fahrenheit
    ```

    Esta descripción breve es un **contrato**: establece qué recibe el proceso y
    qué promete devolver, sin decidir todavía cómo se escribirán las instrucciones.
    El contrato ayuda a separar dos preguntas: “¿qué debe hacer?” y “¿cómo lo hace?”.

    También marca un límite. Si una función recibe grados Celsius, no podemos
    entregarle un texto como `"veinte"` y asumir que sabrá interpretarlo; esa
    posibilidad requeriría otro acuerdo explícito.
    """)
    return


@app.cell
def _():
    def convertir_a_fahrenheit(celsius):
        fahrenheit = celsius * 9 / 5 + 32
        return fahrenheit

    temperatura_convertida = convertir_a_fahrenheit(20)
    return convertir_a_fahrenheit, temperatura_convertida


@app.cell(hide_code=True)
def _(mo, temperatura_convertida):
    mo.md(f"""
    ## 2. Leer una definición y reconocer una llamada

    En `def convertir_a_fahrenheit(celsius):`, `def` anuncia que vamos a definir
    una función y `convertir_a_fahrenheit` le da un nombre al proceso. El bloque
    indentado contiene las instrucciones que se ejecutarán cada vez que la llamemos.

    `celsius` es un **parámetro**: un nombre local que representa la entrada sin
    fijar todavía un valor concreto. En cambio, el `20` de
    `convertir_a_fahrenheit(20)` es un **argumento**: el valor que entregamos en
    esta llamada particular.

    Definir la función no ejecuta su cuerpo. La ejecución comienza con la llamada,
    y `return` entrega el resultado `{temperatura_convertida}` a quien la hizo.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## 3. Reconstruir lo que ocurre durante una llamada

    Para `resultado = convertir_a_fahrenheit(20)`:

    | Paso | Estado |
    |---:|---|
    | 1 | Python localiza la función |
    | 2 | vincula `20` con el parámetro `celsius` |
    | 3 | ejecuta el cuerpo en un espacio local |
    | 4 | calcula `fahrenheit = 68.0` |
    | 5 | `return` entrega `68.0` y termina la llamada |
    | 6 | `resultado` recibe el valor |

    Una llamada posterior vuelve a comenzar con sus propios parámetros y nombres
    locales. No continúa donde terminó la anterior.

    {
        mo.mermaid('''flowchart LR
        A[argumento: 20] --> B[parámetro local: celsius]
        B --> C[ejecutar el cuerpo]
        C --> D[return 68.0]
        D --> E[resultado recibe 68.0]''')
    }

    Sigue las flechas en sentido contrario y comprueba algo importante: el nombre
    `resultado` no existe dentro de la función. Pertenece al lugar desde donde se
    hizo la llamada.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Decidir si queremos mostrar o devolver

    ```python
    def mostrar_doble(numero):
        print(numero * 2)

    def calcular_doble(numero):
        return numero * 2
    ```

    Las dos funciones permiten ver un número en pantalla, pero no producen el mismo
    resultado. `mostrar_doble(4)` imprime `8` y después devuelve `None`, porque no
    tiene `return`. `calcular_doble(4)` devuelve `8`: podemos guardarlo, compararlo
    o usarlo como entrada de otro cálculo.

    `print` comunica algo a una persona durante la ejecución. `return` comunica un
    valor al resto del programa y termina la llamada. Una función puede usar ambos,
    pero uno no sustituye al otro.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Haz que el resultado pueda utilizarse después

    `clasificar_medicion` muestra una etiqueta, pero la variable
    `etiqueta_medicion` recibe `None`. Modifica la función para que devuelva
    `"alta"` desde 10 inclusive y `"baja"` en los demás casos.

    Conserva la decisión condicional y cambia la manera en que cada rama entrega
    su resultado. El Coach revisará el valor que recibe la llamada, no lo que se
    imprime en pantalla.
    """)
    return


@app.cell
def _(feedback):
    def clasificar_medicion(valor):
        if valor >= 10:
            print("alta")
        else:
            print("baja")

    etiqueta_medicion = clasificar_medicion(10)
    feedback.exercise("funciones_retorno", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Hacer visibles las dependencias

    Los nombres creados durante una llamada son **locales**: pertenecen a esa
    ejecución de la función. Sin embargo, Python también permite leer nombres
    definidos afuera. Compara estas dos versiones:

    ```python
    limite_externo = 10
    def cumple(valor):
        return valor >= limite_externo  # dependencia escondida

    def cumple_explicita(valor, limite):
        return valor >= limite
    ```

    En la primera, el resultado depende de `limite_externo`, aunque la llamada
    `cumple(valor)` no lo muestra. A eso nos referimos aquí con **estado escondido**:
    una entrada relevante existe, pero no aparece entre los parámetros.

    La segunda versión hace visible el límite. Por eso resulta más fácil de leer,
    probar y reutilizar con otro valor. No todo nombre externo es un error, pero si
    cambia el resultado conviene preguntarse si debería ser un parámetro.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Ofrecer un caso habitual y documentar el acuerdo

    ```python
    def seleccionar(registros, limite=10):
        '''Devuelve ids cuya medición alcanza el límite.'''
        ...
    ```

    `limite=10` es un **valor predeterminado**: si la llamada no indica otro límite,
    Python usa 10. `seleccionar(registros, limite=15)` reemplaza ese valor solo para
    esa llamada. Los parámetros obligatorios se escriben antes que los que tienen
    un valor predeterminado.

    La cadena ubicada al comienzo del cuerpo es una **docstring**. Su tarea es
    comunicar el contrato público —qué recibe la función, qué devuelve y qué
    condición importa—, no narrar línea por línea la implementación.

    En esta etapa usamos números o textos como valores predeterminados. Una lista
    mutable como valor predeterminado puede conservar cambios entre llamadas y
    requiere un tratamiento que veremos más adelante.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. Seguir una transformación completa de una colección

    Una función puede encapsular el patrón acumulador sin modificar la entrada:

    ```python
    def ids_desde_limite(registros, limite=10):
        ids = []
        for registro in registros:
            if registro["medicion"] >= limite:
                ids.append(registro["id"])
        return ids
    ```

    Lee el cuerpo como una secuencia de decisiones:

    1. crea una lista local vacía para esta llamada;
    2. recorre los registros en su orden original;
    3. añade el id cuando la medición alcanza el límite;
    4. devuelve la lista acumulada.

    Cada llamada crea su propia lista `ids`; por eso una ejecución no arrastra los
    resultados de la anterior. El límite aparece como entrada y la salida conserva
    el orden de los registros que cumplen la condición.

    Si `registros` está vacío, el ciclo no se ejecuta y la función devuelve `[]`.
    Ese caso no necesita una rama especial: surge del estado inicial del acumulador.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Construye una función con un contrato visible

    Desarrolla `resumir_grupo(registros, grupo_objetivo="A")` para que devuelva un
    diccionario con `ids` y `cantidad`, usar solo sus parámetros, conservar el
    orden y funcionar con una lista vacía.

    Antes de editar, identifica las tres partes del proceso: qué lista necesitas
    acumular, qué condición decide si un registro pertenece al grupo y qué dos
    datos formarán el diccionario de salida. El valor predeterminado resuelve el
    caso habitual; la función también debe aceptar otro grupo cuando se indique.
    """)
    return


@app.cell
def _(feedback):
    registros_funcion = [
        {"id": "F01", "grupo": "A"},
        {"id": "F02", "grupo": "B"},
        {"id": "F03", "grupo": "A"},
    ]

    def resumir_grupo(registros, grupo_objetivo="A"):
        # Construye la lista local y devuelve el resumen acordado.
        return None

    resumen_grupo_a = resumir_grupo(registros_funcion)
    resumen_grupo_vacio = resumir_grupo([])
    feedback.exercise("funciones_transferencia", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cierre: explica una llamada de principio a fin

    Elige una de las funciones del cuaderno y explica qué sucede desde que recibe
    los argumentos hasta que devuelve el resultado. Integra en tu explicación las
    ideas de parámetro, nombre local y `return`.

    Añade una comparación breve entre `print` y `return`, y señala una dependencia
    que convendría convertir en parámetro. La meta no es enumerar definiciones,
    sino mostrar cómo se conectan durante una llamada.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    resumen_funciones = mo.ui.text_area(
        label="Mi explicación de una llamada",
        placeholder="Describe el recorrido de los datos y las decisiones de diseño. Este texto no se califica.",
        rows=6,
        full_width=True,
    )
    resumen_funciones
    return


if __name__ == "__main__":
    app.run()
