import websockets
import pprint as pp
import json
import datetime as dt
import asyncio
import threading as thr
from time import sleep
from src.auth.auth_data import *


class Gateway:

  gateway_url = 'wss://gateway.discord.gg/?v=10&encoding=json'
  auth_data = { 'token': None, 'app_id': None, 'secret_key': None }

  loop = None
  ws = None
  asyncio = None

  
  def __init__(self):
    print('init gateway')
    asyncio.run(self.get_gateway())


  async def first_connect(self, d):

    await self.ws.send(json.dumps({"op": 1,"d": d}))
    await self.ws.recv()
  
    return self.ws


  async def auth_app(self):
    print(f'{"-"*20} => subscribe event')

    buffer = []

    await self.ws.send(json.dumps(auth_data))

    buffer.append(await self.ws.recv())
    buffer.append(await self.ws.recv())
    
    buffer = [*map(lambda el: json.loads(el), buffer)]

    with open('src/data/auth_response.json', 'w+', encoding='utf-8') as file: 
      file.write(json.dumps(buffer[0], indent=2))

    print('Write nsubscribe data')

    return self.ws


  async def heartbeat(self, interval):
    while True:
      await asyncio.sleep(interval)
      await self.ws.send(json.dumps({"op": 1,"d": 0}))
      print('Hearbeat event')


  async def event_listener(self):
    while True:
      event = await self.ws.recv()
      print(event)
    

  async def get_gateway(self) -> None:

    self.ws = await websockets.connect(self.gateway_url)

    response = json.loads(await self.ws.recv())

    print(f'First connect data\n{response}')
    
    if response['op'] == 10:

      asyncio.ensure_future(self.heartbeat(10))

      await self.first_connect(0)
      await self.auth_app()
      await self.event_listener()

