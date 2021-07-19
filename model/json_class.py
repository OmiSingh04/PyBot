from discord.ext import commands
from discord import Embed, Color

import json
from os import replace, getcwd, path, mkdir
from time import sleep

data={
	"name":"",
	"user_id":"",
	"treats":"",
	"boosts":""
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
			await ctx.send('Success!!')
		else:
			await ctx.send('Already registered')

	def json_register(self, data):
		if(not(path.isdir(f'{getcwd()}/account'))):
			mkdir(f'{getcwd()}/account')
		elif(not(path.isdir(f'{getcwd()}/account/{data["name"]}.json'))):
			print(path.isdir(f'{getcwd()}/account/{data["name"]}.json'))
			with open(f"{data['name']}.json", 'w') as fp:
				json.dump(data, fp)

			sleep(5)
			replace(f'{getcwd()}/{data["name"]}.json', f'{getcwd()}/account/{data["name"]}.json')

			return True
		else:
			print('edan')
			return False

def setup(bot):
	bot.add_cog(Json(bot))