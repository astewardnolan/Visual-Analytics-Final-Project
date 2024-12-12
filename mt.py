import streamlit as st
import streamlit as sp
import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
from io import BytesIO
import base64
from PIL import Image
import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO
import base64
from MergedIncome import plot_selected_cities  # importing MergedIncome.py
from pie import plot_pie_charts
from milkT import milk_graph
from CrimeRates import plot_crime_rates
from age import plot_age_group_distribution
from race_graphic import race_graph

# Major U.S. cities with coordinates (latitude, longitude)
cities = {
    "Seattle": (47.6062, -122.3321),
    "Chicago": (41.8781, -87.6298),
    "Los Angeles": (34.0522, -118.2437),
    "New York City": (40.7128, -74.0060),
    "Miami": (25.7617, -80.1918),
    "Houston": (29.7604, -95.3698),
    "Boston": (42.3601, -71.0589)  # Added Boston here
}

# Streamlit title
st.title("CityFinder")

# Add a "Help" Button or Section
with st.expander("Help", expanded=False):
    st.write("""
    Find the best city for you! This website provides an interactive map of major U.S. cities, where you can explore various characteristics like race, income, crime rates, housing, walkability, and more. 
    You can select multiple cities and characteristics, and the corresponding graphs will be generated for you to analyze.
    Use the checkboxes to choose characteristics and cities, then press the 'Submit' button to view the results.
    """)

# Create a base map centered on the United States
map_center = [37.0902, -95.7129]  # Centered around the United States
us_map = folium.Map(location=map_center, zoom_start=4)

