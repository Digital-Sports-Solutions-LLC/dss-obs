import asyncio
import websockets
from vars import server
import time

# ALL BROKEN DOES NOT WORK

def on_message(message):
    print(f"Received message: {message}")

def connect_to_websocket(match_id):
    uri = f"ws://{server}/ws/match/{match_id}/"
    print(f"Connecting to {uri}...")

    start_time = time.time()  # Record the start time

    ws = websockets.connect(uri)
    ws.on_message = on_message(ws.message)

    end_time = time.time()  # Record the end time
    print(f"Connected in {end_time - start_time:.2f} seconds.")
    
    asyncio.get_event_loop().run_until_complete(ws)  

def obs(match_id):
    connect_to_websocket(match_id)