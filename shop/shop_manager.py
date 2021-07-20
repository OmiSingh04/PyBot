from discord.ext import commands
from discord import Embed, Color, Message
import os

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if(not(user == self.bot.user)):      
            id = user.id
            user = str(user)
            user_name=user[0:user.index('#')]
            users = os.listdir(f'{os.getcwd()}\\account\\')
            print(f'{user_name}.json')
            if(f'{user_name}.json' in users):
                print("yes")
                # users[users.index(f'{user_name}.json')]['treats']-=1
                print(users[users.index(f'{user_name}.json')])
        


    @commands.command(name='shop')
    async def shop(self, ctx):
        embed = Embed(title='\U0001F3EA shop', color = Color.random())
        embed.add_field(name='\U0001F357 Dog Food', value = "5 Treats \U0001F9B4 (replenishes 5 hunger points)", inline = False)
        embed.add_field(name='\U00002B06 Boosts', value = "1000 Treats \U0001F9B4 (boosts growth by 5% for 2 hours", inline = False)
        reaction = await ctx.send(embed=embed)
        await Message.add_reaction(reaction, '\U0001F357')
        await Message.add_reaction(reaction, '\U00002B06')

    @commands.command(name='acc')
    async def acc(self, ctx):
        embed = Embed(title='Accesories', color = Color.random())
        embed.add_field(name='\U0001F455 T-Shirt', value = "300 Treats \U0001F9B4 (dog gets a T shirt xD)")
        reaction = await ctx.send(embed=embed)
        await Message.add_reaction(reaction, '\U0001F455') 


def setup(bot):
    bot.add_cog(Shop(bot))