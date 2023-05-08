import discord
import json
from student import Student
from discord.ext import commands


with open('./config.json', 'r') as cfg:
    data = json.load(cfg)
    token = data["token"]

print(token)
CHANNEL_ID = '1079912337571598438'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
users = {}
s = None


@bot.event
async def on_ready():
    '''tells user that the bot is now running'''
    print("Bot is now running")


@bot.command()
async def ping(ctx):
    '''tests if the bot responds with pong
    when the user messages ping'''
    await ctx.send('pong!')


@bot.command(help="creates a new student, must give it a uni")
async def createuser(ctx):
    '''takes the discord context and extracts the uni 
    from the message and then creates the student object'''
    username = str(ctx.author)
    uni = ctx.message.content.split(' ')[1]
    print(uni)
    print(username)
    s = Student(username, uni)
    users[username] = s
    print(s)
    print(users)
    await ctx.send('created!')


@bot.command()
async def addclass(ctx):
    '''takes the discord context and extracts class 
    from the message, and then adds a class to the student'''
    username = str(ctx.author)
    users[username].add_class(ctx.message.content.split(' ')[1])
    print(users[username])

    await ctx.send('Added class!')


@bot.command()
async def addprof(ctx):
    '''takes the discord context and extracts professor 
    from the message, and then adds a professor  to the student'''
    username = str(ctx.author)
    users[username].add_prof(ctx.message.content.split(' ')[1])
    print(users[username])
    
    await ctx.send('Added prof!')


# @bot.command()
# async def getusernames(ctx):
#     await ctx.send(df['username'])

# @bot.command()
# async def getclasses(ctx):
#     await ctx.send(df['class_name'][0])

# @bot.command()
# async def getunis(ctx):
#     await ctx.send(df['uni'])

bot.run(token)