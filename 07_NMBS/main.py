from hue import HueLight
from trains import TrainApi

train_api = TrainApi()
starting_location = 'Gent-Sint-Pieters'
end_location = 'Mechelen'
# starting_location = 'Dilbeek'
# end_location = 'Brussel-Noord'
date = '021119'
arrival_time = '1230'
connections = train_api.getConnections(
    starting_location, end_location, date, arrival_time)

# 1. print all the available routes
for conn in connections:
    print(str(conn['departure']['time']) +
          ' - ' + str(conn['arrival']['time']))
    print(conn['departure']['station'] + ' - ' + conn['arrival']['station'])
    print(conn['duration'])
    # print("vias:" + str(len(conn['vias'])))
    print("\n")

selected_connection = connections[0]
trains = []

trains.append(selected_connection['arrival'])

if 'vias' in selected_connection:
    trains.append(selected_connection['vias'])


for train in trains:
    print(train)


'''
1. ask for starting location, end location, expected arrival
2. provide list of routes to take
3. user chooses a route
4. system keeps checking for that specific route
   system bekijkt alle vehicles en kijkt of delay
   vergelijke met afstand volgende voertuig, of nog kan halen
'''
