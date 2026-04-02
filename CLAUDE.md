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

## Documentation Maintenance (MUST FOLLOW)

When making changes to the skill, validation script, or reference docs, you MUST update the relevant documentation in the same commit:

| Change type | Documents to update |
|-------------|-------------------|
| New mod type supported | README.md "Supported Mod Types" section |
| New limitation discovered | README.md "Known Limitations" section |
| Limitation fixed/resolved | README.md "Known Limitations" — remove or update the entry |
| Fetch URL changes | README.md if user-facing, SKILL.md, mod-structure.md |
| Validation rules added/changed | README.md "Known Limitations" if it affects what users can do |
| New OXCE features supported | README.md "Supported Mod Types", common-patterns.md |
| Bug fix | README.md "Known Limitations" — remove the issue if resolved |

__README.md__ is the public-facing introduction — keep the supported mod types, limitations, and usage examples current.

## Architecture

- `skills/modgen/SKILL.md` — Main skill invoked via `/modgen`
- `skills/modgen/references/` — Stable reference docs (mod structure, patterns)
- `scripts/validate_mod.py` — YAML + schema validation for generated mods
- Vanilla game data is fetched live from `raw.githubusercontent.com/MeridianOXC/OpenXcom/oxce-plus/bin/standard/`
- Generated mods output to `~/oxce-mods/<mod-name>/`
