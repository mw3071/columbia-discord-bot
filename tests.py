import asyncio
import discord.ext.test as dpytest
import json
from discord.ext import commands
import discord


with open('config.json', 'r') as cfg:
    data = json.load(cfg)
    token = data["token"]

intents = discord.Intents.all()

async def test_ping():
    bot = commands.Bot(command_prefix='!', intents=intents)
    dpytest.configure(bot)
    await dpytest.message("!ping")
    assert dpytest.verify().message().contains().content("Ping:")


async def test_foo():
    bot = commands.Bot(command_prefix='!', intents=intents)
    dpytest.configure(bot)
    await dpytest.message("!hello")
    assert dpytest.verify().message().content("Hello World!")


asyncio.run(test_ping())
asyncio.run(test_foo())

def test_bot_runs():
    return

def test_send_message():
    return

def test_add_user():
    return

def test_add_class():
    return

def test_add_prof():
    return