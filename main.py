# Cliente Websocket

import asyncio
import websockets

# Envia el mensaje al servidor WebSocket
async def send_message(uri, message):
    async with websockets.connect(uri) as ws:
        await ws.send(message)
        message_received = await ws.recv()
        print(f"Mensaje recibido por parte del servidor: {str(message_received)}")


# Ejecucion principal
if __name__ == "__main__":
    message = input(
        "Buenas! Por favor digite el mensaje que desea enviar al servidor \n"
    )
    print(f"Mensaje recibido: {message}")
    uri = input(
        "Ingrese la direccion del host y el puerto con formato: <HOST>:<PUERTO> \n"
    )
    asyncio.run(send_message(f"ws://{uri}", message))
