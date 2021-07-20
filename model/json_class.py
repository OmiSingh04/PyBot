from discord.ext import commands
from discord import Embed, Color

import json
from os import replace, getcwd, path, mkdir
from time import sleep

data={
	"name":"",
	"user_id":0,
	"treats":0,
	"boosts":0
}

class Json(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='register', aliases=['reg'])
	async def register(self, ctx):
		data['name'] = ctx.author.name
		data['user_id'] = ctx.author.id
		data['treats'] = 500
		data['boosts'] = 0
		if(self.json_register(data)):
			embed = Embed(title='Success', description="You are given 500 treats", color=Color.random())
			await ctx.send(embed=embed)
		else:
			embed = Embed(title="Already registered", description="Seems like you have already registered", color=Color.random())
			await ctx.send(embed=embed)

	def json_register(self, data):
		if(not(path.exists(f'{getcwd()}\\account'))):
			mkdir(f'{getcwd()}\\account')
		elif(not(path.exists(f'{getcwd()}\\account\\{data["name"]}.json'))):
			with open(f"{data['name']}.json", 'w') as fp:
				json.dump(data, fp)
			sleep(5)
			replace(f'{getcwd()}\\{data["name"]}.json', f'{getcwd()}\\account\\{data["name"]}.json')
			return True
		else:
			return False

def setup(bot):
	bot.add_cog(Json(bot))
