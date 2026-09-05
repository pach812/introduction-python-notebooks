# Semana 4 · Ruta de autoaprendizaje: De archivos a datos listos para analizar

Bienvenido a la semana central de preparación y wrangling de datos tabulares. Esta semana
acompaña la transición profesional desde un archivo recién recibido en bruto hasta una
tabla estructurada, validada, transformada, resumida y relacionada con fuentes externas,
dejándola en condiciones óptimas para el modelado y la inferencia científica.

Durante todas las unidades trabajarás con el **Estudio Horizonte**, un caso clínico sintético
multicéntrico de 50 registros de participantes, 10 variables clínicas y tablas relacionadas de
sedes y contactos. Los datos contienen desafíos reales (delimitadores no estándar, valores
codificados, formatos binarios vs texto, discrepancias de etiquetas, faltantes informativos,
mediciones temporales repetidas y duplicados) diseñados deliberadamente para que justifiques
cada decisión técnica antes de aplicarla.

---

## Las nueve unidades de autoaprendizaje

1. **`01_leer_archivos_texto.py` · Leer archivos de texto con intención**
   - Cómo Pandas interpreta caracteres: delimitadores (`sep`), encabezados (`header`), tipos (`dtype`),
     detección de fechas (`parse_dates`, `dayfirst`), códigos de ausencia personalizados (`na_values`)
     y lectura eficiente en bloques (`chunksize`).

2. **`02_elegir_formato_y_escribir.py` · Elegir formato y escribir**
   - Comparación multidimensional de formatos: texto plano (CSV/TSV), binario columnar (Parquet),
     hojas de cálculo (Excel multihoja con `pd.ExcelFile`), HDF5 y serialización (Pickle).
   - Fidelidad de esquemas (preservación de tipos exactos sin pérdida de precisión) y comprobación
     de ciclos de ida y vuelta (*roundtrip*).

3. **`03_auditar_estructura_y_calidad.py` · Auditar estructura y calidad**
   - Diagnosticar antes de intervenir: inspección de estructura (`.info()`, `.describe()`),
     cardinalidad (`.nunique()`), conteo de ausencias, verificación de claves primarias
     y contraste riguroso contra el diccionario oficial de datos.

4. **`04_tratar_datos_faltantes.py` · Tratar datos faltantes**
   - Faltantes como información: distinción entre ausencia aleatoria y estructural.
   - Descarte justificado con `dropna(subset=..., how=..., thresh=...)` vs imputación controlada
     con `fillna()` (constante, media/mediana condicional por grupo) y creación de columnas de
     trazabilidad (`_faltaba`).

5. **`05_corregir_etiquetas_tipos_duplicados.py` · Corregir etiquetas, tipos y duplicados**
   - Limpieza de cadenas vectorizada (`.str.strip().str.lower()`, reemplazos seguros).
   - Coerción segura de tipos numéricos (`pd.to_numeric(..., errors='coerce')`), enteros con soporte
     de nulos (`Int64`) y optimización con variables categóricas (`category`).
   - Auditoría y resolución de duplicados con `duplicated(keep=False)` y `drop_duplicates()`.

6. **`06_transformar_variables.py` · Transformar variables**
   - Derivación reproducible con `.assign()`, cálculo de indicadores fisiológicos vectorizados
     (Presión Arterial Media - PAM).
   - Discretización clínica con `pd.cut()` y cuantiles con `pd.qcut()`.
   - Generación de marcas booleanas de calidad para valores fuera de dominio biológico.

7. **`07_combinar_fuentes.py` · Combinar fuentes**
   - Uniones relacionales con `pd.merge()`: claves, tipos de unión (`inner`, `left`, `outer`),
     prevención de multiplicación involuntaria de filas con `validate='many_to_one'`, sufijos e
     indicador de procedencia (`_merge`).
   - Concatenación y apilamiento de lotes de datos con `pd.concat()`.

8. **`08_formato_ancho_y_largo.py` · Cambiar entre formato ancho y largo**
   - Principios del formato ordenado (*Tidy Data*).
   - Transformación de mediciones repetidas en el tiempo de ancho a largo con `pd.melt()`.
   - Resúmenes y matrices bidimensionales con `pivot()` y `pivot_table()` (usando `aggfunc` y márgenes).

9. **`09_integrar_flujo.py` · Integrar el flujo completo**
   - Ensamblaje de un pipeline de punta a punta: lectura con tipos -> diagnóstico -> limpieza
     -> transformación -> enriquecimiento relacional -> reporte de calidad y exportación.

---

## Cómo interactuar con cada cuaderno

Cada cuaderno está construido como una aplicación reactiva de **Marimo**:
- **Vista recomendada:** Cuaderno normal o vista de diapositivas (`slides`).
- **Ciclo didáctico:** Cada sección incluye una explicación conceptual detallada, ejemplos guiados
  ejecutables (*Worked Examples*), contraejemplos (*Non-examples*) que muestran errores comunes,
  un espacio de práctica interactiva (*TU TURNO*) y un coach automático.
- **Coach interactivo:** Al completar las variables requeridas en una celda de práctica, el Coach
  evaluará tu solución en tiempo real y te dará retroalimentación específica o pistas graduales.
