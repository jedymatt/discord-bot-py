import config

import discord
from discord.ext import commands
import requests
import session

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

cogs = [
    'user',
]


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='?',
            case_insensitive=True
        )

        for cog in cogs:
            self.load_extension(f'cogs.{cog}')


def main():
    bot = Bot()

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')

    @bot.command()
    async def ping(ctx: commands.Context):
        await ctx.send(f'Ping: `{round(bot.latency, 2)}ms`')

    
    # run bot
    bot.run(config.BOT_TOKEN)


if __name__ == '__main__':
    # print(os.getcwd())
    main()
