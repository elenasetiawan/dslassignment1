# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 00:05:33 2025

@author: Asus
"""

import pandas as pd
import matplotlib.pyplot as plt


def continent_avg(year, continent, data):
    """
    Calculates and prints the average FactValueNumeric for a specific continent in a given year.

    Parameters:
        year (int)
        continent (str): The continent to filter by
        data (pd.DataFrame): The dataset containing 'ParentLocation', 'Period', and 'FactValueNumeric'.
    """
    # Filter data for the selected year and continent
    filtered_data = data[(data["Period"] == year) & (data["ParentLocation"] == continent)]
    
    # Calculate the average
    avg_value = filtered_data["FactValueNumeric"].mean()
    
    # Print the result
    return (avg_value)
   
#%%

#number of deaths related to HIV, version 1 = all data
hiv23 = pd.read_csv("hivdeath23.csv")

#removing unnecessary columns gives
data = hiv23[["ParentLocation", "Location", "Period", "FactValueNumeric"]]

#Remove rows where "FactValueNumeric" has no data
data2 = data.dropna(subset=["FactValueNumeric"])
print(data2)

#%%

data_per_continent = [
    [2023, "Africa", continent_avg(2023,"Africa", data2)],
    [2023, "Europe", continent_avg(2023,"Europe", data2)],
    [2023, "Americas", continent_avg(2023,"Americas", data2)],
    [2022, "Africa", continent_avg(2022,"Africa", data2)],
    [2022, "Europe", continent_avg(2022,"Europe", data2)],
    [2022, "Americas", continent_avg(2022,"Americas", data2)],
    [2021, "Africa", continent_avg(2021,"Africa", data2)],
    [2021, "Europe", continent_avg(2021,"Europe", data2)],
    [2021, "Americas", continent_avg(2021,"Americas", data2)],
    [2020, "Africa", continent_avg(2020,"Africa", data2)],
    [2020, "Europe", continent_avg(2020,"Europe", data2)],
    [2020, "Americas", continent_avg(2020,"Americas", data2)],
    [2019, "Africa", continent_avg(2019,"Africa", data2)],
    [2019, "Europe", continent_avg(2019,"Europe", data2)],
    [2019, "Americas", continent_avg(2019,"Americas", data2)],
    [2018, "Africa", continent_avg(2018,"Africa", data2)],
    [2018, "Europe", continent_avg(2018,"Europe", data2)],
    [2018, "Americas", continent_avg(2018,"Americas", data2)],
    [2017, "Africa", continent_avg(2017,"Africa", data2)],
    [2017, "Europe", continent_avg(2017,"Europe", data2)],
    [2017, "Americas", continent_avg(2017,"Americas", data2)],
    [2016, "Africa", continent_avg(2016,"Africa", data2)],
    [2016, "Europe", continent_avg(2016,"Europe", data2)],
    [2016, "Americas", continent_avg(2016,"Americas", data2)],
    [2015, "Africa", continent_avg(2015,"Africa", data2)],
    [2015, "Europe", continent_avg(2015,"Europe", data2)],
    [2015, "Americas", continent_avg(2015,"Americas", data2)],
    [2014, "Africa", continent_avg(2014,"Africa", data2)],
    [2014, "Europe", continent_avg(2014,"Europe", data2)],
    [2014, "Americas", continent_avg(2014,"Americas", data2)],
    [2013, "Africa", continent_avg(2013,"Africa", data2)],
    [2013, "Europe", continent_avg(2013,"Europe", data2)],
    [2013, "Americas", continent_avg(2013,"Americas", data2)],
]
continent_data = pd.DataFrame(data_per_continent)
continent_data = continent_data.rename(columns={0:"Year", 1:"Continent", 2: "HIV Deaths"})

print(continent_data)


#%%

#Splitting the data based on the continents
Africa = continent_data[(continent_data["Continent"] == "Africa")]
Europe = continent_data[(continent_data["Continent"] == "Europe")]
Americas = continent_data[(continent_data["Continent"] == "Americas")]

#Plotting the line graph
plt.figure()

plt.plot(Africa["Year"], Africa["HIV Deaths"], marker="o", label="Africa", alpha=0.5)
plt.plot(Europe["Year"], Europe["HIV Deaths"], marker="o", label="Europe", alpha=0.5)
plt.plot(Americas["Year"], Americas["HIV Deaths"], marker="o", label="Americas", alpha=0.5)

# Labels & Title
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.title("HIV-related Deaths in Selected Continents")
plt.legend(loc="upper right")  # Adjust legend position
plt.grid()

plt.show()


























