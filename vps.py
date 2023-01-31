import asyncio
from telethon import TelegramClient, errors

api_id = 21040680
api_hash = 'dd618b23a8f6870e2c4892c1ebecc9e2'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    group_entities = [await client.get_entity('@ApretasteCuba'),
                      await client.get_entity('@kbola_asere'),
                      await client.get_entity('@SpamEstadosUnidos'),
                      await client.get_entity('@Ganar_Dinero_referidos_Grupo'),
                      await client.get_entity('@Listagram'),
                      #await client.get_entity('@moron_negocia_grupo'),
                      # await client.get_entity('@hFTradersacademy'),
                      await client.get_entity('@todo_spam_grupo')]
    while True:
        for group_entity in group_entities:
            try:
                await client.send_message(group_entity, 'se veende diamantes ')
                await asyncio.sleep(30) # agrega una pausa de 30 segundos
            except errors.UsernameNotOccupiedError:
                # Si el usuario o grupo no existe, simplemente ignorar y continuar
                pass
        await asyncio.sleep(600) # espera 10 minutos

with client:
    client.loop.run_until_complete(main())
