import requests
import json
import time


def huelight(on,color,id):
    if(color == 'green'):
        sat = '0'
        hue = '25535'
    elif(color == 'orange'):
        sat = '250'
        hue = '25535'
    else:
        sat = '254'
        hue = '10'

    url = 'http://localhost:8000/api/newdeveloper/lights/'+id+'/state'
    data = '{ "on": '+on+',"sat":'+sat+', "bri":100,"hue":'+hue+'}'
    headers = {"Content-Type": "application/json"}

    response = requests.put(url, data=data, headers=headers)
    res = response.json()
    print(res)

def switch(state):
    if(state=='green1'):
        huelight('true','green','1')
        huelight('true','red','2')
    else:
        huelight('true','green','2')
        huelight('true','red','1')
    



for x in range(6):
    switch('green1')



