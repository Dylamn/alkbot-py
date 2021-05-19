import re
import discord
import src.commands

from discord import Message
from discord.ext import commands
from src.helpers import get_string


class AlkBot(commands.Bot):
    def __init__(self):
        """Bootstrap the Alkbot"""
        super().__init__(command_prefix="alk!")
        for command in src.commands.__all__:
            self.add_cog(command(self))

    async def on_ready(self):
        """Event executed when the bot has finished booting"""
        print(f"{self.user.display_name} is connected!")

        # Set the bot activity.
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Game(get_string('activity'))
        )

    async def on_message(self, message: Message):
        """Event executed each time a message is posted on the channels where the bot has access"""
        # Process with commands...
        await super(AlkBot, self).on_message(message)

        # Reply to someone who mentions "alk" in their message.
        if re.match('^.*alk[^!]*$', message.content.lower()):
            await message.channel.send(
                get_string('noticed').format(message.author)
            )
