import os
import discord
import random
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = 's!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
    activity=discord.Game(f"s!help on {len(client.guilds)} servers"))
    print('Zepty has connected to discord!')
    
@client.command()
async def ping(ctx):
    await ctx.send(f'**Pong!** Client Side Ping is {round(client.latency * 1000)}ms')
    
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])
