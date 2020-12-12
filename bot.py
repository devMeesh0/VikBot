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

    if message.author == client.user:
        return

    if message.content.startswith('guys'): 
        await message.channel.send('and girls')
    if message.content.startswith('-roast '):
        myId = '<@' + str(message.mentions[0].id) + '>'
        await message.channel.send( ' %s, you are bad ' % myId)
        # await client.send_message('rE, <!@' + str(message.mentions[0].id) + '> is kindof a bumbo')
        # await client.send_message(message.channel, 'rE, %s is a bumbo ' % )
    if message.content.startswith('yoink'): 
        await message.channel.send('stop yoinken\' the wifi bumbo')  
    if message.content.startswith('no u'): 
        await message.channel.send('daaaaamn {.author.name} hit em with dat uno reverse card'.format(message)) 
    if message.content.startswith('shut up'): 
        await message.channel.send('rude')
    if message.content.startswith('this is'): 
        await message.channel.send('is it now?')
    if message.content.startswith('VikBot:'): 
        await message.channel.send('righhhhht...')
    if message.content.startswith('spam'): 
        await message.channel.send('spam-mer? i barely know-her!')
    if message.content.startswith('is it'): 
        await message.channel.send('its not. \nno way... \nwe made it up.\nit\'s a total fabrication')
    if message.content.startswith('-hello'):
        if (message.author.name == 'kgupta_1542'):
            await message.channel.send('shut up kanishk')
        else:
            await message.channel.send('*Hello {.author.name}!*'.format(message))
    if message.content.startswith('kg'):
        # myId = '<@275329109154988043>'
        # await message.channel.send( ' %s, you are bad ' % myId)
        await message.channel.send('is bad')
    if message.content.startswith('-roastme'):  
        await message.channel.send( 'no one:\nnot even vikram:\n{.author.name}: is a potatohead'.format(message))
 
    # if message.content.startswith('-shut down'):
    #     await message.channel.send('shutting down')
    #     await client.logout()
        


client.run('NzM4NTM0NjYwNDc2NTAyMDI2.XyNUAA.C-2CI2jnh1uPQb2XDPRyJZqvxAk')