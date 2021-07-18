from discord.ext import commands
import discord
from discord import Embed, Color, Status
from dotenv import load_dotenv
from db_manager.db_commands import DbCommands
from shop.shop_manager import Shop
import os

load_dotenv()

#Setting the Syntax
bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'))


token = os.getenv('TOKEN')
#db_user = os.getenv('DB_USER')
#db_password = os.getenv('DB_PASSWORD')
#db_database = os.getenv('DB_DATABASE')

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Ready")
    await bot.change_presence(status=Status.idle, activity = discord.Game(name = "Woofies"))

#List of Cogs
extensions = ['cmds.Commands', 'shop.shop_manager']

#initiation of Cogs
for cogs in extensions:
    bot.load_extension(f'{cogs}')

#bot.add_cog(DbCommands(bot, db_user, db_password, db_database))

bot.run(token)