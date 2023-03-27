import discord
import pandas as pd
import json
from discord.ext import commands


with open('config.json', 'r') as cfg:
    data = json.load(cfg)
    token = data["token"]


def create_user(username):
    df.loc[len(df)] = [len(df)-1, username, "", [], []]
    # print("df")
    # print(df)

print(token)
CHANNEL_ID = '1079912337571598438'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
df = pd.DataFrame()
df['index'] = []
df['username'] = []
df['uni'] = []
df['prof'] = [[]]
df['classes'] = [[]]

# print(df)

@bot.event
async def on_ready():
    print("Bot is now running")
    channel = bot.get_channel(CHANNEL_ID)
    # await channel.send("Bot is now running!")

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def addclass(ctx):
    username = str(ctx.author)
    print(username)
    class_name = ctx.message.content.split(' ')[1]
    # print(class_name)
    print("df username: ")
    print(df['username'])
    if df['username'].eq(username).any():
        print("in df")
    else:
    # if username not in df['username']:
        create_user(username)
    # index = df.loc[df['username']==username, 'index']
    # temp = df.iloc[index]['classes'][0]
    # temp.append(class_name)
    # df.iloc[index]['classes'][0] = temp
        
    await ctx.send('Added class!')

@bot.command()
async def addprof(ctx):
    await ctx.send('Added prof!')

@bot.command()
async def addrestaurant(ctx):
    await ctx.send('Added rest!')

@bot.command()
async def getusernames(ctx):
    await ctx.send(df['username'])

@bot.command()
async def getclasses(ctx):
    await ctx.send(df['class_name'][0])

@bot.command()
async def getunis(ctx):
    await ctx.send(df['uni'])

bot.run(token)

