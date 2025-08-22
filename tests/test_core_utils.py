from semver import Version
from vrz.core import Vrz
from vrz.git_utils import Git


def test_latest_version_from_poetry():
    vrz = Vrz()
    assert vrz.latest() is not None
