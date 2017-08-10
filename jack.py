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
    myServer = member.server
    msg = 'Welcome to the Tekken 7 beginners discord {0.mention} ! You have been given the NewBlood role to help the bot assign your other roles. Make sure to check out the set_role channel to choose your roles! You can use HELP_COMMAND to see a list of commands or check out bot_commands.'
    await client.send_message(myServer.default_channel, msg.format(member))

fh = open('jack.conf', 'r')
jack_key = fh.readline().rstrip()
client.run(jack_key)