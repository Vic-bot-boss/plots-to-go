import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px

# Load the dataset
data_path = 'titanic_dataset.csv'  # Change this to your actual file path
df = pd.read_csv(data_path)

# Set global styles
def set_global_styles():
    sns.set(style="whitegrid", palette="muted")
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'axes.titlesize': 16,
        'axes.labelsize': 14,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,
        'legend.fontsize': 12,
        'figure.dpi': 100,
    })

set_global_styles()
consistent_palette = sns.color_palette("viridis")

def save_plot(title, xlabel, ylabel, filename):
    """Helper function to set plot titles, labels, and save the figure."""
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f'images/{filename}.png')
    plt.close()

# Function to plot bar chart
def plot_bar_chart(df, x_col, y_col, title, xlabel, ylabel, filename, palette='viridis'):
    """Creates a bar chart for the mean of y_col grouped by x_col."""
    if x_col not in df.columns or y_col not in df.columns:
        raise ValueError(f"Columns {x_col} or {y_col} not found in DataFrame")
    sns.barplot(x=x_col, y=y_col, data=df, palette=palette)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot histogram
def plot_histogram(df, col, bins, kde, title, xlabel, ylabel, filename, color='blue'):
    """Creates a histogram for the specified column."""
    if col not in df.columns:
        raise ValueError(f"Column {col} not found in DataFrame")
    sns.histplot(df[col].dropna(), bins=bins, kde=kde, color=color)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot scatter plot
def plot_scatter(df, x_col, y_col, hue_col, title, xlabel, ylabel, filename, palette=consistent_palette):
    """Creates a scatter plot for the specified columns, colored by hue_col."""
    if x_col not in df.columns or y_col not in df.columns or hue_col not in df.columns:
        raise ValueError(f"Columns {x_col}, {y_col}, or {hue_col} not found in DataFrame")
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col, palette=palette)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot pairwise relationships
def plot_pairwise(df, hue_col, filename, palette='viridis'):
    """Creates a pairwise relationship plot for the dataframe, colored by hue_col."""
    if hue_col not in df.columns:
        raise ValueError(f"Column {hue_col} not found in DataFrame")
    g = sns.PairGrid(df.dropna(), hue=hue_col, palette=palette)
    g.map_diag(sns.histplot)
    g.map_offdiag(sns.scatterplot)
    g.add_legend()
    plt.savefig(f'images/{filename}.png')
    plt.close()

# Function to plot violin plot
def plot_violin(df, x_col, y_col, hue_col, split, title, xlabel, ylabel, filename, palette='muted'):
    """Creates a violin plot for the specified columns, split by hue_col."""
    if x_col not in df.columns or y_col not in df.columns or hue_col not in df.columns:
        raise ValueError(f"Columns {x_col}, {y_col}, or {hue_col} not found in DataFrame")
    plt.figure(figsize=(12, 8))
    sns.violinplot(x=x_col, y=y_col, hue=hue_col, data=df, split=split, palette=palette)
    plt.legend(title=hue_col)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot stacked bar chart
def plot_stacked_bar(df, x_col, stack_col, title, xlabel, ylabel, filename, colormap='viridis'):
    """Creates a stacked bar chart for the count of stack_col, grouped by x_col."""
    if x_col not in df.columns or stack_col not in df.columns:
        raise ValueError(f"Columns {x_col} or {stack_col} not found in DataFrame")
    df.groupby([x_col, stack_col]).size().unstack().plot(kind='bar', stacked=True, figsize=(10, 7), colormap=colormap)
    plt.legend(title=stack_col)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot 3D scatter plot
def plot_3d_scatter(df, x_col, y_col, z_col, hue_col, title, xlabel, ylabel, zlabel, filename, colormap='viridis'):
    """Creates a 3D scatter plot for the specified columns, colored by hue_col."""
    if x_col not in df.columns or y_col not in df.columns or z_col not in df.columns or hue_col not in df.columns:
        raise ValueError(f"Columns {x_col}, {y_col}, {z_col}, or {hue_col} not found in DataFrame")
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(df[x_col], df[y_col], df[z_col], c=df[hue_col], cmap=colormap, s=50)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.colorbar(sc, label=hue_col)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot sunburst chart
def plot_sunburst(df, path_cols, value_col, color_col, title, filename, colormap='viridis'):
    """Creates a sunburst chart for the specified columns."""
    if not all(col in df.columns for col in path_cols + [value_col, color_col]):
        raise ValueError(f"Some columns from {path_cols}, {value_col}, or {color_col} not found in DataFrame")
    fig = px.sunburst(df, path=path_cols, values=value_col, color=color_col, color_continuous_scale=colormap, title=title)
    fig.write_html(f'images/{filename}.html')

# Function to plot density plot
def plot_density(df, x_col, hue_col, fill, title, xlabel, ylabel, filename, palette='viridis'):
    """Creates a density plot for the specified column, split by hue_col."""
    if x_col not in df.columns or hue_col not in df.columns:
        raise ValueError(f"Columns {x_col} or {hue_col} not found in DataFrame")
    plt.figure(figsize=(12, 8))
    sns.kdeplot(data=df, x=x_col, hue=hue_col, fill=fill, common_norm=False, palette=palette)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot correlation heatmap
