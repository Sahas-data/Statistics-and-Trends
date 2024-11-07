# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ssl

# Bypass SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Load the 'penguins' dataset from seaborn
def load_dataset():
    data = sns.load_dataset("penguins")
    return data

# Display the first few rows and summary of the dataset
def show_data_overview(data):
    print("First few rows of the dataset:")
    print(data.head(), "\n")
    print("Summary statistics of the dataset:")
    print(data.describe(), "\n")

# Plot histogram for bill length
def plot_bill_length_histogram(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['bill_length_mm'], kde=True, color='skyblue')
    plt.title("Histogram of Bill Length")
    plt.xlabel("Bill Length (mm)")
    plt.ylabel("Frequency")
    plt.show()

# Plot boxplot for body mass by species
def plot_body_mass_boxplot(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='species', y='body_mass_g', data=data, palette='coolwarm')
    plt.title("Body Mass by Species")
    plt.xlabel("Species")
    plt.ylabel("Body Mass (g)")
    plt.show()

# Scatterplot of bill length vs. flipper length
def plot_scatter_bill_flipper(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='bill_length_mm', y='flipper_length_mm', hue='species', data=data, palette='Set2')
    plt.title("Scatterplot of Bill Length vs. Flipper Length")
    plt.xlabel("Bill Length (mm)")
    plt.ylabel("Flipper Length (mm)")
    plt.legend(title="Species")
    plt.show()

# Heatmap for correlation matrix
def plot_correlation_heatmap(data):
    plt.figure(figsize=(12, 8))
    numeric_data = data.select_dtypes(include='number')
    correlation = numeric_data.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

# Line plot for body mass by species and sex
def plot_line_body_mass(data):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='species', y='body_mass_g', hue='sex', marker='o', data=data, palette='viridis')
    plt.title("Line Plot of Body Mass by Species and Sex")
    plt.xlabel("Species")
    plt.ylabel("Body Mass (g)")
    plt.show()

# Violin plot for bill depth by species
def plot_violin_bill_depth(data):
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='species', y='bill_depth_mm', data=data, palette='muted')
    plt.title("Violin Plot of Bill Depth by Species")
    plt.xlabel("Species")
    plt.ylabel("Bill Depth (mm)")
    plt.show()

# Main function to run all analyses
def main():
    data = load_dataset()
    show_data_overview(data)
    plot_bill_length_histogram(data)
    plot_body_mass_boxplot(data)
    plot_scatter_bill_flipper(data)
    plot_correlation_heatmap(data)
    plot_line_body_mass(data)
    plot_violin_bill_depth(data)

# Execute the main function
if __name__ == "__main__":
    main()


