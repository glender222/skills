# Metodología de la RSL: PRISMA 2020 y Kitchenham y Charters

La revista no exige PRISMA ni Kitchenham en su guía. Los hallazgos de este módulo llevan la etiqueta `[METODOLOGÍA]`: representan lo que un revisor por pares evaluaría en una revisión sistemática, no un requisito editorial.

## Referencias

| Estándar | Referencia | Uso en esta revisión |
|---|---|---|
| PRISMA 2020 | Page MJ et al. (2021) BMJ 372:n71. https://doi.org/10.1136/bmj.n71 | Transparencia del reporte |
| PRISMA 2020 para resúmenes | Incluido en la misma publicación | Contenido del resumen |
| PRISMA-S | Rethlefsen ML et al. (2021) Syst Rev 10:39. https://doi.org/10.1186/s13643-020-01542-z | Documentación de la búsqueda |
| Kitchenham y Charters | Informe técnico EBSE-2007-01 (2007) | Orientación metodológica |
| SEGRESS | Guía de reporte de estudios secundarios en ingeniería de software | Complementaria. Sus datos bibliográficos se verifican en el `.bib` del manuscrito antes de citarla |

**Regla:** este archivo no amplía la lista de referencias del manuscrito. Si un hallazgo requiere citar un estándar que no está en el `.bib`, el hallazgo lo indica y los autores verifican la referencia.

---

## A. Lista de comprobación PRISMA 2020 (27 ítems)

Para cada ítem, localizar dónde lo reporta el manuscrito (sección y línea). Si no aparece, el hallazgo es `MAYOR`, salvo que la columna «Nota» diga otra cosa.

| Ítem | Sección | Qué debe constar | Nota |
|---|---|---|---|
| 1 | Título | Identificación como revisión sistemática | También es regla del curso (C-01) |
| 2 | Resumen | Ver la lista de la sección B | Debe caber en 150–250 palabras (R-13) |
| 3 | Justificación | Revisión en el contexto del conocimiento existente | El vacío frente a revisiones previas |
| 4 | Objetivos | Objetivos o preguntas explícitos | Pregunta principal y RQ |
| 5 | Elegibilidad | Criterios de inclusión y exclusión, y cómo se agrupan los estudios para la síntesis | |
| 6 | Fuentes de información | Bases, otras fuentes y fecha de la última búsqueda | Con PRISMA-S: incidencias de cada plataforma |
| 7 | Estrategia de búsqueda | Cadenas completas de todas las bases, con filtros y límites | Suele ir en un apéndice |
| 8 | Proceso de selección | Número de revisores, si trabajaron de forma independiente y herramientas de automatización | Uso de IA: ver `uso-ia.md` |
| 9 | Recolección de datos | Cómo se extrajeron los datos, revisores y herramientas de automatización | |
| 10a/b | Variables | Resultados buscados y otras variables; supuestos ante datos faltantes | |
| 11 | Riesgo de sesgo | Instrumento, revisores e independencia | En ingeniería de software suele ser la evaluación de calidad |
| 12 | Medidas de efecto | Medidas por resultado | |
| 13a–f | Métodos de síntesis | Elegibilidad para cada síntesis, preparación de datos, tabulación, métodos, heterogeneidad y sensibilidad | |
| 14 | Sesgo de reporte | Evaluación del riesgo por resultados faltantes | Suele omitirse; se observa como MAYOR |
| 15 | Certeza | Método para evaluar la certeza de la evidencia | Suele omitirse; se observa como MAYOR |
| 16a | Selección | Resultados de la búsqueda y la selección, idealmente con diagrama de flujo | |
| 16b | Selección | Estudios que parecían cumplir los criterios pero se excluyeron, con su motivo | |
| 17 | Características | Cita y características de cada estudio incluido | |
| 18 | Riesgo de sesgo | Resultado por estudio | Calidad por estudio |
| 19 | Resultados individuales | Por resultado y por estudio | |
| 20a–d | Resultados de síntesis | Características de los estudios aportantes, resultados, heterogeneidad y sensibilidad | |
| 21 | Sesgos de reporte | Resultado de la evaluación | Va con el ítem 14 |
| 22 | Certeza | Resultado de la evaluación | Va con el ítem 15 |
| 23a–d | Discusión | Interpretación, limitaciones de la evidencia, limitaciones del proceso e implicaciones | |
| 24a–c | Registro | Registro o su ausencia, acceso al protocolo, y enmiendas | Si hubo enmiendas tras la extracción, se declaran |
| 25 | Apoyo | Fuentes de financiamiento | Coincide con R-21 |
| 26 | Intereses | Intereses en conflicto | Coincide con R-20 |
| 27 | Disponibilidad | Formularios, datos extraídos, código y otros materiales | Coincide con R-23 |

