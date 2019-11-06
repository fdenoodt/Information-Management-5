import requests
import time
from api import Api

class HueLight:
    def __init__(self, id):
      self.api = Api()
      self.id = id
      self.active = False
      self.brightness = 0
      self.sat = 0
      self.hue = 0
      self.user = "newdeveloper"
      self.flash = False

    def create_user(self,ip):
      url='http://'+ip+'/api'
      body='{"devicetype": "smart_alarm_app#client"}'
      headers = {"Content-Type": "application/json"}
      response = self.api.post(url,body,headers)
      self.user = response["success"]["username"]


    def start_alarm(self, ip):
      self.active = True
      self.brightness=1
      while self.brightness<60:
        self.brightness+=1
        self.sendRequest(ip)
        time.sleep(5)
      self.flash()

    def flash(self):
      self.brightness=75
      self.flash=True
      #moet actief blijven to stop_alarm geroepen wordt
      while self.flash:
        self.active=False
        self.send_request(self.ip)
        time.sleep(2)
        self.active=True
        self.send_request(self.ip)
        time.sleep(2)

    def stop_alarm(self, ip):
      self.flash= False
      self.active = False
      self.sendRequest(ip)

    def send_request(self, ip):
      url = 'http://'+ip+'/api/'+self.user+'/lights/' + str(self.id)+'/state'
      data = '{ "on": '+str(self.active)+',"sat":'+str(self.sat) + \
          ', "bri":'+str(self.brightness)+',"hue":'+str(self.hue)+'}'
      headers = {"Content-Type": "application/json"}

      # we gebruiken de api klasse niet aangezien we hier ook headers moeten meegeven
      response = requests.put(url, data=data, headers=headers)
      res = response.json()
      print(res)
      return res