"""Tests for the OXCE mod validation script."""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "scripts" / "validate_mod.py"
FIXTURES = Path(__file__).parent / "fixtures"


def run_validator(mod_path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(mod_path)],
        capture_output=True,
        text=True,
    )


class TestValidMods:
    def test_balance_mod_passes(self):
        result = run_validator(FIXTURES / "valid-balance-mod")
        assert result.returncode == 0, f"stderr: {result.stderr}"

    def test_new_item_mod_passes(self):
        result = run_validator(FIXTURES / "valid-new-item-mod")
        assert result.returncode == 0, f"stderr: {result.stderr}"


class TestInvalidMods:
    def test_no_metadata_fails(self):
        result = run_validator(FIXTURES / "invalid-no-metadata")
        assert result.returncode == 1
        assert "metadata.yml" in result.stderr.lower()

    def test_bad_yaml_fails(self):
        result = run_validator(FIXTURES / "invalid-bad-yaml")
        assert result.returncode == 1
        assert "yaml" in result.stderr.lower() or "parse" in result.stderr.lower()

    def test_unknown_section_fails(self):
        result = run_validator(FIXTURES / "invalid-unknown-section")
        assert result.returncode == 1
        assert "weapons" in result.stderr.lower()

    def test_bad_metadata_fails(self):
        result = run_validator(FIXTURES / "invalid-bad-metadata")
        assert result.returncode == 1
        assert "author" in result.stderr.lower() or "master" in result.stderr.lower()


class TestEdgeCases:
    def test_nonexistent_path_fails(self):
        result = run_validator(Path("/tmp/nonexistent-oxce-mod-abc123"))
        assert result.returncode == 1

    def test_no_rul_files_fails(self, tmp_path):
        metadata = tmp_path / "metadata.yml"
        metadata.write_text(
            'name: "Empty"\nversion: "1.0"\n'
            'description: "No rul files"\nauthor: "Test"\nmaster: xcom1\n'
        )
        result = run_validator(tmp_path)
        assert result.returncode == 1
        assert "rul" in result.stderr.lower()
