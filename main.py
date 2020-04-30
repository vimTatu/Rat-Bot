import asyncio
import random
import time

import discord
from discord.ext import commands, tasks

# from rat_of_the_day import RAT
from settings import discord_token

rat_threads = {}


class MyautAI(commands.Bot):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        await bot.process_commands(message)


bot = MyautAI(command_prefix='!')

@bot.command()
async def rat(ctx):
    channel = ctx.message.channel
    if not channel in rat_threads.keys():
        rat_threads[channel] = True
        while rat_threads[channel] == True:
            users = channel.members
            rat = random.choice(list(users))
            embed = discord.Embed(title="Congrats!", description="Congratulations, {}, on being rat of the day!\nIf your discord server doesn\'t have a rat, it means that rat is you!".format(rat.mention), color=0xd3d3d3)
            await ctx.send(embed=embed)
            await asyncio.sleep(84600)
    else:
        embed=discord.Embed(title="Error!", description="Exception occured! You already has rat in the channel. To stop bot type\n!stop_rat",color=0xff0000)
        await ctx.send(embed=embed)

@bot.command()
async def stop_rat(ctx):
    channel = ctx.message.channel
    if channel in rat_threads.keys():
        rat_threads[channel] = False
        embed = discord.Embed(title="Success!", description="You have successfuly stopped RAT detection bot!", color=-0x90ee90)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error!", description="Bot is not currently running in this text channel!", cloor=0xff0000)
        await ctx.send()

 
bot.run(discord_token)
