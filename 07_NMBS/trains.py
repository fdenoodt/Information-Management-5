from api import Api
from datetime import datetime

class TrainApi:
    def __init__(self):
        self.api = Api()
        self.base_url = "https://api.irail.be/"

    def convert_timestamps(self, connection):
      connection['departure']['time'] = datetime.fromtimestamp(int(connection['departure']['time']))
      connection['arrival']['time'] = datetime.fromtimestamp(int(connection['arrival']['time']))
      
      return connection

    def getConnections(self, starting_location, end_location, date, arrival_time):
        url = self.base_url + "connections/?from=" + starting_location + "&to="+end_location + \
            "&date=" + date + "&time="+arrival_time + \
            "&timesel=arrival&format=json&lang=en&fast=false&typeOfTransport=trains&alerts=false&results=6"
        connections = self.api.get(url)["connection"]

        returing_connections = []
        for conn in connections:
          returing_connections.append(self.convert_timestamps(conn))

       
        return returing_connections
