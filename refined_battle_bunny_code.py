
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

@bot.command()
async def doujin(ctx, *ids):
    '''Generates a nHentai.net link. Usage: m!doujin <Doujin ID>'''
    nIDs = ids
    nlinks = []
    nurl = "https://www.nhentai.net/g/{0}"
    for nID in nIDs:
        nlinks.append(nurl.format(nID))
        await ctx.send("\n".join(nlinks))
 

@bot.command()
async def test(ctx):
    '''Test Command'''
    await ctx.send(ctx.channel.type)

@bot.command(name="reddit")
async def subreddit_spooky(ctx,sub):    
    '''Posts a Hot post from a subreddit. Usage: $reddit <subreddit>'''
    reddit_subreddit = reddit.subreddit(sub)
    if not reddit_subreddit.over18:
        await ctx.send(embed=subreddit_image_embedder(sub))
    elif reddit_subreddit.over18 and (str(ctx.channel.type) == "private") or (not ctx.channel.is_nsfw()):
        await ctx.send("Sorry, you can only access that command in NSFW channels in servers.")
    elif reddit_subreddit.over18 and ctx.channel.is_nsfw():
        await ctx.send(embed=subreddit_image_embedder(sub))
    
@bot.command()
async def aname(ctx,args):
    '''A Name'''
    await ctx.send(args)
    print(args)


#Bot's Token
with open("server_key.txt", "r") as f:
    bot.run(f.read())
