

class Message:

  message = None

  def __init__(self, message) -> None:
    self.message = message


  def get_channel_id(self):
    return self.message['d']['channel_id']


  def get_content(self):
    return self.message['d']['content']


  def get_author(self):
    return self.message['d']['author']