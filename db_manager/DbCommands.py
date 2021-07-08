import mysql.connector
from discord.ext import commands
from discord import Embed, Color

class DbCommands(commands.Cog):
	def __init__(self, bot, user, password):
		self.bot = bot
		self.user = user
		self.password = password
		self.mydb = mysql.connector.connect(
 			host="localhost",
 			user=self.user,
 			password=self.password,
  			database="husky_bot"
		)


	@commands.command(name='register', brief="reg")
	async def register(self, ctx):
		mycursor = self.mydb.cursor()
		sql = '''INSERT INTO USERS VALUES(%s, %s, %s)'''
		val = (ctx.message.author.id, 500, 1)
		mycursor.execute(sql,val)
		self.mydb.commit()
		print(mycursor.rowcount, "record inserted.")
		await ctx.send("Registered! You have 500 treats. You are on level 1 based on activity")