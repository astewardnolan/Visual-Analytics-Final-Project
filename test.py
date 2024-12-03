import streamlit as st
import folium
from streamlit_folium import st_folium
from walk import WalkabilityGraph

# Major U.S. cities with coordinates (latitude, longitude)
cities = {
    "Seattle": (47.6062, -122.3321),
    "Chicago": (41.8781, -87.6298),
    "Los Angeles": (34.0522, -118.2437),
    "New York City": (40.7128, -74.0060),
    "Miami": (25.7617, -80.1918),
    "Houston": (29.7604, -95.3698)
}

# Walkability data for cities (Mock data - Replace with actual data)
walkability_data = {
    "Seattle": 78,
    "Chicago": 70,
    "Los Angeles": 65,
    "New York City": 88,
    "Miami": 60,
    "Houston": 55,
}

# Streamlit title
st.title("Interactive Map of the United States")

# Create a base map centered on the United States
map_center = [37.0902, -95.7129]  # Centered around the United States
us_map = folium.Map(location=map_center, zoom_start=4)

# Add markers for major cities
for city, (lat, lon) in cities.items():
    folium.Marker(
        location=[lat, lon],
        popup=f"<strong>{city}</strong>",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(us_map)

# Display the map in Streamlit using st_folium
st_folium(us_map, width=700, height=500)

# Below the map: Select Characteristics for Data

# Checkbox for selecting "Select All"
select_all = st.checkbox("Select All", key="select_all")

# Conditional checkboxes based on "Select All"
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
    race = st.checkbox("Race")
    age = st.checkbox("Age")
    income = st.checkbox("Income")
    cost_of_milk = st.checkbox("Cost of Milk")
    political_party = st.checkbox("Political Party")
    housing = st.checkbox("Housing")
    crime_rate = st.checkbox("Crime Rate")
    walkability = st.checkbox("Walkability")

# Submit button to process the data
submit_button = st.button("Submit")

# If the submit button is clicked
if submit_button:
    # Collect selected characteristics
    selected_characteristics = []
    if race:
        selected_characteristics.append("Race")
    if age:
        selected_characteristics.append("Age")
    if income:
        selected_characteristics.append("Income")
    if cost_of_milk:
        selected_characteristics.append("Cost of Milk")
    if political_party:
        selected_characteristics.append("Political Party")
    if housing:
        selected_characteristics.append("Housing")
    if crime_rate:
        selected_characteristics.append("Crime Rate")
    if walkability:
        selected_characteristics.append("Walkability")

    # Display the selected characteristics
    if selected_characteristics:
        st.write(f"Selected Characteristics: {', '.join(selected_characteristics)}")
        
        # Here you can add logic to filter the data based on the selected characteristics
        # For now, we just show the selected characteristics
        st.write("You can now fetch data for these characteristics (e.g., from an API).")
    else:
        st.write("Please select at least one characteristic.")

    # If 'Walkability' is selected, generate the walkability graph
    if walkability:
        # Create an instance of the WalkabilityGraph class
        walkability_graph = WalkabilityGraph.WalkabilityGraph(cities, walkability_data)
        
        # Generate and display the walkability graph
        selected_cities = list(cities.keys())  # You could refine this to only include selected cities
        img_base64 = walkability_graph.display_walkability_graph(selected_cities)
        
        # Display the walkability graph as an image
        st.image(f"data:image/png;base64,{img_base64}", use_column_width=True)
        
        # Optionally, add ArcGIS links (you can modify this link format as per your use case)
        for city in selected_cities:
            arcgis_link = f"https://www.arcgis.com/home/webmap/viewer.html?webmap=XYZ&city={city}"  # Replace XYZ with actual map ID
            st.markdown(f"[Explore {city} on ArcGIS]({arcgis_link})")

        st.success("Walkability scores graph and links to ArcGIS displayed successfully!")
