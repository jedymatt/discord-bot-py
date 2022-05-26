from discord.ext import commands
from requests import request
import requests
from cogs.api.character import Character

from cogs.utils.api import create_character


class User(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.group()
    async def user(self, ctx):
        pass

    @user.group()
    async def register(self, ctx):
        response = create_character(ctx.author.id)
        if response.status_code != 200:
            await ctx.send(
                f'{ctx.author.mention} your character has been created.'
            )

        await ctx.send('Unexpected error occured.')

    @user.group()
    async def info(self, ctx):
        character = Character.find_by_discord_id(ctx.author.id)
        await ctx.send(str(character.__dict__))


def setup(bot):
    bot.add_cog(User(bot))
