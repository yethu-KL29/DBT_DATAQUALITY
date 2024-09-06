html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dbt Manifest Visualization</title>
    <style>
        body { font-family: Arial, sans-serif; }
        img { display: block; margin: 0 auto; }
        .chart-container { text-align: center; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>dbt Manifest Visualization</h1>
    <h2>Resource Type Count</h2>
    <div class="chart-container">
        <img src="resource_type_count.png" alt="Resource Type Count">
    </div>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html_content)
