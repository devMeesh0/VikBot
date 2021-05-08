import discord
import os
from reply import *
from functions import *
from discord.ext import commands
import random



intents = discord.Intents.default()
intents.members = True


# this is the client
client = commands.Bot(command_prefix='-', intents = intents)
token = os.getenv("DISCORD_BOT_KEY")



# Finds the correct reply amongst Reply objects
def findReply(message):
    # Set default values
    finalReply = ""

    # Go through all the Reply objects
    for obj in responseList:
        # Max substring start index at 0 if searchType == 1
        endVal = 0 if obj.searchType == 1 else len(message.content) - 1
        index = message.content.find(obj.message)

        # Check if index is a valid value
        if index != -1 and index <= endVal:
            # Get correct reply from Reply object
            finalReply = obj.getReply(message)
            break

    return finalReply





# Define all Replies in a list
responseList = [FuncReply("warp", warp, 100),
                FuncReply("swirl", swirl, 100),
                FuncReply("edge", edges, 100),
                FuncReply("gray", grayscale, 100),
                FuncReply("meme", printBack, 100),
                TextReply("guys", "and girls", 50),
                # TextReply("why", "because...", 10),
                # TextReply("start the war", "war", 100),
                TextReply("yoink", "stop yoinken\' the wifi bumbo", 90),
                TextReply("hello", "Hello {}!", 100, 1, 2,
                      {'kgupta_1542': 'shut up kanishk'}),
                TextReply("this is", "is it now?", 10),
                TextReply("shut up", "rude", 75),
                TextReply("VikBot", "righhhhht...", 85),
                TextReply("spam", "spam-mer? I barely know-her!", 15),
                TextReply("is it", "its not. \nno way... \nwe made it up.\nit\'s a total fabrication", 10),
                TextReply("kg", "is the best", 25, 0, 0,
                      {'marlee noelle': "SUS!",
                       "VikBot": "is bad"}),
                TextReply("ameesh", "", 33, 0, 0,
                      {"VikBot": "ooh vik and ameesh sitting in a tree. Playing a game together, Rocket League"}),
                TextReply("roastme", "no one:\nnot even vikram:\n{}: is a potatohead", 100, 1, 1),
                TextReply("no u", "daaaaamn {} hit em with dat uno reverse card", 15, 1, 1),
                TextReply("girls", "and guys", 25),
                TextReply("roast", "{} you are bad", 100, 1, 3),
                TextReply("vikram", "I am cooler than him :sunglasses:", 25, 30, 30,
                    {'VikBot': "why are you talking to yourself idiot?",
                     'ameesh_daryani': "ooh vik and ameesh sitting in a tree. Playing a game together, Rocket League"}),
                TextReply("kyle", "kyle *would* be like that", 25),
                TextReply("vc", "yes", 65),
                TextReply("hmm", "what?", 10),
                TextReply("bah", "Stop copying Marlee smh", 65, 0, 0,
                      {'marlee noelle': "bah indeed"}),
                TextReply("gottem", "https://tenor.com/view/ladies-and-gentleman-we-got-him-gif-12313683", 100),
                TextReply("pls work", "", 100, 1, 0,
                      {"kyl3": "go get a real job in the real world"}),
                TextReply("pls rob", "", 100, 1, 0,
                      {"kyl3": "bruh you are such a delinquent"}),
                TextReply("bikram", "goat yoga therapy? Yes please", 35, 0, 0,
                      {"VikBot": "love yoga! love goats :love_you_gesture: :star_struck:"}),
                TextReply("spencer", "that koding kid", 50, 0, 0,
                      {"Engineer Zero": "Why you talking to yourself???"}),
                TextReply("snack", "https://tenor.com/view/snack-gif-19586327", 100, 1, 0),
                TextReply("guy", ":gaillou:", 100, 1, 0),
                TextReply("i think you mean", "don't assume fool",65)]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('heroku fuels me.'))


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extention}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extention}')

files = os.getcwd()
for filename in os.listdir(files):
      if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_member_join(member):
    roles = retrieveRoles(member.name)
    for i in roles:
        Filter = filter(str.isdigit, i)
        res = "".join(Filter)
        role = discord.utils.get(member.guild.roles, id = int(res))
        await member.add_roles(role)

@client.event
async def on_message(message):
    # Lower case message content
    message.content = message.content.lower()

    # Ignore messages from bot
    if message.author == client.user:
        return

    # Find correct reply
    finalReply = findReply(message)

    # If reply isn't empty string, send
    if type(finalReply) is str:
        if len(finalReply) > 0:
            await message.channel.send(finalReply)
    else:
        await message.channel.send(file=finalReply)

    await client.process_commands(message)

client.run(token)
