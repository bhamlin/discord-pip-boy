#!env/bin/python3

import discord
import asyncio

import auth
import pipboy

from datetime import datetime
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
    print(str(datetime.now()))
    print('------')

@client.event
async def on_message(message):
    line = message.content
    fields = [x for x in dir(message) if not x.startswith('_')]

    if line.startswith('~p ') and len(line) > 3:
        tmp = await client.send_message(message.channel, choice(__DELAYING))
        stack, result = pipboy.parse(line[3:])
        if stack:
            await client.edit_message(tmp, 'Rolled: {}'.format(', '.join(map(str, stack))))
        if result:
            await client.send_message(message.channel, 'Result: {}'.format(str(result)))
        if not stack and not result:
            await client.edit_message(tmp, '''I don't have a response for you... *[error?]*''')
    elif line.startswith('~g ') and len(line) > 3:
        tmp = await client.send_message(message.channel, choice(__DELAYING))
        response = pipboy.game_opt(message)
        if response:
            await client.edit_message(tmp, response)
        else:
            await client.edit_message(tmp, '''I don't have a response for you... *[error?]*''')
#    elif message.content.startswith('!sleep'):
#        await asyncio.sleep(5)
#        await client.send_message(message.channel, 'Done sleeping')

client.run(auth.token)
