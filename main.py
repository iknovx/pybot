import discord
from discord.ext import commands
import os

token = os.getenv("Token")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.slash_command()
async def hello(ctx):
    await ctx.send("Hello!")