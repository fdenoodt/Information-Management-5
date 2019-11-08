from api import Api
from datetime import datetime, timedelta

class TrainApi:
    def __init__(self):
        self.api = Api()
        self.base_url = "https://api.irail.be/"
        self.date = None
        self.starting_location = None
        self.end_location = None
        self.arrival_time = None

    def datetime_plus_seconds(self, time, seconds):
        return time + timedelta(0, int(seconds))

    def unix_to_datetime(self, time):
        return datetime.fromtimestamp(int(time))

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

    def return_stop(self, trainid, date, station):
        url = self.base_url + "vehicle/?id=" + trainid + '&date='+date+'&format=json'
        vehiculeinfo = self.api.get(url)
        stopid = 0
        while vehiculeinfo['stops']['stop'][stopid]['station'] != station:
            stopid += 1
        stop = vehiculeinfo['stops']['stop'][stopid]
        # delay = stop['arrivalDelay']
        return stop

    def validate_vias(self, selected_connection):
        # per via: arrival time + delay < departure + delay --> goed, else false
        if 'vias' in selected_connection:
            vias = selected_connection['vias']['via']
            for via in vias:
                # in a via you first arrive at a location, then depart again, so arriv must be smaller than depart
                arrival_time = via['arrival']['time']
                arr_seconds_delay = via['arrival']['delay']

                departure_time = via['departure']['time']
                dep_seconds_delay = via['departure']['delay']

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

    def is_on_time(self,selected_connection,max_possible_delay_departure_time)
        return (selected_connection['departure']['time']- datetime.now())


    def verify_delay(self, selected_connection, max_possible_arrival_time_to_arrive_on_time):
        arrival_vehicle_id = selected_connection['arrival']['vehicle']
        arrival_station = selected_connection['arrival']['station']

        arrival_stop = self.return_stop(
            arrival_vehicle_id, self.date, arrival_station)

        expected_time_of_arrival = self.unix_to_datetime(
            arrival_stop['scheduledArrivalTime'])

        delay_of_arrival = arrival_stop['arrivalDelay']

        arrival_time = self.datetime_plus_seconds(
            expected_time_of_arrival, delay_of_arrival)

        # Verify Via's
        if self.validate_vias(selected_connection) == False:
            return False

        # Verify arrival
        # bv komt aan om 14, en wilt aankomen om 13
        if(arrival_time > max_possible_arrival_time_to_arrive_on_time):
            return False

        print("Delay is fine: " + str(int(delay_of_arrival)/60) + " minutes.")
        return True
