from discord.ext import commands
from discord import Embed, Color
class Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("ready")

	@commands.command(name="cmds")
	async def cmds(self, ctx):
		await ctx.send('test')

	@commands.command(name='pet', brief="p")
	async def pet(self, ctx):
		embed=Embed(title="Woof Woof!!", color=Color.blue())
		embed.set_image(url="https://forgifs.com/gallery/d/287041-2/Husky-dog-jealous-of-stuffed-animal.gif")
		await ctx.send(embed=embed)
	
	@commands.command(name='sleep', brief="s")
	async def sleep(self, ctx):
		embed=Embed(title="ZZZzzZZzz!!", color=Color.blue())
		embed.set_image(url="https://media.tenor.com/images/eca1cd1abf2ed496866e7392292cd755/tenor.gif")
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Commands(bot))

