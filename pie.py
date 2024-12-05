import matplotlib.pyplot as plt
import pandas as pd

# Function to plot pie charts for each city in a single pop-up window
def plot_pie_charts(df, cities):
    # Ensure the DataFrame has the expected columns
    if not all(col in df.columns for col in ['Party', 'Votes', 'City']):
        raise ValueError("DataFrame must contain 'Party', 'Votes', and 'City' columns.")
    
    # Strip extra spaces in the City column
    df['City'] = df['City'].str.strip()

    # Number of cities to plot
    num_cities = len(cities)
    
    # Determine the number of rows and columns for the subplot grid
    cols = 2  # Set the number of columns you want
    rows = (num_cities + cols - 1) // cols  # Calculate the number of rows needed
    
    # Create a figure and axes for subplots
    fig, axes = plt.subplots(rows, cols, figsize=(12, 6 * rows))
    
    # Flatten axes to easily index
    axes = axes.flatten()

    # Loop through each city in the provided list
    for i, city in enumerate(cities):
        if city not in df['City'].values:
            print(f"Warning: City '{city}' not found in the DataFrame.")
            continue  # Skip this city if it's not in the DataFrame

        # Filter data for the current city
        city_data = df[df['City'] == city]
        
        # Group by 'Party' and sum 'Votes'
        vote_distribution = city_data.groupby('Party')['Votes'].sum()
        
        # Plot pie chart in the current subplot
        axes[i].pie(vote_distribution, labels=vote_distribution.index, autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'red'])
        axes[i].set_title(f'Vote Distribution in {city}')
        axes[i].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Hide any unused axes (i.e., if the number of cities is less than the total subplots)
    for j in range(num_cities, len(axes)):
        axes[j].axis('off')  # Turn off the unused axes
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    # Show the plot
    plt.show()
    return plt

# Example usage:
df = pd.read_csv('NYCPollAff.csv')

# List of cities you want to generate pie charts for
cities = ["New York City", "Seattle", "Los Angeles", "Boston", "Chicago"]

# Call the function to plot the pie charts
plot_pie_charts(df, cities)
