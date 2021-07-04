from discord.ext import commands
from discord import Embed, Color, Status

bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'))

bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=Status.idle)

extensions = ['cmds.Commands']

for cogs in extensions:
    bot.load_extension(f'{cogs}')

bot.run("token")