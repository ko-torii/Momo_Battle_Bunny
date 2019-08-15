
#Imports
import praw
import discord
import os 
from discord.ext import commands
import random
import asyncio
import re


#sets working dirrectory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Sets Prefix For Bot Commands For commands extension
bot = commands.Bot(command_prefix='m!')

#Redit Instance 
with open("reddit_id.txt", "r") as f:
    with open("reddit_secret.txt", "r") as g:
        reddit = praw.Reddit(client_id=f.read(), client_secret=g.read(
        ), user_agent='<Universal>:<Br12Ir5JUAlZSQ>:<v1> (by /u/WinterAmoeba514)')

#Subreddit Image Embedder Function
def subreddit_image_embedder(subreddit, filter='hot'):
    subred = reddit.subreddit(subreddit)
    neewmeem = subred.hot(limit=50)
    lstmeem = list(neewmeem)
    randsub = random.choice(lstmeem)
    embed = discord.Embed(title=randsub.title,
                          url=randsub.url, colour=0x3498d)
    embed.set_image(url=randsub.url)
    return embed

#Startup Process
@bot.event
async def on_ready():
    #prints on terminal a message after a successful startup of program
    print("Watashi ga kita!")

    #The displayed game of the bot
    CurrentStatus = "TED Talk: Catgirls, the Next Stage Of Human Evolution"
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=CurrentStatus))


class SFW(commands.Cog):
    @commands.command(name="reddit")
    async def subreddit_spooky(self, ctx,sub):    
        '''A hotpost from a specified subreddit. Usage: m!reddit <subreddit>'''
        reddit_subreddit = reddit.subreddit(sub)
        if not reddit_subreddit.over18:
            await ctx.send(embed=subreddit_image_embedder(sub))
        elif reddit_subreddit.over18 and (str(ctx.channel.type) == "private") or (not ctx.channel.is_nsfw()):
            await ctx.send("Sorry, you can only access that command in NSFW channels in servers.")
        elif reddit_subreddit.over18 and ctx.channel.is_nsfw():
            await ctx.send(embed=subreddit_image_embedder(sub))

    @commands.command()
    async def info(self, ctx):
        '''Shows the GitHub repo'''
        await ctx.send("Here's a link to my GitHub Repo")
        bot_info_embed = discord.Embed(title="Battle Bunny Info Card", url="https://github.com/Burri-Taco/Momo_Battle_Bunny",
                                    description="Made by @ShiftyWizard#4823 & @_BurriTaco_#0889 because they'd rather do Python than VB.", color=0xfabcbd)
        bot_info_embed.set_thumbnail(url="https://i.redd.it/27bp6h2z55011.jpg")
        bot_info_embed.set_footer(text="(The code is like, really really bad)")
        await ctx.send(embed= bot_info_embed)
        await ctx.send("For a list of commands, do m!help")
        
    @commands.command()
    async def aname(self,ctx,args):
        '''A Name'''
        await ctx.send(args)
        print(args)


    @commands.command()
    async def test(self, ctx):
        '''States The Channel Type'''
        await ctx.send(ctx.channel.type)


class NSFW(commands.Cog):
    @commands.command()
    async def doujin(self, ctx, *ids):
        '''Generates a nHentai.net link. Usage: m!doujin <Doujin ID>'''
        nIDs = ids
        nlinks = []
        nurl = "https://www.nhentai.net/g/{0}"
        if (str(ctx.channel.type) == "private") or (ctx.channel.is_nsfw()):
            for nID in nIDs:
                nlinks.append(nurl.format(nID))
                await ctx.send("\n".join(nlinks))
        else:
            await ctx.send("Buddy, you can only use this command in NSFW channels")


bot.add_cog(SFW(bot))
bot.add_cog(NSFW(bot))

#Bot's Token
with open("server_key.txt", "r") as f:
    bot.run(f.read())
