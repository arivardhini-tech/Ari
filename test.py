html = """
<html>
<body>
<h1>Department Website Test</h1>
<p>Website is working successfully!</p>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html)

print("Test Passed! index.html created.")
