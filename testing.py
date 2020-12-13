import discord

client = discord.Client()
# str user1



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    # if message.content.startswith('spam'): 
    #     await message.channel.send('spam')

    responses = {
    'guys': 'and girls',
    'why': "because",
    'yoink': 'stop yoinken\' the wifi bumbo',
    'this is': 'is it now?',
    'shut up': 'rude',
    'VikBot:': 'righhhhht...',
    'spam': 'spam-mer? i barely know-her!',
    'is it': 'its not. \nno way... \nwe made it up.\nit\'s a total fabrication',
    'kg': 'is bad',
    '-roastme': 'no one:\nnot even vikram:\n{.author.name}: is a potatohead'.format(message),
    'no u': 'daaaaamn {.author.name} hit em with dat uno reverse card'.format(message)
    }

    if message.author == client.user:
        return

    for call in responses:
        if(message.content.startswith(call)):
            await message.channel.send(responses[call])


    if message.content.startswith('-roast '):
        myId = '<@' + str(message.mentions[0].id) + '>'
        await message.channel.send( ' %s, you are bad ' % myId)
        # await client.send_message('rE, <!@' + str(message.mentions[0].id) + '> is kindof a bumbo')
        # await client.send_message(message.channel, 'rE, %s is a bumbo ' % )
        
    if message.content.startswith('-hello'):
        if (message.author.name == 'kgupta_1542'):
            await message.channel.send('shut up kanishk')
        else:
            await message.channel.send('*Hello {.author.name}!*'.format(message))


    if message.content.startswith():  
        await message.channel.send( )
 
    # if message.content.startswith('-shut down'):
    #     await message.channel.send('shutting down')
    #     await client.logout()
        


client.run('NzM4NTM0NjYwNDc2NTAyMDI2.XyNUAA.Uw9GF-7oZgd7zzGkvd9nbikiwNc')