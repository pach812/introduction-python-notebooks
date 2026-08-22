import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", app_title="Semana 2 · Pruebas y errores")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    from course_widgets import load_feedback

    feedback = load_feedback(
        mo,
        week="week-02-control-collections-functions",
        notebook="10_pruebas_y_errores",
    )
    return feedback, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Pruebas: usar los errores para revisar nuestras ideas

    Una función puede responder bien a una llamada y fallar con otra. Si solo
    probamos un valor cómodo, aprendemos muy poco sobre los límites de su
    comportamiento.

    En este cuaderno convertiremos el contrato de una función en casos concretos,
    usaremos `assert` para comparar lo obtenido con lo esperado y trataremos cada
    falla como información: una pista para revisar una condición o un supuesto.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Convertir una promesa en un caso comprobable

    Contrato: “devuelve `True` si la edad es mayor o igual a un límite”.

    ```python
    def alcanza_limite(edad, limite=60):
        return edad >= limite
    ```

    El contrato todavía es una afirmación general. Para comprobarla necesitamos
    escoger una entrada concreta y deducir, desde el contrato, qué salida debería
    producir. Esa relación entre entrada y resultado esperado forma un **caso de
    prueba**.

    Por ejemplo, con límite 60, la edad 71 debería producir `True`. Pero ese caso
    no permite saber si el código incluyó exactamente el límite. La edad 60 sí
    distingue `>=` de `>`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    razon_inicial_pruebas = mo.ui.text_area(
        label="¿Qué valor probarías para revisar el límite?",
        placeholder="Escribe una entrada y explica qué permitiría descubrir. Este texto no se califica.",
        rows=3,
        full_width=True,
    )
    razon_inicial_pruebas
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ### Sigue el recorrido de un caso de prueba

    {
        mo.mermaid('''flowchart LR
        A[Elegir una entrada] --> B[Llamar la función]
        B --> C[Observar el resultado]
        D[Deducir lo esperado del contrato] --> E{{¿Coinciden?}}
        C --> E
        E -->|sí| F[El caso se cumple]
        E -->|no| G[Revisar el supuesto o el código]''')
    }

    Una coincidencia muestra que la función respondió bien en ese caso; no prueba
    por sí sola que responderá bien para todas las entradas posibles. Por eso
    escogemos varios casos que examinan riesgos diferentes.
    """)
    return


@app.cell
def _():
    def alcanza_limite(edad, limite=60):
        return edad >= limite

    resultado_normal = alcanza_limite(71)
    resultado_frontera = alcanza_limite(60)
    resultado_inferior = alcanza_limite(59)
    assert resultado_normal is True
    assert resultado_frontera is True
    assert resultado_inferior is False
    return alcanza_limite, resultado_frontera, resultado_inferior, resultado_normal


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Escoger casos que revelen errores distintos

    | Caso | Qué examina |
    |---|---|
    | habitual | comportamiento esperado en uso común |
    | frontera | operadores como `<`, `<=`, `>` y `>=` |
    | vacío | supuestos sobre la existencia de elementos |
    | ninguna coincidencia | estabilidad del tipo de salida |
    | todas coinciden | acumulación completa |
    | entrada alternativa válida | uso real de parámetros |

    Estas categorías no son una lista para aplicar mecánicamente. Cada una responde
    a una pregunta sobre el contrato. El caso vacío pregunta qué ocurre cuando no
    hay elementos que recorrer; el caso de frontera revisa qué pasa exactamente en
    el punto donde cambia la regla.

    Un conjunto útil de pruebas intenta distinguir implementaciones. Probar 70 y
    80 confirma dos veces una situación parecida; probar 60 revela si la función
    usó `>` en lugar de `>=`. La calidad depende de lo que cada caso permite
    descubrir, no de acumular muchas llamadas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Hacer visible una diferencia con `assert`

    Una **aserción** expresa algo que esperamos que sea verdadero en ese punto del
    programa. `assert condicion` continúa sin mostrar un informe cuando la
    condición se cumple. Si es falsa, detiene la ejecución y produce
    `AssertionError`:

    ```python
    assert alcanza_limite(60) is True
    ```

    El error no explica automáticamente la causa. Informa que el resultado no
    coincide con la expectativa y nos devuelve al contrato, a la entrada usada y a
    la condición de la función.

    Aquí usamos aserciones como pruebas de desarrollo. No son el mecanismo para
    validar datos enviados por una persona usuaria, porque pueden desactivarse en
    ciertos modos de ejecución.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Diseña tres casos que examinen límites diferentes

    La función `esta_en_rango` debe incluir ambos extremos. Asigna a las tres
    variables llamadas que comprueben un caso interior, un extremo incluido y
    un valor exterior. No reemplaces las llamadas por literales booleanos.

    Los tres resultados no son tres respuestas aisladas: forman un pequeño conjunto
    de evidencia. Escoge entradas que permitan reconocer qué regla examina cada
    caso. El Coach evaluará los valores producidos por las llamadas.
    """)
    return


