import random
import discord

token = "YOUR DISCORD BOT TOKEN"

client = discord.Client()

@client.event
async def on_ready():
    print('[!] Congrats, you did it! The bot is online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$giveaname'):
        name = genname()
        await message.channel.send(name)

def genname():
    first_names = ['Tobias', 'Mccarty', 'Arthur', 'Callahan', 'Vinny', 'Mendoza', 'Cody', 'Castillo', 'Christian', 'Burton', 'Ali', 'Levine', 'Regan', 'Murphy', 'Kamil', 'Finley', 'Alexander', 'Mcclure', 'Wiktor', 'Brennan']
    last_names = ['Ines', 'Bridges', 'Ada', 'Faulkner', 'Mohammad', 'Thomson', 'Kurt', 'Hayden', 'Monty', 'Burns', 'Mitchell', 'Gates', 'Marcus', 'Chang', 'Haseeb', 'Browning', 'Scott', 'Nichols', 'Ciaran', 'Wells']

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    name = first_name + ' ' + last_name

    return name

client.run(token)
