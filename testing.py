import discord

client = discord.Client()
# str user1



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    message.content = message.content.lower()

    if(len(message.mentions) != 0):
        messageSenderId = '<@' + str(message.mentions[0].id) + '>'

    responses = {
    'guys': 'and girls',
    'why': "because...",
    'yoink': 'stop yoinken\' the wifi bumbo',
    'this is': 'is it now?',
    'shut up': 'rude',
    'VikBot:': 'righhhhht...',
    'spam': 'spam-mer? i barely know-her!',
    'is it': 'its not. \nno way... \nwe made it up.\nit\'s a total fabrication',
    'kg': 'is bad',
    '-roastme': 'no one:\nnot even vikram:\n{.author.name}: is a potatohead'.format(message),
    'no u': 'daaaaamn {.author.name} hit em with dat uno reverse card'.format(message),
    'girls': 'and guys',
    '-roast ': ' %s, you are bad ' % messageSenderId,
    'vikram': 'I am cooler than him :sunglasses:',
    'kyle': 'kyle *would* be like that',
    'vc': 'yes',
    'hmm': 'what?'
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
        
    

client.run('NzM4NTM0NjYwNDc2NTAyMDI2.XyNUAA.Uw9GF-7oZgd7zzGkvd9nbikiwNc')