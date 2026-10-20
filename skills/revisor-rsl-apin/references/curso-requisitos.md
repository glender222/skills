# Requisitos del curso (Investigación III, UPeU) y reglas del equipo

**Actualizado:** 2026-10-20

## Fuentes

- Documento del proyecto `marco_del_curso.md` (29 de septiembre de 2026).
- Indicaciones del equipo registradas hasta el 19 de octubre de 2026.

**Limitación.** No se dispone de la rúbrica de evaluación del curso. Este archivo reconstruye las exigencias a partir de las reglas del docente y de las decisiones del equipo. Los hallazgos `[CURSO]` no son requisitos de la revista.

---

## Reglas del docente (`[CURSO]`)

| ID | Regla | Cómo se comprueba | Sev. |
|---|---|---|---|
| C-01 | Tras los dos puntos del título, solo «una revisión sistemática de la literatura» | `\title` | MAYOR |
| C-02 | Título con sustantivos orientados a la búsqueda técnica, y con la variable problema y el área explícitas | `\title` | MENOR |
| C-03 | La pregunta principal es el título convertido en interrogación, término a término | Introducción y Métodos | MAYOR |
| C-04 | Entre seis y siete preguntas secundarias (máximo siete) | Tabla de RQ | MAYOR |
| C-05 | Mínimo 30 estudios incluidos; objetivo del equipo: 30 a 35 | Flujo de selección | MAYOR |
| C-06 | Diagrama PRISMA «de Kitchenham» con cuatro componentes o fases (identificación, cribado, elegibilidad, inclusión) | Figura del flujo | MAYOR |
| C-07 | Análisis bibliométrico con **Bibliometrix/Biblioshiny**, después del PRISMA y de las preguntas | Sección de análisis bibliométrico: herramienta declarada | MAYOR |
| C-08 | Pregunta PICO en la introducción | Introducción | MAYOR |
| C-09 | La pregunta principal se responde con **una sola tabla** que reúne todos los artículos | Resultados: respuesta a la pregunta principal | MAYOR |
| C-10 | No filtrar por acceso abierto ni solo por inglés (IN7 admite inglés y español) | Criterios y filtros | MAYOR |
| C-11 | TMLR no cuenta como revista (cubierto por el DOI obligatorio) | Criterios | MENOR |

## Reglas del equipo (`[EQUIPO]`)

| ID | Regla | Cómo se comprueba | Sev. |
|---|---|---|---|
| E-01 | No narrar el proceso de forma cronológica («parece bitácora»): se declara el resultado final. Las fechas solo se admiten donde PRISMA las exige (fecha de búsqueda, enmiendas del protocolo con fecha y motivo) | `check_tex.py` (T17) + juicio sobre cada fecha | MAYOR |
| E-02 | Los documentos principales (sábana, ficha y artículo) no incluyen historial ni registro de versiones, ni referencian versiones pasadas | Juicio: expresiones como «la versión del 4 de octubre», «antes de la revisión», «respecto de la selección del…» | MAYOR |
| E-03 | Los entregables no llevan correcciones pendientes ni recomendaciones. En el `.tex`, las notas «NOTA PARA LOS AUTORES» y los «Pendiente» deben estar resueltos antes del envío | `check_tex.py` (T09) | BLOQUEANTE para el envío |
| E-04 | La sábana es la fuente de verdad. Ante una discrepancia prevalece sobre la ficha y el artículo, salvo que la sábana sea más antigua que el cambio descrito (ver `rsl-metodologia.md` §E) | Coherencia | MAYOR |
| E-05 | Terminología fijada: «ejemplos adversariales» (forma única), «reversibilidad» frente a «reversibilidad autorizada», «ejemplos no aprendibles» con el término inglés en la primera mención | Búsqueda de variantes | MENOR |
| E-06 | Nunca escribir «ninguna revisión cubre X»: se formula como lo no identificado, con el material de comprobación | Búsqueda de la expresión | MAYOR |

---

## Conflictos conocidos entre el curso y la revista

Se reportan siempre en la tabla «Conflictos entre fuentes» del informe. La decisión es de los autores.

| Tema | Curso o equipo | Revista | Consecuencia |
|---|---|---|---|
| Idioma | El curso trabaja en español | Inglés (R-01, inferido) | Dos versiones del manuscrito, o una sola en inglés para ambos destinos (confirmar con el docente) |
| Herramienta bibliométrica | Bibliometrix/Biblioshiny (C-07) | Sin exigencia | Si el artículo usa otra herramienta, cumple con la revista e incumple C-07 |
| Respuesta a la pregunta principal | Una sola tabla con todos los artículos (C-09) | Sin exigencia; las tablas largas suelen ir a material suplementario | La tabla puede ir en un apéndice o como *Online Resource* (R-46) |
| Resumen | Sin límite conocido | 150–250 palabras (R-13) | Un resumen extenso para el curso no cabe en la revista |
| Palabras clave | Sin límite conocido | Entre 4 y 6 (R-15) | Recortar |
| Fechas e historial | E-01 y E-02 piden declarar el resultado final | PRISMA 24c pide declarar las enmiendas | Las enmiendas se declaran en un único párrafo o tabla, sin narrar el proceso |
