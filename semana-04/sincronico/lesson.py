# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = [
#     "marimo==0.24.0",
#     "numpy==2.5.2",
#     "pandas==3.0.5",
#     "pyarrow==23.0.1",
# ]
# ///

# ruff: noqa: B018, F841

import marimo

__generated_with = "0.24.0"
app = marimo.App(
    width="full",
    app_title="Semana 4 · Workbook en vivo",
    layout_file="layouts/lesson.slides.json",
    css_file="../../assets/ces-theme.css",
)


@app.cell(hide_code=True)
def setup():
    from pathlib import Path
    import marimo as mo
    import numpy as np
    import pandas as pd

    assets = Path(__file__).resolve().parent / "assets"
    return assets, mo, np, pd


@app.cell(hide_code=True)
def activity_01_prompt(mo):
    mo.md(r"""
    # Actividad 1: Importación de archivo delimitado no estándar
    ## Configuración explícita de delimitador, fechas y valores nulos

    El archivo `pacientes_punto_y_coma.csv` contiene registros con delimitador `;`,
    fechas en formato `día/mes/año` y ausencias marcadas como `"SIN_DATO"`.

    **Tu turno:** Carga el archivo utilizando `pd.read_csv` con los parámetros necesarios
    (`sep`, `na_values`, `parse_dates`, `dayfirst`) para que las fechas queden tipificadas
    como temporales y las ausencias se reconozcan como `NaN`.
    """)
    return


@app.cell
def activity_01_workspace(assets, pd):
    # TU TURNO: configure la lectura de pacientes_punto_y_coma.csv
    df_actividad_1 = None

    {
        "archivo": "pacientes_punto_y_coma.csv",
        "resultado": df_actividad_1,
    }
    return


@app.cell(hide_code=True)
def activity_02_prompt(mo):
    mo.md(r"""
    # Actividad 2: Verificación de tipos y esquemas en Parquet
    ## Carga directa de esquemas binarios y comprobación de tipos nativos

    El formato Parquet almacena metadatos y esquemas columnares binarios,
    preservando tipos nativos como enteros nullables y fechas sin pérdida de precisión.

    **Tu turno:** Lee el archivo `pacientes_estudio.parquet` con `pd.read_parquet`
    e inspecciona los tipos de datos de sus columnas (`.dtypes`). Comprueba que la columna
    `fecha_visita` ya cuenta con tipo datetime sin requerir parseo manual.
    """)
    return


@app.cell
def activity_02_workspace(assets, pd):
    # TU TURNO: cargue pacientes_estudio.parquet e inspeccione tipos
    df_actividad_2 = None
    tipo_fecha = None
    es_datetime = None

    {
        "archivo": "pacientes_estudio.parquet",
        "resultado": df_actividad_2,
        "tipo de fecha_visita": tipo_fecha,
        "¿es datetime nativo?": es_datetime,
    }
    return


@app.cell(hide_code=True)
def activity_03_prompt(mo):
    mo.md(r"""
    # Actividad 3: Diagnóstico e integridad del lote de datos
    ## Extracción de métricas estructurales, recuento de ausencias y unicidad de clave

    Antes de transformar cualquier lote, se deben auditar dimensiones, ausencias y cardinalidad de claves primarias.

    **Tu turno:** Carga `pacientes_estudio.csv` y extrae un diagnóstico con: dimensiones (`.shape`),
    participantes únicos en `codigo` (`.nunique()`), conteo de valores nulos en `lectura_sistolica`
    e `imc` (`.isna().sum()`), y verificación de unicidad en la clave `codigo` (`.duplicated().any()`).
    """)
    return


@app.cell
def activity_03_workspace(assets, pd):
    df_recepcion = pd.read_csv(assets / "pacientes_estudio.csv")

    # TU TURNO: extraiga las métricas de diagnóstico del lote
    total_registros = None
    participantes_unicos = None
    faltantes_sistolica = None
    faltantes_imc = None
    hay_codigos_duplicados = None

    {
        "total registros recibidos": total_registros,
        "participantes únicos": participantes_unicos,
        "faltantes sistólica": faltantes_sistolica,
        "faltantes IMC": faltantes_imc,
        "¿hay códigos duplicados?": hay_codigos_duplicados,
    }
    return


