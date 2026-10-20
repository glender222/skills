# Plantilla LaTeX de Springer Nature (`sn-jnl`) para Applied Intelligence

**Verificado el:** 2026-10-20

## Fuentes

| Código | Documento | URL |
|---|---|---|
| LS | LaTeX Author Support | https://www.springernature.com/gp/authors/campaigns/latex-author-support |
| OL | Plantilla oficial en Overleaf, versión 3.1 (diciembre de 2024) | https://www.overleaf.com/latex/templates/springer-nature-latex-template/gsvvftmrppwq |
| SG | Guía para autores de Applied Intelligence | https://link.springer.com/journal/10489/submission-guidelines |

---

## Plantilla recomendada (resuelve I-01)

Se recomienda `sn-jnl`, por cuatro motivos:

- **Vigencia.** `sn-jnl` es la plantilla de Springer Nature con versión de diciembre de 2024. `svjour3` es la clase v3.2 de 2007.
- **Ámbito.** La plantilla sirve para cualquier revista de Springer Nature, incluidas las de Springer (LS).
- **Coherencia con la guía.** La guía de la revista nombra el estilo `sn-basic.bst`, que se distribuye con `sn-jnl` (SG).
- **Referencias numeradas.** La plantilla permite citas numeradas con `sn-basic` mediante la opción `Numbered` (OL).

Clase y opciones propuestas para Applied Intelligence (**recomendación derivada**, no una línea literal de la guía):

```latex
\documentclass[pdflatex,sn-basic,Numbered]{sn-jnl}
```

| Si el manuscrito usa | Hallazgo | Corrección |
|---|---|---|
| `sn-jnl` con `sn-basic,Numbered` | Ninguno | — |
| `sn-jnl` con `sn-mathphys-num` u otro estilo | `[PLANTILLA]` MENOR: el formato de la lista de referencias no coincide con el ejemplo de la revista (R-30) | MECÁNICA: cambiar la opción; recompilar y revisar la lista |
| `sn-jnl` con `sn-basic` sin `Numbered` | `[REVISTA]` MAYOR: las citas salen en formato autor-año y la revista exige números entre corchetes (R-25) | MECÁNICA |
| `svjour3` | `[PLANTILLA]` VERIFICAR: es la plantilla heredada; reportar I-01 | CONTENIDO: la migración afecta al preámbulo, a los autores y al resumen |
| Otra clase | `[PLANTILLA]` MAYOR | CONTENIDO: migrar a `sn-jnl` |

## Requisitos técnicos de la plantilla y del sistema de envío

| ID | Requisito | Fuente | Chequeo | Sev. |
|---|---|---|---|---|
| P-01 | Manuscrito en un único `.tex`, sin `\input{...}` para incluir otros `.tex`. Solo se admite `\input` del `.bbl` | OL | script (T02) | MAYOR |
| P-02 | Sin subcarpetas y sin rutas completas en `\includegraphics`; usar solo el nombre del archivo | LS, SG | script (T03) | BLOQUEANTE |
| P-03 | Editorial Manager compila con TeX Live 2018. Un paquete o una versión más reciente puede fallar aunque compile en local | LS | script (T16: lista de paquetes) + externo | VERIFICAR |
| P-04 | Bibliografía: subir `.bib` y `.bst`, o el `.bbl`. Lo más fiable es pegar el contenido del `.bbl` en el `.tex` en lugar de `\bibliography{...}` | LS | juicio | MENOR |
| P-05 | Sin fuentes personalizadas; caracteres especiales con código TeX (`\'a`, `\~n`) | LS | juicio | MENOR |
| P-06 | Con `pdflatex`, figuras en pdf, jpg o png (EPS solo con `latex`). Evitar subfiguras | OL | script (T15) | MENOR |
| P-07 | Declaraciones: encabezado más subencabezados Funding, Conflict of interest/Competing interests, Ethics approval and consent to participate, Consent for publication, Data availability, Materials availability, Code availability y Author contribution. Si alguno no aplica, se conserva el encabezado con «Not applicable» | OL | script (T08) | MAYOR |
| P-08 | Autor de correspondencia con `\author*` y correo con `\email{}` | OL | script (T06) | BLOQUEANTE |
| P-09 | La guía de la revista prevalece sobre la plantilla cuando difieren | OL | — | — |

## Resolución propuesta para el encabezado de las declaraciones (I-02)

Esta resolución es una `INTERPRETACIÓN`; se reporta como tal.

- Usar el encabezado **«Statements and Declarations»**. Es el único cuya ausencia, según la guía, provoca la devolución del envío como incompleto.
- Debajo, los subencabezados de P-07. Llamar *Competing interests* al de conflictos, que es la forma que usa la guía de la revista.
- «Compliance with Ethical Standards» queda cubierto por los subencabezados *Ethics approval* y *Consent*, con «Not applicable» en una revisión sin participantes.

## Manuscrito en español con `sn-jnl`

Solo aplica mientras el manuscrito esté en español. Si se traduce al inglés (R-01), estos ajustes se retiran.

- `babel` necesita `es-noshorthands`; sin esa opción la clase falla en `\author`.
- Las redefiniciones de `\refname`, `\tablename`, `\figurename` y `\abstractname` deben retirarse en la traducción.
- La palabra «Figura» en las leyendas choca con R-37, que pide «Fig.».
