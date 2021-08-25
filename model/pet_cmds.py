from discord.ext import commands
from discord import Embed, Color
from .pet import Pet

class PetCommands(commands.Cog):
    def __init__(self, bot):
        self.pet = Pet("Husky",  100)
        self.bot = bot
        print("REEEEEEEEEE")

    @commands.Cog.listener()
    async def on_ready(self):
        print("pet cmds ready")
        self.pet.start()

    @commands.command(name = "petstat", brief = "pet")
    async def petstat(self, ctx):
        print("bruh")
        embed = Embed(title = "Pet - Statistics", color = Color.red())
        embed.add_field("Name: ", pet.name, inline = True)
        embed.add_field("Health: ", pet.health, inline = False)
        embed.add_field("Hunger: ", pet.hunger, inline = False)
        await ctx.send(embed = embed)
