import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "data.csv"
df = pd.read_csv(file_path)

# Convert 'Visit Date' to datetime
df['Visit Date'] = pd.to_datetime(df['Visit Date'], dayfirst=True)

# Employee Performance Analysis
plt.figure(figsize=(10, 5))
sns.barplot(x=df['Employee'], y=df['Service Time (min)'], ci=None, palette='coolwarm')
plt.title('Average Service Time per Employee')
plt.xlabel('Employee')
plt.ylabel('Service Time (min)')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Employee'], y=df['Employee Rating'], palette='viridis')
plt.title('Employee Ratings Distribution')
plt.xlabel('Employee')
plt.ylabel('Employee Rating')
plt.xticks(rotation=45)
plt.show()

# Water Consumption Analysis
plt.figure(figsize=(10, 5))
sns.barplot(x=df['Service'], y=df['Water Consumption (liters)'], ci=None, palette='magma')
plt.title('Total Water Consumption per Service Type')
plt.xlabel('Service Type')
plt.ylabel('Water Consumption (liters)')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['Revenue'], y=df['Water Consumption (liters)'], hue=df['Service'], palette='coolwarm')
plt.title('Revenue vs Water Consumption')
plt.xlabel('Revenue')
plt.ylabel('Water Consumption (liters)')
plt.show()

# Equipment Maintenance Analysis
plt.figure(figsize=(10, 5))
sns.histplot(df['Maintenance Frequency (weeks)'], bins=10, kde=True, color='blue')
plt.title('Maintenance Frequency Distribution')
plt.xlabel('Maintenance Frequency (weeks)')
plt.ylabel('Count')
plt.show()
