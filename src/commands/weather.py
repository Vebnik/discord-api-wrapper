import src.api.channels_work as ch
import src.interface.Message as msg

API = ch.ChannelsAPI()


def weather(message: msg.Message):

  API.send_message('Test weather', message.get_channel_id())

