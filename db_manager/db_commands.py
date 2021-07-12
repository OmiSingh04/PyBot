import mysql.connector
from discord.ext import commands
from discord import Embed, Color
from .db_manager import Db_Manager



class DbCommands(commands.Cog):
	def __init__(self, bot, user, password, database):
		self.bot = bot
		self.user = user
		self.password = password
		self.db = Db_Manager(user, password, database)


	@commands.command(name='register', brief="reg")
	async def register(self, ctx):
		x = self.db.register(ctx.message.author.user_id)
		if not x:
			await ctx.send('You are already registered!')
		else:
			await ctx.send('Registered! You have 500 treats. You are level 1 based on activity.')
