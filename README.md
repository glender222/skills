# Skills de glender222

Colección de *agent skills* (estándar abierto `SKILL.md`) compatibles con Claude Code, Codex, Antigravity y otros agentes.

## Skills

| Skill | Descripción |
|---|---|
| [`revisor-rsl-apin`](skills/revisor-rsl-apin) | Revisor previo al envío de una revisión sistemática (RSL) en LaTeX `sn-jnl` a *Applied Intelligence* (Springer): requisitos de la revista, PRISMA 2020, Kitchenham y Charters, requisitos del curso y coherencia con la sábana. |

## Instalación

Con [skills.sh](https://skills.sh):

```bash
# todas las skills del repo
npx skills add glender222/skills

# solo esta skill
npx skills add glender222/skills --skill revisor-rsl-apin
```

El instalador pregunta en qué agentes instalarla (Claude Code, Codex, Antigravity, etc.).

### Manual

Copia `skills/revisor-rsl-apin/` en:

- Claude Code: `~/.claude/skills/` (o `.claude/skills/` del proyecto)
- Codex: `~/.codex/skills/` (o `.agents/skills/`)
- Antigravity: `.agent/skills/` del proyecto

## Requisitos

Python 3.9+; `sabana_dump.py` requiere `openpyxl` (`pip install openpyxl`).
