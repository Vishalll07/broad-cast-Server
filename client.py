import asyncio
import websockets
from colorama import Fore, Style, init

init(autoreset=True)

async def send(websocket):
    while True:
        msg = await asyncio.to_thread(input, f"{Fore.CYAN}You: {Style.RESET_ALL}")
        await websocket.send(msg)

async def receive(websocket):
    async for message in websocket:
        print(f"\n{Fore.GREEN}{message}{Style.RESET_ALL}")

async def send_and_receive(uri):
    async with websockets.connect(uri) as websocket:
        print(f"{Fore.YELLOW}Connected to the server.{Style.RESET_ALL}")
        await asyncio.gather(send(websocket), receive(websocket))

def connect_client(host, port):
    uri = f"ws://{host}:{port}"
    asyncio.run(send_and_receive(uri))
