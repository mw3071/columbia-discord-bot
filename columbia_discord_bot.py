import discord
import pandas as pd
from discord.ext import commands

def create_user(username):
    df.loc[len(df)] = [len(df)-1, username, "", [], []]
    # print("df")
    # print(df)

BOT_TOKEN = 'MTA3OTkwMjk0Njc2ODE5OTcwMA.GuXQeK.qff4xE99peonTNGfMjzcXqSdTNHYTN-ru-leyM'
CHANNEL_ID = '1079912337571598438'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
df = pd.DataFrame()
df['index'] = []
df['username'] = []
df['uni'] = []
df['prof'] = [[]]
df['classes'] = [[]]

print(df)

@bot.event
async def on_ready():
    print("Bot is now running")
    channel = bot.get_channel(CHANNEL_ID)
    # await channel.send("Bot is now running!")

@bot.command()

async def addclass(ctx):
    username = str(ctx.author)
    print(username)
    class_name = ctx.message.content.split(' ')[1]
    print(class_name)
    print(df['username'])
    if username not in df['username']:
        create_user(username)
    # index = df.loc[df['username']==username, 'index']
    # temp = df.iloc[index]['classes'][0]
    # temp.append(class_name)
    # df.iloc[index]['classes'][0] = temp
        
    await ctx.send('Added class!')

async def add_prof(ctx):
    await ctx.send('addclass')

async def add_restaurant(ctx):
    await ctx.send('addrest')

bot.run(BOT_TOKEN)

