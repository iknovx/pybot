import discord
from discord.ext import commands
from config import TOKEN, PREFIX, INTENTS

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=INTENTS,
    help_command=None
)

# --------- LOAD COGS ---------
async def load_extensions():
    await bot.load_extension("cogs.basic")
    await bot.load_extension("events.ready")

@bot.event
async def setup_hook():
    await load_extensions()

# --------- RUN ---------
bot.run(TOKEN)