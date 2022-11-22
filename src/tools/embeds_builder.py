import src.interface.Weather as wea


def get_weather_embeds(data: wea.Weather):
  return {
    "content": "",
    "tts": False,
    "embeds": [{
      "type": "rich",
      "title": 'Weather',
      "description": "",
      "color": 0xa0f188,
      "fields": [{
        "name": 'Temp 🌡️',
        "value": f'{[*data.get_temp()][0]}'
      },
      {
        "name": 'Description ☀️',
        "value": data.get_description()
      }]
    }
  ]
}