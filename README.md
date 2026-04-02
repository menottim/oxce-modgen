# OXCE Mod Generator

A Claude Code skill for generating [OpenXcom Extended (OXCE)](https://github.com/MeridianOXC/OpenXcom) mods from natural language descriptions.

## Background

[OpenXcom](https://github.com/MeridianOXC/OpenXcom) is an open-source reimplementation of the classic 1994 strategy games __UFO: Enemy Unknown__ and __X-COM: Terror From The Deep__. The Extended (OXCE) fork adds a massive data-driven modding layer — most game behavior is controlled by YAML rulesets that can be overridden without touching C++.

The [OXCE mod community on mod.io](https://mod.io/g/openxcom) hosts 400+ mods ranging from single-file balance tweaks (under 1 KB) to total conversions like the 1 GB Warhammer 40K mod. This tool targets the long tail — the YAML-only mods that make up the majority of the ecosystem.

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
