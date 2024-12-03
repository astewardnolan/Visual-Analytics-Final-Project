#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


# Reading in merged file including per-capita income for all our cities
df = pd.read_csv('mergedIncome.csv')


# In[7]:


def plot_selected_cities(data, cities) ->plt:
    """
    Plots a line graph for the given cities.
    
    Args:
        data (DataFrame): Merged DataFrame with 'DATE' and city columns.
        cities (list): List of city names to plot.
    """    
    # Filter DataFrame to include only the 'DATE' and selected cities
    filtered_df = data[['DATE'] + cities]
    
    # Plot each selected city
    plt.figure(figsize=(12, 6))
    for city in cities:
        plt.plot(filtered_df['DATE'], filtered_df[city], marker='o', label=city)
    
    # Formatting the plot
    plt.title('Per-Capita Income Trends by City')
    plt.xlabel('Date')
    plt.ylabel('Per-Capita Income')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return plt

# List of cities to plot
selected_cities = ["Seattle", "LA", "NYC", "Chicago", "Boston", "Houston", "Miami"]
# selected_cities = ["Seattle", "LA"]


# Call the function
#plot_selected_cities(df, selected_cities)


# In[ ]:




