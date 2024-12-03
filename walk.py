# walk.py
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

class WalkabilityGraph:
    def __init__(self, cities, walkability_data):
        """
        Initializes the class with the list of cities and walkability data.
        
        :param cities: Dictionary of cities with their coordinates
        :param walkability_data: Dictionary with walkability data for each city
        """
        self.cities = cities
        self.walkability_data = walkability_data  # Using the walkability data passed as argument
        
    def generate_walkability_graph(self, selected_cities):
        """
        Generate a walkability graph for selected cities.
        
        :param selected_cities: List of cities selected by the user
        :return: Image in base64 format
        """
        # Filter walkability data for selected cities
        selected_data = {city: self.walkability_data[city] for city in selected_cities}

        # Prepare the plot
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(selected_data.keys()), y=list(selected_data.values()), palette='Blues_d')
        plt.title('Walkability Scores of Selected Cities')
        plt.xlabel('City')
        plt.ylabel('Walkability Score')

        # Save the figure to a BytesIO object
        img_buf = BytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0)

        # Convert to base64 to display in Streamlit
        img_base64 = base64.b64encode(img_buf.read()).decode()
        plt.close()  # Close the plot to avoid display of unwanted figures

        return img_base64
    
    def display_walkability_graph(self, selected_cities):
        """
        Display the generated walkability graph with ArcGIS links.
        
        :param selected_cities: List of cities selected by the user
        """
        img_base64 = self.generate_walkability_graph(selected_cities)
        
        # Display the image in Streamlit
        return img_base64
