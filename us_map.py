import streamlit as st
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from PIL import Image
import pandas as pd
# import import_ipynb
import MergedIncome # importing MergedIncome.ipynb

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
st.title("Interactive Map of Major U.S. Cities")

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
    race = st.checkbox("Race")
    age = st.checkbox("Age")
    income = st.checkbox("Income")
    cost_of_milk = st.checkbox("Cost of Milk")
    political_party = st.checkbox("Political Party")
    housing = st.checkbox("Housing")
    crime_rate = st.checkbox("Crime Rate")
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

# Function to generate a graph based on selected characteristics and cities
def generate_graph(selected_characteristics, selected_cities):
    # Example graph generation for selected characteristic
    fig, ax = plt.subplots(figsize=(10, 6))

    # Mocking a bar plot for each selected characteristic and city
    for characteristic in selected_characteristics:
        data = {city: characteristic_data[characteristic].get(city, 0) for city in selected_cities}
        sns.barplot(x=list(data.keys()), y=list(data.values()), ax=ax, label=characteristic)

    ax.set_title(f"Graph for: {', '.join(selected_characteristics)}")
    ax.set_xlabel("City")
    ax.set_ylabel("Value")
    ax.legend()

    # Save the figure to a BytesIO object
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    # Convert to base64 to display in Streamlit
    img_base64 = base64.b64encode(img_buf.read()).decode()
    plt.close()  # Close the plot to avoid display of unwanted figures

    return img_base64

# Handle Submit and Graph Display
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

    # Display the selected characteristics and cities
    if selected_characteristics and selected_cities:
        st.write(f"Selected Characteristics: {', '.join(selected_characteristics)}")
        st.write(f"Selected Cities: {', '.join(selected_cities)}")



        #WRITE CODE FOR GRAPHS HERE!!!
        
        

        # Display multiple graphs for each selected characteristic
        st.subheader("Graphs for Selected Characteristics")
        for characteristic in selected_characteristics:
            st.write(f"Graph for {characteristic}:")
            
            if characteristic == "Income":
                # Reading in the data
                df = pd.read_csv('mergedIncome.csv')
                
                # Generating the plot for the selected cities
                MergedIncome.plot_selected_cities(df, selected_cities)

            #Generate graphs here !!!
            if characteristic == "Housing":
                for city in selected_cities:
                    if city == "Boston":
                        # Streamlit title
                        st.title("Single Family Home Cost Boston")
                        # Load an image from file (ensure the file is in the same directory or provide the full path)
                        img = Image.open("housing_graphs/Boston.png")  # Replace with your PNG file path
                        # Display the image in Streamlit
                        st.image(img, caption="This is your PNG Image", use_column_width=True)
                    if city == "Chicago":
                        # Streamlit title
                        st.title("Single Family Home Cost Chicago")
                        # Load an image from file (ensure the file is in the same directory or provide the full path)
                        img = Image.open("housing_graphs/Chicago.png")  # Replace with your PNG file path
                        # Display the image in Streamlit
                        st.image(img, caption="This is your PNG Image", use_column_width=True)
                    if city == "Houston":
                        # Streamlit title
                        st.title("Single Family Home Cost Houston")
                        # Load an image from file (ensure the file is in the same directory or provide the full path)
                        img = Image.open("housing_graphs/Houston.png")  # Replace with your PNG file path
                        # Display the image in Streamlit
                        st.image(img, caption="This is your PNG Image", use_column_width=True)
                    if city == "Los Angeles":
                        # Streamlit title
                        st.title("Single Family Home Cost L.A")
                        # Load an image from file (ensure the file is in the same directory or provide the full path)
                        img = Image.open("housing_graphs/LA.png")  # Replace with your PNG file path
                        # Display the image in Streamlit
                        st.image(img, caption="This is your PNG Image", use_column_width=True)
                    if city == "Miami":
                        # Streamlit title
                        st.title("Single Family Home Cost Miami")
                        # Load an image from file (ensure the file is in the same directory or provide the full path)
                        img = Image.open("housing_graphs/Miami.png")  # Replace with your PNG file path
                        # Display the image in Streamlit
                        st.image(img, caption="This is your PNG Image", use_column_width=True)
                    if city == "New York City":
                        # Streamlit title
                        st.title("Single Family Home Cost N.Y.C")
                        # Load an image from file (ensure the file is in the same directory or provide the full path)
                        img = Image.open("housing_graphs/NYC.png")  # Replace with your PNG file path
                        # Display the image in Streamlit
                        st.image(img, caption="This is your PNG Image", use_column_width=True)
                    if city == "Seattle":
                        # Streamlit title
                        st.title("Single Family Home Cost Seattle")
                        # Load an image from file (ensure the file is in the same directory or provide the full path)
                        img = Image.open("housing_graphs/Seattle.png")  # Replace with your PNG file path
                        # Display the image in Streamlit
                        st.image(img, caption="This is your PNG Image", use_column_width=True)





           # graph_img_base64 = generate_graph([characteristic], selected_cities)
            #st.image(f"data:image/png;base64,{graph_img_base64}", use_column_width=True)

        # Add Reset Button (X) to clear the graph and selections
        reset_button = st.button("Reset All")
        if reset_button:
            # Reset the checkboxes and graphs
            st.session_state.clear()  # Clears all session state variables (i.e., resets everything)
            st.write("Selections and graphs have been reset.")
    else:
        st.write("Please select at least one characteristic and one city.")
