import pprint as pp
import src.api.channels_work as ch_work
from src.auth.auth_data import *
import json


def message_event(event_data):

  API = ch_work.ChannelsAPI()

  pp.pprint(event_data)

  if event_data['d']['author']['id'] != '965306531476279346':
    channel = event_data['d']['channel_id']
    API.send_message('Hello from python, bitch !', channel)

  
def event_handler(event_data):

  event_type = event_data['t']

  match event_type:
    case 'MESSAGE_CREATE': message_event(event_data)
    case '1': pass
    case '2': pass

  return 0

