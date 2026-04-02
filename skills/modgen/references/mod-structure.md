# OXCE Mod Structure Reference

## Mod Folder Layout

A minimal mod requires only two files:

```
my-mod/
├── metadata.yml          # Required: mod identity and compatibility
└── Ruleset/
    └── mod.rul           # At least one ruleset file
```

A more complete layout:

```
my-mod/
├── metadata.yml
├── Ruleset/
│   ├── items.rul
│   ├── research.rul
│   └── strings.rul
├── Resources/
│   ├── Sprites/
│   └── Sound/
└── Language/
    ├── en-US.yml
    └── fr-FR.yml
```

Ruleset files use `.rul` extension and contain YAML. Multiple `.rul` files in `Ruleset/` are all loaded and merged. File load order within a mod is alphabetical; mods load in dependency order.

---

## metadata.yml Format

All five fields are required:

```yaml
name: My Mod Name
version: "1.0"
description: "One-line description of what this mod does."
author: AuthorName
master: xcom1
```

| Field | Type | Notes |
|---|---|---|
| `name` | string | Display name shown in mod manager |
| `version` | string | Quoted string; semantic versioning recommended |
| `description` | string | Shown in mod manager UI |
| `author` | string | Mod author name |
| `master` | string | `xcom1` for X-COM 1, `xcom2` for Terror from the Deep |

Optional fields:

```yaml
isMaster: false          # true only if this mod is itself a master (rare)
requiredExtendedVersion: "7.0"   # minimum OXCE version
```

---

## The Override Principle

OXCE merges mods on top of the vanilla ruleset. __Only include fields you want to change.__ You do not need to reproduce a full vanilla entry to modify one value.

Example — changing only the sell price of the laser pistol:

```yaml
items:
  - type: STR_LASER_PISTOL
    costSell: 20000
```

This leaves all other laser pistol properties (power, accuracy, sprites, etc.) at their vanilla values. OXCE performs a deep merge keyed on `type`.

__Exceptions:__ A few list-typed fields replace rather than merge (e.g. `requires`, `requiresBuy`). When in doubt, include the full list.

---

## Fetch URLs for Vanilla Rulesets

Use these URLs to read the vanilla data before writing overrides. Replace `{file}` with the path from the table below.

__Base URL:__ `https://raw.githubusercontent.com/MeridianOXC/OpenXcom/oxce-plus/bin/standard/`

| Section | xcom1 path | xcom2 path |
|---|---|---|
| items | `xcom1/Ruleset/items.rul` | `xcom2/Ruleset/items.rul` |
| research | `xcom1/Ruleset/research.rul` | `xcom2/Ruleset/research.rul` |
| crafts | `xcom1/Ruleset/crafts.rul` | `xcom2/Ruleset/crafts.rul` |
| craftWeapons | `xcom1/Ruleset/craftWeapons.rul` | `xcom2/Ruleset/craftWeapons.rul` |
| facilities | `xcom1/Ruleset/facilities.rul` | `xcom2/Ruleset/facilities.rul` |
| manufacture | `xcom1/Ruleset/manufacture.rul` | `xcom2/Ruleset/manufacture.rul` |
| armors | `xcom1/Ruleset/armors.rul` | `xcom2/Ruleset/armors.rul` |
| units | `xcom1/Ruleset/units.rul` | `xcom2/Ruleset/units.rul` |
| difficulty | `xcom1/Ruleset/difficulty.rul` | `xcom2/Ruleset/difficulty.rul` |
| startingBase | `xcom1/Ruleset/startingBase.rul` | `xcom2/Ruleset/startingBase.rul` |

Full example URL: `https://raw.githubusercontent.com/MeridianOXC/OpenXcom/oxce-plus/bin/standard/xcom1/Ruleset/items.rul`

---

## Known Ruleset Sections

These are the top-level keys recognized inside `.rul` files:

```
items
armors
crafts
craftWeapons
ufos
research
manufacture
facilities
ufopaedia
alienDeployments
alienMissions
alienRaces
units
terrains
mapScripts
missionScripts
countries
regions
difficulty
startingBase
extraSprites
extraStrings
vars
interfaces
inventories
cutscenes
globe
music
ufoTrajectories
alienItemLevels
mcdPatches
converter
soldiers
commendations
enviroEffects
startingConditions
```

---

## Damage Type Enum

Used in `items[].damageType`:

| Value | Name |
|---|---|
| 0 | AP (Armor-Piercing) |
| 1 | Incendiary |
| 2 | HE (High Explosive) |
| 3 | Laser |
| 4 | Plasma |
| 5 | Stun |
| 6 | Melee |
| 7 | Acid |
| 8 | Smoke |

---

## Battle Type Enum

Used in `items[].battleType`:

| Value | Name | Notes |
|---|---|---|
| 1 | Firearm | Standard ranged weapon |
| 2 | Ammo | Ammunition clip |
| 3 | MediKit | Healing item |
| 4 | Scanner | Motion scanner |
| 5 | MindProbe | Mind probe |
| 6 | PsiAmp | Psi amplifier |
| 7 | Grenade | Thrown explosive |
| 8 | ProximityGrenades | Proximity mine |
| 9 | MediKit (secondary) | Alternate medkit type |
| 10 | BlasterLauncher | Guided projectile weapon |
| 11 | Corpse | Soldier/alien corpse item |
