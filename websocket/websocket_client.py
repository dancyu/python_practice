import asyncio
import websockets
'''
This is a sample to connect a websocket.

the websocket wss://stream.aylanetworks.com/stream?stream_key=daa66a8e086340e394e16bd9bf1ba58b
may become invalid.
you can change to your websocket stream uri.

'''


async def hello():
    uri = "wss://stream.aylanetworks.com/stream?stream_key=daa66a8e086340e394e16bd9bf1ba58b"
    async with websockets.connect(uri) as websocket:
        #name = input("What's your name? ")

        await websocket.send(Z)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
