from hue import HueLight
from trains import TrainApi
import datetime
import time

train_api = TrainApi()
# 1 ask for the data (nu gebruiken we test data)
# indien de verwachte trein te laat is en er geen vroegere is dan wil je misschien een latere trein dan je gewilde arrival_time. (geeft ons de optie om een latere trein te kunnen kiezen)
max_later = 100  # in min
# maximum aantal minuten dat de trein te laat mag zijn
max_delay = 15  # in min

#
alarm = 100

starting_location = 'Gent-Sint-Pieters'
# starting_location = 'Brussel-Noord'
# end_location = 'Arlon'
end_location = 'Dilbeek'
# end_location = 'Brussel-Noord'
date = '051119'
# arrival time versimpelen (als je max later = 100 en je arrival_time = 2300 dan moet je dus 00000 en niet 2400)   andere vb ook (dus als je minuten toevoeg mag je niet  1260 of 1270)
arrival_time = str(int('1230') + max_later)

connections = train_api.getConnections(
    starting_location, end_location, date, arrival_time)

# 2. print all the available routes
for conn in connections:
    print(str(conn['departure']['time']) +
          ' - ' + str(conn['arrival']['time']))
    stops = str('')
    if 'vias' in conn:
        if 'via' in conn['vias']:
            viaid = 1
            for via in conn['vias']['via']:
                stops += ' ('+via['direction']['name'] + \
                    ') - ' + str(via['station'])
                viaid += 1
        print(conn['id']+': '+conn['departure']['station'] + stops + ' ('+conn['vias']['via'][int(conn['vias']
                                                                                                  ['number'])-1]['departure']['direction']['name'] + ')' + ' - ' + conn['arrival']['station'])
    else:
        print(conn['id']+': '+conn['departure']['station'] + ' ('+conn['departure']
              ['direction']['name'] + ')' + ' - ' + conn['arrival']['station'])
    # id = conn['vias']['number']
    # '('++')'          [1]['departure']['direction']['name']
    print("duration: " + conn['duration'])

print('\n')
print('Choose a route:')

# 3
originalid = int(input())
selected_connection = connections[originalid]

print(selected_connection)

# 4
while selected_connection['departure']['time'] >= datetime.datetime.now():
    is_on_time = train_api.verify_delay(selected_connection, date)

    if is_on_time == False:
        # Pick new connection
        connections = train_api.getConnections(
            starting_location, end_location, date, arrival_time)

        print("connection has changed to something different")
        selected_connection = connections[0]

    time.sleep(30)

'''
1. ask for starting location, end location, expected arrival
2. provide list of routes to take
3. user chooses a route
4. system keeps checking for that specific route
   system bekijkt alle vehicles en kijkt of delay
   vergelijke met afstand volgende voertuig, of nog kan halen
'''
