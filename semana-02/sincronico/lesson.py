# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = ["marimo==0.23.16"]
# ///

# ruff: noqa: B018, F841

import marimo

__generated_with = "0.23.16"
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
    return frontera_c05, participantes_estudio


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
    return (
        consentimiento_practica_c01,
        decision_practica_c01,
        edad_practica_c01,
        formulario_practica_c01,
    )


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
    return


@app.cell(hide_code=True)
def exercise_loop_prompt(mo):
    mo.md(r"""
    # Problema 3 · Seleccionar los códigos elegibles
    ## Recorran todos los registros y apliquen la regla completa

    El resultado debe ser una lista nueva. Antes de ejecutar, escriban qué
    códigos esperan conservar.
    """)
    return


@app.cell
def exercise_loop(participantes_estudio):
    codigos_practica_c03 = []

    # TU TURNO: recorre participantes_estudio.
    # Conserva el código únicamente cuando se cumpla la regla completa.

    codigos_practica_c03
    return


@app.cell(hide_code=True)
def exercise_function_prompt(mo):
    mo.md(r"""
    # Problema 4 · Convertir el recorrido en una función
    ## Entradas: registros y límites · salida: lista de códigos

    La función debe producir el mismo resultado sin depender de variables
    externas ni terminar antes de recorrer toda la lista.
    """)
    return


@app.cell
def exercise_function():
    def seleccionar_participantes(registros, edad_minima, edad_maxima):
        """Devuelve los códigos que cumplen la regla del estudio ficticio."""
        # TU TURNO: construye el cuerpo completo desde este contrato.
        ...

    seleccionar_participantes
    return (seleccionar_participantes,)


@app.cell(hide_code=True)
def exercise_debug(mo):
    mo.md(r"""
    # Problema 5 · Una función que falla solo en las fronteras
    ## Describan la diferencia, propongan una causa y cambien una decisión

    Después de corregirla, vuelvan a comprobar los casos habitual, frontera y
    vacío.
    """)
    return


@app.cell
def boundary_defect(frontera_c05):
    def seleccionar_con_frontera_abierta_c05(registros):
        seleccionados = []
        for registro in registros:
            if (
                18 < registro["edad"] < 65
                and registro["consentimiento"]
                and registro["formulario"]
            ):
                seleccionados.append(registro["codigo"])
        return seleccionados

    observado_defecto_c05 = seleccionar_con_frontera_abierta_c05(frontera_c05)
    esperado_defecto_c05 = ["L18", "L65"]

    {
        "observado": observado_defecto_c05,
        "esperado": esperado_defecto_c05,
    }
    return


@app.cell(hide_code=True)
def final_live_coding_prompt(mo):
    mo.md(r"""
    # Problema 6 · Crear una función de seguimiento desde cero
    ## Devuelvan los códigos con consentimiento y formulario incompleto

    La función recibe una lista de registros y devuelve una lista nueva sin
    modificar la entrada. Con los registros de la sesión, el resultado esperado
    es `['P05']`.
    """)
    return


@app.cell
def final_live_coding_workspace():
    # TU TURNO: escribe aquí tu solución completa.
    ...
    return


if __name__ == "__main__":
    app.run()
