import requests
import json


class ChannelsAPI:

  token = 'OTY1MzA2NTMxNDc2Mjc5MzQ2.GcqOQQ.nph61JZSy22zJ8X5DsP4pPc-yKPvPYILDFDv5g'

  def __init__(self):
    pass


  def post_message(self, channels: str, data: dict):
    headers = {
      'authorization': self.token,
      'content-type': 'application/json'
    }

    res = requests.post(f'https://ptb.discord.com/api/v9/channels/{channels}/messages', json.dumps(data), headers=headers)

    print(res.json())



ch_api = ChannelsAPI()

msg_data = {
  "content": "Hello, World!",
  "tts": False,
  "embeds": [{
    "title": "Hello, Embed!",
    "description": "This is an embedded message."
  }]
}

ch_api.post_message('968599370721271838', msg_data)
