from discord.ext import commands
from discord import Embed, Color, Message
import os
import json

class Shop(commands.Cog):
    channel = 0
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global channel
        if(not(user == self.bot.user)):      
            id = user.id
            user = str(user)
            user_name=user[0:user.index('#')]
            data = self.get_userinfo(user_name)
            if(not(data==None)):
                if(str(reaction) == '\U0001F357'):
                    data['treats']-=5
                    if(self.save_userinfo(user_name, data)):
                        await channel.send(f'<@!{id}>',embed=Embed(title='`Payment done!!`', color=Color.random()))
        
    def get_userinfo(self, user):
        users = os.listdir(f'{os.getcwd()}\\account\\')
        if(f'{user}.json' in users):
            data=json.load(open(f'{os.getcwd()}\\account\\{user}.json'))
            return data
        else:
            return None

    def save_userinfo(self, user, data):
        with open(f"{os.getcwd()}\\account\\{user}.json", 'w') as d:
            json.dump(data, d)
        return True

    @commands.command(name='shop', aliases=['s', 'sh'])
    async def shop(self, ctx):
        global channel
        embed = Embed(title='\U0001F3EA shop', color = Color.random())
        embed.add_field(name='\U0001F357 Dog Food', value = "`5 Treats \U0001F9B4 (replenishes 5 hunger points)`", inline = False)
        embed.add_field(name='\U00002B06 Boosts', value = "`1000 Treats \U0001F9B4 (boosts growth by 5% for 2 hours)`", inline = False)
        reaction = await ctx.send(embed=embed)
        channel=ctx.channel
        await Message.add_reaction(reaction, '\U0001F357')
        await Message.add_reaction(reaction, '\U00002B06')

    @commands.command(name='accessories', aliases=['acc', 'a'])
    async def accessories(self, ctx):
        embed = Embed(title='Accessories', color = Color.random())
        embed.add_field(name='\U0001F455 T-Shirt', value = "`300 Treats \U0001F9B4 (dog gets a T shirt xD)`")
        reaction = await ctx.send(embed=embed)
        await Message.add_reaction(reaction, '\U0001F455') 

    @commands.command(name='leaderboard', aliases=['leader', 'board', 'lb'])
    async def leaderboard(self, ctx):
        embed=Embed(title='Leaderboard', color=Color.random())
        users = os.listdir(f'{os.getcwd()}\\account\\')
        treats = []
        users_list = []
        for user in users:
            data=json.load(open(f'{os.getcwd()}\\account\\{user}'))
            treats.append(data["treats"])
            users_list.append(data["name"])
        un_treats=treats    
        self.mergeSort(treats)
        index =self.find_index(un_treats, treats)
        for i in index:
            embed.add_field(name=f'`{users_list[i]}`', value=f"`{un_treats[i]} treats`", inline=False)
        await ctx.send(embed=embed)    

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid=len(arr)//2

            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i=j=k=0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1

            while i < len(L):
                arr[k]=L[i]
                i+=1
                k+=1

            while j < len(R):
                arr[k]=R[j]
                j+=1
                k+=1

    def find_index(self, arr, sorted_arr):
        index_list=[]
        i=0
        j=0
        while i<=len(sorted_arr)-1:
            if(sorted_arr[j]==arr[i]):
                index_list.append(i)
                j+=1
                if(j==len(sorted_arr)):
                    break
                i=0
            else:
                i+=1
        
        return index_list

def setup(bot):
    bot.add_cog(Shop(bot))