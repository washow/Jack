import discord
import asyncio
import re

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

# Event for when a new memeber joins the server
# This message will be sent into the general channel and as a direct message to the user
@client.event
async def on_member_join(member):
    server = member.server
    # TODO: Uppdate the welcome mention with what will be said in TekkenNB
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(member, fmt.format(member, server))
    mainChannel = discord.utils.get(server.channels, name='general')
    await client.send_message(mainChannel, fmt.format(member, server))

# Event for when a user wants to change their region
@client.event
async def on_message(message):
    if message.content.startswith('.myregion'):
        await client.send_message(message.channel, 'Test')
        args = message.content.split()
        westCoast = re.compile('west\s?coast', re.I)
        matchVar = westCoast.match(args[1])
        if matchVar:
            westCoastRole = discord.utils.get(server.roles, name='WestCoast')
            await client.add_roles(message.author, [westCoastRole])
            # await client.send_message(send_message(message.channel, message.author.mention + ' you are in the West Coast!'))

fh = open('jack.conf', 'r')
jack_key = fh.readline().rstrip()
client.run(jack_key)