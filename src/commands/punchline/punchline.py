import random

from discord.ext import commands
from src.helpers import load_strings


class Punchline(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._punchlines: list = load_strings('commands/punchline/punchline.json')

    @commands.command()
    async def punch(self, ctx: commands.Context):
        """Send a random punchline on the channel where it was requested"""
        punchline = random.choice(self._punchlines)
        await ctx.send(punchline)
