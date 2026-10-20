# Requisitos de Applied Intelligence (Springer)

**Verificado el:** 2026-10-20
**ISSN electrónico:** 1573-7497 · **ISSN impreso:** 0924-669X
**Revisión por pares:** single-anonymous
**Envío:** Editorial Manager (https://www.editorialmanager.com/apin)

## Fuentes

| Código | URL |
|---|---|
| SG | https://link.springer.com/journal/10489/submission-guidelines |
| AS | https://link.springer.com/journal/10489/aims-and-scope |
| ED | https://link.springer.com/journal/10489/ethics-and-disclosures |

## Cómo se usa este archivo

- La columna **Chequeo** indica cómo se verifica cada requisito: `script` lo cubre `check_tex.py` (entre paréntesis, el identificador del chequeo), `juicio` requiere leer el manuscrito y `externo` requiere un dato o una comprobación fuera de los archivos.
- La columna **Sev.** es la severidad por defecto; la Fase 2 puede ajustarla con justificación.
- La columna **Certeza** indica de dónde sale el requisito:
  - `explícito`: está escrito en la guía;
  - `inferido`: se deduce de la guía o de la práctica de la revista, pero no está escrito como exigencia.

---

## 1. Idioma, alcance y tipo de artículo

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-01 | Manuscrito en inglés | SG | **inferido** | script (T10) | BLOQUEANTE |
| R-02 | Encaje en el alcance: la revista pone el énfasis en investigación nueva, original e innovadora más que en aplicar tecnologías existentes a otros datos | AS | explícito | juicio | MAYOR |
| R-03 | Que la revista acepte artículos de revisión | — | **no verificado** | externo | VERIFICAR |

**Notas:**

- **R-01.** La guía no declara el idioma como exigencia. Sí ofrece servicios de edición en inglés y todos los artículos de la portada están en inglés. Se reporta como `INTERPRETACIÓN` con severidad BLOQUEANTE, porque enviar en otro idioma tiene alta probabilidad de rechazo sin revisión.
- **R-02.** El alcance lista explícitamente *privacy preserving systems*. Para una RSL, la pregunta que debe responderse es qué conocimiento nuevo aporta la síntesis. El argumento del vacío en la introducción es la evidencia que se evalúa.
- **R-03.** La guía no lista tipos de artículo. Se comprueba en el desplegable de tipo de artículo de Editorial Manager o con la oficina editorial.

## 2. Envío y archivos fuente

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-04 | Entregar todas las fuentes editables (LaTeX con estilos y figuras) y el PDF compilado. Sin el conjunto completo, el artículo no se considera para revisión | SG | explícito | juicio | BLOQUEANTE |
| R-05 | El envío LaTeX no usa subcarpetas, ni para figuras ni para la bibliografía | SG | explícito | script (T03) | BLOQUEANTE |
| R-06 | Material ya publicado (figuras, tablas, texto): permiso del titular para impresión y en línea, con evidencia adjunta | SG | explícito | juicio | MAYOR |

## 3. Página de título

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-07 | Título conciso e informativo | SG | explícito | juicio | MENOR |
| R-08 | Nombre de los autores y afiliación completa: institución, departamento, ciudad, país | SG | explícito | script (T06) + juicio | MAYOR |
| R-09 | Autor de correspondencia indicado con claridad y con correo activo | SG | explícito | script (T06) | BLOQUEANTE |
| R-10 | ORCID de 16 dígitos de cada autor, si lo tiene | SG | explícito | script (T06) | MENOR |
| R-11 | Agradecimientos en sección separada; organismos financiadores con su nombre completo | SG | explícito | juicio | MENOR |
| R-12 | Declaración de contribución de los autores. En artículos de revisión debe indicar quién tuvo la idea, quién hizo la búsqueda y el análisis, y quién redactó o revisó críticamente | SG | explícito | juicio | MAYOR |

## 4. Resumen y palabras clave

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-13 | Resumen de 150 a 250 palabras | SG | explícito | script (T04) | MAYOR |
| R-14 | Resumen sin abreviaturas no definidas ni referencias | SG | explícito | script (T04) + juicio | MAYOR |
| R-15 | Entre 4 y 6 palabras clave | SG | explícito | script (T05) | MAYOR |

## 5. Texto

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-16 | Encabezados con numeración decimal y como máximo tres niveles | SG | explícito | script (T07) | MENOR |
| R-17 | Abreviaturas definidas en su primera mención y usadas de forma consistente | SG | explícito | juicio | MENOR |
| R-18 | Notas al pie: no consisten solo en una cita, nunca contienen datos bibliográficos ni figuras o tablas; se usan notas al pie, no notas finales | SG | explícito | script (T13) | MENOR |

## 6. Declaraciones

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-19 | Sección «Statements and Declarations». Sin las declaraciones relevantes, el envío se devuelve como incompleto | SG | explícito | script (T08) | BLOQUEANTE |
| R-20 | *Competing interests* (intereses financieros y no financieros). Obligatoria también en artículos de revisión | SG | explícito | script (T08) + dato del autor | BLOQUEANTE |
| R-21 | *Funding*, con financiador y número de subvención; o la declaración de que no hubo financiamiento | SG | explícito | script (T08) + dato del autor | MAYOR |
| R-22 | Otras declaraciones: aprobación ética, consentimiento, disponibilidad de datos, materiales y código, y contribución de los autores | SG | explícito | script (T08) | MAYOR |
| R-23 | Declaración de disponibilidad de datos. Es obligatoria para la «investigación original»; su aplicación a una revisión no está escrita | SG | inferido | juicio | MAYOR |
| R-24 | Uso de LLM documentado en Métodos. El *copy editing* asistido no se declara (ver `uso-ia.md`) | SG | explícito | juicio | MAYOR |

## 7. Referencias

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-25 | Citas en el texto con números entre corchetes | SG | explícito | script (T01: opción `Numbered`) | MAYOR |
| R-26 | La lista incluye solo obras citadas y publicadas o aceptadas. Las comunicaciones personales y los trabajos no publicados se mencionan solo en el texto | SG | explícito | script (T14) + juicio | MAYOR |
| R-27 | Lista numerada de forma consecutiva | SG | explícito | estilo `.bst` | MENOR |
| R-28 | DOI como enlace completo (`https://doi.org/...`) siempre que exista | SG | explícito | script (T14) | MENOR |
| R-29 | Revistas abreviadas según la ISSN LTWA; si hay duda, título completo | SG | explícito | juicio | MENOR |
| R-30 | Formato de referencia tipo Springer Basic: «Autores (Año) Título. Revista vol:págs. DOI» | SG | explícito | script (T01) | MENOR |
| R-31 | Evitar la autocitación excesiva o coordinada | SG | explícito | juicio | MENOR |

**Nota sobre R-26.** Las preimpresiones (arXiv) no son «publicadas o aceptadas» en sentido editorial estricto. Es `INTERPRETACIÓN`: se reportan las entradas de preimpresión para que los autores decidan si citan la versión editorial cuando exista.

## 8. Tablas

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-32 | Numeración arábiga; citadas en el texto en orden consecutivo | SG | explícito | script (T12) | MENOR |
| R-33 | Cada tabla con título que explique sus componentes | SG | explícito | juicio | MENOR |
| R-34 | Material ya publicado identificado con la referencia al final del título de la tabla | SG | explícito | juicio | MAYOR |
| R-35 | Notas de tabla con letras minúsculas en superíndice (asteriscos para significancia) | SG | explícito | juicio | MENOR |

## 9. Figuras

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-36 | Numeración arábiga; citadas en orden consecutivo; partes indicadas con a, b, c | SG | explícito | script (T12) | MENOR |
| R-37 | Leyenda que empieza con «Fig.» en negrita y número, sin puntuación tras el número ni al final de la leyenda | SG | explícito | script (T11: punto final) | MENOR |
| R-38 | Leyenda que identifica todos los elementos de la figura; material ya publicado citado al final | SG | explícito | juicio | MENOR |
| R-39 | Formato: EPS para vectores, TIFF para tonos continuos (MS Office aceptado); fuentes incrustadas; archivos nombrados `Fig1.eps` | SG | explícito | script (T03: extensión) | MENOR |
| R-40 | Resolución mínima: 1200 dpi línea, 300 dpi tonos continuos, 600 dpi combinada; líneas de al menos 0,1 mm | SG | explícito | externo | MENOR |
| R-41 | Color en RGB de 8 bits; si se imprime en blanco y negro, la información debe seguir distinguiéndose | SG | explícito | externo | MENOR |
| R-42 | Rotulación en Helvetica o Arial, de 8 a 12 pt y consistente; sin títulos dentro de la figura | SG | explícito | externo | MENOR |
| R-43 | Ancho de columna: 84 o 174 mm y alto máximo de 234 mm (revistas grandes), o 119 × 195 mm (revistas pequeñas). No consta qué formato tiene Applied Intelligence | SG | **no verificado** | externo | VERIFICAR |
| R-44 | Accesibilidad: leyenda descriptiva, patrones además del color y contraste mínimo de 4.5:1 en los rótulos | SG | explícito | juicio | MENOR |
| R-45 | Imágenes generadas con IA: según la política de Springer sobre imágenes generativas | SG | explícito | juicio | MAYOR |

## 10. Material suplementario

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-46 | Citado en el texto como «Online Resource N»; archivos nombrados `ESM_N.ext`; cada uno con leyenda | SG | explícito | juicio | MENOR |
| R-47 | Cada archivo suplementario incluye el título del artículo, la revista, los autores, y la afiliación y el correo del autor de correspondencia | SG | explícito | externo | MENOR |
| R-48 | Texto en PDF; hojas de cálculo en `.csv` o `.xlsx` | SG | explícito | externo | MENOR |

## 11. Integridad y autoría

| ID | Requisito | Fuente | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-49 | Sin envío simultáneo a otra revista; transparencia sobre el reciclaje de texto propio | SG | explícito | externo | BLOQUEANTE |
| R-50 | Se aplica detección de plagio (Similarity Check / iThenticate) | ED | explícito | externo | MAYOR |
| R-51 | Investigación de doble uso: identificarla si puede usarse indebidamente | SG | explícito | juicio | VERIFICAR |
| R-52 | Grupo de autores, autor de correspondencia y orden fijados al enviar. No se aceptan cambios tras la aceptación | SG | explícito | externo | MAYOR |
| R-53 | La carta al editor informa del reuso de material y del material no publicado incluido | SG | explícito | externo | MENOR |
| R-54 | Revisores sugeridos: independientes, de países e instituciones distintos, con correo institucional | SG | explícito | externo | MENOR |
| R-55 | No hace falta anonimizar el manuscrito (revisión single-anonymous) | ED | explícito | — | — |

## 12. Requisitos añadidos tras el contraste sección por sección (2026-10-20)

| ID | Requisito | Sección de la guía | Certeza | Chequeo | Sev. |
|---|---|---|---|---|---|
| R-56 | Si se citan conjuntos de datos (por ejemplo, la matriz de extracción depositada), van en la lista de referencias con identificador persistente y los elementos DataCite: creador, título, repositorio, año e identificador | Research Data Policy | explícito | juicio | MENOR |
| R-57 | Se recomienda depositar los datos en un repositorio público; los autores deben poder enviar los datos que sustentan los resultados si se les piden | Research Data Policy; Ethical Responsibilities | explícito | juicio | MAYOR |
| R-58 | *Competing interests* abarca los intereses de los últimos 3 años desde el inicio del trabajo (o de antes, si pueden percibirse como influyentes). Si todos los autores declaran lo mismo, basta una declaración conjunta | Competing Interests | explícito | dato del autor | MAYOR |
| R-59 | La información de financiamiento también se registra en el formulario del sistema de envío, además de en las declaraciones | Competing Interests | explícito | externo | MENOR |
| R-60 | Las notas al pie del título o de los autores no llevan símbolo de referencia | Text, Footnotes | explícito | juicio | MENOR |
| R-61 | Las figuras de un apéndice siguen la numeración del texto principal (no A1, A2); las del material suplementario se numeran aparte | Artwork, Figure Numbering | explícito | juicio | MENOR |
| R-62 | Las figuras se envían dentro del cuerpo del texto, salvo que el tamaño del archivo lo impida | Artwork, Figure Placement | explícito | juicio | MENOR |
| R-63 | Los cuatro criterios de autoría se cumplen para **cada** autor, incluido el asesor: contribución sustancial, redacción o revisión crítica, aprobación de la versión final y responsabilidad sobre el trabajo | Authorship principles | explícito | dato del autor | MAYOR |
| R-64 | No hacer afirmaciones falsas sobre una entidad (persona o empresa) ni descripciones que puedan leerse como ataques personales; aplica al juzgar los estudios del corpus | Ethical Responsibilities | explícito | juicio | MAYOR |
| R-65 | El sistema compila las fuentes LaTeX en un PDF que el autor debe aprobar al final del envío; ese PDF es el que se usa para la revisión | LaTeX and Online Submission | explícito | externo | BLOQUEANTE |
| R-66 | Sin fabricación, falsificación ni manipulación de datos o imágenes, y sin dividir un mismo estudio en varias publicaciones (*salami slicing*) | Ethical Responsibilities | explícito | juicio | BLOQUEANTE |

## 13. Fuera del alcance de la revisión previa al envío

No generan hallazgos. La skill los menciona solo si el usuario pregunta.

| Sección de la guía | Motivo |
|---|---|
| Editing Services | Es informativa; la guía dice que esos servicios no son un requisito |
| After acceptance | Ocurre después de la aceptación (pruebas, licencia, separatas, color impreso) |
| Open Choice y Open access publishing | Es una decisión de publicación (APC y financiamiento institucional), no un requisito de cumplimiento |
| Additional Information for Changes to authorship | Solo aplica si se cambia la autoría después del envío; R-52 cubre fijarla antes |
| Audio, vídeo y animaciones (SI) | No aplica a este manuscrito |
| Mistakes to avoid during manuscript preparation | Cubierta en la sección 14 a partir de la versión genérica de Springer Nature; la versión con `journalId=10489` bloquea la consulta automática |
| Publication and funding (checklist) | Decidir antes del envío entre acceso abierto con APC o suscripción. Es una decisión de publicación, no un requisito; se menciona en el informe como decisión pendiente si el usuario no la ha tomado |

## 14. Checklist previo al envío de Springer Nature («Get your manuscript ready»)

**Fuentes:** versión genérica en https://beta.springernature.com/pre-submission y sus subpáginas, consultada el 2026-10-20. La versión de la revista (https://link.springer.com/pre-submission?journalId=10489) no se pudo leer de forma automática; su equivalencia con la genérica es `INTERPRETACIÓN`.

| ID | Requisito | Página del checklist | Chequeo | Sev. |
|---|---|---|---|---|
| CK-01 | Los editores leen primero la carta de presentación, el resumen, la conclusión y las referencias para decidir el encaje. La carta debe justificar el encaje con el alcance (R-02) y el aporte | What editors look for | juicio (carta, si se proporciona) | MAYOR |
| CK-02 | La investigación aporta conocimiento nuevo a un área activa; en una RSL, la conclusión debe enunciar el aporte de la síntesis, no solo resumir | What editors look for | juicio | MAYOR |
| CK-03 | Redacción clara y concisa | What editors look for; Language editing | juicio | MAYOR |
| CK-04 | Confirmar que la revista acepta el tipo de manuscrito (coincide con R-03) | Choosing a journal | externo | VERIFICAR |
| CK-05 | Comprobar los límites de palabras o caracteres del título, del título corto (*running title*), del resumen y del texto. La guía de Applied Intelligence solo fija el del resumen | Submission guidelines | script (T04) + juicio | VERIFICAR |
| CK-06 | Estructura simple con Título, Resumen, Introducción, Métodos, Resultados y Discusión; la guía de la revista prevalece | Structure and layout | juicio | MENOR |
| CK-07 | Cada figura y tabla con leyenda, citada en el texto y numerada de forma consistente con sus menciones (coincide con R-32, R-36 y T12) | Figures and tables | script (T12) | MENOR |
| CK-08 | Tablas con unidades claras, espaciado suficiente y tipografía legible | Figures and tables | script (T18) + juicio | MENOR |
| CK-09 | Incluir todas las declaraciones requeridas; enviar sin ellas es un error que el checklist señala (coincide con R-19 a R-22) | Editorial policies | script (T08) | BLOQUEANTE |
| CK-10 | Archivos en los formatos aceptados (coincide con R-04 y R-39) | Submission guidelines | script (T03) | MAYOR |

**Herramienta Curie.** El checklist ofrece una herramienta de IA (Curie) para editar el idioma. Usarla solo para gramática y estilo es *copy editing* según IA-03; usarla para traducir no lo es (ver `uso-ia.md`).

**Nota sobre R-51.** Las perturbaciones proactivas y sus contramedidas pueden leerse como técnicas de envenenamiento de datos y como formas de romper protecciones. Que exijan una declaración de doble uso es `INTERPRETACIÓN`; se reporta para que los autores decidan.

---

## Inconsistencias internas de la guía

No se resuelven por defecto: se reportan junto con la opción que recomienda `plantilla-snjnl.md`.

| ID | Inconsistencia | Evidencia |
|---|---|---|
| I-01 | La guía recomienda la plantilla Springer Nature (`sn-jnl`) y, en otra sección, el paquete macro de Springer con la opción «smallcondensed», que pertenece a `svjour3` (v3.2, 2007) | SG, secciones «Text» y «Author tools» |
| I-02 | El encabezado de las declaraciones aparece con tres nombres: «Statements and Declarations», «Declarations» antes de las referencias y «Compliance with Ethical Standards» | SG |
| I-03 | Los agradecimientos se piden en la página de título, pero `sn-jnl` los sitúa en `\backmatter` | SG frente a la plantilla |
| I-04 | La declaración de disponibilidad de datos es obligatoria para la «investigación original»; no se dice si aplica a revisiones | SG |
