import src.tools.logger as logger
from src.auth.auth_data import *
import src.decorators.commands as commands


@commands.commands
def message_event(event_data):
  logger.info_event('Recv MESSAGE_CREATE event')

  
async def event_handler(event_data):

  event_type = event_data['t']

  match event_type:
    case 'MESSAGE_CREATE': message_event(event_data)
    case '1': pass
    case '2': pass

  return 0
