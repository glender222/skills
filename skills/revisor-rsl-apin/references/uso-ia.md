# Uso de inteligencia artificial: requisitos y chequeo

**Verificado el:** 2026-10-20

## Fuentes

- **Springer.** Guía de Applied Intelligence, sección «Title Page» (párrafo sobre LLM): https://link.springer.com/journal/10489/submission-guidelines
- **Proyecto.** Declaración registro a registro conforme al *position statement* de Cochrane, Campbell, JBI y CEE (2025), citado en el manuscrito como `flemyng2025position`. Su referencia se verifica en el `.bib`; no se añade desde aquí.

---

## 1. Qué exige la revista

| ID | Requisito | Certeza |
|---|---|---|
| IA-01 | Un LLM no puede figurar como autor | explícito |
| IA-02 | El uso de un LLM se documenta en la sección de Métodos o, si no la hay, en otra parte adecuada | explícito |
| IA-03 | El *copy editing* asistido por IA no requiere declaración. Springer lo define como mejoras de legibilidad, estilo, gramática, ortografía, puntuación y tono de un texto escrito por humanos; no incluye trabajo editorial generativo ni creación autónoma de contenido | explícito |
| IA-04 | En todos los casos hay responsabilidad humana sobre el texto final | explícito |
| IA-05 | Las imágenes generadas con IA siguen la política de Springer sobre imágenes generativas | explícito |

## 2. Clasificación de cada uso

Para cada uso de IA, decidir en cuál de estos tres casos cae:

| Uso | ¿Se declara ante la revista? | Certeza de la clasificación |
|---|---|---|
| Cribado, elegibilidad, evaluación de calidad, arbitraje, extracción, codificación, deduplicación asistida, búsqueda asistida de candidatos | **Sí, en Métodos** (IA-02) | HECHO: es trabajo metodológico, no edición de estilo |
| Corrección de gramática y estilo de un texto escrito por los autores | No (IA-03) | HECHO |
| **Traducción** del manuscrito del español al inglés | **No definido por la guía** | INTERPRETACIÓN: la definición de *copy editing* no menciona la traducción, y traducir produce un texto nuevo en otro idioma |
| Redacción de secciones (resumen, discusión) a partir de notas o datos | Sí (IA-02) | HECHO: es creación de contenido |
| Revisión del manuscrito con esta skill | Solo si la revisión introduce contenido; las correcciones mecánicas de formato no lo requieren | INTERPRETACIÓN |

**Traducción.** Recomendación por defecto, marcada como recomendación: declararla en la sección de uso de IA. Declarar de más tiene un costo bajo; no declarar un uso que la revista considera generativo tiene un costo alto. La decisión final es de los autores.

## 3. Chequeo con la sábana (hoja X6)

Si se proporcionó la sábana:

1. Volcar la hoja X6 con `scripts/sabana_dump.py`.
2. Agrupar sus filas por propósito: cribado, elegibilidad, calidad, arbitraje, búsqueda, deduplicación, codificación o extracción, y auditoría.
3. Para cada grupo, comprobar que la sección de uso de IA del manuscrito lo menciona. Un grupo registrado en X6 que el manuscrito no menciona es un hallazgo `[IA]` MAYOR.
4. Comprobar que el manuscrito no presenta como concordancia entre investigadores el acuerdo entre dos configuraciones de IA.
5. Comprobar que declara qué ratificó el equipo humano y qué no.
6. Las filas de X6 con «No verificable con la evidencia proporcionada» (sesión, prompt o versión no conservados) deben figurar como limitación de reproducibilidad en las amenazas a la validez.
7. **Usos posteriores a la sábana.** Si se usó IA para traducir, redactar o revisar el artículo después de la última fila de X6, el hallazgo es `[IA]` VERIFICAR, con la pregunta: «¿Se registró en X6 el uso de IA para <tarea> con herramienta, versión, fecha, propósito e instrucción?».

Si no se proporcionó la sábana, se revisa solo la sección del manuscrito con los criterios de IA-02 e IA-03, y el contraste con X6 sale como `NO VERIFICABLE`.

## 4. Redacción mínima que debe contener la sección

Es una lista de contenido, no un texto para copiar:

- herramientas y versiones, o la constancia de que la versión no se conservó;
- fases en que se usaron;
- cómo se controló cada uso (revisores ciegos, arbitraje, ratificación);
- qué ratificaron los autores y qué no;
- dónde está el registro completo (material suplementario o repositorio);
- uso para traducción o edición, si lo hubo.
