# Code cell 1
# %matplotlib inline
from matplotlib import colors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium

# code cell 2
# This should be a local path
dataset_path = './Map-Crime_Incidents-Previous_Three_Months.csv'

SF = pd.read_csv(dataset_path)

pd.set_option('display.max_rows', 10)  # Visualize 10 rows
# SF
# SF.columns
# len(SF)

SF['Month'] = SF['Date'].apply(lambda row: int(row[0:2]))
SF['Day'] = SF['Date'].apply(lambda row: int(row[3:5]))

print(SF['Month'][0:2])
print(SF['Day'][0:2])

print(type(SF['Month'][0]))

del SF['IncidntNum']

# Code cell 11
print(SF.drop('Location', axis=1, inplace=True))  # dees doet niks?

print(SF.columns)

CountCategory = SF['Category'].value_counts()
print(CountCategory)

print("\n")
print("\n")
# Code cell 14
SF['Category'].value_counts(ascending=True)
print(SF['Category'].value_counts(ascending=True))

# Possible code for the challenge question
print(SF['PdDistrict'].value_counts(ascending=True))

AugustCrimes = SF[SF['Month'] == 8]
AugustCrimes

# code cell 18
# Possible code for the question: How many burglaries were reported in the month of August?
AugustCrimes = SF[SF['Month'] == 8]
AugustCrimesB = SF[SF['Category'] == 'BURGLARY']
len(AugustCrimesB)

# Code cell 19
Crime0704 = SF.query('Month == 7 and Day == 4')
Crime0704

# Code cell 20
SF.columns

plt.plot(SF['X'], SF['Y'], 'ro')
plt.show()

pd_districts = np.unique(SF['PdDistrict'])
pd_districts_levels = dict(zip(pd_districts, range(len(pd_districts))))
pd_districts_levels

# Code cell 23
SF['PdDistrictCode'] = SF['PdDistrict'].apply(
    lambda row: pd_districts_levels[row])

# Code cell 24
plt.scatter(SF['X'], SF['Y'], c=SF['PdDistrictCode'])
plt.show()

# Code cell 25
districts = np.unique(SF['PdDistrict'])
print(list(colors.cnames.values())[0:len(districts)])

color_dict = dict(
    zip(districts, list(colors.cnames.values())[0:-1:len(districts)]))
color_dict

# Code cell 27
# Create map
map_osm = folium.Map(location=[SF['Y'].mean(), SF['X'].mean()], zoom_start=12)
plotEvery = 50
obs = list(zip(SF['Y'], SF['X'], SF['PdDistrict']))

for el in obs[0:-1:plotEvery]:

    folium.CircleMarker(el[0:2], color=color_dict[el[2]],
                        fill_color=el[2], radius=10).add_to(map_osm)


map_osm
