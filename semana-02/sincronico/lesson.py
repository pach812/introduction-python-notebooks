# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = ["marimo==0.23.16"]
# ///

# ruff: noqa: B018, F841

import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="full",
    app_title="Semana 2 · Workbook en vivo",
    layout_file="layouts/lesson.slides.json",
    css_file="../../assets/ces-theme.css",
)


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _():
    participantes_estudio = [
        {
            "codigo": "P01",
            "edad": 34,
            "consentimiento": True,
            "formulario": True,
        },
        {
            "codigo": "P02",
            "edad": 17,
            "consentimiento": True,
            "formulario": True,
        },
        {
            "codigo": "P03",
            "edad": 65,
            "consentimiento": True,
            "formulario": True,
        },
        {
            "codigo": "P04",
            "edad": 42,
            "consentimiento": False,
            "formulario": True,
        },
        {
            "codigo": "P05",
            "edad": 29,
            "consentimiento": True,
            "formulario": False,
        },
    ]
    frontera_c05 = [
        {
            "codigo": "L18",
            "edad": 18,
            "consentimiento": True,
            "formulario": True,
        },
        {
            "codigo": "L65",
            "edad": 65,
            "consentimiento": True,
            "formulario": True,
        },
    ]
    return (participantes_estudio,)


@app.cell(hide_code=True)
def exercise_rule_prompt(mo):
    mo.md(r"""
    # Problema 1 · Explicar la primera razón que detiene el proceso
    ## Completen las ramas y comprueben las edades 18, 65 y 66

    Revisen en este orden: rango de edad, consentimiento y formulario. El
    resultado debe indicar `continúa` o la primera condición que no se cumple.
    """)
    return


@app.cell
def exercise_rule():
    edad_practica_c01 = 65
    consentimiento_practica_c01 = True
    formulario_practica_c01 = True

    # TU TURNO: reemplaza cada marcador por una condición o un resultado.
    if False:  # COMPLETA: condición sobre la edad
        decision_practica_c01 = "COMPLETA: resultado por edad"
    elif False:  # COMPLETA: condición sobre el consentimiento
        decision_practica_c01 = "COMPLETA: resultado por consentimiento"
    elif False:  # COMPLETA: condición sobre el formulario
        decision_practica_c01 = "COMPLETA: resultado por formulario"
    else:
        decision_practica_c01 = "COMPLETA: resultado cuando todo se cumple"

    decision_practica_c01
    return


@app.cell(hide_code=True)
def exercise_collections_prompt(mo):
    mo.md(r"""
    # Problema 2 · Incorporar un nuevo registro
    ## Agreguen P06 a la copia de trabajo sin modificar la lista original

    Al terminar, la fuente conserva cinco registros y la copia contiene seis.
    """)
    return


@app.cell
def exercise_collections(participantes_estudio):
    registros_practica_c02 = participantes_estudio.copy()
    nuevo_registro_c02 = {
        "codigo": "P06",
        "edad": 51,
        "consentimiento": True,
        "formulario": True,
    }

    # TU TURNO: agrega nuevo_registro_c02 a la copia de trabajo.

    registros_practica_c02
    return (registros_practica_c02,)


@app.cell(hide_code=True)
def exercise_loop_prompt(mo):
    mo.md(r"""
    # Situación 3 · La revisión manual ya no escala

    La coordinación necesita una bitácora que permita comprobar que cada persona
    fue revisada. Construyan una lista de diccionarios con `codigo` y `edad`, en
    el mismo orden de llegada.

    Pasa la informacion del `registros_practica_c02` a la nueva `bitacora_revision_c03`.

    **Criterio:** cinco entradas; la primera corresponde a P01 y la última a P05.

    Antes de programar: ¿qué cambia en cada vuelta y qué debe permanecer?
    """)
    return


@app.cell
def exercise_loop(registros_practica_c02):
    bitacora_revision_c03 = []

    # TU TURNO: recorre participantes_estudio y construye cada entrada.
    for participante in registros_practica_c02:
        bitacora_revision_c03.append(participante)
        print(f"paciente {participante['codigo']} agregado!")

    bitacora_revision_c03
    return


@app.cell(hide_code=True)
def exercise_records_prompt(mo):
    mo.md(r"""
    # Situación 4 · La bitácora no organiza el trabajo

    El equipo necesita dos colas: personas que continúan y personas que requieren
    revisión.

    **Apliquen la regla completa _(edad, consentimiento y formulario)_** y conserven solamente los códigos.

    **Criterio:** `continuan` contiene P01 y P03; `revision` contiene P02, P04 y P05.

    Antes de programar: ¿cómo garantizarán que cada código llegue a una sola cola?
    """)
    return


