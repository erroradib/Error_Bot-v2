import discord
from discord.ext import commands
from discord.utils import *

class welcome(commands.Cog, name='welcome'):

    def __init__(self, client):
        self.client = client

    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name="new role")
        channel = self.client.get_channel(856917408013877296)
        embed=discord.Embed(description=f'Hi {member.mention}, Welcome to the server!', color=0x0bf9f9)
        await member.add_roles(role)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(856917408013877296)
        embed = discord.Embed(description=f'{member.name} just left the server!')
        await channel.send(embed=embed)




def setup(client):
    client.add_cog(welcome(client))
    print("Welcome is Running")