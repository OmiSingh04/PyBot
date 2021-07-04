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
