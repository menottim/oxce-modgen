# OXCE Mod Generator

A Claude Code skill for generating [OpenXcom Extended (OXCE)](https://github.com/MeridianOXC/OpenXcom) mods from natural language descriptions.

## Table of Contents

- [Background](#background)
- [What It Does](#what-it-does)
- [Install](#install)
- [Usage](#usage)
- [Supported Mod Types](#supported-mod-types)
- [Known Limitations](#known-limitations)
- [Requirements](#requirements)

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

## Known Limitations

__Out of scope — these mod types require custom assets or deep engine knowledge:__
- Custom sprites, sounds, or map tiles (the generator reuses existing asset indices)
- Y-Script scripting hooks (OXCE's custom scripting language)
- Total conversions (too large for a single skill invocation)
- Mod compatibility checking (would require loading other mods to detect conflicts)

__Known issues:__
- __Fetch URLs may 404 on branch restructures.__ The skill fetches vanilla stats from the `oxce-plus` branch on GitHub. If the OXCE repo restructures its `bin/standard/` directory, fetches will fail. The skill handles this gracefully (asks user for manual values) but won't auto-recover.
- __damageType enum in reference docs is approximate.__ The actual values in OXCE's data files may differ from the enum table. The skill prioritizes fetched data over the reference doc, but if fetching fails, the enum could mislead.
- __No OXCE-extension-specific validation.__ OXCE adds keys beyond vanilla (e.g., `categories`, `tags`, `compatibleAmmo`, `attraction`). The validator accepts these silently but doesn't verify their structure.
- __Single-master mods only.__ Generated mods target either `xcom1` or `xcom2`, not both. Cross-game mods require manual editing.

## Requirements

- Claude Code
- Python 3.10+ with PyYAML (for validation)
