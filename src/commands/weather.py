import src.api.channels_work as ch
import src.interface.Message as msg
import src.interface.Weather as wea
import src.tools.embeds_builder as emb
from src.tools.get_env import get_env
import requests


def get_fresh_weather(content: str) -> wea.Weather:

  content = content.split(' ')[-1]
  apikey = get_env('WEATHER_API_TOKEN')

  root_url = lambda city, apikey: f'https://api.openweathermap.org/data/2.5/weather?q=\
    {city}&units=metric&lang=ru&appid={apikey}'

  response = requests.get(root_url(content, apikey)).json()
  weather = wea.Weather(response)

  return weather


def weather(message: msg.Message):

  API = ch.ChannelsAPI()

  weather = get_fresh_weather(message.get_content())
  data = emb.get_weather_embeds(weather)

  API.send_message(data, message.get_channel_id())

