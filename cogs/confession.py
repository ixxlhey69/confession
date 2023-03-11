from ast import Delete
import discord
from discord import DMChannel
from discord.ext import commands
import random
import string

def gen_key():
    alpha, num = list(string.ascii_lowercase), list(string.digits)
    mapper = []
    for i in range(10):
        x = ('y', 'n')
        if random.choice(x) == 'y':
            if random.choice(x) == 'y':
                mapper.append(random.choice(alpha).upper())
            else:
                mapper.append(random.choice(alpha))
        else:
            mapper.append(str(random.choice(num)))

    return ''.join(map(str, mapper))

class confession(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.code = {}
        self.conf_channel = 990358106389217293
        self.rmv_channel = 990360126147919932

    @commands.command()
    async def confess(self, ctx, *, confession: str):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            channel = self.bot.get_channel(self.conf_channel)
            code = gen_key()
            embed = discord.Embed()
            embed.title = f"Confession ID {code}"
            embed.description = confession
            await ctx.send(f'Your confession ID is {code}')
            await ctx.send("If you want to remove the confession from the channel do .request (ID number) and I'll notify the admins to take it off.", delete_after=10)
            confession_msg = await channel.send(embed=embed)
            self.code[code] = confession_msg.id
        else:
            await ctx.send("This command only works in my dms!")

    @commands.command(aliases=["rq"])
    async def request(self,ctx, code=None):
        rmv_channel = self.bot.get_channel(self.rmv_channel)
        conf_channel = self.bot.get_channel(self.conf_channel)

        """"TO Avoid Fake codes being sent!"""
        if code == None:
            await ctx.send("Please enter confession code", delete_after=10)

        confession = await conf_channel.fetch_message(self.code[code])

        if not confession:
            await ctx.send("Please enter the correct ID", delete_after=10)

        await rmv_channel.send(f"Please remove confession {code}")

    @commands.command(aliases=["removeconfession"])
    @commands.has_permissions(manage_messages=True)
    async def rc(self, ctx, code : str=None ):
        conf_channel = self.bot.get_channel(self.conf_channel)
        
        if code == None:
            await ctx.send("Please enter confession code", delete_after=10)

        confession = await conf_channel.fetch_message(self.code[code])

        if not confession:
            await ctx.send("Please enter the correct ID", delete_after=5)
        
        await ctx.message.delete()
        await confession.delete()

def setup(bot):
    bot.add_cog(confession(bot))
