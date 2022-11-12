import websockets
import json
import asyncio


class Gateway:

  gateway_url = 'wss://gateway.discord.gg/?v=10&encoding=json'

  auth_data = {
    'token': None,
    'app_id': None,
    'secret_key': None,
  }


  def __init__(self, token: str, app_id: str, secret_key: str):

    print('init gateway')

    self.auth_data['token'] = token
    self.auth_data['app_id'] = app_id
    self.auth_data['secret_key'] = secret_key

    asyncio.run(self.get_gateway())
    pass


  async def get_gateway(self) -> None:
    async with websockets.connect(self.gateway_url) as ws:

      d = 251
      response = json.loads(await ws.recv())
      interaval = response['d']['heartbeat_interval']
      
      while True:
        await ws.send(json.dumps({"op": 1,"d": d}))
        print(await ws.recv())

        await asyncio.sleep(interaval/1000)
      


  
  