@app.cell(hide_code=True)
def activity_04_prompt(mo):
    mo.md(r"""
    # Actividad 4: Gestión de datos ausentes con dropna y fillna
    ## Descarte selectivo de variables críticas e imputación trazable de covariables

    En el Estudio Horizonte, un registro sin `lectura_sistolica` no es viable para el objetivo
    primario del estudio, mientras que las ausencias en `imc` pueden imputarse con la mediana del conjunto.

    **Tu turno:** Aplica `dropna(subset=['lectura_sistolica'])` sobre el DataFrame. Luego,
    crea una columna booleana indicadora `imc_imputado` con los nulos de `imc` y rellena las
    ausencias de `imc` con la mediana muestral usando `fillna()`.
    """)
    return


@app.cell
def activity_04_workspace(assets, pd):
    df_base_c04 = pd.read_csv(assets / "pacientes_estudio.csv")

    # TU TURNO: aplique dropna selectivo en sistólica e imputación trazable en imc
    df_tratado_c04 = None
    mediana_imc_c04 = None

    {
        "filas resultantes": len(df_tratado_c04) if df_tratado_c04 is not None else None,
        "mediana aplicada": mediana_imc_c04,
        "resultado": df_tratado_c04,
    }
    return


@app.cell(hide_code=True)
def activity_05_prompt(mo):
    mo.md(r"""
    # Actividad 5: Detección y eliminación de registros duplicados
    ## Inspección con duplicated(keep=False) y deduplicación controlada

    El archivo de pacientes contiene registros redundantes por retransmisión técnica de formularios.

    **Tu turno:** Consulta las filas con códigos repetidos utilizando `.duplicated(subset=['codigo'], keep=False)`
    para inspección previa. Luego, aplica `.drop_duplicates(subset=['codigo'], keep='first')` y verifica
    que la clave `codigo` quede como identificador único.
    """)
    return


@app.cell
def activity_05_workspace(assets, pd):
    df_base_c05 = pd.read_csv(assets / "pacientes_estudio.csv")

    # TU TURNO: inspeccione con keep=False y elimine duplicados con keep='first'
    duplicados_auditados_c05 = None
    df_depurado_c05 = None
    clave_es_unica_c05 = None

    {
        "duplicados auditados": duplicados_auditados_c05,
        "filas conservadas": len(df_depurado_c05) if df_depurado_c05 is not None else None,
        "¿clave única garantizada?": clave_es_unica_c05,
    }
    return


@app.cell(hide_code=True)
def activity_06_prompt(mo):
    mo.md(r"""
    # Actividad 6: Estandarización de texto con métodos .str
    ## Corrección de espacios y formato de capitalización en variables categóricas

    La columna `sede` en `pacientes_estudio.csv` presenta inconsistencias textuales
    con espacios accidentales y mezclas de mayúsculas (e.g. `" norte "`, `"SUR"`).

    **Tu turno:** Aplica sobre `sede` la secuencia vectorizada `.str.strip().str.capitalize()`.
    Comprueba mediante `.unique()` que la cantidad de categorías se reduzca exactamente a tres
    (`Norte`, `Sur`, `Centro`).
    """)
    return


@app.cell
def activity_06_workspace(assets, pd):
    df_base_c06 = pd.read_csv(assets / "pacientes_estudio.csv")

    # TU TURNO: estandarice la columna sede con .str.strip().str.capitalize()
    sedes_limpias_c06 = None
    conteo_categorias_c06 = None

    {
        "sedes únicas obtenidas": sedes_limpias_c06.unique().tolist() if sedes_limpias_c06 is not None else None,
        "total categorías únicas": conteo_categorias_c06,
    }
    return


@app.cell(hide_code=True)
def activity_07_prompt(mo):
    mo.md(r"""
    # Actividad 7: Conversión explícita y optimización de tipos
    ## Asignación de tipos Int64 y category para optimización estructural

    La variable `numero_visitas` representa conteos que pueden contener nulos y `estado_seguimiento`
    es una variable cualitativa con un conjunto cerrado de valores posibles.

    **Tu turno:** Convierte `numero_visitas` al tipo de entero nullable `"Int64"` y `estado_seguimiento`
    al tipo `"category"`. Consulta las categorías creadas accediendo a `.cat.categories`.
    """)
    return


@app.cell
def activity_07_workspace(assets, pd):
    df_base_c07 = pd.read_csv(assets / "pacientes_estudio.csv")

    # TU TURNO: convierta numero_visitas a Int64 y estado_seguimiento a category
    df_tipificado_c07 = None

    {
        "tipo numero_visitas": str(df_tipificado_c07["numero_visitas"].dtype) if df_tipificado_c07 is not None else None,
        "tipo estado_seguimiento": str(df_tipificado_c07["estado_seguimiento"].dtype) if df_tipificado_c07 is not None else None,
        "categorías asignadas": list(df_tipificado_c07["estado_seguimiento"].cat.categories) if df_tipificado_c07 is not None else None,
    }
    return


