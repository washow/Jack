import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
       await client.send_message(message.channel, 'Pong!')

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(member, fmt.format(member, server))
    mainChannel = discord.utils.get(server.channels, name='general', type=ChannelType.text)
    await client.send_message(mainChannel, fmt.format(member, server))

fh = open('jack.conf', 'r')
jack_key = fh.readline().rstrip()
client.run(jack_key)