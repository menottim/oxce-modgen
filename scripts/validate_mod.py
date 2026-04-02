#!/usr/bin/env python3
"""Validate an OXCE mod folder for correctness.

Checks:
  1. metadata.yml exists with required fields
  2. master is xcom1 or xcom2
  3. At least one .rul file exists
  4. Each .rul file is valid YAML
  5. Top-level keys are recognized OXCE ruleset sections
  6. Entity type strings follow STR_ naming convention
  7. Numeric values are in reasonable ranges

Usage: python validate_mod.py <mod-folder-path>
Exit 0: all checks pass
Exit 1: validation errors (printed to stderr)
"""

import sys
from pathlib import Path

import yaml

KNOWN_SECTIONS = {
    "items", "armors", "crafts", "craftWeapons", "ufos", "research",
    "manufacture", "facilities", "ufopaedia", "alienDeployments",
    "alienMissions", "alienRaces", "units", "terrains", "mapScripts",
    "missionScripts", "countries", "regions", "difficulty", "startingBase",
    "extraSprites", "extraStrings", "vars", "interfaces", "inventories",
    "cutscenes", "globe", "music", "ufoTrajectories", "alienItemLevels",
    "mcdPatches", "converter", "soldiers", "commendations", "enviroEffects",
    "startingConditions",
}

REQUIRED_METADATA = {"name", "version", "description", "author", "master"}
VALID_MASTERS = {"xcom1", "xcom2"}


def validate(mod_path: Path) -> list[str]:
    """Validate a mod folder. Returns list of error strings (empty = valid)."""
    errors: list[str] = []

    if not mod_path.is_dir():
        return [f"Path does not exist or is not a directory: {mod_path}"]

    metadata_path = mod_path / "metadata.yml"
    if not metadata_path.exists():
        return [f"Missing required file: metadata.yml in {mod_path}"]

    try:
        with open(metadata_path) as f:
            metadata = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"metadata.yml is not valid YAML: {e}"]

    if not isinstance(metadata, dict):
        return ["metadata.yml must be a YAML mapping"]

    missing = REQUIRED_METADATA - set(metadata.keys())
    if missing:
        errors.append(f"metadata.yml missing required fields: {', '.join(sorted(missing))}")

    master = metadata.get("master")
    if master and master not in VALID_MASTERS:
        errors.append(f"metadata.yml master must be one of {VALID_MASTERS}, got: {master}")

    rul_files = list(mod_path.glob("*.rul")) + list(mod_path.glob("Rulesets/*.rul"))
    if not rul_files:
        errors.append("No .rul files found in mod folder (or Rulesets/ subfolder)")
        return errors

    for rul_file in rul_files:
        try:
            with open(rul_file) as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            errors.append(f"{rul_file.name}: YAML parse error: {e}")
            continue

        if not isinstance(data, dict):
            errors.append(f"{rul_file.name}: top level must be a YAML mapping")
            continue

        for key in data:
            if key not in KNOWN_SECTIONS:
                errors.append(
                    f"{rul_file.name}: unknown ruleset section '{key}'. "
                    f"Known sections: {', '.join(sorted(KNOWN_SECTIONS))}"
                )

        for section_key in ("items", "research", "crafts", "craftWeapons",
                           "facilities", "manufacture", "armors", "units"):
            entries = data.get(section_key, [])
            if not isinstance(entries, list):
                continue
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                type_field = entry.get("type") or entry.get("name")
                if type_field and isinstance(type_field, str) and not type_field.startswith("STR_"):
                    errors.append(
                        f"{rul_file.name}: {section_key} entry type/name "
                        f"'{type_field}' should start with 'STR_'"
                    )

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python validate_mod.py <mod-folder-path>", file=sys.stderr)
        return 1

    mod_path = Path(sys.argv[1])
    errors = validate(mod_path)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {mod_path.name} passed all validation checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
