import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Tuplas")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback
    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="03_tuplas",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Tuplas: cuando cada posición debe conservar su lugar

    Algunas colecciones representan algo que no debería cambiar de forma: una
    coordenada tiene dos componentes, un intervalo tiene dos extremos y un periodo
    puede acordarse como año, mes inicial y mes final. En estos casos importa tanto
    el orden como la estabilidad de las posiciones.

    En este cuaderno aprenderás a crear, consultar y desempaquetar tuplas. Al final
    podrás explicar cuándo esa estructura comunica mejor que una lista y cuándo
    conviene usar otra representación.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Antes de elegir la estructura: ¿qué tendría sentido cambiar?

    Imagina que una coordenada se guarda como `(6.25, -75.56)`. Si después se
    añade un tercer valor sin explicar qué significa, la representación deja de
    ser clara. ¿Qué diferencia encuentras entre ese caso y una lista de tareas, que
    sí necesita crecer o reducirse?

    Escribe una idea inicial. No se califica; la retomaremos al final.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    respuesta_inicial_tuplas = mo.ui.text_area(
        label="¿Qué clase de información guardarías en una colección que no debería cambiar de forma?",
        placeholder="Pienso que una tupla serviría para... porque...",
        rows=3,
        full_width=True,    )
    respuesta_inicial_tuplas
    return (respuesta_inicial_tuplas,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Construir una secuencia estable

    Una **tupla** es una secuencia ordenada: cada elemento ocupa una posición y un
    mismo valor puede aparecer varias veces. A diferencia de una lista, una vez
    creada no permite reemplazar, añadir ni retirar posiciones. Esta propiedad se
    llama **inmutabilidad de la secuencia**.

    ```python
    coordenada = (6.25, -75.56)
    intervalo = (10, 20)
    vacia = ()
    un_elemento = (42,)
    ```

    La coma es la que define la tupla. Por eso `(42,)` contiene un elemento,
    mientras que `(42)` sigue siendo el número `42` entre paréntesis.

    La restricción no es una carencia que debamos corregir: puede comunicar que la
    forma del dato es parte del acuerdo. Si necesitamos que la colección crezca o
    que sus posiciones cambien, una lista expresa mejor esa intención.
    """)
    return


@app.cell
def _():
    rango_demo = (10, 20, 30, 40)
    extremo_inicial = rango_demo[0]
    extremo_final = rango_demo[-1]
    centro_rango = rango_demo[1:3]
    return centro_rango, extremo_final, extremo_inicial, rango_demo


@app.cell(hide_code=True)
def _(centro_rango, extremo_final, extremo_inicial, mo):
    mo.md(f"""
    ## Ubicar elementos sin alterar la secuencia

    En `rango_demo = (10, 20, 30, 40)`, la posición `0` contiene
    `{extremo_inicial}` y la posición `-1` contiene `{extremo_final}`. El corte
    `[1:3]` toma las posiciones 1 y 2 y produce `{centro_rango}`; el resultado
    conserva el tipo tupla.

    Los índices y los cortes sirven para consultar, no para modificar. Intentar
    `rango_demo[0] = 5` produce `TypeError`: Python protege la estabilidad que
    elegimos al usar una tupla.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Consultar y combinar sin modificar el original

    Una vez entendida la estabilidad de las posiciones, podemos revisar las
    operaciones que sí tienen sentido. Las primeras cuatro consultan información;
    las dos últimas construyen una tupla nueva.

    | Operación | Resultado |
    |---|---|
    | `len(tupla)` | cantidad de elementos |
    | `valor in tupla` | comprobación de pertenencia |
    | `tupla.count(valor)` | número de apariciones |
    | `tupla.index(valor)` | primera posición del valor |
    | `tupla_a + tupla_b` | nueva tupla concatenada |
    | `tupla * 3` | nueva tupla repetida |

    Por ejemplo, `(10, 20) + (30,)` produce `(10, 20, 30)`, pero ninguna de las
    tuplas originales cambia. `index` también tiene un límite importante: produce
    `ValueError` si el valor buscado no existe.
    """)
    return


@app.cell
def _():
    registro_minimo = ("A01", 42, "A")
    codigo_tupla, edad_tupla, grupo_tupla = registro_minimo
    return codigo_tupla, edad_tupla, grupo_tupla, registro_minimo


@app.cell(hide_code=True)
def _(codigo_tupla, edad_tupla, grupo_tupla, mo):
    mo.md(f"""
    ## Darle un nombre al significado de cada posición

    Cuando las posiciones tienen un significado acordado, podemos asignarlas a
    varios nombres en una sola instrucción. Esta operación se llama
    **desempaque**:

    `codigo, edad, grupo = ("A01", 42, "A")` vincula la primera posición con
    `codigo`, la segunda con `edad` y la tercera con `grupo`. En este ejemplo se
    obtienen `{codigo_tupla}`, `{edad_tupla}` y `{grupo_tupla}`.

    Python necesita la misma cantidad de nombres y elementos; de lo contrario
    aparece `ValueError`. Además, si hay muchos atributos o no resulta evidente
    qué significa cada posición, un diccionario con claves explícitas suele leerse
    mejor.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Reconoce el significado de tres posiciones

    `periodo` guarda año, mes inicial y mes final. Desempácalo en
    `anio_periodo`, `mes_inicio` y `mes_fin`, y calcula `duracion_meses`
    incluyendo ambos extremos. Antes de escribir la fórmula, prueba con los meses
    3 a 6: cuenta cuántos meses forman parte del periodo y usa ese resultado para
    comprobar tu cálculo.
    """)
    return


@app.cell
def _(feedback):
    periodo = (2026, 3, 6)
    # Desempaca periodo y calcula la duración, incluidos los dos extremos.
    anio_periodo = None
    mes_inicio = None
    mes_fin = None
    duracion_meses = None
    feedback.exercise("tuplas_desempaque", locals())
    return anio_periodo, duracion_meses, mes_fin, mes_inicio


@app.cell(hide_code=True)
def _(mo):
    explicacion_desempaque = mo.ui.text_area(
        label="¿Por qué la duración necesita tener en cuenta los dos extremos?",
        placeholder="Si el periodo comienza en... y termina en..., entonces...",
        rows=3,
        full_width=True,    )
    explicacion_desempaque
    return (explicacion_desempaque,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Decide cuándo la estabilidad ayuda y cuándo estorba

    Una tupla funciona bien para coordenadas, dimensiones, intervalos, parejas
    devueltas por algunos métodos y resultados pequeños cuyas posiciones ya tienen
    un significado acordado.

    No es una buena elección cuando la colección debe crecer, sus elementos deben
    editarse o las posiciones son difíciles de recordar. La pregunta útil no es
    «¿puedo guardar estos valores en una tupla?», sino «¿quiero comunicar que estas
    posiciones deben permanecer estables?».

    Hay un matiz: una tupla no vuelve inmutables los objetos que contiene. Si una
    de sus posiciones guarda una lista, esa lista interna todavía puede cambiar.
    La inmutabilidad protege las posiciones de la tupla; no transforma todo lo que
    hay dentro.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Diseña un resumen con una forma acordada

    A partir de `valores_resumen`, crea `resumen_tupla` con exactamente tres
    posiciones y en este orden: mínimo, máximo y cantidad. Calcula cada valor a
    partir de la lista; no escribas los resultados a mano.

    Al revisar tu resultado, una persona debería poder desempaquetarlo como
    `minimo, maximo, cantidad` sin tener que adivinar el orden.
    """)
    return


