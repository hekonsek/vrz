import os
import shlex
import subprocess

from vrz.core import Git


def test_list_tags_sorted_alphanumerically(tmp_path):
    repo_path = tmp_path / "repo"
    repo_path.mkdir()

    subprocess.run(
        shlex.split("git init"),
        cwd=repo_path,
        check=True,
        capture_output=True,
        text=True,
    )
    (repo_path / "a.txt").write_text("content")
    subprocess.run(
        shlex.split("git add a.txt"),
        cwd=repo_path,
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        shlex.split("git commit -m 'init'"),
        cwd=repo_path,
        check=True,
        capture_output=True,
        text=True,
    )

    for tag in ["v2", "v10", "v1"]:
        subprocess.run(
            shlex.split(f"git tag {shlex.quote(tag)}"),
            cwd=repo_path,
            check=True,
            capture_output=True,
            text=True,
        )

    cwd = os.getcwd()
    os.chdir(repo_path)
    try:
        tags = Git().list_tags()
    finally:
        os.chdir(cwd)

    assert tags == ["v1", "v2", "v10"]

