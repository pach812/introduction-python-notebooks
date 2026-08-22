import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Diccionarios")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback
    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="04_diccionarios",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Diccionarios: encontrar un valor por su significado

    En una lista, una posición responde preguntas como «¿qué hay de primero?». En
    muchos registros necesitamos otra clase de pregunta: «¿cuál es el grupo?» o
    «¿qué estado tiene esta muestra?». Un diccionario permite identificar cada
    valor con un nombre.

    A lo largo del cuaderno crearás, consultarás, modificarás y recorrerás
    diccionarios. Al final podrás elegir entre un acceso obligatorio y uno
    opcional, y explicar por qué esta estructura representa bien ciertos problemas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Antes de mirar la sintaxis: ¿cómo buscarías un dato?

    Piensa en un registro de participante que contiene identificación, edad, grupo
    y estado. Podríamos memorizar que la edad está en la segunda posición, pero el
    código sería difícil de leer y frágil si cambia el orden.

    ¿Qué ventaja tendría consultar `registro["edad"]` en lugar de `registro[1]`?
    Escribe una idea inicial; esta respuesta no se califica.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    respuesta_inicial_diccionarios = mo.ui.text_area(
        label="¿Qué comunica una clave que una posición numérica no comunica?",
        placeholder="Una clave como 'edad' permite...",
        rows=3,
        full_width=True,    )
    respuesta_inicial_diccionarios
    return (respuesta_inicial_diccionarios,)


