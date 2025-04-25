import shlex
import subprocess
import requests as request


class Poetry:
    def version_bump_minor(self):
        subprocess.run(
            shlex.split("poetry version minor"),
            check=True,
            capture_output=True,
            text=True,
        )

    def version_read(self):
        output = subprocess.run(
            shlex.split("poetry version -s"),
            check=True,
            capture_output=True,
            text=True,
        )
        return output.stdout.strip()

    def is_published(self, package_name):
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = request.get(url)
        return response.status_code != 404

    def is_current_project_published(self):
        project_name = self.project_name()
        return self.is_published(project_name)

    def publish(self):
        subprocess.run(
            shlex.split("poetry publish --build"),
            check=True,
            capture_output=True,
            text=True,
        )
        return True

    def project_name(self):
        output = subprocess.run(
            shlex.split("poetry version"),
            check=True,
            capture_output=True,
            text=True,
        )
        return output.stdout.split()[0].strip()


class Git:
    def is_git_repo(self):
        try:
            subprocess.run(
                shlex.split("git rev-parse --is-inside-work-tree"),
                check=True,
                capture_output=True,
                text=True,
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def create_tag(self, tag_name):
        subprocess.run(
            shlex.split(f"git tag {tag_name}"),
            check=True,
            capture_output=True,
            text=True,
        )

    def push_tag(self, tag_name):
        subprocess.run(
            shlex.split(f"git push origin {tag_name}"),
            check=True,
            capture_output=True,
            text=True,
        )

    def push(self):
        subprocess.run(
            shlex.split("git push"),
            check=True,
            capture_output=True,
            text=True,
        )

    def add(self, file: str):
        subprocess.run(
            shlex.split(f"git add {file}"),
            check=True,
            capture_output=True,
            text=True,
        )

    def commit(self, message: str):
        subprocess.run(
            shlex.split(f"git commit -m '{message}'"),
            check=True,
            capture_output=True,
            text=True,
        )


class VersionSubstitution:
    def replace_version(self, file_path: str, old_version: str, new_version: str):
        with open(file_path, "r") as file:
            content = file.read()

        new_content = content.replace(old_version, new_version)

        with open(file_path, "w") as file:
            file.write(new_content)
