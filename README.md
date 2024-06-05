# Visualization Scripts

This repository contains a collection of Python scripts to create various visualizations using the Titanic dataset as example. These scripts are designed to be generic and reusable for other datasets with minimal modifications.

Link to Titanic dataset: https://www.kaggle.com/datasets/brendan45774/test-file

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Example Plots](#example-plots)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/titanic-visualizations.git
    cd titanic-visualizations
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the Titanic dataset CSV file named `tested.csv` in the root directory of the repository.

2. Run the script to generate the desired plots. Example:
    ```sh
    python generate_plots.py
    ```

## Visualizations

The following visualizations can be generated using the provided scripts:

1. **Bar Chart**: Survival rate by gender
2. **Histogram**: Age distribution of passengers
3. **Scatter Plot**: Age vs. Fare
4. **Pairwise Relationships**: Pairwise relationships of selected columns
5. **Violin Plot**: Fare distribution by class and survival status
6. **Stacked Bar Chart**: Number of passengers by class and embarkation port
7. **3D Scatter Plot**: Age, Fare, and Pclass
8. **Sunburst Chart**: Hierarchical distribution of classes and survival
9. **Density Plot**: Age distribution by survival status
10. **Correlation Heatmap**: Correlation heatmap of numerical features
11. **Boxplot**: Age distribution by survival status
12. **Pie Chart**: Survival status proportion
13. **Count Plot**: Number of passengers by class
14. **Strip Plot**: Age distribution by class and survival status
15. **Heatmap of Missing Values**: Pattern of missing values in the dataset

## Example Plots

Here are some example plots generated using the provided scripts:

1. **Bar Chart**: ![Survival Rate by Gender](images/survival_rate_by_gender.png)
2. **Histogram**: ![Age Distribution of Passengers](images/age_distribution.png)
3. **Scatter Plot**: ![Age vs. Fare](images/age_vs_fare.png)
4. **Pairwise Relationships**: ![Pairwise Relationships](images/facet_grid.png)
5. **Violin Plot (Fare)**: ![Fare Distribution by Class and Survival Status](images/violin_fare_class_survival.png)
6. **Violin Plot (Age)**: ![Age Distribution by Class and Survival Status](images/violin_age_class_survival.png)
7. **Stacked Bar Chart**: ![Number of Passengers by Class and Embarkation Port](images/stacked_bar_class_embarked.png)
8. **3D Scatter Plot**: ![3D Scatter Plot of Age, Fare, and Pclass](images/3d_scatter_age_fare_pclass.png)
9. **Sunburst Chart**: ![Hierarchical Distribution of Classes and Survival](images/sunburst_class_survival.html)
10. **Density Plot**: ![Age Distribution by Survival Status](images/density_age_survival.png)
11. **Correlation Heatmap**: ![Correlation Heatmap of Titanic Dataset](images/correlation_heatmap.png)
12. **Boxplot**: ![Age Distribution by Survival Status](images/boxplot_age_survival.png)
13. **Pie Chart**: ![Survival Status Proportion](images/pie_chart_survival.png)
14. **Count Plot (Class)**: ![Number of Passengers by Class](images/count_plot_pclass.png)
15. **Count Plot (Embarked)**: ![Count of Passengers by Embarkation Port](images/count_plot_embarked.png)
16. **Strip Plot**: ![Age Distribution by Class and Survival Status](images/strip_plot_age_class_survival.png)
17. **Heatmap of Missing Values**: ![Heatmap of Missing Values in Titanic Dataset](images/missing_values_heatmap.png)

To generate these images, run the example usage code provided in the script.


