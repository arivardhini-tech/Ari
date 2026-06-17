 import os
import importlib

def test_html_file_created():
    # Importing dept.py executes the code
    import dept
    importlib.reload(dept)

    # Check if the file was created
    assert os.path.exists("department.html")


def test_html_content():
    import dept
    importlib.reload(dept)

    with open("department.html", "r") as file:
        content = file.read()

    assert "<title>Department Website</title>" in content
    assert "Computer Science Department" in content
    assert "Dr. Kumar - HOD" in content
    assert "cse@college.edu" in content
