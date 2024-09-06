# dbt Manifest Visualizations

This project provides visualizations for a dbt (Data Build Tool) manifest file, using various Seaborn plots and a table representation for data quality metrics. The visualizations help in understanding the structure, performance, and quality of your dbt models.

## Visualizations

### DBT Data Quality Metrics
![DBT Data Quality Metrics](images/metrics_table.png)

### Hexagonal Bin Plot of Unique ID and File Path Lengths
![Hexagonal Bin Plot](images/hexbin_plot.png)

### Heatmap of Schema vs Materialization
![Heatmap of Schema vs Materialization](images/heatmap_schema_materialization.png)

### Test Results Status Distribution
![Test Results Status Distribution](images/test_results_status_pie.png)

### Scatter Plot of Test Execution Times
![Scatter Plot of Test Execution Times](images/test_execution_times_scatter.png)

### KDE Plot of Execution Times
![KDE Plot of Execution Times](images/execution_times_kde.png)

### Violin Plot of Test Execution Times by Status
![Violin Plot of Test Execution Times by Status](images/execution_times_violin.png)

### Pair Plot of Model DataFrame Attributes
![Pair Plot of Model DataFrame Attributes](images/pair_plot_models.png)

### Distribution of Resource Types in dbt Manifest
![Distribution of Resource Types in dbt Manifest](images/resource_types_distribution.png)

### Box Plot of Unique IDs and File Paths Lengths
![Box Plot of Unique IDs and File Paths Lengths](images/boxplot_lengths.png)

## Usage

To use these visualizations, ensure that you have the required images in the `images` directory of your project. You can view the visualizations by opening the `index.html` file in a web browser.

## HTML Code

Below is the HTML code used to display these visualizations:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dbt Manifest Visualizations</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
        }
        .container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        .chart {
            margin: 20px;
            max-width: 600px;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>dbt Manifest Visualizations</h1>
    <div class="container">
        <div class="chart">
            <h2>DBT Data Quality Metrics</h2>
            <img src="images/metrics_table.png" alt="DBT Data Quality Metrics">
        </div>
        <div class="chart">
            <h2>Hexagonal Bin Plot of Unique ID and File Path Lengths</h2>
            <img src="images/hexbin_plot.png" alt="Hexagonal Bin Plot">
        </div>
        <div class="chart">
            <h2>Heatmap of Schema vs Materialization</h2>
            <img src="images/heatmap_schema_materialization.png" alt="Heatmap of Schema vs Materialization">
        </div>
        <div class="chart">
            <h2>Test Results Status Distribution</h2>
            <img src="images/test_results_status_pie.png" alt="Test Results Status Distribution">
        </div>
        <div class="chart">
            <h2>Scatter Plot of Test Execution Times</h2>
            <img src="images/test_execution_times_scatter.png" alt="Scatter Plot of Test Execution Times">
        </div>
        <div class="chart">
            <h2>KDE Plot of Execution Times</h2>
            <img src="images/execution_times_kde.png" alt="KDE Plot of Execution Times">
        </div>
        <div class="chart">
            <h2>Violin Plot of Test Execution Times by Status</h2>
            <img src="images/execution_times_violin.png" alt="Violin Plot of Test Execution Times by Status">
        </div>
        <div class="chart">
            <h2>Pair Plot of Model DataFrame Attributes</h2>
            <img src="images/pair_plot_models.png" alt="Pair Plot of Model DataFrame Attributes">
        </div>
        <div class="chart">
            <h2>Distribution of Resource Types in dbt Manifest</h2>
            <img src="images/resource_types_distribution.png" alt="Distribution of Resource Types in dbt Manifest">
        </div>
        <div class="chart">
            <h2>Box Plot of Unique IDs and File Paths Lengths</h2>
            <img src="images/boxplot_lengths.png" alt="Box Plot of Unique IDs and File Paths Lengths">
        </div>
    </div>
</body>
</html>
