html = """
<html>
<head>
<title>Department Website</title>
</head>
<body>
<h1>Computer Science Department</h1>
<p>Welcome to our department website.</p>

<h2>Faculty</h2>
<ul>
<li>Dr. Kumar - HOD</li>
<li>Dr. Priya - Professor</li>
</ul>

<h2>Contact</h2>
<p>Email: cse@college.edu</p>
</body>
</html>
"""

with open("department.html", "w") as file:
    file.write(html)

print("Website created successfully!")
