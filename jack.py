import discord
import asyncio
import re
import csv

client = discord.Client()
tnb_quotes = []

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

# Event for when a user wants to change their region
@client.event
async def on_message(message):
    server = message.author.server
    if message.content.startswith('^tnbquote'):
        myquote = get_quote()
        await client.send_message(message.channel, myquote)

fh = open('jack.conf', 'r')
jack_key = fh.readline().rstrip()
client.run(jack_key)
with open('Tnbquotes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_quote = row['What is the quote?'] + " -"+row['Who said it?']
        tnb_quotes.append(new_quote)

for q in tnb_quotes:
    print(q)