def plot_correlation_heatmap(df, title, filename, colormap='viridis'):
    """Creates a correlation heatmap for the dataframe."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap=colormap, cbar=True)
    save_plot(title, '', '', filename)

# Function to plot boxplot
def plot_boxplot(df, x_col, y_col, title, xlabel, ylabel, filename, palette='viridis'):
    """Creates a boxplot for the specified columns."""
    if x_col not in df.columns or y_col not in df.columns:
        raise ValueError(f"Columns {x_col} or {y_col} not found in DataFrame")
    plt.figure(figsize=(10, 8))
    sns.boxplot(x=x_col, y=y_col, data=df, palette=palette)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot pie chart
def plot_pie_chart(df, col, labels, title, filename, colormap='viridis'):
    """Creates a pie chart for the specified column."""
    if col not in df.columns:
        raise ValueError(f"Column {col} not found in DataFrame")
    counts = df[col].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette(colormap, len(labels)))
    save_plot(title, '', '', filename)

# Function to plot count plot
def plot_count_plot(df, col, title, xlabel, ylabel, filename, palette='viridis'):
    """Creates a count plot for the specified column."""
    if col not in df.columns:
        raise ValueError(f"Column {col} not found in DataFrame")
    sns.countplot(x=col, data=df, palette=palette)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot strip plot
def plot_strip_plot(df, x_col, y_col, hue_col, jitter, dodge, title, xlabel, ylabel, filename, palette='viridis'):
    """Creates a strip plot for the specified columns, colored by hue_col."""
    if x_col not in df.columns or y_col not in df.columns or hue_col not in df.columns:
        raise ValueError(f"Columns {x_col}, {y_col}, or {hue_col} not found in DataFrame")
    plt.figure(figsize=(12, 8))
    sns.stripplot(x=x_col, y=y_col, hue=hue_col, data=df, jitter=jitter, palette=palette, dodge=dodge)
    plt.legend(title=hue_col)
    save_plot(title, xlabel, ylabel, filename)

# Function to plot heatmap of missing values
def plot_missing_values_heatmap(df, title, filename, colormap='viridis'):
    """Creates a heatmap to visualize missing values in the dataframe."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.isnull(), cbar=False, cmap=colormap)
    save_plot(title, '', '', filename)

# Example usage with comments
# Bar chart: Survival rate by gender
plot_bar_chart(df, 'Sex', 'Survived', 'Survival Rate by Gender', 'Gender', 'Survival Rate', 'survival_rate_by_gender')

# Histogram: Age distribution
plot_histogram(df, 'Age', 30, True, 'Age Distribution of Passengers', 'Age', 'Frequency', 'age_distribution')

# Scatter plot: Age vs. Fare
plot_scatter(df, 'Age', 'Fare', 'Survived', 'Age vs. Fare', 'Age', 'Fare', 'age_vs_fare')

# Pairwise relationships: Pairwise relationships of selected columns
plot_pairwise(df[['Age', 'Fare', 'Pclass', 'Survived']], 'Survived', 'facet_grid')

# Violin plot: Fare distribution by class and survival status
plot_violin(df, 'Pclass', 'Fare', 'Survived', True, 'Fare Distribution by Class and Survival Status', 'Passenger Class', 'Fare', 'violin_fare_class_survival')

# Violin plot: Age distribution by class and survival status
plot_violin(df, 'Pclass', 'Age', 'Survived', True, 'Age Distribution by Class and Survival Status', 'Passenger Class', 'Age', 'violin_age_class_survival')

# Stacked bar chart: Number of passengers by class and embarkation port
plot_stacked_bar(df, 'Pclass', 'Embarked', 'Number of Passengers by Class and Embarkation Port', 'Passenger Class', 'Number of Passengers', 'stacked_bar_class_embarked')

# 3D scatter plot: Age, Fare, and Pclass
plot_3d_scatter(df, 'Age', 'Fare', 'Pclass', 'Survived', '3D Scatter Plot of Age, Fare, and Pclass', 'Age', 'Fare', 'Pclass', '3d_scatter_age_fare_pclass')

# Sunburst chart: Hierarchical distribution of classes and survival
plot_sunburst(df, ['Pclass', 'Sex', 'Survived'], 'PassengerId', 'Survived', 'Hierarchical Distribution of Classes and Survival', 'sunburst_class_survival')

# Density plot: Age distribution by survival status
plot_density(df, 'Age', 'Survived', True, 'Age Distribution by Survival Status', 'Age', 'Density', 'density_age_survival')

# Correlation heatmap: Correlation heatmap of numerical features
plot_correlation_heatmap(df.select_dtypes(include=[float, int]), 'Correlation Heatmap of Titanic Dataset', 'correlation_heatmap')

# Boxplot: Age distribution by survival status
plot_boxplot(df, 'Survived', 'Age', 'Age Distribution by Survival Status', 'Survived', 'Age', 'boxplot_age_survival')

# Pie chart: Survival status proportion
plot_pie_chart(df, 'Survived', ['Not Survived', 'Survived'], 'Survival Status Proportion', 'pie_chart_survival')

# Count plot: Number of passengers by class
plot_count_plot(df, 'Pclass', 'Number of Passengers by Class', 'Passenger Class', 'Number of Passengers', 'count_plot_pclass')

# Count plot: Count of passengers by embarkation port
plot_count_plot(df, 'Embarked', 'Count of Passengers by Embarkation Port', 'Embarkation Port', 'Number of Passengers', 'count_plot_embarked')

# Strip plot: Age distribution by class and survival status
plot_strip_plot(df, 'Pclass', 'Age', 'Survived', True, True, 'Age Distribution by Class and Survival Status', 'Passenger Class', 'Age', 'strip_plot_age_class_survival')

# Heatmap of missing values: Visualizes the pattern of missing values in the dataset
plot_missing_values_heatmap(df, 'Heatmap of Missing Values in Titanic Dataset', 'missing_values_heatmap')
