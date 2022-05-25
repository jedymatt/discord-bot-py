import imp
from discord.ext import commands
from session import session


class User(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.group()
    async def user(self, ctx):
        pass

    @user.group()
    async def register(self, ctx):
        session.post('/api/characters', json={'params': ctx.message.content})
        await ctx.send('Registered')


def setup(bot):
    bot.add_cog(User(bot))
