import requests
import json
import time
from secret_keys import HUE_EMULATOR_URL

def huelight(on,color,id):
    if(color == 'green'):
        sat = '0'
        hue = '100' #25535
    elif(color == 'orange'):
        sat = '250'
        hue = '200' #4000
    else:
        sat = '254'
        hue = '10'

    url = HUE_EMULATOR_URL +id+'/state'
    data = '{ "on": '+on+',"sat":'+sat+', "bri":100,"hue":'+hue+'}'
    headers = {"Content-Type": "application/json"}

    response = requests.put(url, data=data, headers=headers)
    res = response.json()
    print(res)

def switch(state):
    if(state=='green1'):  
        huelight('true','orange','2')
        time.sleep(3)
        huelight('true','red','2')
        huelight('true','green','1')       
    else:
        huelight('true','orange','1')
        time.sleep(3)
        huelight('true','red','1')
        huelight('true','green','2')

# while True:
#     switch('green1')
#     time.sleep(1)
#     switch('red1')
#     time.sleep(1)





from datetime import datetime

def get(url = HUE_EMULATOR_URL):
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res
    
seconds_active = 0
last_check = datetime.now()


while True:
    response = get()
    new_date = datetime.now()
    difference = (new_date - last_check)

    for item in response:
        print(response[item]['state']['on'])
            
'''
energie berekene
kijken bij fluvius? 
0.5 eurocent
hoeveel verbruiken per killowhat

analyse --> zoeken, dus bronnen...
harvard syst naar referen
harvard reference guide

1000 woorden voor implementatie --> code telt ook als woord

intro
analyse
implementatie
reflectie
    hoe verbeteren
    hoe hue zich kan verbeteren

voor nmbs moet ook op die manier
'''