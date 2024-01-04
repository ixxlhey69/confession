import discord
from ast import Delete
from discord.ext import commands
from discord import DMChannel
import random
from discord.ext import tasks
import asyncio
import os
import random
import string


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

code = {}
conf_channel = 1093103560742412308        #990358106389217293, 1001140755269681273
rmv_channel = 990360126147919932

bot.remove_command('help')

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

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name="Use !confess in my dms."))

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(f'Hey there! Thank you for inviting me into **{guild}** server :D !')
        break

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.default)
async def confess( ctx, *, confession: str):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        colors = (0x071932, 0x082540, 0x023C4D, 0x0D4848, 0x032D39)
        code = gen_key()
        embed = discord.Embed(color = random.choice(colors))
        embed.title = f"Confession ID {code}"
        embed.description = confession
        #for i in range(len(conf_channel)):
        #  channel = bot.get_channel(conf_channel[i])
        #  confession_msg = await channel.send(embed=embed)
        #code[code] = 
        channel = bot.get_channel(conf_channel)
        await channel.send(embed=embed)
        
        await ctx.send(f'Your confession ID is {code}')
        await ctx.send("If you want to remove the confession from the channel do .request (ID number) and I'll notify the admins to take it off.")

    else:
        await ctx.send("This command only works in my dms!")

@bot.command(aliases=["rq"])
async def request(ctx, *, code : str=None):
    #rmv_channel = 990360126147919932
    #conf_channel = 990358106389217293
    
    rmv_channel2 = bot.get_channel(990360126147919932)

    if code == None:
        await ctx.send("Please enter confession code", delete_after=10)

    else:

        await rmv_channel2.send(f"Please remove confession {code}")

#@bot.command(aliases=["removeconfession"])
#async def rc( ctx, code : str=None ):
#    conf_channel = 990358106389217293
#    
#    if code == None:
#        await ctx.send("Please enter confession code", delete_after=10)
#
#    confession = await conf_channel.fetch_message(code[code])
#
#    if not confession:
#        await ctx.send("Please enter the correct ID", delete_after=5)
#    
#    await ctx.message.delete()
#    await confession.delete()

bot.run('MTAwMTA4MTc0NjkxMTE0MTk2OA.GIAept.6-Ziv5Oe7yUjFngB3dWDRV2rqWKuQPPPcCFvH0')