# Add markers for major cities on the map
for city, (lat, lon) in cities.items():
    folium.Marker(
        location=[lat, lon],
        popup=f"<strong>{city}</strong>",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(us_map)

# Display the map in Streamlit using st_folium
st_folium(us_map, width=700, height=500)

# Below the map: Select Characteristics for Data
st.subheader("Select Characteristics")

# Checkbox for selecting "Select All"
select_all = st.checkbox("Select All Characteristics", key="select_all")

# If "Select All" is checked, automatically check all individual checkboxes
if select_all:
    race = True
    age = True
    income = True
    cost_of_milk = True
    political_party = True
    housing = True
    crime_rate = True
    walkability = True
else:
    cost_of_milk = st.checkbox("Cost of Milk")
    race = st.checkbox("Race")
    age = st.checkbox("Age")
    income = st.checkbox("Income")

    political_party = st.checkbox("2024 Election Voting")
    housing = st.checkbox("Housing")
    crime_rate = st.checkbox("Crime")
    walkability = st.checkbox("Walkability")

# Below the characteristics, allow users to select cities

# Display checkboxes for selecting cities
st.subheader("Select Cities")

# Select All Cities Checkbox
select_all_cities = st.checkbox("Select All Cities", key="select_all_cities")

# If "Select All Cities" is checked, automatically check all individual checkboxes
selected_cities = []
if select_all_cities:
    selected_cities = list(cities.keys())  # Select all cities
else:
    for city in cities.keys():
        if st.checkbox(city, key=city):  # Add checkbox for each city
            selected_cities.append(city)

# Submit button to process the data
submit_button = st.button("Submit")

# Handle Submit and Graph Display
if submit_button:
    # Collect selected characteristics
    selected_characteristics = []
    if cost_of_milk:
        selected_characteristics.append("Cost of Milk")
    if race:
        selected_characteristics.append("Race")
    if age:
        selected_characteristics.append("Age")
    if income:
        selected_characteristics.append("Income")
    if political_party:
        selected_characteristics.append("2024 Election Voting")
    if housing:
        selected_characteristics.append("Housing")
    if crime_rate:
        selected_characteristics.append("Crime")
    if walkability:
        selected_characteristics.append("Walkability")

    # Display the selected characteristics and cities
    if selected_characteristics and selected_cities:
        st.write(f"Selected Characteristics: {', '.join(selected_characteristics)}")
        st.write(f"Selected Cities: {', '.join(selected_cities)}")

        # Display multiple graphs for each selected characteristic
        st.subheader("Graphs for Selected Characteristics")
        for characteristic in selected_characteristics:
            st.write(f"Graph for {characteristic}:")

            if characteristic == "Cost of Milk":
                # Load milk price data (assuming the data is available)
                milk_data = pd.read_csv('milkprices.csv')

                # Define the list of available characteristics (Milk Price)
                characteristics = ['Milk Price']

                # Streamlit UI for selecting characteristic and cities
                st.title("Coordinated View: Milk Prices")

                #selected_characteristic = st.selectbox("Select characteristic to visualize", characteristics)
                cities = milk_data['City'].unique()
            
                selected_cities = st.multiselect("Selected cities to display", cities, default=selected_cities)
                if "Los Angeles" in selected_cities:
                    st.write("Data for Los Angeles is not available")

                # Filter the data based on selected cities
                filtered_data = milk_data[milk_data['City'].isin(selected_cities)]

                # If cities are selected, proceed with visualizing the bar chart and line chart
                if len(selected_cities) > 0:
                    # Create subplots to display bar chart and line chart together
                    fig = sp.make_subplots(
                        rows=1, cols=2, 
                        column_widths=[0.6, 0.4],  # Bar chart takes more space
                        subplot_titles=("Average Milk Price by City 2023", "Milk Prices Per Month 2023"),
                        shared_yaxes=True
                    )

                    # Create Bar Chart
                    bar_trace = go.Bar(
                        x=filtered_data['City'],
                        y=filtered_data['Avg'],
                        hoverinfo='x+y',
                        name="Average Milk Price",
                        marker=dict(color='skyblue')
                    )
                    fig.add_trace(bar_trace, row=1, col=1)

                    # Add Line Charts for each selected city
                    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct']
                    for city in selected_cities:
                        city_data = milk_data[milk_data['City'] == city]
                        milk_prices = city_data[months].values.flatten()  # Flatten month data for plotting
                        
                        # Generate a random RGB color and convert it to the proper string format
                        random_color = np.random.rand(3,)  # This generates an array of 3 random values (R, G, B)
                        color_str = f"rgb({int(random_color[0] * 255)}, {int(random_color[1] * 255)}, {int(random_color[2] * 255)})"
                        
                        # Add the line trace to the figure for this city
                        fig.add_trace(go.Scatter(
                            x=months,
                            y=milk_prices,
                            mode='lines+markers',
                            name=f"Milk Prices in {city}",
                            line=dict(color=color_str),  # Use the color_str here
                            marker=dict(symbol='circle'),
                            visible=True  # Initially set to visible, toggleable via the legend
                        ), row=1, col=2)

                    # Update layout
                    fig.update_layout(
                        title="Milk Price Visualization",
                        showlegend=True,
                        xaxis_title="City",
                        yaxis_title="Price ($)",
                        hovermode='closest',
                        plot_bgcolor='white',
                        height=600
                    )

                    # Display the plot
                    st.plotly_chart(fig)

                else:
                    st.write("Please select at least one city to visualize the milk prices.")

            # The rest of your graph generation code continues...
            if characteristic == "Income":
                df = pd.read_csv('mergedIncome.csv')
                graph = plot_selected_cities(df, selected_cities)
                st.pyplot(graph)

            # Additional graphs for other characteristics like Race, Crime, etc.
            if characteristic == "2024 Election Voting":
                df = pd.read_csv('NYCPollAff.csv')
                graph = plot_pie_charts(df, selected_cities)
                st.pyplot(graph)

            if characteristic == "Race":
                graph = race_graph(selected_cities)
                st.pyplot(graph)

            if characteristic == "Crime":
                df = pd.read_csv('mergedCrimeRates.csv')
                graphs = plot_crime_rates(df, selected_cities)
                for graph in graphs:
                    st.pyplot(graph)

            if characteristic == "Age":
                graph = plot_age_group_distribution(selected_cities)
                st.pyplot(graph)