@app.cell(hide_code=True)
def activity_08_prompt(mo):
    mo.md(r"""
    # Actividad 8: Creación de variables calculadas con .assign()
    ## Derivación de indicadores cuantitativos mediante expresiones vectorizadas

    Para calcular variables analíticas sin mutar el DataFrame original ni alterar la fuente,
    utilizamos el método `.assign()`.

    **Tu turno:** Descarta filas sin sistólica y utiliza `.assign()` para derivar una estimación
    diastólica aproximada (`diastolica_aprox = lectura_sistolica * 0.62`) y la Presión Arterial Media:
    $$\text{PAM} = \text{diastolica\_aprox} + \frac{\text{lectura\_sistolica} - \text{diastolica\_aprox}}{3}$$
    Redondea a 1 decimal y comprueba que la tabla original no contenga la columna `pam`.
    """)
    return


@app.cell
def activity_08_workspace(assets, pd):
    df_base_c08 = pd.read_csv(assets / "pacientes_estudio.csv").dropna(subset=["lectura_sistolica"])

    # TU TURNO: use .assign() para calcular diastolica_aprox y pam
    df_con_pam_c08 = None

    {
        "columnas en resultado": list(df_con_pam_c08.columns) if df_con_pam_c08 is not None else None,
        "muestra calculada": df_con_pam_c08[["codigo", "lectura_sistolica", "pam"]].head(3) if df_con_pam_c08 is not None else None,
    }
    return


@app.cell(hide_code=True)
def activity_09_prompt(mo):
    mo.md(r"""
    # Actividad 9: Discretización de variables continuas con pd.cut
    ## Segmentación por rangos teóricos y asignación de categorías clínicas

    El protocolo del estudio segmenta el Índice de Masa Corporal (IMC) en tres intervalos clínicos:
    - `< 25.0`: `"Normal"`
    - `[25.0, 30.0)`: `"Sobrepeso"`
    - `>= 30.0`: `"Obesidad"`

    **Tu turno:** Aplica `pd.cut` sobre la variable `imc` utilizando los puntos de corte
    `[0, 25.0, 30.0, 100.0]`, las etiquetas `['Normal', 'Sobrepeso', 'Obesidad']` y `right=False`.
    Examina el conteo de registros por categoría con `.value_counts()`.
    """)
    return


@app.cell
def activity_09_workspace(assets, pd):
    df_base_c09 = pd.read_csv(assets / "pacientes_estudio.csv").dropna(subset=["imc"])

    # TU TURNO: aplique pd.cut con los límites teóricos y etiquetas indicadas
    categoria_imc_c09 = None

    {
        "distribución de IMC": categoria_imc_c09.value_counts().to_dict() if categoria_imc_c09 is not None else None,
        "nulos resultantes": int(categoria_imc_c09.isna().sum()) if categoria_imc_c09 is not None else None,
    }
    return


@app.cell(hide_code=True)
def activity_10_prompt(mo):
    mo.md(r"""
    # Actividad 10: Cruce relacional de tablas con pd.merge
    ## Integración de datos de sedes y validación de correspondencia many-to-one

    La información de ciudad y equipamiento de referencia reside en el archivo externo `sedes_estudio.csv`.

    **Tu turno:** Estandariza la columna `sede` en los pacientes (`.str.strip().str.capitalize()`),
    carga `sedes_estudio.csv` y realiza un cruce relacional con `pd.merge` usando `on='sede'`,
    `how='left'` y `validate='many_to_one'`. Comprueba que ningún paciente quede con `ciudad` nula.
    """)
    return


@app.cell
def activity_10_workspace(assets, pd):
    df_pacientes_c10 = pd.read_csv(assets / "pacientes_estudio.csv").assign(
        sede=lambda d: d["sede"].str.strip().str.capitalize()
    )
    df_sedes_c10 = pd.read_csv(assets / "sedes_estudio.csv")

    # TU TURNO: combine las tablas con pd.merge(..., how='left', validate='many_to_one')
    df_unificado_c10 = None

    {
        "filas en tabla unificada": len(df_unificado_c10) if df_unificado_c10 is not None else None,
        "ciudades vinculadas": df_unificado_c10["ciudad"].unique().tolist() if df_unificado_c10 is not None else None,
        "nulos en ciudad tras cruce": int(df_unificado_c10["ciudad"].isna().sum()) if df_unificado_c10 is not None else None,
    }
    return