@app.cell
def _(feedback):
    def esta_en_rango(valor, minimo, maximo):
        return minimo <= valor <= maximo

    # Diseña una llamada para cada familia de casos descrita arriba.
    prueba_interior = None
    prueba_extremo = None
    prueba_exterior = None
    feedback.exercise("pruebas_casos", locals())
    return prueba_exterior, prueba_extremo, prueba_interior


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Pasar de una falla a una hipótesis

    **Depurar** consiste en localizar y corregir la causa de un comportamiento que
    no coincide con lo esperado. Una prueba fallida reduce el problema: conocemos
    al menos una entrada, un resultado obtenido y un resultado esperado.

    A partir de esa evidencia:

    1. conserva la entrada mínima que reproduce el fallo;
    2. compara obtenido y esperado;
    3. formula una hipótesis sobre condición, estado inicial o actualización;
    4. cambia una cosa;
    5. repite la prueba fallida y luego las anteriores.

    Supón que el caso habitual pasa, el vacío pasa y solo falla el valor exactamente
    igual al límite. Esa combinación dirige la atención hacia el operador de
    comparación, no hacia el acumulador completo.

    No conviene cambiar varias líneas al tiempo: aunque el resultado mejore, sería
    difícil saber qué hipótesis era correcta. Un cambio pequeño seguido de la misma
    prueba permite aprender de la evidencia.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Corrige una causa y conserva la evidencia

    `contar_desde_limite` debería contar valores mayores o iguales al límite, pero
    una prueba de frontera falla. Corrige la función y conserva los tres casos como
    evidencia de que el cambio no dañó lo que ya funcionaba.

    Compara los tres resultados antes de editar. Si el caso habitual y el vacío ya
    funcionan, evita reescribir las partes que los producen. Busca la decisión que
    trata de manera diferente al valor exactamente igual al límite y cambia solo
    esa parte.
    """)
    return


@app.cell
def _(feedback):
    def contar_desde_limite(valores, limite):
        conteo = 0
        for valor_prueba in valores:
            if valor_prueba > limite:  # revisa el contrato
                conteo = conteo + 1
        return conteo

    caso_habitual_prueba = contar_desde_limite([12, 15, 20], 10)
    caso_frontera_prueba = contar_desde_limite([9, 10, 11], 10)
    caso_vacio_prueba = contar_desde_limite([], 10)
    feedback.exercise("pruebas_transferencia", locals())
    return caso_frontera_prueba, caso_habitual_prueba, caso_vacio_prueba


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cierre: explica qué aprendimos de una falla

    Reconstruye el caso de frontera de la última actividad. Explica qué entrada se
    usó, qué resultado se esperaba, qué resultado produjo la primera versión y por
    qué esa diferencia dirigió la revisión hacia un operador concreto.

    Incluye en tu explicación por qué una colección vacía merece una prueba y qué
    información aporta `AssertionError`. Describe la depuración como un ciclo de
    evidencia e hipótesis, no como una sucesión de cambios al azar.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    resumen_pruebas = mo.ui.text_area(
        label="Lo que una falla permitió descubrir",
        placeholder="Relaciona entrada, resultado esperado, resultado obtenido e hipótesis. Este texto no se califica.",
        rows=6,
        full_width=True,
    )
    resumen_pruebas
    return


if __name__ == "__main__":
    app.run()
