from api import Api
from datetime import datetime, timedelta


class TrainApi:
    def __init__(self):
        self.api = Api()
        self.base_url = "https://api.irail.be/"
        date = None
        starting_location = None
        end_location = None
        arrival_time = None

    def convert_timestamps(self, connection):
        connection['departure']['time'] = datetime.fromtimestamp(
            int(connection['departure']['time']))
        connection['arrival']['time'] = datetime.fromtimestamp(
            int(connection['arrival']['time']))

        if 'vias' in connection:
            counter = 0
            for via in connection['vias']['via']:
                connection['vias']['via'][counter]['arrival']['time'] = datetime.fromtimestamp(
                    int(via['arrival']['time']))

                connection['vias']['via'][counter]['departure']['time'] = datetime.fromtimestamp(
                    int(via['departure']['time']))
                counter += 1

        return connection

    def get_connections(self, starting_location, end_location, date, arrival_time):
        self.starting_location = starting_location
        self.end_location = end_location
        self.date = date
        self.arrival_time = arrival_time

        url = self.base_url + "connections/?from=" + starting_location + "&to="+end_location + \
            "&date=" + date + "&time="+arrival_time + \
            "&timesel=arrival&format=json&lang=en&fast=false&typeOfTransport=trains&alerts=false&results=6"
        connections = self.api.get(url)["connection"]

        returing_connections = []
        for conn in connections:
            returing_connections.append(self.convert_timestamps(conn))

        return returing_connections

    def return_delay(self, trainid, date, station):
        url = self.base_url + "vehicle/?id=" + trainid + '&date='+date+'&format=json'
        vehiculeinfo = self.api.get(url)
        stopid = 0
        while vehiculeinfo['stops']['stop'][stopid]['station'] != station:
            stopid += 1
        delay = vehiculeinfo['stops']['stop'][stopid]['delay']
        return delay

    def validate_vias(self, selected_connection):
        # per via: arrival time + delay < departure + delay --> goed, else false
        if 'vias' in selected_connection:
            vias = selected_connection['vias']['via']
            for via in vias:
                # in a via you first arrive at a location, then depart again, so arriv must be smaller than depart
                arrival_time = via['arrival']['time']
                arr_seconds_delay = via['arrival']['delay']

                departure_time = via['arrival']['time']
                dep_seconds_delay = via['arrival']['delay']

                arrival_time = arrival_time + \
                    timedelta(0, int(arr_seconds_delay))  # 0 days, x seconds

                departure_time = departure_time + \
                    timedelta(0, int(dep_seconds_delay))

                if arrival_time < departure_time:
                    # on time
                    break
                else:  # not on time --> must search for a new route/connection
                    return False

        return True

    def verify_delay(self, selected_connection, max_delay=15):
        print("LALALALAL")
        arrival_vehicle_id = selected_connection['arrival']['vehicle']
        arrival_station = selected_connection['arrival']['station']

        delay_of_arrival = self.return_delay(
            arrival_vehicle_id, self.date, arrival_station)

        if self.validate_vias(selected_connection) == False:
            return False

        if int(delay_of_arrival) > int(max_delay):  # evaluated in seconds
            # Search other route
            return False

        print("Delay is on fine: " + delay_of_arrival)
        return True
