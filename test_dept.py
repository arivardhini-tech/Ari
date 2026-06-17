import os
import importlib

def test_html_file_created():
    import dept
    importlib.reload(dept)

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
