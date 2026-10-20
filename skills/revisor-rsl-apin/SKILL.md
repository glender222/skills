---
name: revisor-rsl-apin
description: Revisor previo al envío de la revisión sistemática (RSL) sobre perturbaciones proactivas a la revista Applied Intelligence (Springer, ISSN 1573-7497). Verifica el manuscrito LaTeX (sn-jnl) contra los requisitos de la revista, la plantilla de Springer Nature, PRISMA 2020 y Kitchenham y Charters, los requisitos del curso Investigación III y la coherencia con la sábana de la RSL; produce un informe de hallazgos con fuente, evidencia y severidad, y solo tras aprobación aplica o entrega las correcciones mecánicas. Úsala siempre que se pida revisar, auditar, chequear o preparar el artículo de la RSL para Applied Intelligence o para su envío, comprobar si cumple los requisitos de la revista o del curso, revisar el .tex, las declaraciones, el resumen, las figuras, las referencias, el uso de IA o la coherencia artículo–sábana, aunque no se nombre la revista ni la skill.
---

# Revisor de la RSL para Applied Intelligence

Esta skill revisa el manuscrito de la RSL antes de enviarlo a Applied Intelligence. Produce un **diagnóstico**: un informe de hallazgos. Las correcciones se aplican **solo después de que el usuario apruebe** el informe, y solo las mecánicas.

## Qué hace y qué no hace

| Hace | No hace |
|---|---|
| Comprueba el `.tex`, el `.bib` y las figuras contra los requisitos de cada fuente | Decidir conflictos entre fuentes (revista frente a curso): los reporta |
| Separa hallazgos verificados de interpretaciones y de lo no verificable | Redactar declaraciones (financiamiento, conflictos, contribuciones) con hechos que el usuario no ha dado |
| Contrasta el artículo con la sábana (`.xlsx`) cuando está disponible | Inventar DOI, cifras, autores ni características de los estudios |
| Tras aprobación, aplica cambios mecánicos o entrega un prompt para el agente LaTeX | Aplicar cambios de contenido sin aprobación expresa |

## Principios de la revisión

Aplican a todo el informe:

1. **Evidencia o nada.** Cada hallazgo cita archivo y línea, celda de la sábana o URL del requisito. Si no se puede comprobar, se escribe «No verificable con la evidencia proporcionada».
2. **Tres niveles de certeza.** Cada hallazgo se marca como:
   - `HECHO`: comprobado en el archivo;
   - `INTERPRETACIÓN`: el requisito admite más de una lectura;
   - `NO VERIFICABLE`: falta el archivo o el dato.
3. **La fuente se declara.** Cada hallazgo lleva una etiqueta: `[REVISTA]`, `[PLANTILLA]`, `[METODOLOGÍA]`, `[CURSO]`, `[EQUIPO]`, `[IA]` o `[COHERENCIA]`. Un incumplimiento del curso no es un incumplimiento editorial, y viceversa.
4. **Los conflictos no se resuelven en silencio.** Si dos fuentes exigen cosas incompatibles, se reportan ambas con la consecuencia de cada opción, y la decisión queda para el usuario.
5. **Las premisas del usuario se examinan.** Si una indicación del usuario contradice la evidencia de los archivos, el informe lo señala con la evidencia.
6. **Tono técnico e impersonal.** Sin valoraciones sobre el trabajo ni sobre el equipo.

## Entradas

Antes de empezar, hay que localizar:

- **Manuscrito principal `.tex`** (obligatorio). Si hay varios, el que contiene `\documentclass`.
- **`.bib` o `.bbl`, y las figuras**: en el mismo directorio o en el que indique el usuario.
- **Sábana `sabana_RSL_v*.xlsx`** (opcional). Habilita los chequeos de coherencia y de uso de IA.
- **Ficha del tema `.docx`** (opcional). Solo para los chequeos del curso.
- **Carta de presentación** (opcional). Es lo primero que leen los editores junto con el resumen, la conclusión y las referencias (CK-01). Si no se proporciona, CK-01 sale como `NO VERIFICABLE` y se pregunta por ella.

Si falta el `.tex`, la revisión se detiene y se pide. Si falta otro archivo, los chequeos que dependen de él salen como `NO VERIFICABLE` y la revisión continúa.

## Flujo

### Fase 1 — Chequeo automático

Ejecutar desde la carpeta de la skill:

```bash
python3 scripts/check_tex.py RUTA/articulo.tex --root RUTA/ --json hallazgos_auto.json
```

`--root` es la carpeta del envío; con ella el script comprueba las figuras y el `.bib`. El script imprime una tabla de hallazgos con su identificador. Cubre lo que se puede comprobar sin juicio:

- clase y opciones de `sn-jnl`, `\input`, subcarpetas;
- longitud y citas en el resumen, número de palabras clave;
- autor de correspondencia, correo y ORCID;
- niveles de encabezado, notas al pie, leyendas de figura;
- orden de primera cita de figuras y tablas, sección de declaraciones;
- notas pendientes de los autores, idioma, fechas en el cuerpo;
- coherencia de las claves de cita con el `.bib`.

Si hay sábana, ejecutar también:

```bash
python3 scripts/sabana_dump.py RUTA/sabana.xlsx --sheets "X6 Uso de IA" "X7 PRISMA" --json sabana.json
```

La salida vuelca las hojas como datos. Si una celda tiene fórmula sin valor calculado, el volcado muestra la fórmula. En ese caso la cifra se marca `NO VERIFICABLE` salvo que se recalcule, por ejemplo abriendo y guardando el libro en LibreOffice.

