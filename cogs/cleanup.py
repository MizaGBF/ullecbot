import discord
from discord.ext import commands
import datetime

cleanlist = ['nigga']
sendchannel = [1031518257678647306]
class cleanupCog(commands.Cog, name="cleanup"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def cleanup(self, ctx):
        channel = ctx.channel
        yeet = 0
        read = 0
        afterdate = datetime.datetime(year=2017,month=1,day=2)
        async for message in channel.history(limit=None):
            print(read)
            for i in cleanlist:
                read = read + 1
                if i in message.content.lower():
                    yeet = yeet + 1
                    print(yeet)
                    channel = self.bot.get_channel(1031518257678647306)
                    await channel.send(message.author.name)
                    await message.delete()
        await ctx.send("clean completed")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def checkmsg(self, ctx):
        channel = ctx.channel
        afterdate = datetime.datetime(year=2016,month=12,day=27)
        async for message in channel.history(limit=1, after=afterdate):
            print(afterdate)
            print(message.content)
            print(message.created_at)



def setup(bot):
    bot.add_cog(cleanupCog(bot))
    print('cleanup cog loaded')