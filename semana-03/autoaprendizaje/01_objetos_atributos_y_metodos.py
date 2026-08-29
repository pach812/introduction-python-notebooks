# ruff: noqa: B018

import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="medium",
    app_title="Semana 3 · Objetos, atributos y métodos",
)


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-03-objects-scientific-tools",
        notebook="01_objetos_atributos_y_metodos",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Objetos: valores que saben hacer cosas

    Hasta ahora has trabajado con números, textos, listas y diccionarios. En
    Python, cada uno de esos valores es un **objeto**: tiene un tipo, conserva
    cierta información y ofrece operaciones que corresponden a ese tipo.

    En este cuaderno vas a aprender a:

    - diferenciar el objeto del nombre que usamos para encontrarlo;
    - reconocer el tipo de un objeto;
    - distinguir un atributo de un método;
    - interpretar la notación con punto;
    - observar si una operación modifica un objeto o devuelve otro valor;
    - reconocer por qué esta forma de organizar el código resulta útil;
    - inspeccionar objetos que no conocías sin tener que memorizar todo.

    No vamos a crear clases. La meta de esta semana es aprender a usar con
    criterio los objetos que ya ofrecen Python, NumPy y Pandas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Recupera una idea conocida

    Mira estas dos expresiones sin ejecutarlas todavía:

    ```python
    "  control  ".strip
    "  control  ".strip()
    ```

    ¿Crees que producen lo mismo? Escribe qué diferencia esperas encontrar y
    qué papel podrían cumplir los paréntesis.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    respuesta_inicial_objetos = mo.ui.text_area(
        label="¿Qué crees que cambia al agregar los paréntesis?",
        placeholder="Escribe una explicación breve antes de ejecutar los ejemplos.",
        rows=3,
        full_width=True,
    )
    respuesta_inicial_objetos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
            ## Construye el modelo: tipo, estado y operaciones

            Un **objeto** es un valor que existe durante la ejecución de Python.
            Su tipo determina cómo puede representarse y qué operaciones tiene
            disponibles. El objeto también conserva un estado observable: para
            una lista, por ejemplo, ese estado incluye sus elementos y su orden.

            El nombre de una variable no es el objeto. Es una referencia que nos
            permite encontrarlo y usarlo.
            """),
            mo.mermaid(r"""flowchart LR
                N["nombre: mediciones"] --> O["objeto lista\n0x7f9a1c2b3f40"]
                O --> T["tipo: list"]
                O --> E["estado: 8, 12, 9"]
                O --> P["operaciones: append, copy, count..."]"""),
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Separa el objeto del nombre que lo referencia

    Para trabajar con objetos conviene distinguir cuatro ideas:

    | Idea | Pregunta que responde | Ejemplo |
    |---|---|---|
    | **Nombre** | ¿Cómo encuentro el objeto en el programa? | `mediciones` |
    | **Tipo** | ¿Qué clase de valor es y qué operaciones admite? | `list` |
    | **Estado** | ¿Qué información contiene ahora? | `[8, 12, 9]` |
    | **Identidad** | ¿Es el mismo objeto? | dos nombres pueden apuntar a una lista |

    El nombre no guarda una copia automática del objeto. Python lo relaciona
    con un objeto que existe durante la ejecución. Por eso, dos nombres pueden
    permitirnos llegar a la misma lista.
    """)
    return


