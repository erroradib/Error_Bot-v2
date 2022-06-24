#Ami kintu event use kori nai :)

import os
import traceback
import sys
import discord
from discord.ext import tasks, commands
from config import TOKEN
from itertools import cycle
from discord.utils import get

owner_id = None #nije nijer ta dao
client = commands.Bot(commands.when_mentioned_or('.'))
client.case_insensitive=True
client.remove_command('help')

status = cycle([
    'Mention me for help'
    'Error Security',
    'error_adib',
    'Python 3.10.0',
    '.cp',
    'ERROR_GAMING',
    'For your security'
])

@tasks.loop(seconds=3)
async def status_swap():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(next(status)))

@client.event
async def on_ready():
    print(f'{client.user} is ready!')
    status_swap.start()


#CONTROL PANEL
@client.command()
async def cp(ctx):
  embed=discord.Embed(title="Control Panel", color=0x00ff2a)
  embed.add_field(name=".Admin", value="Admin Info", inline=True)
  embed.add_field(name=".Mod", value="Moderator Info", inline=True)
  embed.add_field(name=".Release", value="If you impounded, then type this command", inline=True)
  embed.add_field(name=".Const", value="Construction Side!", inline=True)
  await ctx.send(embed=embed)

@client.command()
async def rel(ctx):
  embed=discord.Embed(color=0x1eff00)
  embed.add_field(name='ㅤ', value="**Pending...**", inline=False)
  await ctx.send(embed=embed)


extensions=[
            'cogs.ping',
            'cogs.welcome'
]

if __name__ == "__main__":
  for extension in extensions:
    try:
      client.load_extension(extension)

    except Exception as e:
      print(f"Error Occur! {extension}", file=sys.stderr)
      traceback.print_exc()



client.run(TOKEN)

