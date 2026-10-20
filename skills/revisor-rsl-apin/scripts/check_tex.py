#!/usr/bin/env python3
"""Chequeos deterministas del manuscrito LaTeX contra los requisitos de
Applied Intelligence y la plantilla sn-jnl.

Uso:
    python3 check_tex.py articulo.tex [--root CARPETA] [--json salida.json]

Solo reporta lo que puede comprobar sin juicio. Cada hallazgo es un hecho sobre
el texto; la severidad que se asigna aquí es la de partida, y la revisión con
criterio puede ajustarla. Sin dependencias externas (Python >= 3.9).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path

SEV_ORDER = {"BLOQUEANTE": 0, "MAYOR": 1, "MENOR": 2, "VERIFICAR": 3, "INFO": 4}


@dataclass
class Finding:
    check: str
    severity: str
    source: str
    requirement: str
    message: str
    lines: list[int] = field(default_factory=list)
    evidence: str = ""


# ---------------------------------------------------------------- utilidades

def strip_comments(text: str) -> str:
    """Elimina comentarios % (no escapados) conservando el número de líneas."""
    out = []
    for line in text.split("\n"):
        m = re.search(r"(?<!\\)%", line)
        out.append(line[: m.start()] if m else line)
    return "\n".join(out)


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def read_group(text: str, pos: int) -> tuple[str, int] | None:
    """Lee un argumento {...} que empieza en text[pos] (saltando espacios y
    argumentos opcionales [...]). Devuelve (contenido, posición final)."""
    n = len(text)
    i = pos
    while i < n:
        while i < n and text[i] in " \t\n*":
            i += 1
        if i < n and text[i] == "[":
            depth = 0
            while i < n:
                if text[i] == "[":
                    depth += 1
                elif text[i] == "]":
                    depth -= 1
                    if depth == 0:
                        i += 1
                        break
                i += 1
            continue
        break
    if i >= n or text[i] != "{":
        return None
    depth = 0
    start = i
    while i < n:
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1 : i], i + 1
        i += 1
    return None


def find_commands(text: str, name: str):
    """Itera (posición, argumento) de cada \\name{...}."""
    for m in re.finditer(r"\\" + re.escape(name) + r"(?![A-Za-z])", text):
        g = read_group(text, m.end())
        if g is not None:
            yield m.start(), g[0]


def latex_to_plain(s: str) -> str:
    s = re.sub(r"\$[^$]*\$", " X ", s)
    s = re.sub(r"\\(cite[a-z]*|ref|eqref|label)\*?(\[[^\]]*\])?\{[^}]*\}", " ", s)
    s = re.sub(r"\\[,;:! ]", " ", s)
    s = s.replace("~", " ").replace("---", " ").replace("--", " ")
    s = re.sub(r"\\[A-Za-z]+\*?", " ", s)
    s = re.sub(r"[{}]", " ", s)
    s = s.replace("\\%", "%")
    return re.sub(r"\s+", " ", s).strip()


def count_words(plain: str) -> int:
    return len([t for t in plain.split(" ") if re.search(r"[A-Za-zÁÉÍÓÚÑáéíóúñü0-9]", t)])


def env_blocks(text: str, envs: tuple[str, ...]):
    """Itera (nombre_env, inicio, fin, contenido) de los entornos dados."""
    pat = re.compile(r"\\begin\{(" + "|".join(re.escape(e) for e in envs) + r")\}")
    for m in pat.finditer(text):
        env = m.group(1)
        end = text.find("\\end{" + env + "}", m.end())
        if end == -1:
            continue
        yield env, m.start(), end, text[m.end() : end]


# ------------------------------------------------------------------- chequeos

def check_class(t: str, F: list):
    m = re.search(r"\\documentclass(\[[^\]]*\])?\{([^}]+)\}", t)
    if not m:
        F.append(Finding("T01", "BLOQUEANTE", "PLANTILLA", "P-09",
                         "No se encontró \\documentclass: no es el archivo principal."))
        return
    opts = [o.strip() for o in (m.group(1) or "[]")[1:-1].split(",") if o.strip()]
    cls = m.group(2).strip()
    ln = [line_of(t, m.start())]
    ev = m.group(0)
    if cls == "svjour3":
        F.append(Finding("T01", "VERIFICAR", "PLANTILLA", "I-01",
                         "Clase svjour3 (heredada). La guía también recomienda sn-jnl; ver plantilla-snjnl.md.",
                         ln, ev))
        return
    if cls != "sn-jnl":
        F.append(Finding("T01", "MAYOR", "PLANTILLA", "I-01",
                         f"Clase '{cls}': no es la plantilla de Springer Nature (sn-jnl).", ln, ev))
        return
    styles = [o for o in opts if o.startswith("sn-") and o != "sn-jnl"]
    if "sn-basic" in styles and "Numbered" in opts:
        return
    if "sn-basic" in styles:
        F.append(Finding("T01", "MAYOR", "REVISTA", "R-25",
                         "sn-basic sin 'Numbered': las citas saldrían autor-año; la revista exige números entre corchetes.",
                         ln, ev))
        return
    F.append(Finding("T01", "MENOR", "PLANTILLA", "R-30",
                     f"Estilo de referencias {styles or 'no declarado'}: la revista nombra sn-basic.bst; "
                     "propuesta: [pdflatex,sn-basic,Numbered].", ln, ev))


def check_input(t: str, F: list):
    for m in re.finditer(r"\\(input|include)(?![A-Za-z])\s*\{?([^}\s]*)", t):
        target = m.group(2)
        if target.endswith(".bbl"):
            continue
        F.append(Finding("T02", "MAYOR", "PLANTILLA", "P-01",
                         f"\\{m.group(1)}{{{target}}}: la plantilla pide un único .tex.",
                         [line_of(t, m.start())]))


def check_graphics(t: str, root: Path | None, F: list):
    exts = [".pdf", ".png", ".jpg", ".jpeg", ".eps", ".tif", ".tiff"]
    for m in re.finditer(r"\\includegraphics(\[[^\]]*\])?\{([^}]*)\}", t):
        path = m.group(2).strip()
        ln = [line_of(t, m.start())]
        if "/" in path or "\\" in path or ":" in path:
            F.append(Finding("T03", "BLOQUEANTE", "REVISTA", "R-05 / P-02",
                             f"Figura en subcarpeta o con ruta: '{path}'. El envío no admite subcarpetas.", ln))
        name = Path(path).name
        if root is not None:
            cand = [root / path] if Path(path).suffix else [root / (path + e) for e in exts]
            if not any(c.exists() for c in cand):
                F.append(Finding("T03", "MAYOR", "PLANTILLA", "R-04",
                                 f"No se encontró el archivo de figura '{path}' bajo {root}.", ln))
        suf = Path(name).suffix.lower()
        if suf in (".png", ".jpg", ".jpeg"):
            F.append(Finding("T03", "VERIFICAR", "REVISTA", "R-39 / R-40",
                             f"Figura en mapa de bits '{name}': comprobar resolución (≥300/600/1200 dpi según tipo); "
                             "la guía prefiere EPS (vector) o TIFF.", ln))
        if not re.match(r"(?i)^fig\d+", name):
            F.append(Finding("T03", "MENOR", "REVISTA", "R-39",
                             f"Nombre de figura '{name}': la guía pide 'Fig' + número (p. ej. Fig1.eps).", ln))


def check_abstract(t: str, F: list):
    found = list(find_commands(t, "abstract"))
    if not found:
        m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", t, re.S)
        if m:
            found = [(m.start(), m.group(1))]
    if not found:
        F.append(Finding("T04", "MAYOR", "REVISTA", "R-13", "No se encontró el resumen."))
        return
    pos, body = found[0]
    ln = [line_of(t, pos)]
    words = count_words(latex_to_plain(body))
    if not 150 <= words <= 250:
        F.append(Finding("T04", "MAYOR", "REVISTA", "R-13",
                         f"Resumen de {words} palabras (exigido: 150–250).", ln))
    if re.search(r"\\cite", body):
        F.append(Finding("T04", "MAYOR", "REVISTA", "R-14", "El resumen contiene citas (\\cite).", ln))
    heads = re.findall(r"\\textbf\{([^}]*)\}", body)
    if heads:
        F.append(Finding("T04", "VERIFICAR", "REVISTA", "R-13",
                         f"Resumen estructurado con subtítulos {heads}: la guía no los menciona; "
                         "la plantilla los desaconseja salvo que la revista los permita.", ln))
    plain = latex_to_plain(body)
    acr = sorted({a for a in re.findall(r"\b[A-Z][A-Z0-9-]{1,}[a-z]?\b", plain) if not re.fullmatch(r"[IVX]+", a)})
    if acr:
        F.append(Finding("T04", "VERIFICAR", "REVISTA", "R-14",
                         f"Siglas en el resumen: {', '.join(acr)}. Comprobar que cada una se define en el resumen.", ln))


def check_keywords(t: str, F: list):
    found = list(find_commands(t, "keywords"))
    if not found:
        F.append(Finding("T05", "MAYOR", "REVISTA", "R-15", "No se encontraron palabras clave (\\keywords)."))
        return
    pos, body = found[0]
    kws = [k.strip() for k in re.split(r"[,;]", latex_to_plain(body)) if k.strip()]
    if not 4 <= len(kws) <= 6:
        F.append(Finding("T05", "MAYOR", "REVISTA", "R-15",
                         f"{len(kws)} palabras clave (exigido: 4–6): {kws}", [line_of(t, pos)]))


def check_authors(t: str, raw: str, F: list):
    authors = [(m.start(), m.group(1)) for m in re.finditer(r"\\author(\*?)(?=\s*[\[{])", t)]
    if not authors:
        F.append(Finding("T06", "BLOQUEANTE", "REVISTA", "R-08", "No se encontraron autores (\\author)."))
        return
    if not any(star == "*" for _, star in authors):
        F.append(Finding("T06", "BLOQUEANTE", "REVISTA", "R-09 / P-08",
                         "Ningún \\author* : no está marcado el autor de correspondencia.",
                         [line_of(t, authors[0][0])]))
    emails = list(find_commands(t, "email"))
    if not emails:
        F.append(Finding("T06", "BLOQUEANTE", "REVISTA", "R-09 / P-08",
                         "Ningún \\email{}: el autor de correspondencia necesita correo activo.",
                         [line_of(t, authors[0][0])]))
    orcids = re.findall(r"\b\d{4}-\d{4}-\d{4}-\d{3}[\dX]\b", raw)
    if len(set(orcids)) < len(authors):
        F.append(Finding("T06", "MENOR", "REVISTA", "R-10",
                         f"{len(set(orcids))} ORCID para {len(authors)} autores (se piden si existen).",
                         [line_of(t, authors[0][0])]))
    for pos, body in find_commands(t, "affil"):
        missing = [k for k in ("orgname", "city", "country") if "\\" + k not in body]
        if missing:
            F.append(Finding("T06", "MAYOR", "REVISTA", "R-08",
                             f"Afiliación sin {missing}.", [line_of(t, pos)]))


def check_headings(t: str, F: list):
    for m in re.finditer(r"\\(paragraph|subparagraph)\*?\{", t):
        F.append(Finding("T07", "MENOR", "REVISTA", "R-16",
                         f"\\{m.group(1)}: cuarto nivel o inferior de encabezado (máximo tres niveles).",
                         [line_of(t, m.start())]))


DECL_ITEMS = {
    "Funding": r"funding|financiaci[oó]n|financiamiento",
    "Competing interests": r"competing interests?|conflicts? of interests?|conflicto de intereses|intereses en conflicto",
    "Ethics approval": r"ethics approval|aprobaci[oó]n [eé]tica",
    "Consent": r"consent|consentimiento",
    "Data availability": r"data availability|disponibilidad de (los )?datos",
    "Materials availability": r"materials? availability|disponibilidad de (los )?materiales",
    "Code availability": r"code availability|disponibilidad de(l)? c[oó]digo|datos y c[oó]digo",
    "Author contribution": r"author'?s?'? contributions?|contribuci[oó]n de (los )?autores",
}


def check_declarations(t: str, raw: str, F: list):
    m = re.search(r"\\section\*?\{([^}]*(Declaration|Declaracion|Declaración)[^}]*)\}", t, re.I)
    if not m:
        F.append(Finding("T08", "BLOQUEANTE", "REVISTA", "R-19",
                         "No hay sección de declaraciones; la revista devuelve el envío como incompleto."))
        return
    ln = [line_of(t, m.start())]
    title = m.group(1).strip()
    if title.lower() != "statements and declarations":
        F.append(Finding("T08", "MENOR", "REVISTA", "R-19 / I-02",
                         f"Encabezado '{title}': la guía usa 'Statements and Declarations'.", ln))
    nxt = re.search(r"\\(section|begin\{appendices\}|bibliography)\b", t[m.end():])
    body = t[m.end(): m.end() + (nxt.start() if nxt else len(t))]
    for item, pat in DECL_ITEMS.items():
        if not re.search(pat, body, re.I):
            sev = "BLOQUEANTE" if item == "Competing interests" else "MAYOR"
            F.append(Finding("T08", sev, "REVISTA", "R-20–R-22 / P-07",
                             f"Falta la declaración '{item}' (si no aplica: 'Not applicable').", ln))
    raw_body_start = line_of(t, m.start())
    raw_lines = raw.split("\n")
    end_line = line_of(t, m.end() + (nxt.start() if nxt else len(t) - m.end()))
    pend = [i + 1 for i in range(raw_body_start - 1, min(end_line, len(raw_lines)))
            if re.search(r"Pendiente|NOTA PARA LOS AUTORES|TODO|\[COMPLETAR\]", raw_lines[i])]
    if pend:
        F.append(Finding("T08", "BLOQUEANTE", "REVISTA", "R-20 / R-21",
                         "Declaraciones con contenido pendiente (dato del autor).", pend))


def check_pending(raw: str, F: list):
    lines = [i + 1 for i, l in enumerate(raw.split("\n"))
             if re.search(r"NOTA PARA LOS AUTORES|\bTODO\b|\bFIXME\b|\bXXX\b|\[COMPLETAR\]", l)]
    if lines:
        F.append(Finding("T09", "BLOQUEANTE", "EQUIPO", "E-03",
                         f"{len(lines)} notas pendientes de los autores en el .tex (resolver antes del envío).",
                         lines))


ES = {"de", "la", "que", "el", "en", "los", "las", "del", "por", "una", "con", "para", "se", "su", "como", "más", "este", "esta"}
EN = {"the", "of", "and", "to", "in", "is", "that", "for", "with", "as", "are", "this", "by", "on", "which", "from", "be"}


def check_language(t: str, F: list):
    b = t.find("\\begin{document}")
    toks = re.findall(r"[a-záéíóúñ]+", latex_to_plain(t[b:]).lower())
    es = sum(1 for w in toks if w in ES)
    en = sum(1 for w in toks if w in EN)
    if es > en:
        F.append(Finding("T10", "BLOQUEANTE", "REVISTA", "R-01",
                         f"El manuscrito está en español (palabras funcionales ES {es} frente a EN {en}). "
                         "Requisito de idioma inglés: inferido, no explícito en la guía."))


def check_captions(t: str, F: list):
    for env, s, e, body in env_blocks(t, ("figure", "figure*")):
        for pos, cap in find_commands(body, "caption"):
            plain = latex_to_plain(cap).rstrip()
            if plain.endswith("."):
                F.append(Finding("T11", "MENOR", "REVISTA", "R-37",
                                 "Leyenda de figura terminada en punto (la guía pide sin puntuación final).",
                                 [line_of(t, s + len("\\begin{" + env + "}") + pos)]))


def check_order(t: str, F: list):
    body_start = t.find("\\begin{document}")
    for kind, envs, req in (("figura", ("figure", "figure*"), "R-36"),
                            ("tabla", ("table", "table*", "longtable", "sidewaystable", "sidewaystable*"), "R-32")):
        labels = []
        spans = []
        for env, s, e, body in env_blocks(t, envs):
            spans.append((s, e))
            for lm in re.finditer(r"\\label\{([^}]+)\}", body):
                labels.append((lm.group(1), s))
                break
        labels.sort(key=lambda x: x[1])
        first_ref = {}
        for rm in re.finditer(r"\\(?:ref|autoref|cref|Cref)\{([^}]+)\}", t):
            if rm.start() < body_start:
                continue
            for key in rm.group(1).split(","):
                key = key.strip()
                inside_own = any(s <= rm.start() <= e for (lab, s0) in labels if lab == key
                                 for (s, e) in spans if s == s0)
                if key not in first_ref and not inside_own:
                    first_ref[key] = rm.start()
        unref = [lab for lab, _ in labels if lab not in first_ref]
        if unref:
            F.append(Finding("T12", "MENOR", "REVISTA", req,
                             f"{kind.capitalize()}s sin cita en el texto: {unref}.",
                             [line_of(t, p) for lab, p in labels if lab in unref]))
        cited = [(lab, first_ref[lab]) for lab, _ in labels if lab in first_ref]
        order_by_ref = [lab for lab, _ in sorted(cited, key=lambda x: x[1])]
        order_by_num = [lab for lab, _ in cited]
        if order_by_ref != order_by_num:
            bad = [f"{a} (n.º {order_by_num.index(a) + 1})" for a, b in zip(order_by_ref, order_by_num) if a != b]
            F.append(Finding("T12", "MENOR", "REVISTA", req,
                             f"{kind.capitalize()}s no citadas por primera vez en orden numérico; "
                             f"primeras desviaciones: {bad[:4]}.",
                             [line_of(t, first_ref[order_by_ref[0]])]))


def check_footnotes(t: str, F: list):
    for pos, body in find_commands(t, "footnote"):
        rest = re.sub(r"\\cite[a-z]*\*?(\[[^\]]*\])?\{[^}]*\}", "", body)
        if not latex_to_plain(rest).strip(" .;,"):
            F.append(Finding("T13", "MENOR", "REVISTA", "R-18",
                             "Nota al pie que consiste solo en una cita.", [line_of(t, pos)]))


def parse_bib(text: str) -> dict:
    entries = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        typ, key = m.group(1).lower(), m.group(2)
        if typ in ("comment", "string", "preamble"):
            continue
        depth, i = 1, text.find("{", m.start()) + 1
        while i < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        entries[key] = (typ, text[m.end(): i])
    return entries


def check_bibliography(t: str, root: Path | None, F: list):
    bibs = [b.strip() for _, arg in find_commands(t, "bibliography") for b in arg.split(",")]
    has_thebib = "\\begin{thebibliography}" in t
    if not bibs and not has_thebib:
        F.append(Finding("T14", "MAYOR", "REVISTA", "R-26", "No se encontró bibliografía."))
        return
    cited = set()
    for m in re.finditer(r"\\cite[a-zA-Z]*\*?(\[[^\]]*\])*\{([^}]*)\}", t):
        cited.update(k.strip() for k in m.group(2).split(",") if k.strip())
    if root is None or not bibs:
        F.append(Finding("T14", "VERIFICAR", "REVISTA", "R-26 / R-28",
                         f"{len(cited)} claves citadas; .bib no comprobado (sin --root o con thebibliography)."))
        return
    entries = {}
    for b in bibs:
        p = root / (b if b.endswith(".bib") else b + ".bib")
        if "/" in b:
            F.append(Finding("T14", "BLOQUEANTE", "REVISTA", "R-05", f"Bibliografía en subcarpeta: '{b}'."))
        if not p.exists():
            F.append(Finding("T14", "MAYOR", "PLANTILLA", "R-04", f"No se encontró {p.name} bajo {root}."))
            continue
        entries.update(parse_bib(p.read_text(encoding="utf-8", errors="replace")))
    if not entries:
        return
    missing = sorted(cited - entries.keys())
    if missing:
        F.append(Finding("T14", "MAYOR", "REVISTA", "R-26",
                         f"{len(missing)} claves citadas sin entrada en el .bib: {missing[:10]}"))
    no_doi = sorted(k for k in cited & entries.keys() if not re.search(r"\bdoi\s*=", entries[k][1], re.I))
    if no_doi:
        F.append(Finding("T14", "VERIFICAR", "REVISTA", "R-28",
                         f"{len(no_doi)} entradas citadas sin campo doi: {no_doi[:12]}"))
    pre = sorted(k for k in cited & entries.keys()
                 if re.search(r"arxiv|eprint|preprint|openreview", entries[k][1], re.I))
    if pre:
        F.append(Finding("T14", "VERIFICAR", "REVISTA", "R-26",
                         f"{len(pre)} entradas parecen preimpresiones; comprobar si existe versión editorial: {pre[:12]}"))


def check_subfig(t: str, F: list):
    m = re.search(r"\\usepackage(\[[^\]]*\])?\{[^}]*\b(subfig|subcaption|subfigure)\b", t)
    if m:
        F.append(Finding("T15", "MENOR", "PLANTILLA", "P-06",
                         f"Paquete {m.group(2)}: la plantilla pide evitar subfiguras.", [line_of(t, m.start())]))


def check_packages(t: str, F: list):
    pk = []
    for _, arg in find_commands(t, "usepackage"):
        pk += [p.strip() for p in arg.split(",") if p.strip()]
    if pk:
        F.append(Finding("T16", "VERIFICAR", "PLANTILLA", "P-03",
                         f"Paquetes cargados: {', '.join(pk)}. Editorial Manager compila con TeX Live 2018; "
                         "revisar el registro de compilación del sistema."))


def check_table_fonts(t: str, F: list):
    envs = ("table", "table*", "longtable", "sidewaystable", "sidewaystable*")
    for env, s, e, body in env_blocks(t, envs):
        small = re.findall(r"\\(tiny|scriptsize)\b", body)
        if small:
            F.append(Finding("T18", "VERIFICAR", "REVISTA", "CK-08",
                             f"Tabla con tipografía \\{small[0]}: comprobar legibilidad al tamaño final.",
                             [line_of(t, s)]))


MESES = r"(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre|" \
        r"January|February|March|April|May|June|July|August|September|October|November|December)"


def check_dates(t: str, F: list):
    b = t.find("\\begin{document}")
    a = t.find("\\begin{appendices}")
    end = a if a != -1 else len(t)
    hits = [m.start() for m in re.finditer(r"\b\d{1,2}\s+(de\s+)?" + MESES + r"\b", t[b:end], re.I)]
    if hits:
        F.append(Finding("T17", "VERIFICAR", "EQUIPO", "E-01 / E-02",
                         f"{len(hits)} fechas en el cuerpo del artículo. Comprobar cuáles exige PRISMA "
                         "(fecha de búsqueda, enmiendas) y cuáles narran el proceso.",
                         [line_of(t, b + h) for h in hits]))


# --------------------------------------------------------------------- salida

def render(findings: list[Finding], tex: Path) -> str:
    findings.sort(key=lambda f: (SEV_ORDER.get(f.severity, 9), f.check))
    out = [f"# Chequeo automático — {tex.name}", ""]
    counts = {}
    for f in findings:
        counts[f.severity] = counts.get(f.severity, 0) + 1
    out.append("Resumen: " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items(), key=lambda x: SEV_ORDER[x[0]]))
                              or "sin hallazgos"))
    out.append("")
    out.append("| # | Chequeo | Severidad | Fuente | Requisito | Hallazgo | Líneas |")
    out.append("|---|---|---|---|---|---|---|")
    for i, f in enumerate(findings, 1):
        lines = ", ".join(map(str, f.lines[:8])) + (" …" if len(f.lines) > 8 else "")
        msg = f.message.replace("|", "\\|")
        out.append(f"| A{i:02d} | {f.check} | {f.severity} | [{f.source}] | {f.requirement} | {msg} | {lines} |")
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tex", type=Path)
    ap.add_argument("--root", type=Path, help="carpeta del envío (figuras y .bib)")
    ap.add_argument("--json", type=Path, help="guardar hallazgos en JSON")
    a = ap.parse_args(argv)
    if not a.tex.exists():
        print(f"No existe {a.tex}", file=sys.stderr)
        return 2
    raw = a.tex.read_text(encoding="utf-8", errors="replace")
    t = strip_comments(raw)
    F: list[Finding] = []
    check_class(t, F)
    check_input(t, F)
    check_graphics(t, a.root, F)
    check_abstract(t, F)
    check_keywords(t, F)
    check_authors(t, raw, F)
    check_headings(t, F)
    check_declarations(t, raw, F)
    check_pending(raw, F)
    check_language(t, F)
    check_captions(t, F)
    check_order(t, F)
    check_footnotes(t, F)
    check_bibliography(t, a.root, F)
    check_subfig(t, F)
    check_packages(t, F)
    check_dates(t, F)
    check_table_fonts(t, F)
    print(render(F, a.tex))
    if a.json:
        a.json.write_text(json.dumps([asdict(f) for f in F], ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
