#!env/bin/python3

import discord
import asyncio

import auth

import pipboy

from random import choice

__DELAYING = (
    'Modernizing GURPs...',
    'Readying against a charge...',
    'Applying bonuses...',
    'Rolling initiative...',
    'Saving versus death magic...',
    'Checking for Mountain Dew...',
    'Attacking the darkness...',
    'Applying boot to the head...',
)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    line = message.content
    fields = [x for x in dir(message) if not x.startswith('_')]

    if line.startswith('~p ') and len(line) > 3:
        # print('--------------------------------')
        # print({field: getattr(message, field) for field in fields})
        tmp = await client.send_message(message.channel, choice(__DELAYING))
#        async for log in client.logs_from(message.channel, limit=100):
#            if log.author == message.author:
#                counter += 1
        stack, result = pipboy.parse(line[3:])
        if stack:
            await client.edit_message(tmp, 'Rolled: {}'.format(', '.join(map(str, stack))))
        if result:
            await client.send_message(message.channel, 'Result: {}'.format(str(result)))
        if not stack and not result:
            await client.edit_message(tmp, '''I don't have a response for you... *[error?]*''')
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(auth.token)
