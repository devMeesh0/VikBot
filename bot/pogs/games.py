import discord
from discord.ext import commands
import random
from functions import *

class games(commands.Cog):

	def __init__(self, client):
		self.client = client 

	@commands.command()
	async def kick(self, ctx, member: discord.Member, *, reason = None):
		await member.kick(reason=reason)

	@commands.command()
	async def roulette(self, ctx, *, reason = None):
	    if random.randrange(1,7) == 1:

    		arr = [str(r.id) for r in ctx.message.author.roles]
    		arr.insert(0, str(ctx.message.guild))
    		arr.insert(1, str(ctx.message.author))
	    	storeRoles(arr)   
	    	
	    	await ctx.message.author.kick(reason=reason)
	    	link = await ctx.channel.create_invite(max_age = 300)
	    	await ctx.send('hah DED!')

	    	channel = await ctx.message.author.create_dm()
    		await channel.send(link)
    		await channel.send('hah dumbo u died... feel free to join again, but be ready for ridicule')
	    else:
	    	await ctx.send('ew u alive still??!?')
	
def setup(client):
	client.add_cog(games(client))