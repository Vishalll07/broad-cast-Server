import asyncio
import websockets

clients = {}  # maps websocket -> user_id
client_id_counter = 1

async def handler(websocket):
    global client_id_counter
    user_id = f"User {client_id_counter}"
    client_id_counter += 1
    clients[websocket] = user_id

    print(f"New connection: {user_id} ({websocket.remote_address})")

    try:
        async for message in websocket:
            broadcast_message = f"{user_id}: {message}"
            await broadcast(broadcast_message, sender=websocket)
    except websockets.exceptions.ConnectionClosed:
        print(f"{user_id} disconnected")
    finally:
        del clients[websocket]

async def broadcast(message, sender=None):
    for client in clients:
        if client != sender:  # don't send back to sender
            await client.send(message)

async def run_server(host, port):
    print(f"Server started on ws://{host}:{port}")
    async with websockets.serve(handler, host, port):
        await asyncio.Future()  # Run forever

def start_server(host, port):
    asyncio.run(run_server(host, port))
