from api import Api
from datetime import datetime


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

        return connection

    def getConnections(self, starting_location, end_location, date, arrival_time):
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

    def verify_delay(self, selected_connection, max_delay=15):
        arrival_vehicle_id = selected_connection['arrival']['vehicle']
        arrival_station = selected_connection['arrival']['station']

        delay_of_arrival = self.return_delay(
            arrival_vehicle_id, self.date, arrival_station)

        if 'vias' in selected_connection:
            vias = selected_connection['vias']
            print('there are vias lol')

        if int(delay_of_arrival) > int(max_delay):
            # Search other route
            return False

        print("delay is on time: " + delay_of_arrival)
        return True
