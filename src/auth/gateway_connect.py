import websockets
import json
import asyncio
import datetime as dt
import src.auth.auth_data as aud


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


  async def auth(self, ws):    
    await ws.send(json.dumps('auth_data'))
    return ws


  async def first_connect(self, ws, d):
    print(f'{"-"*20} => {dt.datetime.today().strftime("%H:%M:%S")}\nheartbeat event')

    await ws.send(json.dumps({"op": 1,"d": d}))
    print(await ws.recv())
    await asyncio.sleep(2)

    return ws


  async def auth_app(self, ws):
    print(f'{"-"*20} => {dt.datetime.today().strftime("%H-%M-%S")}\nsubscribe event')

    buffer = []

    await ws.send(json.dumps(aud.auth_data))
    buffer.append(await ws.recv())
    buffer.append(await ws.recv())
    
    print(buffer)

    await asyncio.sleep(2)

    return ws


  async def get_gateway(self) -> None:

    async with websockets.connect(self.gateway_url) as ws:

      response = json.loads(await ws.recv())
      interaval = response['d']['heartbeat_interval']

      print(f'First connect data\n{response}')
      
      if response['op'] == 10:
        await self.first_connect(ws, 251)
        await self.auth_app(ws)

        while True:
          await self.first_connect(ws, 251)

