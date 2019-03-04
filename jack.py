import discord
import asyncio
import re
import csv
import random

client = discord.Client()
tnb_quotes = []

@client.async_event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.async_event
def on_message(message):
    if message.content.startswith('!ping'):
       yield from client.send_message(message.channel, 'Pong!')

# Event for when a user wants to print a quote
@client.async_event
def on_message(message):
    server = message.author.server
    if message.content.startswith('^tnbquote'):
        yield from client.send_message(message.channel, random.choice(tnb_quotes))

with open('Tnbquotes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        tempquote = row[2].lower()
        if "nig" not in tempquote:
            new_quote = row[2] + " -"+row[1]
            tnb_quotes.append(new_quote)

for q in tnb_quotes:
    print(q)

fh = open('jack.conf', 'r')
jack_key = fh.readline().rstrip()
client.run(jack_key)
