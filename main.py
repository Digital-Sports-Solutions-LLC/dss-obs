from selector import selector
from websocket import message
import asyncio
import threading

selector_thread = threading.Thread(target=selector)
selector_thread.start()

asyncio.run(message())

    