@app.cell(hide_code=True)
def activity_11_prompt(mo):
    mo.md(r"""
    # Actividad 11: Concatenación vertical con pd.concat
    ## Consolidación de entregas periódicas y reindexación secuencial

    El equipo operativo envía registros diarios en lotes separados: `contactos_dia_1.csv`
    y `contactos_dia_2.csv`.

    **Tu turno:** Carga ambos archivos y apílalos verticalmente usando
    `pd.concat([dia_1, dia_2], ignore_index=True)`. Calcula la suma total de personas
    contactadas y el total agrupado por sede.
    """)
    return


@app.cell
def activity_11_workspace(assets, pd):
    df_dia_1_c11 = pd.read_csv(assets / "contactos_dia_1.csv")
    df_dia_2_c11 = pd.read_csv(assets / "contactos_dia_2.csv")

    # TU TURNO: apile ambos DataFrames con pd.concat(..., ignore_index=True)
    df_contactos_total_c11 = None
    total_personas_c11 = None

    {
        "total registros consolidados": len(df_contactos_total_c11) if df_contactos_total_c11 is not None else None,
        "personas contactadas totales": total_personas_c11,
        "contactos por sede": df_contactos_total_c11.groupby("sede")["personas_contactadas"].sum().to_dict() if df_contactos_total_c11 is not None else None,
    }
    return


@app.cell(hide_code=True)
def activity_12_prompt(mo):
    mo.md(r"""
    # Actividad 12: Reestructuración de formato ancho a largo con pd.melt
    ## Despivotado de mediciones repetidas a estructura de datos ordenados

    En el archivo `presion_ancha.csv`, las tomas de seguimiento (`pas_inicial`, `pas_mes_1`, `pas_mes_3`)
    están en columnas horizontales.

    **Tu turno:** Transforma la tabla a formato largo usando `pd.melt()` especificando
    `id_vars=['codigo', 'sede']`, `value_vars=['pas_inicial', 'pas_mes_1', 'pas_mes_3']`,
    `var_name='visita'` y `value_name='pas'`. Luego genera una matriz resumen bidimensional con `pd.pivot_table()`.
    """)
    return


@app.cell
def activity_12_workspace(assets, pd):
    df_ancho_c12 = pd.read_csv(assets / "presion_ancha.csv")

    # TU TURNO: desempaca la tabla con pd.melt() y resume con pivot_table()
    df_largo_c12 = None
    matriz_resumen_c12 = None

    {
        "filas formato largo": len(df_largo_c12) if df_largo_c12 is not None else None,
        "primeras 3 observaciones": df_largo_c12.head(3) if df_largo_c12 is not None else None,
        "matriz resumen": matriz_resumen_c12,
    }
    return


@app.cell(hide_code=True)
def activity_13_prompt(mo):
    mo.md(r"""
    # Actividad 13: Ejecución del pipeline sobre un nuevo lote
    ## Procesamiento automatizado de nuevas entregas y auditoría de valores atípicos

    Ha llegado una nueva entrega en `lote_b_transferencia.csv`. Debemos procesarla
    aplicando el pipeline y auditando casos extremos.

    **Tu turno:** Carga `lote_b_transferencia.csv`, estandariza la columna `sede`,
    realiza el cruce con `sedes_estudio.csv`, e incorpora una bandera de auditoría
    `edad_inverosimil = df['edad'] > 110` para señalar valores atípicos sin descartar la fila arbitrariamente.
    """)
    return


@app.cell
def activity_13_workspace(assets, pd):
    df_lote_nuevo_c13 = pd.read_csv(assets / "lote_b_transferencia.csv")
    df_sedes_c13 = pd.read_csv(assets / "sedes_estudio.csv")

    # TU TURNO: aplique el pipeline y la bandera edad_inverosimil sobre el lote nuevo
    df_transferencia_c13 = None
    alertas_edad_c13 = None

    {
        "total registros procesados": len(df_transferencia_c13) if df_transferencia_c13 is not None else None,
        "casos con alerta de edad": alertas_edad_c13,
        "detalle de alertas": df_transferencia_c13[df_transferencia_c13["edad_inverosimil"]][["codigo", "edad", "sede"]] if df_transferencia_c13 is not None and "edad_inverosimil" in df_transferencia_c13.columns else None,
    }
    return


if __name__ == "__main__":
    app.run()
