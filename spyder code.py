# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:20:29 2025

@author: Asus
"""

import pandas as pd
import matplotlib.pyplot as plt

#number of deaths related to HIV, version 1 = all data
hiv23 = pd.read_csv("hivdeath23.csv")

#removing unnecessary columns gives
data = hiv23[["ParentLocation", "Location", "Period", "FactValueNumeric"]]

#Remove rows where "FactValueNumeric" has no data
data2 = data.dropna(subset=["FactValueNumeric"])
print(data2)


#%%

# Filter dataset for each country
Italy = data2[(data2["Location"] == "Italy")]
Ukraine = data2[(data2["Location"] == "France")]
Greece = data2[(data2["Location"] == "Greece")]
Spain = data2[(data2["Location"] == "Spain")]
Portugal = data2[(data2["Location"] == "Portugal")]


# Create figure
plt.figure(figsize=(10, 5))

# Plot each country separately

plt.plot(Italy["Period"], Italy["FactValueNumeric"], marker="o", label="Italy", alpha=0.5)
plt.plot(Ukraine["Period"], Ukraine["FactValueNumeric"], marker="o", label="Ukraine", alpha=0.5)
plt.plot(Greece["Period"], Greece["FactValueNumeric"], marker="o", label="Greece", alpha=0.5)
plt.plot(Spain["Period"], Spain["FactValueNumeric"], marker="o", label="Spain", alpha=0.5)
plt.plot(Portugal["Period"], Portugal["FactValueNumeric"], marker="o", label="Portugal", alpha=0.5)

# Labels & Title
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.title("HIV-related Deaths in Selected Countries in Europe")
plt.legend(fontsize=7, loc="upper right")  # Adjust legend position
plt.grid()

# Show the plot
plt.show()















































