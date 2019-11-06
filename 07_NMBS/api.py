import requests

class Api:

  def get(self, url):
    json_data = requests.get(url).json()
    return json_data
    # json_status = json_data["info"]["statuscode"]

  def post(self,url,body,headers):
    response = requests.post(url, data=body, headers=headers)
    res = response.json()
    print(res)
    return res