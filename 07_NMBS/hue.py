import requests


class HueLight:
    def __init__(self, id):
        self.id = id
        self.active = False
        self.brightness = 0
        # self.r = 0
        # self.g = 0
        # self.b = 0
        self.sat = 0
        self.hue = 0
        self.user = "newdeveloper"

    def startAlarm(self, ip):
        self.active = True
        self.sendRequest(ip)

        # vb voor kleuren
        # if(color == 'green'):
        #     self.sat = '0'
        #     self.hue = '25535'
        # elif(color == 'orange'):
        #     self.sat = '250'
        #     self.hue = '25535'
        # else:
        #     self.sat = '254'
        #     self.hue = '10'

    def stopAlarm(self, ip):
        self.active = False
        self.sendRequest(ip)

    def sendRequest(self, ip):
        url = 'http://'+ip+'/api/'+self.user+'/lights/' + str(self.id)+'/state'
        data = '{ "on": '+str(self.active)+',"sat":'+str(self.sat) + \
            ', "bri":'+str(self.brightness)+',"hue":'+str(self.hue)+'}'
        headers = {"Content-Type": "application/json"}

        # we gebruiken de api klasse niet aangezien we hier ook headers moeten meegeven
        response = requests.put(url, data=data, headers=headers)
        res = response.json()
        print(res)
        return res


a = HueLight(1)
a.sendRequest("10.110.161.202:8000")
