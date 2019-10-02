import secret_keys

import urllib.parse
import requests


main_api = "http://www.mapquestapi.com/directions/v2/route?"
key = secret_keys.MAPQUEST_KEY


def locate(orig = "Washington", dest = "Baltimaore"):
  url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

  json_data = requests.get(url).json()
  json_status = json_data["info"]["statuscode"]

  if(json_status == 0):
    print(str(json_data["route"]["distance"])+"miles")
    km = "{:.2f}".format(json_data["route"]["distance"]*1.61)
    print(str(km)+" km")
    print(json_data["route"]["formattedTime"])
    print(json_data["route"]["fuelUsed"])
   
  else:
    print("err " + str(json_status))


locate()