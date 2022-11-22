import src.api.channels_work as ch
import src.interface.Message as msg
import src.interface.Weather as wea
import src.tools.embeds_builder as emb
import json
import requests


API = ch.ChannelsAPI()

def get_fresh_weather(content: str) -> wea.Weather:

  content = content.split(' ')[-1]
  apikey = '45f7e2c819a679be072c90b6ee3f1592'

  root_url = lambda city, apikey: f'https://api.openweathermap.org/data/2.5/weather?q=\
    {city}&units=metric&lang=ru&appid={apikey}'

  response = requests.get(root_url(content, apikey)).json()
  weather = wea.Weather(response)

  return weather


def weather(message: msg.Message):
  weather = get_fresh_weather(message.get_content())
  data = emb.get_weather_embeds(weather)

  API.send_embeds(data, message.get_channel_id())

