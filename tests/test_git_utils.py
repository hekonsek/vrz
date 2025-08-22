import shlex
import subprocess

from vrz.git_utils import Git


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

    tags = Git(repo_path).list_tags()

    assert tags == ["v1", "v2", "v10"]


def test_should_find_latest_version():
    Git().fetch_tags()
    assert Git().latest_version() is not None