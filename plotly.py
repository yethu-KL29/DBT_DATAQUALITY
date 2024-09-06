import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict, Counter

# Load manifest.json
with open('target/manifest.json') as f:
    manifest = json.load(f)

# Load run_results.json
with open('target/run_results.json') as f:
    run_results = json.load(f)

# Extract relevant data
models = manifest['nodes']
test_results = [result for result in run_results['results'] if 'test' in result['unique_id']]

# Create DataFrames
model_data = []
for model_id, model in models.items():
    model_data.append({
        'model_id': model_id,
        'resource_type': model['resource_type'],
        'materialized': model['config'].get('materialized', 'unknown'),
        'schema': model.get('schema', 'unknown'),
        'unique_id_length': len(model['unique_id']),
        'file_path_length': len(model['path'])
    })

df_models = pd.DataFrame(model_data)

test_data = []
for result in test_results:
    test_data.append({
        'unique_id': result['unique_id'],
        'status': result['status'],
        'execution_time': result.get('execution_time', np.nan),
        'message': result.get('message', '')
    })

df_tests = pd.DataFrame(test_data)

# Aggregated metrics
metrics = {
    'Total Tests': len(df_tests),
    'Passed Tests': sum(df_tests['status'] == 'pass'),
    'Failed Tests': sum(df_tests['status'] == 'error'),
    'Tests with Execution Time': sum(~df_tests['execution_time'].isna()),
    'Tests with Timing': sum(df_tests['execution_time'] > 0)
}

# Accuracy, Completeness, and Consistency calculations
metrics['Accuracy (%)'] = (metrics['Passed Tests'] / metrics['Total Tests']) * 100
metrics['Completeness (%)'] = (metrics['Tests with Timing'] / metrics['Total Tests']) * 100
metrics['Consistency (%)'] = (metrics['Passed Tests'] / metrics['Total Tests']) * 100
metrics['Unknown Timelines (%)'] = ((metrics['Total Tests'] - metrics['Tests with Timing']) / metrics['Total Tests']) * 100

# Convert metrics to DataFrame
df_metrics = pd.DataFrame(list(metrics.items()), columns=['Metric', 'Value'])

# Hexagonal Bin Plot
plt.figure(figsize=(12, 8))
plt.hexbin(df_models['unique_id_length'], df_models['file_path_length'], gridsize=30, cmap='Blues')
plt.colorbar(label='Count')
plt.xlabel('Unique ID Length')
plt.ylabel('File Path Length')
plt.title('Hexagonal Bin Plot of Unique ID and File Path Lengths')
plt.tight_layout()
plt.savefig('hexbin_plot.png')
plt.close()

# Heatmap of Schema vs Materialization
pivot_table = df_models.pivot_table(index='schema', columns='materialized', aggfunc='size', fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap of Schema vs Materialization')
plt.xlabel('Materialization Type')
plt.ylabel('Schema')
plt.tight_layout()
plt.savefig('heatmap_schema_materialization.png')
plt.close()

# Pie Chart of Test Status Distribution
status_counts = df_tests['status'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('muted'))
plt.title('Test Results Status Distribution')
plt.tight_layout()
plt.savefig('test_results_status_pie.png')
plt.close()

# Scatter Plot of Execution Times
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_tests.index, y='execution_time', hue='status', data=df_tests, palette='deep')
plt.title('Scatter Plot of Test Execution Times')
plt.xlabel('Test Index')
plt.ylabel('Execution Time (s)')
plt.tight_layout()
plt.savefig('test_execution_times_scatter.png')
plt.close()

# KDE Plot of Execution Times
plt.figure(figsize=(10, 6))
sns.kdeplot(df_tests['execution_time'].dropna(), shade=True, color='r')
plt.title('KDE Plot of Test Execution Times')
plt.xlabel('Execution Time (s)')
plt.ylabel('Density')
plt.tight_layout()
plt.savefig('execution_times_kde.png')
plt.close()

# Violin Plot of Execution Times by Status
plt.figure(figsize=(10, 6))
sns.violinplot(x='status', y='execution_time', data=df_tests, palette='muted')
plt.title('Violin Plot of Test Execution Times by Status')
plt.xlabel('Test Status')
plt.ylabel('Execution Time (s)')
plt.tight_layout()
plt.savefig('execution_times_violin.png')
plt.close()

# Pair Plot of df_models DataFrame
sns.pairplot(df_models[['unique_id_length', 'file_path_length', 'schema']], diag_kind='kde')
plt.suptitle('Pair Plot of Model DataFrame Attributes', y=1.02)
plt.tight_layout()
plt.savefig('pair_plot_models.png')
plt.close()

# Distribution of Resource Types in dbt Manifest
resource_types = defaultdict(int)
for model_id, model in models.items():
    resource_type = model['resource_type']
    resource_types[resource_type] += 1

plt.figure(figsize=(12, 8))
sns.barplot(x=list(resource_types.keys()), y=list(resource_types.values()), palette='pastel')
plt.xlabel('Resource Type')
plt.ylabel('Count')
plt.title('Distribution of Resource Types in dbt Manifest')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('resource_types_distribution.png')
plt.close()

# Box Plot of Unique IDs and File Paths Lengths
plt.figure(figsize=(12, 8))
sns.boxplot(data=[df_models['unique_id_length'], df_models['file_path_length']], palette='Set2')
plt.xlabel('Type')
plt.ylabel('Length')
plt.title('Box Plot of Unique IDs and File Paths Lengths')
plt.xticks([0, 1], ['Unique ID Length', 'File Path Length'])
plt.tight_layout()
plt.savefig('boxplot_lengths.png')
plt.close()

# Table Representation for Metrics
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df_metrics.values, colLabels=df_metrics.columns, cellLoc='center', loc='center')
table.scale(1, 1.5)
plt.title('DBT Data Quality Metrics')
plt.tight_layout()
plt.savefig('metrics_table.png')
plt.close()
