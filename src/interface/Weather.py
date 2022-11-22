

class Weather:

  weather_data = None

  def __init__(self, weather_data):
    self.weather_data = weather_data


  def get_description(self):
    return self.weather_data['weather'][0]['description']

  
  def get_temp(self):
    return self.weather_data['main'].values()