# OXCE Mod Generator

## Overview

A Claude Code skill that generates installable OpenXcom Extended (OXCE) mods from natural language descriptions. Fetches current vanilla game data from the OXCE GitHub repo at runtime.

## Git Identity

Always use personal identity:
```
git -c user.name="menottim" -c user.email="menottim@users.noreply.github.com" commit ...
```

## Commands

__Run validation tests:__
```bash
python -m pytest tests/ -v
```

__Validate a mod folder:__
```bash
python scripts/validate_mod.py <path-to-mod-folder>
```

## Architecture

- `skills/modgen/SKILL.md` — Main skill invoked via `/modgen`
- `skills/modgen/references/` — Stable reference docs (mod structure, patterns)
- `scripts/validate_mod.py` — YAML + schema validation for generated mods
- Vanilla game data is fetched live from `raw.githubusercontent.com/MeridianOXC/OpenXcom/oxce-plus/bin/standard/`
- Generated mods output to `~/oxce-mods/<mod-name>/`
