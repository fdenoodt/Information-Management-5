import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium

DF = pd.read_csv('./Data/Map-Crime_Incidents-Previous_Three_Months.csv')

DF.head()

##
pd.set_option('display.max_rows', 10)

##

DF.columns

##

DF['Month'] = DF.Date.apply(lambda row: str(row[0:2]))
DF['Day'] = DF.Date.apply(lambda row: str(row[3:5]))

##

type(DF['Month'][0:2])
##


del DF['IncidntNum']
del DF['Date']

##

# 1 = columns, #0 = rows
DF.drop(['Location'], axis=1)

##
count_category = DF.Category.value_counts(ascending=True)

##
print(count_category)

##

DF = DF[DF.Month == '08']

##

plt.plot(DF.X, DF.Y, 'ro')
plt.show()
##

pd_districts = np.unique(DF['PdDistrict'])
pd_districts_levels = dict(zip(pd_districts, range(len(pd_districts))))


##
pd_districts_levels
##

DF['PdDistrictCode'] = DF['PdDistrict'].apply(lambda row: pd_districts_levels[row])
##
DF['PdDistrict']

##
DF.PdDistrictCode

##

from matplotlib import colors
districts = np.unique(DF['PdDistrict'])
print(list(colors.cnames.values())[0:len(districts)])

##

color_dict = dict(zip(districts, list(colors.cnames.values())[0:-1:len(districts)]))
##
color_dict

##

map_osm = folium.Map(location=[DF.Y.mean(), DF.X.mean()], zoom_start=12)
plotEvery = 50
obs = list(zip( DF['Y'], DF['X'], DF['PdDistrict'])) 
##

for el in obs[0:-1:plotEvery]:
    folium.CircleMarker(el[0:2], color=color_dict[el[2]], fill_color=el[2],radius=10).add_to(map_osm)


##
map_osm

##

obs[0:-1:5]

##

