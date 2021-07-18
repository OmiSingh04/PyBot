from discord.ext import commands
from discord import Embed, Color

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='shop')
    async def shop(self, ctx):
        embed = Embed(title='shop', color = Color.random())
        embed.add_field(name='Dog Food', value = "5 Treats (replenishes 5 hunger points)")
        await ctx.send(embed=embed)

    @commands.command(name='acc')
    async def acc(self, ctx):
        embed = Embed(title='Accesories', color = Color.random())
        embed.add_field(name='T-Shirt', value = "300 treats (dog gets a T shirt xD)")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Shop(bot))