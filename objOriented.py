import discord
import random

client = discord.Client()


class Reply:
    def __init__(self, message, reply, frequency=100, userDict={}):
        self.message = message
        self.reply = reply
        self.frequency = frequency
        self.userDict = userDict

    def addSpecialReply(self, user, reply):
        self.userDict.update({user: reply})

    def removeSpecialReply(self, user):
        self.userDict.pop(user)

    def getReply(self, user):
        finalReply = ""

        if self.frequency > random.randint(1, 100):
            finalReply = self.reply

            for currUser in self.userDict:
                if currUser == user:
                    finalReply = self.userDict[currUser]
                    break

        return finalReply


def findReply(message, user):
    finalReply = ""

    for obj in responseList:
        if message.find(obj.message) != -1:
            finalReply = obj.getReply(user)
            break

    return finalReply


responseList = [Reply("guys", "and girls", 50),
                Reply("why", "because...", 50),
                Reply("yoink", "stop yoinken\' the wifi bumbo", 25),
                Reply("-hello", "Hello!", 100,
                      {'kgupta_1542': 'shut up kanishk'}),
                Reply("this is", "is it now?", 5),
                Reply("shut up", "rude", 75),
                Reply("VikBot", "righhhhht...", 5),
                Reply("spam", "spam-mer? I barely know-her!", 10),
                Reply("is it", "its not. \nno way... \nwe made it up.\nit\'s a total fabrication", 5),
                Reply("kg", "is the best", 10,
                      {'marlee noelle': "SUS!",
                       "VikBot": "is bad"}),
                Reply("ameesh", "", 33,
                      {"VikBot": "ooh vik and ameesh sitting in a tree. Playing a game together, Rocket League"}),
                Reply("-roastme", "no one:\nnot even vikram:\nameesh: is a potatohead"),
                Reply("no u", "daaaaamn hit em with dat uno reverse card", 15),
                Reply("girls", "and guys", 25),
                Reply("-roast", "you are bad", 100),
                Reply("vikram", "I am cooler than him :sunglasses:", 15,
                    {'VikBot': "why are you talking to yourself idiot?",
                     'ameesh_daryani': "ooh vik and ameesh sitting in a tree. Playing a game together, Rocket League"}),
                Reply("kyle", "kyle *would* be like that", 15),
                Reply("vc", "yes", 65),
                Reply("hmm", "what?", 10),
                Reply("bah", "Stop copying Marlee smh", 65,
                      {'marlee noelle': "bah indeed"}),
                Reply("gottem", "https://tenor.com/view/ladies-and-gentleman-we-got-him-gif-12313683", 100),
                Reply("pls work", "", 100,
                      {"Kyler Fung", "go get a real job in the real world"}),
                Reply("bikram", "goat yoga therapy? Yes please", 35,
                      {"VikBot": "love yoga! love goats :love_you_gesture: :star_struck:"})]


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
