from hue import HueLight
from trains import TrainApi
import datetime
import time


def display_vias(conn):
    stops = ''
    if 'via' in conn['vias']:
        viaid = 1
        for via in conn['vias']['via']:
            stops += ', via: ('+via['direction']['name'] + \
                ') - ' + str(via['station'])
            viaid += 1
        print(conn['departure']['station'] + stops + ' ('+conn['vias']['via'][int(conn['vias']
                                                                                  ['number'])-1]['departure']['direction']['name'] + ')' + ' - ' + conn['arrival']['station'])
    else:
        print(conn['id']+': '+conn['departure']['station'] + ' ('+conn['departure']
              ['direction']['name'] + ')' + ' - ' + conn['arrival']['station'])


def display_connection(conn):
    print("******************")
    message = conn['id']
    message = message + ' : ' + str(conn['departure']['time'])
    message = message + ' - ' + str(conn['arrival']['time'])

    print(message)
    display_vias(conn)

    print("Duration: " + str(int(conn['duration']) / 60) + " minutes")
    print("\n")


train_api = TrainApi()
hue = HueLight(1)
hue.create_user(ip)
# 1 ask for the data (nu gebruiken we test data)
# indien de verwachte trein te laat is en er geen vroegere is dan wil je misschien een latere trein dan je gewilde arrival_time. (geeft ons de optie om een latere trein te kunnen kiezen)
max_later = 0  # in min
# maximum aantal minuten dat de trein te laat mag zijn
max_delay = 15  # in min

alarm = 100

starting_location = 'Gent-Sint-Pieters'
end_location = 'Dilbeek'
date = '081119'

str_last_available_arrival_time = str(int('1420') + max_later)
last_available_arrival_DATE_time = datetime.datetime(
    2000+int(date[4:6]),
    int(date[2:4]),
    int(date[0:2]),
    int(str_last_available_arrival_time[0:2]),
    int(str_last_available_arrival_time[3:5]))

connections = train_api.get_connections(
    starting_location, end_location, date, '1630')  # + 30 min, zodat een vertraging nog steeds gesimuleerd kan worden, in realiteit wil je hier 1420 hebben

# 2. print all the available routes
print("\n")
print('Available routes:')
for conn in connections:
    display_connection(conn)


print('\n')
print('Choose a route:')

originalid = int(input())
selected_connection = connections[originalid]

print("\n")
print("Selected route:")
display_connection(selected_connection)

# 4
while is_time:
    try:
        print("Verifying connection...")
        is_on_time = train_api.verify_delay(
            selected_connection, last_available_arrival_DATE_time)
        print("The currently selected train is on time: " + str(is_on_time))

        if is_on_time == False:
            # Pick new connection
            connections = train_api.get_connections(
                starting_location, end_location, date, str_last_available_arrival_time)

            selected_connection = connections[0]

            print("A new route/connection has been selected:")
            display_connection(selected_connection)
        is_time=

        time.sleep(10)
    except:
        print("Oops something went wrong.")

hue.start_alarm()

input()

hue.stop_alarm()

    print("\n")