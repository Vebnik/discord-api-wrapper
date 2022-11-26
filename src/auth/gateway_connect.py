import websockets
import json
import asyncio
from src.auth.auth_data import auth_data
import src.event.event_handler as evt
import src.tools.logger as logger


class Gateway:

  gateway_url = 'wss://gateway.discord.gg/?v=10&encoding=json'
  

  def __init__(self):
    logger.info('init gateway')
    asyncio.run(self.get_gateway())


  async def first_connect(self, d):

    await self.ws.send(json.dumps({"op": 1,"d": d}))
    await self.ws.recv()
  
    return self.ws


  async def auth_app(self):
    buffer = []

    await self.ws.send(json.dumps(auth_data))

    buffer.append(await self.ws.recv())
    buffer.append(await self.ws.recv())
    
    buffer = [*map(lambda el: json.loads(el), buffer)]

    with open('src/data/auth_response.json', 'w+', encoding='utf-8') as file: 
      file.write(json.dumps(buffer[0], indent=2))

    logger.info(f'subscribe event => {buffer[0]["d"]["resume_gateway_url"]}\n{"-"*20}')
    return self.ws


  async def heartbeat(self, interval: int) -> None:
    while True:
      await asyncio.sleep(interval)
      await self.ws.send(json.dumps({"op": 1,"d": None}))
      logger.info('Heartbeat event')


  async def event_listener(self) -> None:
    while True:
      event = json.loads(await self.ws.recv())

      if event['t']: 
        asyncio.ensure_future(evt.event_handler(event))
        continue

      logger.info(event)
      

  async def get_gateway(self) -> None:

    self.ws = await websockets.connect(self.gateway_url)

    response = json.loads(await self.ws.recv())

    logger.connect_log(response)
    
    if response['op'] == 10:

      asyncio.ensure_future(self.heartbeat(30))

      await self.first_connect(0)
      await self.auth_app()
      await self.event_listener()