@app.cell
def _():
    participante_demo = {
        "id": "A01",
        "edad": 42,
        "grupo": "A",
        "activo": True,
    }
    return (participante_demo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Relacionar cada clave con su valor

    Un **diccionario** es una colección de asociaciones. Cada asociación une una
    clave única con un valor: la clave permite localizar el dato por su significado
    y el valor contiene la información que queremos guardar.

    ```text
    clave       "id"     "edad"    "grupo"    "activo"
                 ↓          ↓          ↓           ↓
    valor      "A01"       42         "A"         True
    ```

    Las claves son únicas dentro de un diccionario. Si asignamos otra vez la misma
    clave, reemplazamos su valor; no creamos una segunda copia de la clave. Los
    valores sí pueden repetirse y tener tipos diferentes.

    El diccionario conserva el orden de inserción, pero no lo elegimos para buscar
    por posición. Lo elegimos para consultar por clave. `{}` crea uno vacío y cada
    asociación se escribe `clave: valor`.
    """)
    return


@app.cell
def _(participante_demo):
    id_obligatorio = participante_demo["id"]
    sede_opcional = participante_demo.get("sede")
    sede_con_alternativa = participante_demo.get("sede", "sin registrar")
    return id_obligatorio, sede_con_alternativa, sede_opcional


@app.cell(hide_code=True)
def _(id_obligatorio, mo, sede_con_alternativa, sede_opcional):
    mo.md(f"""
    ## Decide qué debe pasar cuando falta una clave

    - `participante_demo["id"]` produce `{id_obligatorio}`.
    - `.get("sede")` produce `{sede_opcional}` si la clave falta.
    - `.get("sede", "sin registrar")` produce `{sede_con_alternativa}`.

    Las dos formas responden a decisiones distintas. Los corchetes son apropiados
    cuando la clave es obligatoria: si falta, `KeyError` hace visible que el
    registro no cumple lo esperado. `.get` sirve cuando la ausencia está prevista
    y ya decidimos cómo representarla, por ejemplo con `None` o con el texto
    `"sin registrar"`.

    Usar `.get` para todo no siempre es más seguro. También podría ocultar un error
    de escritura en el nombre de una clave que sí debía existir.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cambiar asociaciones sin perder de vista el original

    Los diccionarios son **mutables**: podemos añadir, reemplazar o retirar
    asociaciones después de crearlos. Antes de elegir una operación, conviene
    preguntar si queremos transformar el registro existente o producir una versión
    nueva que conserve la fuente.

    | Operación | Efecto |
    |---|---|
    | `d["clave"] = valor` | añade o reemplaza una pareja |
    | `d.update({"a": 1})` | añade o reemplaza varias parejas |
    | `d.pop("clave")` | elimina y devuelve el valor |
    | `del d["clave"]` | elimina sin devolver |
    | `d.clear()` | elimina todas las parejas |
    | `d.copy()` | produce una copia superficial |

    En marimo mantendremos las modificaciones relacionadas en una misma celda o
    construiremos una copia. Así queda visible qué versión depende de cuál y se
    evita modificar el mismo objeto desde celdas diferentes.
    """)
    return


@app.cell
def _(participante_demo):
    participante_actualizado = participante_demo.copy()
    participante_actualizado["grupo"] = "B"
    participante_actualizado["sede"] = "Centro"
    estado_retirado = participante_actualizado.pop("activo")
    return estado_retirado, participante_actualizado


@app.cell(hide_code=True)
def _(estado_retirado, mo, participante_actualizado):
    mo.md(f"""
    El ejemplo toma tres decisiones en orden:

    1. `copy()` crea un diccionario separado para conservar el registro original.
    2. Las asignaciones cambian `grupo` y añaden la nueva clave `sede`.
    3. `pop("activo")` retira la asociación y devuelve su valor, que quedó guardado
       como `{estado_retirado}`.

    La copia termina como `{participante_actualizado}` y el diccionario original no
    cambia.

    Un diccionario puede contener listas u otros diccionarios. Esa composición es
    útil, pero una estructura demasiado anidada aumenta la carga de lectura; en
    esta semana usaremos registros planos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Recorre claves, valores o asociaciones según la pregunta

    No siempre necesitamos observar el diccionario de la misma manera. La pregunta
    del problema determina qué vista resulta más clara:

    - `d.keys()` ofrece las claves.
    - `d.values()` ofrece los valores.
    - `d.items()` ofrece parejas `(clave, valor)`.
    - `clave in d` pregunta por las **claves**, no por los valores.

    ```python
    for clave, valor in participante.items():
        print(clave, valor)
    ```

    En el ciclo, `.items()` ofrece una asociación a la vez. Cada asociación es una
    tupla de dos posiciones, por eso el desempaque asigna la primera a `clave` y la
    segunda a `valor`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Construye una versión actualizada de un registro

    Crea `muestra_actualizada` como copia de `muestra_base`. Cambia `estado` a
    `"procesada"`, añade `calidad` con valor `"válida"` y elimina `temporal`.

    Haz los cambios sobre la copia. Al terminar, `muestra_base` debe conservar la
    información con la que comenzó el ejercicio.
    """)
    return


@app.cell
def _(feedback):
    muestra_base = {"id": "M01", "estado": "pendiente", "temporal": True}
    # Crea una copia y realiza allí los tres cambios solicitados.
    muestra_actualizada = None
    feedback.exercise("diccionarios_edicion", locals())
    return (muestra_actualizada,)


@app.cell(hide_code=True)
def _(mo):
    explicacion_copia_diccionario = mo.ui.text_area(
        label="¿Por qué fue importante crear una copia antes de editar el registro?",
        placeholder="La copia permite que... mientras el original...",
        rows=3,
        full_width=True,    )
    explicacion_copia_diccionario
    return (explicacion_copia_diccionario,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Compara el diccionario con otras colecciones

    Un diccionario representa bien un registro con atributos, una configuración,
    una tabla de consulta o un conteo por categoría. En todos esos casos queremos
    llegar a un valor mediante una clave con significado.

    No es la mejor elección para una secuencia consultada por posición, un conjunto
    de valores únicos sin datos asociados o un grupo pequeño de posiciones fijas.
    Allí una lista, un conjunto o una tupla puede comunicar mejor la intención.

    Vale la pena vigilar cuatro situaciones: acceder a una clave inexistente,
    confundir claves con valores al usar `in`, repetir una clave en un literal y
    reemplazarla sin notarlo, o modificar el diccionario mientras se recorren sus
    claves.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Convierte repeticiones en una tabla de frecuencias

    Construye `frecuencias_grupo` a partir de `grupos_fuente`. Cada clave será un
    grupo y cada valor indicará cuántas veces aparece. El algoritmo debe funcionar
    aunque aparezca un grupo nuevo.

    Recorre la lista una vez. Para cada grupo, decide si debes iniciar su conteo o
    aumentar el que ya existe. Prueba mentalmente las tres primeras entradas
    (`"A"`, `"B"`, `"A"`) y observa cómo debería cambiar el diccionario.
    """)
    return


@app.cell
def _(feedback):
    grupos_fuente = ["A", "B", "A", "C", "B", "A"]
    # Recorre la fuente y actualiza el conteo asociado con cada grupo.
    frecuencias_grupo = None
    feedback.exercise("diccionarios_transferencia", locals())
    return (frecuencias_grupo,)


@app.cell(hide_code=True)
def _(mo):
    explicacion_frecuencias = mo.ui.text_area(
        label="¿Qué representa cada clave y qué representa cada valor en tu resultado?",
        placeholder="La clave representa... y su valor indica...",
        rows=3,
        full_width=True,    )
    explicacion_frecuencias
    return (explicacion_frecuencias,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Explica por qué la clave cambia la forma de pensar el problema

    Escribe una explicación conectada: parte de un ejemplo de registro o conteo,
    explica por qué sus claves deben ser únicas, decide cuándo usarías `[]` o
    `.get()` y cuenta qué aporta `.items()` al recorrerlo. Cierra comparando esta
    representación con una lista simple.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    resumen_diccionarios = mo.ui.text_area(
        label="Resume con tus palabras cuándo elegirías un diccionario.",
        placeholder="Elegiría un diccionario cuando... porque...",
        rows=5,
        full_width=True,    )
    resumen_diccionarios
    return (resumen_diccionarios,)


if __name__ == "__main__":
    app.run()
