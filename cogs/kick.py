import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep
from datetime import datetime

class Mod(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def kick(self,ctx,member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f':white_check_mark: The member {user.mention} is kicked.')

def setup(client):
    client.add_cog(Mod(client))
