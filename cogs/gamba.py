import discord
from discord.ext import commands
import json


class gambaCog(commands.Cog, name="gamba"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def race(self, ctx):
        
                



    
def setup(bot):
    bot.add_cog(gambaCog(bot))
    print('uwu gamba loaded')