@app.cell
def _(feedback):
    valores_resumen = [8, 12, 5, 19, 12]
    # Calcula los tres valores y reúnelos en una tupla, en el orden acordado.
    resumen_tupla = None
    feedback.exercise("tuplas_transferencia", locals())
    return (resumen_tupla,)


@app.cell(hide_code=True)
def _(mo):
    explicacion_resumen_tupla = mo.ui.text_area(
        label="¿Qué acuerdo necesita conocer alguien para interpretar esta tupla?",
        placeholder="La primera posición representa..., la segunda...",
        rows=3,
        full_width=True,    )
    explicacion_resumen_tupla
    return (explicacion_resumen_tupla,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explica tu elección de estructura

    Imagina que debes explicarle a otra persona por qué elegiste una tupla. Incluye
    en tu respuesta qué comparte con una lista, qué significa que sea inmutable,
    por qué `(5,)` necesita la coma y en qué caso preferirías claves explícitas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    resumen_tuplas = mo.ui.text_area(
        label="Escribe una explicación breve con un ejemplo propio.",
        placeholder="Elegiría una tupla cuando... En cambio, usaría...",
        rows=5,
        full_width=True,    )
    resumen_tuplas
    return (resumen_tuplas,)


if __name__ == "__main__":
    app.run()
