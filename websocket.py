from websockets.sync.client import connect
from vars import server
import asyncio

websocket = None

async def message():
    while True:
        try:
            message = await websocket.recv()
            if message:
                print(f"Received message: {message}")
        except Exception as e:
            print(f"An error occurred: {e}")
        await asyncio.sleep(0.1)

def connect_to_websocket(match_id):
    global websocket
    uri = f"ws://{server}/ws/match/{match_id}/"
    print(f"Connecting to {uri}...")

    with connect(uri) as ws:
        websocket = ws  # Update the global websocket variable
        print("Connected!")

def disconnect_from_websocket():
    global websocket
    if websocket:
        print(f"Disconnecting from websocket...")
        websocket.close()
        websocket = None
    
    
    