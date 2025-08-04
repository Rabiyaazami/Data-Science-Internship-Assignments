import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Optional: Print the current directory for debugging
print("Working directory:", os.getcwd())

# Load the dataset
df = pd.read_csv('kerala.csv')

# Preview the data
print("First 5 rows:")
print(df.head())

# Summary of the dataset
print("\nData Info:")
print(df.info())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Correlation heatmap
plt.figure(figsize=(10, 6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='viridis')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Optional: Distribution of target column (guessing 'Damage' or similar, adjust name if needed)
if 'Damage' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Damage'], kde=True)
    plt.title("Distribution of Flood Damage")
    plt.xlabel("Damage (₹ or Units)")
    plt.tight_layout()
    plt.show()
else:
    print("\nColumn 'Damage' not found – update the column name based on your dataset.")
