# Semana 4 · Limpieza, preparación y combinación de datos

En esta sesión sincrónica trabajaremos sobre el lote de datos del Estudio Horizonte,
un estudio epidemiológico multicéntrico ficticio. Aprenderemos a transformar
archivos crudos, heterogéneos y con inconsistencias en tablas analíticas validadas,
garantizando la inmutabilidad de las fuentes originales y la trazabilidad de cada decisión.

El workbook contiene 13 actividades prácticas numeradas secuencialmente, exactamente
iguales a las desarrolladas durante la sesión con el docente:

1. **Importación de archivo delimitado no estándar** (`pacientes_punto_y_coma.csv`): delimitadores, fechas y nulos.
2. **Verificación de tipos y esquemas en Parquet** (`pacientes_estudio.parquet`): almacenamiento columnar y tipos nativos.
3. **Diagnóstico e integridad del lote de datos** (`pacientes_estudio.csv`): dimensiones, tipos, nulos y unicidad de clave.
4. **Gestión de datos ausentes con dropna y fillna**: descarte crítico e imputación con trazabilidad.
5. **Detección y eliminación de registros duplicados**: inspección previa con `keep=False` y deduplicación controlada.
6. **Estandarización de texto con métodos .str**: normalización de categorías y corrección de espacios.
7. **Conversión explícita y optimización de tipos**: coerción con `pd.to_numeric`, enteros `Int64` y tipos `category`.
8. **Creación de variables calculadas con .assign()**: derivación funcional de la Presión Arterial Media (PAM).
9. **Discretización de variables continuas con pd.cut**: segmentación por intervalos teóricos de IMC.
10. **Cruce relacional de tablas con pd.merge** (`sedes_estudio.csv`): validación `many_to_one` e integridad referencial.
11. **Concatenación vertical con pd.concat** (`contactos_dia_1.csv`, `contactos_dia_2.csv`): consolidación y reindexación.
12. **Reestructuración de formato ancho a largo con pd.melt** (`presion_ancha.csv`): datos ordenados (Tidy Data) y matrices resumen.
13. **Ejecución del pipeline sobre un nuevo lote** (`lote_b_transferencia.csv`): flujo automatizado y auditoría de casos atípicos.

## Cómo abrir el cuaderno

Para ejecutar y editar el cuaderno interactivo de la sesión sincrónica:

```bash
uv run marimo edit semana-04/sincronico/lesson.py
```

Si estás trabajando directamente sobre la estructura del repositorio de desarrollo:

```bash
uv run marimo edit materials/v2/students/live-coding/week-04-data-cleaning-wrangling/lesson.py
```

## Una pregunta para orientar el trabajo

En cada actividad pregúntate: *¿qué comprobación programática demuestra que los datos no perdieron su significado original tras la transformación?* Verificar dimensiones (`.shape`), ausencia de nulos inesperados (`.isna().sum()`) y unicidad de claves (`.is_unique`) te asegurará que cada paso produce una tabla lista para el análisis exploratorio.

> **Nota metodológica:** Todos los datos, identificadores y mediciones corresponden a un caso ficticio diseñado exclusivamente con fines pedagógicos y académicos.