@app.cell
def _():
    lista_original_identidad = [8, 12]
    lista_alias_identidad = lista_original_identidad

    son_el_mismo_objeto = lista_alias_identidad is lista_original_identidad
    lista_alias_identidad.append(15)

    {
        "¿son el mismo objeto?": son_el_mismo_objeto,
        "lista vista desde el primer nombre": lista_original_identidad,
        "lista vista desde el segundo nombre": lista_alias_identidad,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La modificación se observa desde ambos nombres porque no había dos listas:
    los dos conducían al mismo objeto. El operador `is` comprueba identidad;
    pregunta si se trata del mismo objeto. En cambio, `==` compara si dos
    valores son equivalentes.

    En el trabajo cotidiano suele interesar más `==`. La identidad resulta útil
    aquí para comprender por qué una modificación puede aparecer en otro lugar
    del programa y por qué una copia debe crearse de forma explícita.
    """)
    return


@app.cell
def _():
    mediciones_modelo = [8, 12, 9]
    texto_modelo = "control"
    numero_modelo = 12

    (
        type(mediciones_modelo),
        type(texto_modelo),
        type(numero_modelo),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `type(...)` devuelve el tipo del objeto. El resultado no es una etiqueta
    decorativa: permite anticipar qué operaciones tendrán sentido.

    - una lista puede recibir otro elemento;
    - un texto puede producir una versión en mayúsculas;
    - un número puede participar en operaciones aritméticas.

    Intentar una operación que el tipo no ofrece puede producir `TypeError`.
    Ese error informa que nuestro modelo del objeto no coincide con lo que
    Python recibió.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lee la notación con punto

    La expresión `objeto.nombre` busca un **atributo** en el objeto. Un atributo
    es un nombre que el objeto expone como parte de su interfaz: puede permitir
    consultar información o acceder a una operación.

    Cuando el atributo contiene una operación que puede llamarse, hablamos de un
    **método**. Los paréntesis realizan la llamada:

    ```python
    objeto.metodo      # recupera el método
    objeto.metodo()    # llama el método
    ```

    El punto no significa “continuar la frase”. Significa buscar ese nombre en
    el objeto que aparece a la izquierda.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
            ## Reconoce la interfaz de un objeto

            La **interfaz** es el conjunto de nombres que podemos usar para
            interactuar con un objeto. No necesitamos conocer cómo está
            construido por dentro para aprovecharla.

            | Forma | Qué hacemos | Ejemplo que verás esta semana |
            |---|---|---|
            | `objeto.atributo` | consultamos información | `arreglo.shape` |
            | `objeto.metodo()` | solicitamos una operación | `arreglo.mean()` |
            | `objeto.metodo(valor)` | aportamos un argumento | `lista.append(15)` |

            Un método también es un atributo, pero tiene una diferencia clave:
            es **invocable**. Por eso necesita paréntesis para ejecutarse.
            """),
            mo.mermaid(r"""flowchart LR
                O["objeto"] --> I["interfaz"]
                I --> A["atributos<br/>información accesible"]
                I --> M["métodos<br/>operaciones invocables"]
                A --> EA["arreglo.shape"]
                M --> EM["arreglo.mean()"]"""),
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Desarma una llamada antes de ejecutarla

    Lee `observaciones.append(15)` de izquierda a derecha:

    1. `observaciones` encuentra el objeto que recibirá la operación;
    2. el punto busca un nombre en su interfaz;
    3. `append` selecciona el método;
    4. los paréntesis llaman ese método;
    5. `15` es el argumento que la operación necesita.

    El objeto situado a la izquierda del punto importa. Aunque varios tipos
    compartan un nombre de método, cada tipo define qué significa esa operación
    y qué argumentos acepta.
    """)
    return


@app.cell
def _():
    texto_atributos = "  control  "
    atributo_strip = texto_atributos.strip
    resultado_strip = texto_atributos.strip()

    (
        atributo_strip,
        callable(atributo_strip),
        resultado_strip,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Anticipa tres resultados posibles

    Antes de usar un método nuevo, conviene revisar qué recibe, qué modifica y
    qué devuelve. Estos patrones aparecerán con frecuencia:

    | Patrón | Ejemplo | Dónde queda el resultado |
    |---|---|---|
    | devuelve un objeto nuevo | `texto.strip()` | en el valor retornado |
    | modifica el objeto | `lista.append(15)` | en la misma lista; retorna `None` |
    | calcula y devuelve un resumen | `lista.count(8)` | en el valor retornado |

    Esta tabla sirve para orientar la lectura, no como una regla universal. La
    documentación de cada método confirma su comportamiento.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En la salida anterior aparecen tres evidencias distintas:

    1. `texto_atributos.strip` recupera un método ligado a ese texto;
    2. `callable(...)` confirma que ese valor puede llamarse;
    3. `texto_atributos.strip()` ejecuta la operación y devuelve otro texto.

    El texto original no cambia. Los objetos `str` son inmutables: sus métodos
    producen nuevos valores en lugar de alterar el texto existente.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Practica la diferencia entre recuperar y llamar

    El texto de trabajo tiene espacios en ambos extremos. Guarda el atributo
    `strip`, comprueba si puede llamarse y luego úsalo para producir `"control"`.

    La celda ya prepara el objeto y recupera el método. Completa únicamente las
    dos decisiones pendientes y vuelve a ejecutar para revisar el resultado.
    """)
    return


@app.cell
def _(feedback):
    texto_ejercicio_objetos = "  control  "
    metodo_limpieza = texto_ejercicio_objetos.strip

    # TU TURNO: comprueba el método y llámalo.
    es_invocable = None
    resultado_limpio = None

    feedback.exercise("objetos_metodo", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Distingue el efecto del valor retornado

    No todos los métodos se comportan como `strip`. Las listas son mutables:
    algunos de sus métodos cambian el mismo objeto.

    `append(...)` agrega un elemento al final de una lista. Su resultado visible
    está en la lista modificada; el método devuelve `None`. Por eso conviene
    separar dos preguntas:

    - ¿qué cambió en el objeto?
    - ¿qué valor devolvió la llamada?
    """)
    return


@app.cell
def _():
    agenda_metodos = ["P01", "P02"]
    retorno_agenda = agenda_metodos.append("P03")

    {
        "lista después de append": agenda_metodos,
        "valor retornado": retorno_agenda,
    }
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Un error frecuente consiste en escribir:

    ```python
    agenda = agenda.append("P03")
    ```

    Después de esa línea, `agenda` queda ligada al retorno de `append`, es decir,
    a `None`. La lista sí fue modificada, pero perdimos el nombre que usábamos
    para encontrarla. La alternativa clara es llamar el método sin reasignar:

    ```python
    agenda.append("P03")
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Transfiere la idea sin modificar la fuente

    Conserva intacta la lista `observaciones_originales`. Crea una copia, agrega
    el valor `15` a la copia y guarda también lo que devuelve `append`.

    Al finalizar deben existir dos listas independientes. El retorno del método
    y el objeto modificado responden preguntas diferentes.
    """)
    return