@app.cell
def exercise_records(registros_practica_c02):
    continuan_c03 = []
    revision_c03 = []

    for _participante in registros_practica_c02:

        # cualquier que se inclumpla lo descarta.
        reglas_para_revision = ( 
            _participante["edad"] < 18 
            or _participante["edad"] > 65 
            or not _participante["consentimiento"] 
            or not _participante["formulario"]
        )

        # aquí se deben cumplir todas las reglas.
        reglas_para_pasar = (
            _participante["edad"] >= 18 or _participante["edad"] <= 65
            and _participante["consentimiento"]
            and _participante["formulario"]
        )
    
        # revisar edad.
        if reglas_para_revision:
            revision_c03.append(_participante["codigo"])
        else: 
            continuan_c03.append(_participante["codigo"])

    # TU TURNO: clasifica cada registro en exactamente una cola.

    continuan_c03, revision_c03
    return


@app.cell(hide_code=True)
def exercise_filter_prompt(mo):
    mo.md(r"""
    # Situación 5 · «Requiere revisión» no explica qué hacer

    Construyan registros con `codigo` y el primer `motivo` que detuvo el proceso.
    Respeten este orden: edad, consentimiento y formulario.

    **Criterio:** P02→`edad`, P04→`consentimiento`, P05→`formulario`.

    Antes de programar: si fallan dos condiciones, ¿qué rama decide el motivo?
    """)
    return


@app.cell
def exercise_filter(registros_practica_c02):
    casos_continua_c03 = []
    casos_revision_c03 = []

    registros_practica_c02[1]["formulario"] = False

    # TU TURNO: conserva codigo y primer motivo de cada caso detenido.
    for _participante in registros_practica_c02:
        motivos = []
    
        # aquí se deben cumplir todas las reglas.
        regla_edad = (_participante["edad"] >= 18 and _participante["edad"] <= 65)
        regla_consentimiento = ( _participante["consentimiento"])
        regla_formulario =(_participante["formulario"])
    
        # revisar edad.
        if regla_edad and regla_consentimiento and regla_formulario:
            casos_continua_c03.append(_participante)
            continue
        if not regla_edad:
            motivos.append("edad")
        if not regla_consentimiento:
            motivos.append("consentimiento")
        if not regla_formulario:
            motivos.append("formulario")
    
        casos_revision_c03.append(
                {
                    "codigo": _participante["codigo"],
                    "motivos": motivos
                }
            )

    casos_continua_c03, casos_revision_c03
    return


@app.cell(hide_code=True)
def exercise_count_prompt(mo):
    mo.md(r"""
    # Situación 6 · Hay que distribuir la carga de revisión

    Resuman cuántos casos corresponden a cada motivo. El resultado debe poder
    consultarse por `edad`, `consentimiento` y `formulario`.

    **Criterio:** los tres conteos valen 1 y suman la cantidad de casos de revisión.

    Antes de programar: ¿qué dato de cada caso indica cuál contador debe cambiar?
    """)
    return


@app.cell
def exercise_count():
    carga_revision_c03 = {
        "edad": 0,
        "consentimiento": 0,
        "formulario": 0,
    }

    # TU TURNO: actualiza el conteo que corresponda a cada motivo.

    carga_revision_c03
    return


@app.cell(hide_code=True)
def exercise_while_prompt(mo):
    mo.md(r"""
    # Situación 7 · Un formulario pendiente requiere contacto

    Para P05 se simulan estas respuestas: `[False, False, True]`. Registren cada
    intento y deténganse cuando haya respuesta o se alcancen tres intentos.

    **Criterio:** intentos `[1, 2, 3]`; cierre `respuesta recibida`.

    Antes de programar: ¿qué dos hechos pueden volver falsa la condición del ciclo?
    """)
    return


@app.cell
def exercise_while():
    respuestas_contacto_c03 = [False, False, True]
    intento_contacto_c03 = 0
    intentos_realizados_c03 = []
    hubo_respuesta_c03 = False

    # TU TURNO: coordina el máximo y la respuesta dentro de un while.

    cierre_contacto_c03 = "respuesta recibida" if hubo_respuesta_c03 else "sin respuesta"
    intentos_realizados_c03, cierre_contacto_c03
    return


@app.cell
def _():
    # funciones con o sin retorno. 

    ## funcion sin retorno: 

    def check_numerico(numero):
        """Esta funcion imprime un valor numerico"""
        if not isinstance(numero, (int,float)):
            print("El valor ingresado no es un numero, no se puede imprimir")
        else:
            print(numero)
            print(type(numero))


    check_numerico(45.4)

    # funcion con retorno:
    def check_numerico_con_retorno(numero):
        """Esta funcion imprime un valor numerico"""
        if not isinstance(numero, (int,float)):
            print("El valor ingresado no es un numero, no se puede imprimir")
        else:
            print(numero)
            print(type(numero))
            return numero

    resultado_func = check_numerico_con_retorno(45.3)

    return


