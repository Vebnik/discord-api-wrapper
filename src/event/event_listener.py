import websockets
import asyncio
import json


class Event_Listen():

  test_wss_url = 'wss://gateway-us-east1-b.discord.gg'


  def __init__(self):
    asyncio.run(self.gatewat_connect())


  async def auth_connect(self, ws):
    await ws.send(json.dumps({"op": 1,"d": 0}))
    return ws


  async def gatewat_connect(self):
    async with websockets.connect(self.test_wss_url) as ws:

      await self.auth_connect(ws)

      while True:
        event = await ws.recv()
        print('on event listener', event)
