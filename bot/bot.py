import discord
import os
from reply import *
from functions import *

client = discord.Client()
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
responseList = [FuncReply("-meme", printBack, 100),
                TextReply("guys", "and girls", 50),
                TextReply("why", "because...", 50),
                TextReply("yoink", "stop yoinken\' the wifi bumbo", 90),
                TextReply("-hello", "Hello {}!", 100, 1, 2,
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
                TextReply("-roastme", "no one:\nnot even vikram:\n{}: is a potatohead", 100, 1, 1),
                TextReply("no u", "daaaaamn {} hit em with dat uno reverse card", 15, 1, 1),
                TextReply("girls", "and guys", 25),
                TextReply("-roast", "{} you are bad", 100, 1, 3),
                TextReply("vikram", "I am cooler than him :sunglasses:", 15, 0, 0,
                    {'VikBot': "why are you talking to yourself idiot?",
                     'ameesh_daryani': "ooh vik and ameesh sitting in a tree. Playing a game together, Rocket League"}),
                TextReply("kyle", "kyle *would* be like that", 25),
                TextReply("vc", "yes", 65),
                TextReply("hmm", "what?", 10),
                TextReply("bah", "Stop copying Marlee smh", 65, 0, 0,
                      {'marlee noelle': "bah indeed"}),
                TextReply("gottem", "https://tenor.com/view/ladies-and-gentleman-we-got-him-gif-12313683", 100),
                TextReply("pls work", "", 100, 1, 0,
                      {"Kyler Fung": "go get a real job in the real world"}),
                TextReply("pls rob", "", 100, 1, 0,
                      {"Kyler Fung": "bruh you are such a delinquent"}),
                TextReply("bikram", "goat yoga therapy? Yes please", 35, 0, 0,
                      {"VikBot": "love yoga! love goats :love_you_gesture: :star_struck:"}),
                TextReply("spencer", "that koding kid", 50, 0, 0,
                      {"Engineer Zero": "Why you talking to yourself???"}),
                TextReply("-snack", "https://tenor.com/view/snack-gif-19586327", 75, 1, 0),
                TextReply("guy", "test :gaillou: ", 100, 0, 0),
                TestReply(":bbb:", "https://tenor.com/view/rage-iquit-angry-table-flip-studying-gif-4905184")]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


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
    if len(finalReply) > 0:
        await message.channel.send(finalReply)

client.run(token)