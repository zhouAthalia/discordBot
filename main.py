import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',intents = intents)

@client.event
async def on_ready():
    print("Beep Beep Boop activating")

@client.event
async def on_member_join(channel):
    await channel.send('Hi Welcome! \n Please fill out this form if you would like to let into the sheCodes server: https://docs.google.com/forms/d/e/1FAIpQLSfeKguqxwmrIC0h-mDYX0Ay7NyMWMlfiivoNwINCWU_k8q6vA/viewform')

@client.command()
async def test(ctx):
    await ctx.send('test working')

@client.command()
async def apply(ctx): #Starts embed
    await ctx.send('Please fill out this form if you would like to let into the sheCodes server: https://docs.google.com/forms/d/e/1FAIpQLSfeKguqxwmrIC0h-mDYX0Ay7NyMWMlfiivoNwINCWU_k8q6vA/viewform')

@client.command()
async def features(ctx): 
    await ctx.send('here is a list of all commands for the bot \n  t! start for tetris \n ! wanted @ user for a wanted poser \n ! game to start tic tac toe \n ! earn to earn otters and ! bal to check your balance of otters')


client.run('Token here')
