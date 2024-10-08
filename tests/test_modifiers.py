import pathlib
import shutil

import pytest

import pyprojectize

HERE = pathlib.Path(__file__).parent
ORIGINAL = HERE / "original.spec"
SPECS = set(HERE.glob("*.spec")) - {ORIGINAL}
SPEC_PARAMS = {pytest.param(s, id=s.stem) for s in SPECS}


def test_all_modifiers_have_spec_files():
    expected = {HERE / f"{m}.spec" for m in pyprojectize._modifiers}
    assert expected
    assert SPECS >= expected


@pytest.mark.parametrize("expectedspec", SPEC_PARAMS)
def test_spec(expectedspec, tmp_path, monkeypatch):
    testspec = tmp_path / "testspec.spec"
    shutil.copy(ORIGINAL, testspec)
    if expectedspec.stem == "__all__":
        pyprojectize.main([str(testspec)])
    else:
        for modifier in expectedspec.stem.split("__"):
            pyprojectize.main([str(testspec), "-o", modifier])
    assert expectedspec.read_text() == testspec.read_text()
