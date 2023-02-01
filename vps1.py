import asyncio
from telethon import TelegramClient, errors

api_id = 29577035
api_hash = 'a1b79892e940a0033e36914534d01e70'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    group_entities = [await client.get_entity('@MLC_isladelajuventud'),
                      await client.get_entity('@compraisla'),
                      await client.get_entity('@isla_venta'),
                      await client.get_entity('@Isla_De_La_Juventud_Ventas'),
                      await client.get_entity('@ventasisladepinos'),
                      await client.get_entity('@geronabusiness'),
                      # await client.get_entity('@hFTradersacademy'),
                      await client.get_entity('@comprasyventasenlaisla')]
    while True:
        for group_entity in group_entities:
            try:
                await client.send_message(group_entity, '📯 BUSCO 📯\n\nMLC 145 💳‼️\nEURO 145 💶‼️\nUSD 145 💵‼️\n\n📫 DISPONIBLES 24 hrs, no dude escribir o llamar será bien atendido 📌\n\n🛎️ REMESAS 🛎️\n100 🇺🇸14000cup 🇨🇺\n115 🇺🇸 x 100mlc 🇨🇺\n110 🇺🇸x 100usd 🇨🇺\n\n🛡️ Nuestro servicio es de alta seguridad. 🛡️\n🛡️ Le brindamos a nuestros clientes la mejor atención para su comodidad y confianza. 🛡️\n🛡️ Todo presencial. 🛡️\n🛡️ Nos marca la buena referencia. 🛡️\n\n🚨🚩🚨\nCuide su dinero de imitadores y estafadores. 🚨🚩🚨')
                await asyncio.sleep(60) # agrega una pausa de 60 segundos
            except errors.UsernameNotOccupiedError:
                # Si el usuario o grupo no existe, simplemente ignorar y continuar
                pass
        await asyncio.sleep(9488) # espera 2:48 horas 

with client:
    client.loop.run_until_complete(main())

