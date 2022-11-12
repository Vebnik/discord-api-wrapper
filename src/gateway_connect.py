import requests as req


class Gateway:

  auth_data = {
    'token': None,
    'app_id': None,
    'secret_key': None,
  }

  def __init__(self, token, app_id, secret_key):

    self.auth_data['token'] = token
    self.auth_data['app_id'] = app_id
    self.auth_data['secret_key'] = secret_key

    self.get_gateway()
    pass


  def get_gateway(self):
    
    pass
