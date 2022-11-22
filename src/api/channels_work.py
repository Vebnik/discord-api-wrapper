import pprint as pp
import requests
import json


class ChannelsAPI:

  token = 'OTY1MzA2NTMxNDc2Mjc5MzQ2.GcqOQQ.nph61JZSy22zJ8X5DsP4pPc-yKPvPYILDFDv5g'

  headers = {
    'authorization': f"Bot {token}",
    'content-type': 'application/json'
  }

  root_api_url = 'https://discord.com/api/v9/'

  def __init__(self): pass


  def send_message(self, data, channel):
    data = { "content": data, "tts": False }
    response = requests.post(f'{self.root_api_url}/channels/{channel}/messages', headers=self.headers, data=json.dumps(data))

    if response.status_code > 200:
      pp.pprint(response.json())
    pp.pprint(response.status_code)
    

  def send_embeds(self, data, channel):
    response = requests.post(f'{self.root_api_url}/channels/{channel}/messages', headers=self.headers, data=json.dumps(data))

    if response.status_code > 200:
      pp.pprint(response.json())
    pp.pprint(response.status_code)
