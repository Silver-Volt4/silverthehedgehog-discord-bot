import importlib
import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
import random

import data.spook

def setup(bot: discord.Bot):
    importlib.reload(data.spook)
    instance = Silvy(bot)
    bot.add_cog(instance)
    bot.user_command(name="Hug this user")(instance._hug)
    bot.user_command(name="Wish this user a happy birthday")(instance._bday)


class Silvy(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    g = SlashCommandGroup("silv", "Silver related fluff")

    @g.command(description="Gift somebody a warm hug!")
    async def hug(self, ctx, user: discord.User):
        await self._hug(ctx, user)

    async def _hug(self, ctx, user: discord.User):
        hug_from = ctx.author.mention
        if user == ctx.author:
            hug_from = self.bot.user.mention
        embed = discord.Embed(
            title="Aww, I love hugs! 😊",
            description=(
                "{} *hugs* {}".format(hug_from, user.mention)),
            url="https://solar-socks.tumblr.com/post/620691516062597120/wanting-to-spread-some-love-and-positive-vibes"
        )
        embed.set_image(
            url="https://64.media.tumblr.com/675559b932140f379cf55368701bcf1d/d162caca11d6dba1-ad/s1280x1920/1d12928ccff2b2f94424a496cbe21c8811aaa874.png"
        )
        embed.set_footer(text="SilvBot")
        await ctx.respond(embed=embed)

    @g.command(description="Wish somebody a happy birthday!")
    async def bday(self, ctx, user: discord.User):
        await self._bday(ctx, user)

    async def _bday(self, ctx, user: discord.User):
        embed = discord.Embed(
            title=f"Happy birthday, {str(user)}!"
        )
        embed.set_image(
            url="https://i.imgur.com/Kb9sajK.png"
        )
        embed.set_footer(text="SilvBot")
        await ctx.respond(embed=embed)

    @g.command(
        description="IT'S NO USE!"
    )
    async def snouse(self, ctx):
        embed = discord.Embed(
            title="It's no use!",
            url="https://www.youtube.com/watch?v=Oq8AgIS3ZgU"
        )
        embed.set_image(
            url="https://i.ytimg.com/vi/tLfVHgiPjJA/maxresdefault.jpg")
        embed.set_footer(text="SilvBot")
        await ctx.respond(embed=embed)

    @g.command(description="Send some spooky art for Spooktober")
    async def spook(self, ctx):
        embed = discord.Embed(
            title="Boo! Happy Halloween!",
        )
        url = random.choice(data.spook.spook)
        print("spook:", url)
        embed.set_image(url=url)
        embed.set_footer(text="SilvBot")
        await ctx.respond(embed=embed)
