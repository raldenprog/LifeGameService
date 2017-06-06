import asyncio
import logging
import socket


logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s ',
                    level=logging.INFO)


async def main_server(reader, writer):
    print('Connection from {}'.format(
       writer.get_extra_info('peername')
    ))
    while True:
        data = await reader.read(100)
        if data:
            message = data.decode()
            print("Echoing back: {!r}".format(message))
            writer.write(data)
            await writer.drain()
            #writer.close()
        else:
            print("Terminating connection")
            writer.close()
            break

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.ensure_future(
            asyncio.start_server(main_server, '127.0.0.1', 7777),
            loop=loop
        )
    )
    loop.run_forever()
