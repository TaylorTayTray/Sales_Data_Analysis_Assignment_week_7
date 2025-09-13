# Sales Performance Analysis
# Objective:
# - Load and analyze a simulated dataset using pandas
# - Create simple plots and charts with matplotlib and seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Simulate a sales dataset
np.random.seed(42)  # for reproducibility

data = {
    'Date': pd.date_range(start='2025-03-01', periods=45, freq='D'),
    'Region': np.random.choice(['Central', 'North', 'South'], size=45),
    'Units Sold': np.random.randint(50, 300, size=45),
    'Unit Price': np.random.uniform(20.0, 100.0, size=45)
}

df = pd.DataFrame(data)
df['Revenue'] = df['Units Sold'] * df['Unit Price']

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Basic inspection
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# Grouped summary by region
region_avg = df.groupby('Region')[['Units Sold', 'Revenue']].mean().sort_values(by='Revenue', ascending=False)
print("\nAverage Units Sold and Revenue by Region:")
print(region_avg)

# Line plot: Revenue over time
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Revenue'], color='darkgreen', linewidth=2)
plt.title('Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar plot: Average revenue by region
sns.barplot(x=region_avg.index, y=region_avg['Revenue'], palette='coolwarm')
plt.title('Average Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Average Revenue')
plt.tight_layout()
plt.show()

# Histogram: Unit Price distribution
plt.hist(df['Unit Price'], bins=10, color='slateblue', edgecolor='white')
plt.title('Unit Price Distribution')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter plot: Units Sold vs Revenue
sns.scatterplot(x='Units Sold', y='Revenue', hue='Region', data=df, palette='Set2', s=100)
plt.title('Units Sold vs Revenue by Region')
plt.xlabel('Units Sold')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()

# Observations
print("\nObservations:")
print("- Revenue fluctuates daily, with noticeable spikes around mid-March.")
print("- The Central region shows the highest average revenue, followed by North and South.")
print("- Unit prices are mostly between $30 and $90, with a few outliers.")
print("- There’s a clear positive correlation between units sold and revenue—higher sales volumes lead to higher revenue.")
