import pandas as pd
import matplotlib.pyplot as plt

def plot_age_demographics(cities):
    # Load the CSV data
    df = pd.read_csv('age.csv', header=0)  # Ensure the first row is used as column names

    # Strip spaces from column names
    df.columns = df.columns.str.strip()

    # Define the demographic rows we are interested in (age group percentages)
    demographic_rows = [
        'Persons under 5 years, percent',
        'Persons under 18 years, percent',
        'Persons 65 years and over, percent'
    ]

    # Filter the DataFrame to include only the relevant demographic rows
    df_demographics = df[df['Fact'].isin(demographic_rows)]

    # Drop the 'Fact' column for easier manipulation
    df_demographics = df_demographics.drop(columns=['Fact'])

    # Transpose the DataFrame to have cities as columns and demographic categories as rows
    df_demographics = df_demographics.T

    # Clean the data: Remove '%', commas, and convert to numeric
    for col in df_demographics.columns:
        df_demographics[col] = df_demographics[col].replace({'%': '', ',': ''}, regex=True).astype(float)

    # Set the demographic categories as index
    df_demographics.index = [
        'Persons under 5 years',
        'Persons under 18 years',
        'Persons 65 years and over'
    ]

    # Loop through each demographic category and plot
    for index in df_demographics.index:
        plt.figure(figsize=(10, 6))
        plt.bar(df_demographics.columns, df_demographics.loc[index], color='skyblue')
        plt.title(f'Age Demographics: {index}')
        plt.ylabel('Percentage')
        plt.xticks(rotation=45)
        plt.ylim(0, 30)  # Adjust y-axis limit as needed
        plt.tight_layout()  # Adjust layout to prevent overlap
        plt.show()  # Show the plot

# Example usage
cities = [
    "Houston city, Texas", 
    "Los Angeles city, California", 
    "New York city, New York", 
    "Seattle city, Washington", 
    "Miami city, Florida", 
    "Chicago city, Illinois", 
    "Boston city, Massachusetts"
]

# Call the function to plot the age demographics for the specified cities
plot_age_demographics(cities)