Un hallazgo del script es un `HECHO` sobre el texto, pero su severidad final la fija la Fase 2. Por ejemplo, una fecha en el cuerpo es un hecho; que constituya «narración cronológica» es una interpretación.

### Fase 2 — Revisión con criterio, por módulo

Leer solo el archivo de referencia del módulo que se está revisando:

| Módulo | Archivo | Cuándo |
|---|---|---|
| Revista | `references/apin-requisitos.md` | Siempre |
| Plantilla LaTeX | `references/plantilla-snjnl.md` | Siempre (preparación del envío) |
| Metodología RSL | `references/rsl-metodologia.md` | Siempre que se revise el contenido, no solo el formato |
| Curso | `references/curso-requisitos.md` | Cuando el entregable también se evalúa en el curso |
| Uso de IA | `references/uso-ia.md` | Siempre; con sábana, contrastando la hoja X6 |

Por cada requisito del archivo de referencia:

1. Buscar la evidencia en el manuscrito, o en la salida del script si ya la cubre.
2. Registrar el hallazgo **solo si hay incumplimiento, ambigüedad o falta de evidencia**. Los cumplimientos se resumen en una línea por módulo, sin listarlos uno a uno.
3. Asignar la severidad:

| Severidad | Criterio |
|---|---|
| `BLOQUEANTE` | La revista devuelve el envío o lo rechaza sin revisión. Por ejemplo, falta la sección de declaraciones, el idioma no es aceptado o faltan las fuentes editables. |
| `MAYOR` | Un revisor lo observaría con probabilidad alta o compromete la validez. Por ejemplo, un ítem PRISMA sin reportar o cifras del artículo que no coinciden con la sábana. |
| `MENOR` | Formato o estilo que la producción corrige o que no altera la evaluación. |
| `VERIFICAR` | No se puede decidir con la evidencia disponible; se indica qué comprobar y dónde. |

### Fase 3 — Informe

Usar siempre esta estructura:

```markdown
# Revisión previa al envío — Applied Intelligence
Fecha: AAAA-MM-DD · Manuscrito: <archivo> · Sábana: <archivo o «no proporcionada»>
Requisitos verificados el: <fecha de verificación de references/apin-requisitos.md>

## Resumen
| Severidad | [REVISTA] | [PLANTILLA] | [METODOLOGÍA] | [CURSO] | [EQUIPO] | [IA] | [COHERENCIA] |
(conteo por celda)

## Bloqueantes
| ID | Fuente | Certeza | Evidencia (archivo:línea) | Requisito (ID y URL) | Corrección propuesta | Tipo de corrección |

## Mayores
(misma tabla)

## Menores
(misma tabla, agrupada si son repetitivos)

## A verificar
| ID | Qué comprobar | Dónde | Por qué no se pudo decidir |

## Conflictos entre fuentes
| Tema | Fuente A exige | Fuente B exige | Consecuencia de cada opción |

## Preguntas para los autores
(preguntas precisas, una por dato faltante)

## Módulos sin hallazgos
(una línea por módulo)
```

En la columna «Tipo de corrección» se usa uno de estos valores:

- `MECÁNICA`: se puede aplicar sin decidir contenido; por ejemplo, la opción de clase, el punto final de una leyenda o una ruta de figura.
- `CONTENIDO`: requiere decidir o redactar contenido; por ejemplo, el resumen, la discusión o la traducción.
- `DATO DEL AUTOR`: requiere un hecho que solo los autores conocen; por ejemplo, financiamiento, conflictos o contribuciones.

Terminar el informe con: «Indicar qué hallazgos se aprueban para corregir». **No aplicar nada en este turno.**

### Fase 4 — Corrección, solo tras aprobación

Aplicar únicamente los hallazgos que el usuario apruebe por ID.

- **`MECÁNICA`**:
  - Si el entorno tiene acceso al `.tex` (Claude Code, Codex), editar el archivo, compilar si hay `pdflatex` disponible y reportar el resultado.
  - Si no hay acceso, entregar un **prompt para el agente LaTeX del usuario** con el formato de abajo.
- **`CONTENIDO`**: entregar una propuesta de texto marcada como «borrador, requiere validación de los autores», junto al texto actual. Las cifras, citas o DOI que no estén en el manuscrito o en la sábana no se introducen.
- **`DATO DEL AUTOR`**: no se redacta. Se formula la pregunta precisa y, si existe, se indica la redacción modelo de la revista con los huecos marcados `[COMPLETAR]`.

Formato del prompt para el agente LaTeX:

````markdown
Aplica en `<archivo.tex>` los siguientes cambios, en este orden. No modifiques nada más.

1. [ID] <descripción>
   Buscar (texto exacto):
   ```latex
   <fragmento actual>
   ```
   Reemplazar por:
   ```latex
   <fragmento nuevo>
   ```

Al terminar: compila con pdflatex + bibtex + pdflatex ×2 y reporta errores y advertencias nuevas.
````

Después de corregir, volver a ejecutar `check_tex.py` y reportar qué hallazgos quedaron cerrados.

## Vigencia de los requisitos

Los requisitos de la revista se verificaron en la fecha que figura al inicio de `references/apin-requisitos.md`.

- **Más de 90 días desde la verificación:** antes de revisar, volver a consultar la página de *Submission guidelines* y registrar los cambios en el archivo.
- **Sin acceso web:** indicar en el informe la fecha de verificación usada.

## Compatibilidad

La carpeta sigue el estándar abierto de agent skills (`SKILL.md` con `name` y `description`, más `scripts/` y `references/`), así que se instala igual en Claude y en Codex. Los scripts requieren Python 3.9 o superior; `sabana_dump.py` requiere además `openpyxl`.
