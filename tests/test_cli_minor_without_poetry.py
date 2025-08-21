import os
import shlex
import subprocess
import sys
from pathlib import Path


def test_minor_command_reads_version_from_git_tags(tmp_path):
    repo_path = tmp_path / "repo"
    repo_path.mkdir()

    subprocess.run(shlex.split("git init -b master"), cwd=repo_path, check=True, capture_output=True, text=True)
    subprocess.run(shlex.split("git config user.email test@example.com"), cwd=repo_path, check=True, capture_output=True, text=True)
    subprocess.run(shlex.split("git config user.name Test"), cwd=repo_path, check=True, capture_output=True, text=True)

    (repo_path / "a.txt").write_text("content")
    subprocess.run(shlex.split("git add a.txt"), cwd=repo_path, check=True, capture_output=True, text=True)
    subprocess.run(shlex.split("git commit -m initial"), cwd=repo_path, check=True, capture_output=True, text=True)

    subprocess.run(shlex.split("git tag v1.2.3"), cwd=repo_path, check=True, capture_output=True, text=True)

    # Setup remote so pushing tags succeeds
    remote_path = tmp_path / "remote.git"
    subprocess.run(shlex.split(f"git init --bare {remote_path}"), check=True, capture_output=True, text=True)
    subprocess.run(shlex.split(f"git remote add origin {remote_path}"), cwd=repo_path, check=True, capture_output=True, text=True)
    subprocess.run(shlex.split("git push -u origin master"), cwd=repo_path, check=True, capture_output=True, text=True)
    subprocess.run(shlex.split("git push origin v1.2.3"), cwd=repo_path, check=True, capture_output=True, text=True)

    env = os.environ.copy()
    env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1])

    result = subprocess.run(
        [sys.executable, "-m", "vrz.cli", "minor"],
        cwd=repo_path,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Version bumped to 1.3.0." in result.stdout

    tags = subprocess.run(
        shlex.split("git tag"),
        cwd=repo_path,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip().splitlines()
    assert "v1.3.0" in tags
