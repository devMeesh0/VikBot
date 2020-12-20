import discord
import os
from PIL import Image
from discord.ext import commands

client = discord.Client()
token = os.getenv("DISCORD_BOT_KEY")


description = '''BRO ITS VIKBOT.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', description=description, intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    


@client.event
async def on_message(message):
    message.content = message.content.lower()
    messageSenderId = ''

    if(len(message.mentions) != 0):
        messageSenderId = '<@' + str(message.mentions[0].id) + '>'
        

    responses = {'guys': 'and girls', 'why': "because...", 'yoink': 'stop yoinken\' the wifi bumbo', 'this is': 'is it now?', 'shut up': 'rude', 'VikBot:': 'righhhhht...', 'spam': 'spam-mer? i barely know-her!', 'is it': 'its not. \nno way... \nwe made it up.\nit\'s a total fabrication', 'kg': 'is bad', '-roastme': 'no one:\nnot even vikram:\n{.author.name}: is a potatohead'.format(message), 'no u': 'daaaaamn {.author.name} hit em with dat uno reverse card'.format(message), 'girls': 'and guys', '-roast ': ' %s, you are bad ' % messageSenderId, 'vikram': 'I am cooler than him :sunglasses:', 'kyle': 'kyle *would* be like that', 'vc': 'yes', 'hmm': 'what?', 'bro': 'YES?!?!' 
    }

    if message.author == client.user:
        return

    for call in responses:
        if(message.content.startswith(call)):
            await message.channel.send(responses[call])
        
    if message.content.startswith('-hello'):
        if (message.author.name == 'kgupta_1542'):
            await message.channel.send('shut up kanishk')
        else:
            await message.channel.send('*Hello {.author.name}!*'.format(message))
        
# def imageProcessor(image):

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)



client.run(token)
