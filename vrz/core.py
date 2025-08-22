"""Core utilities for vrz.

Currently this module provides the :class:`VersionSubstitution` helper which
allows replacing version strings inside arbitrary files.  Git and Poetry
utilities used to live here, but have been moved into dedicated modules to
keep concerns separated.
"""


class VersionSubstitution:
    """Replace occurrences of a version string in a file."""

    def replace_version(self, file_path: str, old_version: str, new_version: str):
        with open(file_path, "r") as file:
            content = file.read()

        new_content = content.replace(old_version, new_version)

        with open(file_path, "w") as file:
            file.write(new_content)


__all__ = ["VersionSubstitution"]

