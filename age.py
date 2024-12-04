#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
df = pd.read_csv('age_clean.csv')

# Function to plot population distribution by age group for each city
def plot_age_group_distribution(data, cities) -> plt:
    """
    Generates bar charts for the population distribution by age group for each city.

    Args:
        data (DataFrame): DataFrame with population data by age group.
        cities (list): List of city names to plot.
    """
    # Rename the age group columns to be more readable
    age_group_names = {
        'UNDER5_TOT': 'Under 5 Years',
        'AGE513_TOT': 'Ages 5-13 Years',
        'AGE1417_TOT': 'Ages 14-17 Years',
        'AGE1824_TOT': 'Ages 18-24 Years',
        'AGE2544_TOT': 'Ages 25-44 Years',
        'AGE4564_TOT': 'Ages 45-64 Years',
        'AGE65PLUS_TOT': '65+ Years'
    }
    city_colors = {
        "Seattle": "#40c9cd",
        "Los Angeles": "#e5c343",
        "New York City": "#b8b9b8",
        "Chicago": "#66aff0",
        "Boston": "#c62205",
        "Houston": "darkblue",
        "Miami": "#ff73ce"
    }
    # Create a new figure for each city
    plots = []  # List to store plot objects
    
    for city in cities:
        # Filter the data for the current city and for the year 2023
        city_data = data[(data['NAME'].str.contains(city, case=False))]
        
        # If no data for the city or year 2023, skip
        if city_data.empty:
            continue
        
        # Extract the data for the specified city (we assume there will be only one row after filtering by city and year)
        city_data_row = city_data.iloc[0]
        
        # Extract the values for each age group
        age_values = [city_data_row[age_group] for age_group in age_group_names.keys()]
        
        # Create a bar plot for the age distribution
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(age_group_names.values(), age_values, color=city_colors.get(city, 'gray'))
        
        # Set plot labels and title
        ax.set_title(f'Population by Age Group for {city} (Year 2023)')
        ax.set_xlabel('Age Group')
        ax.set_ylabel('Population')
        ax.grid(axis='y', linestyle='--', linewidth=0.7)
        plt.tight_layout()

        # Append the figure to the list of plots
        plots.append(fig)
    
    return plots

# List of cities to plot (from the 'NAME' column)
cities = ["Seattle", "Los Angeles", "New York City", "Chicago", "Boston", "Houston", "Miami"]

# Call the function to generate plots
plots = plot_age_group_distribution(df, cities)

# Display all plots
for plot in plots:
    plt.show()
