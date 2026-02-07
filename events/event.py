import discord
from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"✅ Logged in as {self.bot.user} ({self.bot.user.id})")

        activity = discord.Game(name="with discord.py")
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=activity
        )

async def setup(bot: commands.Bot):
    await bot.add_cog(Ready(bot))