import pprint as pp
import requests
import json
from src.tools.get_env import get_env


class ChannelsAPI:

  token = get_env('BOT_TOKEN')

  headers = {
    'authorization': f"Bot {token}",
    'content-type': 'application/json'
  }

  root_api_url = 'https://discord.com/api/v9/'


  def send_message(self, data, channel):
    response = requests.post(f'{self.root_api_url}/channels/{channel}/messages', headers=self.headers, data=json.dumps(data))

    if response.status_code > 200:
      pp.pprint(response.json())
    pp.pprint(response.status_code)
