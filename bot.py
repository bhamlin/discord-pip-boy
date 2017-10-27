#!env/bin/python3

import discord
import asyncio

import auth

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    print('--------------------------------')
    line = message.content
    fields = [x for x in dir(message) if not x.startswith('_')]
    print({field: getattr(message, field) for field in fields})

    if line.startswith('~p ') and len(line) > 3:
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(auth.token)
