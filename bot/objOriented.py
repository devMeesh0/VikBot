import discord
import random
import os

client = discord.Client()
token = os.getenv("DISCORD_BOT_KEY")

class Reply:
    def __init__(self, message, reply, frequency=100, searchType=0, inputType=0, userDict={}):
        self.message = message
        self.reply = reply
        self.frequency = frequency

        # 0 -> contains, 1 -> startswith
        self.searchType = searchType

        # 0 -> none, 1 -> author name, 2 -> author mention, 3 -> message mention
        self.inputType = inputType
        self.userDict = userDict

    # Adds a special reply
    def addSpecialReply(self, user, reply):
        self.userDict.update({user: reply})

    # Removes a special reply
    def removeSpecialReply(self, user):
        self.userDict.pop(user)

    # Returns correct reply given user
    def getReply(self, user):
        finalReply = ""

        # Probability test to see if bot sends message
        if self.frequency > random.randint(1, 100):
            # Set default message
            finalReply = self.reply

            # Check for any special messages
            for currUser in self.userDict:
                if currUser == user:
                    finalReply = self.userDict[currUser]
                    break

        return finalReply

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
            finalReply = obj.getReply(message.author.name)

            # Format based on inputType key
            if obj.inputType == 1:
                finalReply = finalReply.format(message.author.name)
            elif obj.inputType == 2:
                finalReply = finalReply.format(message.author.mention)
            elif obj.inputType == 3:
                mention = '<@' + str(message.mentions[0].id) + '>' if len(message.mentions) > 0 else ""
                finalReply = finalReply.format(mention)
            break

    return finalReply

# Define all Replies in a list
responseList = [Reply("guys", "and girls", 50),
                Reply("why", "because...", 50),
                Reply("yoink", "stop yoinken\' the wifi bumbo", 90),
                Reply("-hello", "Hello {}!", 100, 1, 2,
                      {'kgupta_1542': 'shut up kanishk'}),
                Reply("this is", "is it now?", 10),
                Reply("shut up", "rude", 75),
                Reply("VikBot", "righhhhht...", 85),
                Reply("spam", "spam-mer? I barely know-her!", 15),
                Reply("is it", "its not. \nno way... \nwe made it up.\nit\'s a total fabrication", 10),
                Reply("kg", "is the best", 25,
                      {'marlee noelle': "SUS!",
                       "VikBot": "is bad"}),
                Reply("ameesh", "", 33,
                      {"VikBot": "ooh vik and ameesh sitting in a tree. Playing a game together, Rocket League"}),
                Reply("-roastme", "no one:\nnot even vikram:\n{}: is a potatohead", 100, 1, 1),
                Reply("no u", "daaaaamn {} hit em with dat uno reverse card", 15, 1, 1),
                Reply("girls", "and guys", 25),
                Reply("-roast", "{} you are bad", 100, 1, 3),
                Reply("vikram", "I am cooler than him :sunglasses:", 15,
                    {'VikBot': "why are you talking to yourself idiot?",
                     'ameesh_daryani': "ooh vik and ameesh sitting in a tree. Playing a game together, Rocket League"}),
                Reply("kyle", "kyle *would* be like that", 25),
                Reply("vc", "yes", 65),
                Reply("hmm", "what?", 10),
                Reply("bah", "Stop copying Marlee smh", 65,
                      {'marlee noelle': "bah indeed"}),
                Reply("gottem", "https://tenor.com/view/ladies-and-gentleman-we-got-him-gif-12313683", 100),
                Reply("pls work", "", 100, 1, 0,
                      {"Kyler Fung": "go get a real job in the real world"}),
                Reply("pls rob", "", 100, 1, 0,
                      {"Kyler Fung": "bruh you are such a delinquent"}),
                Reply("bikram", "goat yoga therapy? Yes please", 35,
                      {"VikBot": "love yoga! love goats :love_you_gesture: :star_struck:"}),
                Reply("spencer", "that koding kid", 50,
                      {"Engineer Zero": "Why you talking to yourself???"})]


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