## B. Resumen según PRISMA 2020 para resúmenes (12 ítems)

1. Identificación como revisión sistemática.
2. Objetivos.
3. Criterios de elegibilidad.
4. Fuentes y fecha de la última búsqueda.
5. Método de evaluación del riesgo de sesgo.
6. Método de síntesis.
7. Estudios incluidos (número y características).
8. Resultados de la síntesis.
9. Limitaciones de la evidencia.
10. Interpretación.
11. Financiamiento.
12. Registro.

Los ítems 11 y 12 suelen faltar en resúmenes de revistas de ingeniería. Su ausencia se reporta como `MENOR`, porque compite con el límite de 250 palabras de la revista. Un recorte del resumen debe conservar los ítems 1, 2, 7, 8 y 9.

## C. Kitchenham y Charters: fases y comprobaciones

| Fase | Actividad | Qué comprobar en el manuscrito |
|---|---|---|
| Planificación | Necesidad de la revisión | Revisiones previas identificadas y su cobertura, sin afirmar ausencias no comprobadas |
| Planificación | Preguntas de investigación | Pregunta principal y RQ trazables al marco PICO o PICOC |
| Planificación | Protocolo | Si se congeló antes de ejecutar; enmiendas con fecha y motivo |
| Ejecución | Identificación | Cadenas, bases y validación de la búsqueda frente a un conjunto de referencia (cuasi-sensibilidad) |
| Ejecución | Selección | Criterios, doble revisión y concordancia |
| Ejecución | Calidad | Instrumento, umbral fijado antes de puntuar y uso de la calidad en la síntesis |
| Ejecución | Extracción | Formulario definido antes de extraer y control de la extracción |
| Ejecución | Síntesis | Método declarado y separación entre lo reportado, lo calculado y lo interpretado |
| Reporte | Amenazas a la validez | Clasificación (constructo, interna, externa, fiabilidad) con su mitigación |

## D. Comprobaciones de calidad del razonamiento

Estas comprobaciones aplican los principios del proyecto. Su severidad es `MAYOR` cuando afectan a una conclusión.

- **Proporciones con su denominador.** Cada cifra de la síntesis tiene su denominador y coincide con las tablas y apéndices.
- **Recuentos coherentes.** Los recuentos del flujo suman igual en el texto, en la tabla del flujo, en la figura PRISMA y en la sábana (ver `[COHERENCIA]`).
- **Sin causalidad indebida.** Las conclusiones no afirman causalidad a partir de asociaciones entre estudios.
- **Hipótesis como hipótesis.** Una hipótesis de trabajo no se presenta como hallazgo.
- **Ausencias comprobadas.** «Ningún estudio» y «no se ha identificado» están respaldados por la extracción.
- **Corpus y citas contextuales separados.** Los estudios del corpus se distinguen de las citas contextuales.
- **Fechas solo donde aportan.** Las enmiendas posteriores a la extracción se declaran. La narración cronológica fuera del registro de enmiendas se reporta como `[EQUIPO]` (ver `curso-requisitos.md`, E-01).

## E. Coherencia artículo–sábana

Solo aplica si se proporcionó la sábana.

| ID | Comprobación | Hoja de la sábana | Sev. |
|---|---|---|---|
| K-01 | Recuentos del flujo de selección (identificados, cribados, excluidos, no recuperados, evaluados, incluidos) | X7 PRISMA | MAYOR |
| K-02 | Número de estudios incluidos y sus identificadores | ARTICULOS SELECCIONADOS | MAYOR |
| K-03 | Puntuaciones de calidad citadas en el texto (media, mínimo, umbral) | Preguntas de Calidad - Final | MAYOR |
| K-04 | Usos de IA declarados frente a registrados | X6 Uso de IA | MAYOR |
| K-05 | Ecuación de búsqueda y recuentos por base | Control de Búsqueda | MAYOR |

**Si las fechas no coinciden.** Si la versión de la sábana es anterior a cambios que el artículo describe, cada discrepancia se reporta como `VERIFICAR`, con la fecha de cada fuente. No se reporta como error mientras no se confirme cuál es la versión vigente.
