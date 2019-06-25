import discord
from discord.ext import commands
import random


class diceCog(commands.Cog, name="dice"):
    def __init__(self, bot):
        self.bot = bot

    def dice(self, sides):
        roll = random.randint(1,sides)
        return str(roll)

# the idea is you can choose the number of dice and what dice to roll
    @commands.command()
    async def roll(self, ctx, *arg):
        r = 0
        resultnum = 0
        output = []
        author = ctx.author.name
        titlestring = author + " just rolled the dice 🎲"
        embed = discord.Embed(color=9062d3)
        embed.set_author(name="ullec bot")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        try:
            if len(arg) > 2:
                raise Exception
            if len(arg) == 1:
                b = arg[0]
                b = b.strip("d")
                b = int(b)
                result = self.dice(b)
                rolls = 1
            if len(arg) == 2:
                for id, i in enumerate(arg):
                    g = arg[id]
                    if "d" in g:
                        b = g
                        b = b.strip("d")
                        b = int(b)
                        if id == 0:
                            rolls = int(arg[1])
                        if id == 1:
                            rolls = int(arg[0])
                        if rolls > 14:
                            raise Exception
                    pass
            while rolls > r:
                r += 1
                result = self.dice(b)
                resultnum = resultnum + int(result)
                resultstring = "You rolled "+ result+"/"+str(b)
                output.append(resultstring)
            if b > 100:
                raise Exception

            foutput = '\n'.join(output)
            embed.add_field(name=titlestring, value=foutput)
            totalstr = "Total of " + str(resultnum)
            embed.add_field(name=totalstr, value="\u200b")
            await ctx.send(embed=embed)
        except Exception:
            await ctx.message.add_reaction(emoji=':worst:579662420537114626')

    

def setup(bot):
    bot.add_cog(diceCog(bot))
    print('dice cog loaded')