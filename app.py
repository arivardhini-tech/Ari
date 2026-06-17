# app.py

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Computer Science Department</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 40px;
        }

        .container {
            background: white;
            padding: 20px;
            border-radius: 10px;
        }

        h1 {
            color: navy;
        }

        h2 {
            color: darkgreen;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Computer Science Department</h1>

        <p>Welcome to our department website.</p>

        <h2>About Us</h2>
        <p>
            The Computer Science Department provides quality education
            in programming, data science, artificial intelligence,
            and software engineering.
        </p>

        <h2>Faculty</h2>
        <ul>
            <li>Dr. Kumar - HOD</li>
            <li>Dr. Priya - Professor</li>
            <li>Dr. Raj - Assistant Professor</li>
        </ul>

        <h2>Courses Offered</h2>
        <ul>
            <li>Python Programming</li>
            <li>Data Structures</li>
            <li>Database Management Systems</li>
            <li>Web Development</li>
        </ul>

        <h2>Contact</h2>
        <p>Email: cse@college.edu</p>
        <p>Phone: +91 9876543210</p>
    </div>
</body>
</html>
"""

with open("department.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Website created successfully!")
print("Open department.html in your browser.")
