import discord

client = discord.Client()


class Reply:
    def __init__(self, message, reply, userDict={}):
        self.message = message
        self.reply = reply
        self.userDict = userDict

    def addSpecialReply(self, user, reply):
        self.userDict.update({user: reply})

    def removeSpecialReply(self, user):
        self.userDict.pop(user)

    def getReply(self, user):
        finalReply = self.reply

        for currUser in self.userDict:
            if currUser == user:
                finalReply = self.userDict[user]
                break

        return finalReply


def findReply(message, user):
    finalReply = ""

    for obj in responseList:
        if message.startswith(obj.message):
            finalReply = obj.getReply(user)
            break

    return finalReply


responseList = [Reply("guys", "and girls"),
                Reply("why", "because..."),
                Reply("yoink", "stop yoinken\' the wifi bumbo"),
                Reply("-hello", "Hello!", {'kgupta_1542': 'shut up kanishk'}),
                Reply("this is", "is it now?"),
                Reply("shut up", "rude"),
                Reply("VikBot", "righhhhht..."),
                Reply("spam", "spam-mer? I barely know-her!"),
                Reply("is it", "its not. \nno way... \nwe made it up.\nit\'s a total fabrication"),
                Reply("kg", "is the best",
                      {'marlee noelle': "SUS!"}),
                Reply("-roastme", "no one:\nnot even vikram:\nameesh: is a potatohead"),
                Reply("no u", "daaaaamn hit em with dat uno reverse card"),
                Reply("girls", "and guys"),
                Reply("-roast", "you are bad"),
                Reply("vikram", "I am cooler than him :sunglasses:",
                    {'VikBot': "why are you talking to yourself idiot?",
                     'ameesh_daryani': "ooh vik and ameesh sitting in a tree. Playing a game together, Rocket League"}),
                Reply("kyle", "kyle *would* be like that"),
                Reply("vc", "yes"),
                Reply("hmm", "what?"),
                Reply("Bah", "",
                      {'marlee noelle': "https://tenor.com/view/spongebob-laughing-lol-haha-happy-gif-15812661"}),
                Reply("gottem", "https://tenor.com/view/ladies-and-gentleman-we-got-him-gif-12313683")]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return

    finalReply = findReply(message.content, message.author.name)
    if len(finalReply) > 0:
        await message.channel.send(finalReply)

client.run('NzM4NTM0NjYwNDc2NTAyMDI2.XyNUAA.Uw9GF-7oZgd7zzGkvd9nbikiwNc')
