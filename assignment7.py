# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# --- STEP 1: LOAD THE DATASET ---
# (Replace 'your_dataset.csv' with the actual file)
try:
    df = pd.read_csv('your_dataset.csv')  # For CSV files
    # df = pd.read_excel('your_dataset.xlsx')  # For Excel files
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")

# --- STEP 2: EXPLORE THE DATA ---
print("\n--- Data Exploration ---")
# Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Basic statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# --- STEP 3: DATA ANALYSIS ---
print("\n--- Basic Analysis ---")
# Example: Mean of a numeric column (adjust column name)
if 'numeric_column' in df.columns:
    mean_value = df['numeric_column'].mean()
    print(f"\nMean of 'numeric_column': {mean_value:.2f}")

# Example: Count of categories (adjust column name)
if 'category_column' in df.columns:
    category_counts = df['category_column'].value_counts()
    print("\nCategory Distribution:")
    print(category_counts)

# --- STEP 4: DATA VISUALIZATION ---
print("\n--- Visualizations ---")
plt.figure(figsize=(10, 6))


# Bar plot for categories
if 'category_column' in df.columns:
    plt.subplot(1, 2, 2)
    df['category_column'].value_counts().plot(kind='bar', color='salmon')
    plt.title("Category Counts")
    plt.xlabel("Category")
    plt.ylabel("Count")

plt.tight_layout()
plt.show()

# --- STEP 5: FINDINGS & OBSERVATIONS ---
print("\n--- Key Findings ---")
print("1. The dataset contains X rows and Y columns.")
print("2. Missing values detected in [column_name] (if any).")
print("3. The distribution of [numeric_column] shows [skewness/trend].")
print("4. The most frequent category in [category_column] is [value].")