@app.cell(hide_code=True)
def exercise_function_prompt(mo):
    mo.md(r"""
    # Situación 8 · Otra sede necesita la misma regla

    Completen una función que reciba un registro y devuelva `continua`, `edad`,
    `consentimiento` o `formulario`. Debe conservar el orden del protocolo.

    **Criterio:** P01→`continua`; P02→`edad`; P04→`consentimiento`.

    Antes de programar: ¿qué debe llegar como argumento y qué debe devolver la función?
    """)
    return


@app.function
def clasificar_participante(participante, edad_minima, edad_maxima):
    """
    Que quiero: que se clasifique un participante por edad, consentimiento y formulario.
    Que recibe: una lista de participantes en la variable registro, una edad minima y maxima a filtrar.
    que devuleve: si el participante cumple con las condiciones devuelve el codigo del participante y sus motivos si no cumple.

    return: un diccionario con datos de paticipante o codigo y motivos de fallo/exclusion.
    """
    motivos = []
    
    # aquí se deben cumplir todas las reglas.
    regla_edad = (participante["edad"] >= edad_minima and participante["edad"] <= edad_maxima)
    regla_consentimiento = (participante["consentimiento"])
    regla_formulario =(participante["formulario"])
    
    # revisar condiciones, si cumple devolvemos el participante.
    if regla_edad and regla_consentimiento and regla_formulario:
        return participante
    if not regla_edad:
        motivos.append("edad")
    if not regla_consentimiento:
        motivos.append("consentimiento")
    if not regla_formulario:
        motivos.append("formulario")
    
    return {"codigo": participante["codigo"],"motivos_de_revision": motivos}


@app.cell
def _(participantes_estudio):
    # queremos ejecutar la funcion clasificar_participante por cada elemnto (participante) en la lista de estudio. 
    for _participante in participantes_estudio:
        print(f"Clasificando participante {_participante['codigo']}:")
        resultado = clasificar_participante(participante=_participante, edad_minima=18, edad_maxima=65)
        print(resultado)

    participantes_estudio
    return


@app.cell(hide_code=True)
def exercise_integrated_prompt(mo):
    mo.md(r"""
    # Situación 9 · La sede necesita el resumen completo

    Construyan una función que use `clasificar_registro_c04` y devuelva un
    diccionario con las listas `continuan` y `revision`.

    **Criterio:** las dos listas cubren los cinco registros sin repetir ninguno.

    Antes de programar: ¿qué responsabilidad conserva cada una de las dos funciones?
    """)
    return


@app.cell
def exercise_integrated():
    def organizar_jornada_c04(registros, edad_minima, edad_maxima):
        # TU TURNO: construye y devuelve las dos listas del resumen.
        ...

    organizar_jornada_c04
    return


@app.cell(hide_code=True)
def exercise_debug(mo):
    mo.md(r"""
    # Situación 10 · Los casos habituales pasan, las fronteras no

    Comparen observado y esperado, localicen una sola decisión responsable y
    vuelvan a ejecutar.

    **Criterio:** 18 y 65 producen `continua`; 17 y 66 producen `edad`.

    Antes de editar: ¿cuál es el primer caso donde observado y esperado difieren?
    """)
    return


@app.cell
def boundary_defect():
    def clasificar_edad_c05(edad):
        if 18 < edad < 65:
            return "continua"
        return "edad"

    # TU TURNO: corrige la función y conserva los cuatro casos de comprobación.
    casos_frontera_c05 = {17: "edad", 18: "continua", 65: "continua", 66: "edad"}
    {edad: clasificar_edad_c05(edad) for edad in casos_frontera_c05}
    return


@app.cell(hide_code=True)
def final_live_coding_prompt(mo):
    mo.md(r"""
    # Situación 11 · Preparar el seguimiento del día siguiente

    Desde cero, creen una función que reciba registros y devuelva una lista de
    diccionarios con `codigo` e `intentos_maximos` para quienes tienen
    consentimiento y formulario pendiente.

    **Criterio:** obtiene `[{'codigo': 'P05', 'intentos_maximos': 3}]`, sin
    modificar la entrada.

    Antes de programar: ¿qué estructura del proceso anterior pueden reutilizar
    aunque la regla y la forma de la salida hayan cambiado?
    """)
    return


@app.cell
def final_live_coding_workspace():
    ...
    return


if __name__ == "__main__":
    app.run()
