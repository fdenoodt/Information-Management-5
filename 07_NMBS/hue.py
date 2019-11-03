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
    self.user

  def startAlarm(self,ip):
    self.active = True
    sendRequest(ip)

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


  def stopAlarm(self,ip):
    self.active = False
    sendRequest(ip)

  def sendRequest(self,ip):
    url = 'http://'+ip+'/api/'+self.user+'/lights/'+self.id+'/state'
    data = '{ "on": '+self.active+',"sat":'+self.sat+', "bri":'+self.brightness+',"hue":'+self.hue+'}'
    headers = {"Content-Type": "application/json"}
    
    #we gebruiken de api klasse niet aangezien we hier ook headers moeten meegeven
    response = requests.put(url, data=data, headers=headers)
    res = response.json()
    