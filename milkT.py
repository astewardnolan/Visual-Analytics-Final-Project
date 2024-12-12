import pandas as pd
import matplotlib.pyplot as plt



df_milk = pd.read_csv("milkprices.csv")

def milk_graph(cities:list[str]):
    data = [
        ['Boston, MA', 4.46],
        ['Miami, FL', 4.18],
        ['New York, NY', 5.05],
        ['Houston, TX', 4.08],
        ['Seattle, WA', 4.62],
        ['Chicago, IL', 5.24],
        ['Los Angeles', 0.0]
    ]

    columns = ['City', 'Price']

    df_milk = pd.DataFrame(data, columns=columns)

    # city dummy variables
    boston = False
    miami = False
    nyc = False
    houston = False
    seattle = False
    chicago = False
    losangeles = False

    #print(df_milk)
    if ("Boston") in cities:

        boston = True
    if "Miami" in cities:

        miami = True
    if "New York City" in cities:


        nyc = True
    if "Los Angeles" in cities:

        losangeles = True
    if "Houston" in cities:

        houston = True
    if "Seattle" in cities:

        seattle = True
    if "Chicago" in cities:

        chicago = True


    # selecting cities
    cities_index_list = []

    if boston == True:
        cities_index_list.append(0)
    if miami == True:
        cities_index_list.append(1)
    if nyc == True:
        cities_index_list.append(2)
    if houston == True:
        cities_index_list.append(3)
    if seattle == True:
        cities_index_list.append(4)
    if chicago == True:
        cities_index_list.append(5)
    if losangeles == True:
        cities_index_list.append(6)

    print(cities_index_list)

    cities = []
    prices = []

    for i in cities_index_list:
        city  = df_milk['City'][i]
        print(city)
        print(cities)
        cities.append(city)
        #print(df_milk['City'][i])

    for i in cities_index_list:
        prices.append(df_milk['Price'][i])
        #print(df_milk['Price'][i])

    #cities = df_milk['City'][0] 
    #prices = df_milk['Price'][0] 

    # Create the bar chart
    plt.bar(cities, prices)

    # Add labels and title
    plt.xlabel('Cities')
    plt.xticks(rotation=45)
    plt.ylabel('Prices')
    plt.title('Average Price of Milk by City')
    if losangeles == True:
        print("Data for Los Angeles is not available.")
    # Display the chart
    plt.show()
    return plt
    
