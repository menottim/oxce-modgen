---
name: OXCE Mod Generator
description: >
  Generate installable OpenXcom Extended (OXCE) mods from natural language.
  Use when the user says /modgen, asks to create an OXCE mod, or wants to
  modify OpenXcom game balance, items, research, crafts, or facilities.
  Fetches live vanilla stats, generates YAML rulesets, validates output.
---

# OXCE Mod Generator

Generate installable OpenXcom Extended mods from a natural language description.

## Workflow

### Phase 1: Understand Intent

Parse the user's description. Ask clarifying questions **one at a time**:

1. **What to change:** Which items, weapons, crafts, research topics, or facilities? All of a category or specific ones?
2. **How much:** Percentages, specific values, or relative adjustments?
3. **Which stats:** Cost, accuracy, damage, TU cost, research time, etc.?
4. **Target game:** UFO Defense (`xcom1`) or Terror From The Deep (`xcom2`)? Default to `xcom1`.
5. **Mod name:** Suggest one based on the description; let the user override.

Skip questions whose answers are obvious from the description. "Make plasma weapons more expensive" doesn't need question 1.

### Phase 2: Fetch Vanilla Stats

Based on what the mod touches, fetch the relevant vanilla `.rul` files.

Read `skills/modgen/references/mod-structure.md` for the fetch URL table. The base URL is:
`https://raw.githubusercontent.com/MeridianOXC/OpenXcom/oxce-plus/bin/standard/`

Use WebFetch to pull each needed `.rul` file. Extract only the entries relevant to the mod.

**Fetch failure:** If WebFetch fails, tell the user: "I couldn't fetch current vanilla stats (network issue or URL change). You can provide the values manually, or give me an alternative URL." Do not guess at stats.

Present current values and propose changes:

> "Current STR_PLASMA_RIFLE: costBuy 36900, accuracySnap 86, accuracyAimed 100
> Proposed: costBuy 73800 (+100%), accuracySnap 92 (+7%), accuracyAimed 110 (+10%)
> Look right?"

### Phase 3: Generate Mod

After the user approves values, generate the mod folder.

1. Create directory: `~/oxce-mods/<mod-name>/`
2. Write `metadata.yml` with name, version "1.0", description, author, and master
3. Write `<mod-name>.rul` with **only the changed fields** (OXCE merges on top of vanilla)
4. Show a summary of what was generated

Read `skills/modgen/references/common-patterns.md` for working examples of each mod type. Use the closest pattern as a template.

### Phase 4: Validate

Run the validation script:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/validate_mod.py" ~/oxce-mods/<mod-name>
```

If validation fails, fix the issues and re-validate. Common fixes:
- Unknown section name → check spelling against known sections in mod-structure.md
- Missing STR_ prefix → add it to type/name fields
- Missing metadata fields → add them

### Phase 5: Install Instructions

After validation passes, tell the user:

> **To install your mod:**
> 1. Copy `~/oxce-mods/<mod-name>/` to your OpenXcom `mods/` directory
> 2. Launch the game → Options → Mods
> 3. Enable "<mod-name>" and click OK
>
> The mod will take effect on next game load. It's safe to enable mid-campaign.

## Rules

- **Override only changed fields.** Never copy the full vanilla definition — OXCE merges mods on top.
- **Use STR_ prefix** for all type/name identifiers.
- **Reuse existing sprite indices** when creating new items (bigSprite, floorSprite, handSprite). Pick a visually similar existing item's sprites.
- **Always include extraStrings** when adding new items so they have display names.
- **One .rul file per mod** unless the mod is complex enough to warrant splitting.
- **Default author** to "ModGen" unless the user specifies.
- **Default version** to "1.0".
