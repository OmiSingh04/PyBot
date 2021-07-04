import discord
from discord.ext import commands
from discord.ext.commands import Bot
import sys

client = commands.Bot(command_prefix=";")

token = sys.argv[1]

@client.command()
async def hello(ctx):
    await ctx.send("Woof!")

@client.command()
async def cool(ctx):
    await ctx.send("cool cool cool cool cool cool")

client.run(token)

#main file code
# from discord.ext import commands
# from discord import Embed, Color, Status

# bot = commands.Bot(command_prefix=commands.when_mentioned_or('#'))

# bot.remove_command('help')

# @bot.event
# async def on_ready():
#     await bot.change_presence(status=Status.idle)

# extensions = ['Commands', 'Accesories', 'Shop']

# for cogs in extensions:
#     bot.load_extension(f'{cogs}')

# bot.run(token)


# Commands file code
# from discord.ext import commands
# from discord import Embed, Color

# class Command(commands.Cog):
#     def _init_(self, bot):
#         self.bot = bot

#     @commands.group(name='commands', invoke_without_command=True)
#     async def cmdshelp(self, ctx):
#         await ctx.send('test')

#     @cmdshelp.command(name="synatx")
#     async def syntax(self, ctx):
#         await ctx.send('test')