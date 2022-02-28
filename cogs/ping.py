import discord
from discord.ext import commands

class ping(commands.Cog, name='ping'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        emoji = discord.utils.get(self.client.emojis, name='clyde_witch')
        embed = discord.Embed(
            title=f"{emoji} Pong!",
            description=f"```The bot latency is {round(self.client.latency * 1000)}ms!```",
            color=0x42F56C
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ping(client))
    print("Ping is Running")