@app.cell
def _(feedback):
    observaciones_originales = [8, 12, 9]

    # TU TURNO: crea una copia, agrega 15 y conserva el retorno de append.
    observaciones_trabajo = "PENDIENTE"
    retorno_append = "PENDIENTE"

    feedback.exercise("objetos_copia", locals())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
            ## ¿Qué aporta organizar programas alrededor de objetos?

            La **programación orientada a objetos (POO)** organiza una parte del
            programa alrededor de objetos que reúnen estado y operaciones
            relacionadas. Al usar listas, textos, arrays o DataFrames ya estás
            aprovechando objetos, aunque todavía no estés creando tipos propios.

            Sus beneficios más visibles son:

            - **abstracción:** usamos una interfaz clara sin conocer cada detalle
              interno;
            - **cohesión:** los datos y las operaciones relacionadas permanecen
              cerca;
            - **consistencia:** los objetos del mismo tipo responden a una
              interfaz común;
            - **reutilización:** una operación aprendida sirve para muchos
              objetos del mismo tipo;
            - **composición:** un programa conecta objetos con responsabilidades
              distintas.
            """),
            mo.mermaid(r"""flowchart LR
                P["problema"] --> O["objeto"]
                O --> E["estado"]
                O --> I["interfaz"]
                I --> A["atributos"]
                I --> M["métodos"]
                E --> R["código organizado"]
                A --> R
                M --> R"""),
        ],
        gap=1,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La POO no hace que cualquier programa sea automáticamente mejor. Para una
    transformación pequeña, una expresión o una función puede ser más clara.
    Python combina varios estilos: funciones, expresiones y objetos suelen
    convivir en un mismo análisis.

    En esta semana importa aprender a **usar** objetos y leer su interfaz. Crear
    clases propias, decidir herencia o diseñar jerarquías corresponde a otro
    nivel y no es necesario para comenzar a trabajar con herramientas
    científicas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inspecciona un objeto cuando no conoces su interfaz

    No necesitas memorizar todos los atributos y métodos. Puedes combinar tres
    fuentes de evidencia:

    - `type(objeto)` identifica el tipo;
    - `dir(objeto)` enumera nombres disponibles;
    - la documentación explica qué recibe y qué devuelve cada operación.

    `dir` es un inventario, no una explicación. Para una primera exploración
    suele ser más útil filtrar los nombres que empiezan por guion bajo y luego
    consultar solo el que responde a la tarea actual.
    """)
    return


@app.cell
def _():
    registro_inspeccion = {
        "codigo": "P01",
        "estado": "completo",
    }
    nombres_publicos_registro = [
        nombre
        for nombre in dir(registro_inspeccion)
        if not nombre.startswith("_")
    ]

    nombres_publicos_registro
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Observa que aparecen nombres como `get`, `items`, `keys` y `values`. No hace
    falta aprenderlos todos al mismo tiempo. La pregunta concreta decide cuál
    consultar:

    ```python
    registro_inspeccion.get("estado")
    registro_inspeccion.keys()
    ```

    En los siguientes cuadernos aplicaremos esta misma lectura a módulos, arrays,
    Series y DataFrames.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cierra con una explicación propia

    Describe con tus palabras qué reúne un objeto y diferencia nombre, tipo,
    estado, atributo y método. Incluye qué indican el punto y los paréntesis, y
    menciona una ventaja concreta de trabajar mediante una interfaz.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    cierre_objetos = mo.ui.text_area(
        label="¿Cómo leerías objeto.metodo() en voz alta?",
        placeholder="Explica qué se busca, qué se llama y dónde observas el resultado.",
        rows=4,
        full_width=True,
    )
    cierre_objetos
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lo que conviene conservar

    - Todo valor de Python es un objeto con un tipo.
    - Un nombre permite encontrar un objeto; dos nombres pueden referirse al
      mismo objeto.
    - El estado describe la información actual y la interfaz reúne las formas de
      interactuar con el objeto.
    - `objeto.atributo` busca un nombre asociado con el objeto.
    - Un método es un atributo invocable; los paréntesis realizan la llamada.
    - Una operación puede devolver un valor nuevo, modificar el objeto o hacer
      ambas cosas de manera explícita.
    - Organizar estado y operaciones alrededor de objetos favorece la
      abstracción, la consistencia y la reutilización, pero no reemplaza otros
      estilos de programación.
    - `type`, `dir` y la documentación permiten explorar objetos desconocidos.

    El próximo cuaderno extiende este modelo: un módulo también es un objeto con
    nombres accesibles mediante la notación con punto.
    """)
    return


if __name__ == "__main__":
    app.run()
