import pprint as pp
import requests
import json


class ChannelsAPI:

  token = 'OTY1MzA2NTMxNDc2Mjc5MzQ2.GcqOQQ.nph61JZSy22zJ8X5DsP4pPc-yKPvPYILDFDv5g'

  root_api_url = 'https://discord.com/api/v9/'

  def __init__(self):
    pass


  def send_message(self, data, channel):

    headers = {
      'authorization': f"Bot {self.token}",
      'content-type': 'application/json'
    }
  
    data = {
      "content": data,
      "tts": False
    }
    
    response = requests.post(f'{self.root_api_url}/channels/{channel}/messages', headers=headers, data=json.dumps(data))
    pp.pprint(response.json())

