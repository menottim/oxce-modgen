# OXCE Mod Generator

A Claude Code skill for generating [OpenXcom Extended (OXCE)](https://github.com/MeridianOXC/OpenXcom) mods from natural language descriptions.

## What It Does

Invoke `/modgen` in Claude Code with a description like "make plasma weapons more expensive but more accurate" and it will:

1. Ask clarifying questions about your intent
2. Fetch current vanilla game stats from the OXCE repo
3. Propose specific changes for your approval
4. Generate a complete, installable mod folder
5. Validate the output YAML

## Install

Add this repo as a Claude Code plugin:

```bash
claude plugin add ~/oxce-modgen
```

## Usage

```
/modgen make plasma weapons 2x more expensive
/modgen increase laser weapon accuracy by 15%
/modgen add a new craft with 20 soldier capacity
```

Generated mods are written to `~/oxce-mods/<mod-name>/`. Copy the folder to your OpenXcom `mods/` directory and enable it in Options > Mods.

## Supported Mod Types

- Balance tweaks (weapon stats, costs, accuracy)
- New items (weapons, equipment, ammo)
- Research tree modifications
- Starting base changes
- Difficulty scaling
- Economy rebalancing
- QoL tweaks

## Requirements

- Claude Code
- Python 3.10+ with PyYAML (for validation)
