import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset from sklearn
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]  # Add species column

# Display first 5 rows
print("First 5 rows:")
display(iris_df.head())

# Check data types and missing values
print("\nData Info:")
print(iris_df.info())

print("\nMissing Values:")
print(iris_df.isnull().sum())

print("Summary Statistics:")
display(iris_df.describe())
# Mean of numerical columns per species
species_stats = iris_df.groupby('species').mean()
display(species_stats)
plt.figure(figsize=(10, 4))
plt.plot(iris_df.index, iris_df['sepal length (cm)'], color='green')
plt.title("Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 5))
iris_df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.xticks(rotation=0)
plt.show()
plt.figure(figsize=(8, 5))
sns.histplot(iris_df['sepal width (cm)'], bins=15, kde=True, color='purple')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=iris_df,
    x='sepal length (cm)',
    y='petal length (cm)',
    hue='species',
    palette='viridis'
)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()
