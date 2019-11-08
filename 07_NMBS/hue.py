import requests
import time
from api import Api


class HueLight:
    def __init__(self, id):
        self.api = Api()
        self.id = id
        self.active = False
        self.brightness = 0
        self.sat = '254'
        self.hue = '25535'
        self.user = "newdeveloper"
        self.is_flashing = False

    # def create_user(self, ip):
    #     url = 'http://'+ip+'/api'
    #     body = '{"devicetype": "smart_alarm_app#client"}'
    #     headers = {"Content-Type": "application/json"}
    #     response = self.api.post(url, body, headers)
    #     self.user = response["success"]["username"]

    def start_alarm(self, ip):
        self.active = True
        self.brightness = 1
        while self.brightness < 90:
            self.brightness += 5
            self.send_request(ip)
            time.sleep(1)
        self.flash(ip)

    def flash(self, ip):
        self.brightness = 100
        self.is_flashing = True
        # moet actief blijven to stop_alarm geroepen wordt
        while self.is_flashing:
            self.active = False
            self.send_request(ip)
            time.sleep(0.5)
            self.active = True
            self.send_request(ip)
            time.sleep(0.5)

    def stop_alarm(self, ip):
        self.is_flashing = False
        self.active = False
        self.send_request(ip)

    def send_request(self, ip):
        url = 'http://'+ip+'/api/'+self.user+'/lights/' + str(self.id)+'/state'
        if self.active == True:
            data = '{ "on": '+str(self.active)+',"sat":'+str(self.sat) + \
                ', "bri":'+str(self.brightness)+',"hue":'+str(self.hue)+'}'
        else:
             data = '{ "on": '+str(self.active)+'}'
        headers = {"Content-Type": "application/json"}

        # we gebruiken de api klasse niet aangezien we hier ook headers moeten meegeven
        response = requests.put(url, data=data, headers=headers)
        res = response.json()
        print(res)
        return res
