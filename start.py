
# script.module.websocketclient
import asyncio
import websockets
from jsonrpcclient.clients.websockets_client import WebSocketsClient


async def main():
    websockets.WebSocketClientProtocol
    async with websockets.connect('ws://kodi:kodi@localhost:8080/jsonrpc') as ws:
        response = await WebSocketsClient(ws).request('Addons.GetAddons')
    print(response)

asyncio.get_event_loop().run_until_complete(main())
