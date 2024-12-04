#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('mergedCrimeRates.csv')


# In[12]:


def plot_crime_rates(data, cities) -> plt:
    """
    Generates a histogram for each city's crime rates across the months of 2023 with specified colors.
    
    Args:
        data (DataFrame): DataFrame with 'series' as city names and monthly crime data.
        cities (list): List of city names to plot.
    """
    # Mapping of cities to their respective colors
    
    city_colors = {
        "Seattle": "#40c9cd",
        "Los Angeles": "#e5c343",
        "New York City": "#b8b9b8",
        "Chicago": "#66aff0",
        "Boston": "#c62205",
        "Houston": "darkblue",
        "Miami": "#ff73ce"
    }
    
    months = [col for col in data.columns if col != 'series']
    plots = []  # List to store plt objects

    
    for city in cities:
        # Filter the data for the current city
        city_data = data[data['series'] == city]
        
        # Plot the histogram using the city's specific color
        plt.figure(figsize=(10, 6))
        plt.bar(months, city_data.iloc[0, 1:].values, color=city_colors.get(city, 'gray'))
        plt.title(f'Violent Crime Reports for {city} (2023)')
        plt.xlabel('Month')
        plt.ylabel('Number of Crimes per Month')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', linewidth=0.7)
        plt.tight_layout()
        plt.show()
        
        plots.append(plt)
        return plots

# List of cities to plot
# cities = ["Seattle Police Department", "Los Angeles Police Department", 
#                   "New York City Police Department", "Chicago Police Department", 
#                   "Boston Police Department", "Houston Police Department", "Miami Police Department"]
cities = ["Seattle", "Los Angeles", 
                  "New York City", "Chicago", 
                  "Boston", "Houston", "Miami"]
# Call the function
plot_crime_rates(df, cities)


# In[ ]:




