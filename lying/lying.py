import discord
from discord.ext import commands
import asyncio
from random import choice as randchoice

class Lying:
    """And then there's this asshole."""

    def __init__(self, bot):
        self.bot = bot
        self.responses = {
            "none" : ["https://i.imgur.com/l6CJa0a.jpg",
                "https://i.imgur.com/F2FzhOr.jpg",
                "https://i.imgur.com/1iZ0IcA.jpg",
                "https://i.imgur.com/G3wzFDa.jpg",
                "https://i.imgur.com/f1WMscl.jpg",
                "https://i.imgur.com/hNgA5Sx.png",
                "https://i.imgur.com/dPtngzD.jpg"
        }


    @commands.command(pass_context=True, aliases=['lying?','lying','right?'])
    async def lying(self, ctx, *, question="none"):
        """Lying!"""
        author = ctx.message.author
        msg = ""
        found = []
        for k,v in self.responses.items():
            if k in question.lower():
                found.append(v)
        if found:
            msg = randchoice(randchoice(found))
        if not msg:
            msg = randchoice(self.responses["none"])
        await asyncio.sleep(1)
        await self.bot.say(msg.format(author=author))
        if "sing it for me" in question.lower() and "Audio" in self.bot.cogs and author.voice_channel:
            audio = self.bot.get_cog("Audio")
            if audio.music_player.is_done():
                link = "https://www.youtube.com/watch?v=hchUl3QlJZE"
                # probably dont need. just too lazy to check.
                ctx.message.content = "{}play {}".format(self.bot.command_prefix[0],link)
                if await audio.check_voice(ctx.message.author, ctx.message):
                    audio.queue.append(link)

def setup(bot):
    bot.add_cog(Lying(bot))
