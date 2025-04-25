from vrz.core import Poetry  # Replace with the actual path to your Poetry class

def test_inited_project_returns_project_name(tmp_path):
    # GIVEN a temporary directory for initializing a new Poetry project
    project_path = tmp_path

    # WHEN initializing the project using the init_project method
    poetry = Poetry.init_project(project_path)

    # THEN the project name should match the name of the temporary directory
    project_name = poetry.project_name()
    assert project_name == tmp_path.name.replace("_", "-")
