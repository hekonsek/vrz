import sys
from pathlib import Path

# Ensure the package root is available on sys.path so that "vrz" can be imported
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from vrz.core import Poetry

def test_inited_project_returns_project_name(tmp_path):
    # GIVEN a temporary directory for initializing a new Poetry project
    project_path = tmp_path

    # WHEN initializing the project using the init_project method
    poetry = Poetry.init_project(project_path)

    # THEN the project name should match the name of the temporary directory
    project_name = poetry.project_name()
    assert project_name == tmp_path.name.replace("_", "-")

def test_is_poetry_project_true(tmp_path):
    # GIVEN an initialized Poetry project
    Poetry.init_project(tmp_path)

    # THEN the directory should be recognized as a Poetry project
    assert Poetry(tmp_path).is_poetry_project()


def test_is_poetry_project_false(tmp_path):
    # No pyproject.toml file present
    assert not Poetry(tmp_path).is_poetry_project()
