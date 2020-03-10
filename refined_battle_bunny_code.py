
#Imports
import praw
import discord
import os 
from discord.ext import commands
import random
import asyncio
import re
import time
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from random import seed
from random import randint
from dotenv import load_dotenv

#tbh idk what this does but without it the random commands don't work
seed(1)


#sets working dirrectory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
print("Successfully Loaded Bot Token")
GUILD = os.getenv('DISCORD_GUILD')
print("Successfully connected to Guild")
prawID = os.getenv('PRAWID')
print('Successfully connected Reddit ID')
prawTKN = os.getenv('PRAWTOKEN')
print("Approved Reddit API Token")

client = discord.Client()


#Sets Prefix For Bot Commands For commands extension
bot = commands.Bot(command_prefix='m!')

#Redit Instance 
reddit = praw.Reddit(client_id=prawID, client_secret=prawTKN , user_agent='<Universal>:<Br12Ir5JUAlZSQ>:<v1> (by /u/WinterAmoeba514)')

#Subreddit Image Embedder Function
def subreddit_image_embedder(subreddit, filter='hot'):
    subred = reddit.subreddit(subreddit)
    newmeme = subred.hot(limit=50)
    lstmeem = list(newmeme)
    randsub = random.choice(lstmeem)
    embed = discord.Embed(title=randsub.title,
                          url=randsub.url, colour=0x3498d)
    embed.set_image(url=randsub.url)
    return embed

#Startup Process
@bot.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    print("Successful startup, connecting to Discord...")
    print(f'{bot.user} has connected to Discord!')

    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    #The displayed game of the bot
    CurrentStatus = "Bunny Girl Simulator"
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(type=discord.ActivityType.playing, name=CurrentStatus))



class SFW(commands.Cog):
    @commands.command(name="reddit")
    async def subreddit_spooky(self, ctx, sub):    
        '''A hotpost from a specified subreddit. Usage: m!reddit <subreddit>'''
        reddit_subreddit = reddit.subreddit(sub)
        if not reddit_subreddit.over18:
            await ctx.send(embed=subreddit_image_embedder(sub))
        elif reddit_subreddit.over18 and (str(ctx.channel.type) == "private") or (not ctx.channel.is_nsfw()):
            await ctx.send("Sorry, that subreddit is NSFW, try running the command again in a NSFW channel")
        elif reddit_subreddit.over18 and ctx.channel.is_nsfw():
            await ctx.send(embed=subreddit_image_embedder(sub))

    @commands.command()
    async def info(self, ctx):
        '''Shows the GitHub repo''' 
        await ctx.send("Here's a link to my GitHub Repo")
        bot_info_embed = discord.Embed(title="Battle Bunny Info Card",
                                    url="https://github.com/ko-torii/Momo_Battle_Bunny",
                                    description="Made by Kotori’s Fried Chicken#8426 because they'd rather do Python than VB.",
                                    color=0xfabcbd)
        bot_info_embed.set_thumbnail(url="https://i.redd.it/27bp6h2z55011.jpg")
        bot_info_embed.set_footer(text="(The code is like, really really bad)")
        await ctx.send(embed= bot_info_embed)
        await ctx.send("For a list of commands, do m!help")


    @commands.command()
    async def kizuna(self, ctx):
        '''Random Kizuna Ai content'''
        ksub = "KizunaA_Irl"
        await ctx.send(embed=subreddit_image_embedder(ksub))

class NSFW(commands.Cog):
    @commands.command()
    async def sauce(self, ctx, *ids):
        '''Generates a nHentai.net link. Usage: m!doujin <nHentai ID>'''
        nIDs = ids
        nlinks = []
        nurl = "https://www.nhentai.net/g/{0}"
        if (str(ctx.channel.type) == "private") or (ctx.channel.is_nsfw()):
            for nID in nIDs:
                nlinks.append(nurl.format(nID))
                await ctx.send("\n".join(nlinks))
        else:
            await ctx.send("Buddy, you can only use this command in NSFW channels")
    @commands.command()
    async def randomsauce(self,ctx):
        '''Generates a random nHentai.net link. Usage: m!randdoujin'''
        randNID = randint(0, 300000)
        nurl = "https://www.nhentai.net/g/"
        if (str(ctx.channel.type) == "private") or (ctx.channel.is_nsfw()):
            await ctx.send(nurl + str(randNID))
        else:
            await ctx.send("Buddy, you can only use this command in NSFW channels")


    @commands.command()
    async def order(self, ctx, *orders):
        '''Generates a Hentai Cafe Link. Usage: m!cafe <Hentai Cafe ID>'''
        cafeIDs = orders
        cafeLink = []
        cafeURL = "https://hentai.cafe/hc.fyi/{0}"
        if (str(ctx.channel.type) == "private") or (ctx.channel.is_nsfw()):
            for cafeID in cafeIDs :
                cafeLink.append(cafeURL.format(cafeID))
                await ctx.send("\n".join(cafeLink))
        else:
            await ctx.send("Buddy, you can only use this command in NSFW channels")

    @commands.command()
    async def randomorder(self,ctx):
        '''Generates a random Hentai Cafe link. Usage: m!randomorders'''
        randCafeID = randint(0, 14800)
        cafeURL = "https://hentai.cafe/hc.fyi/"
        if (str(ctx.channel.type) == "private") or (ctx.channel.is_nsfw()):
            await ctx.send(cafeURL + str(randCafeID))
        else:
            await ctx.send("Buddy, you can only use this command in NSFW channels")



class Administration(commands.Cog):
    @commands.command(name="purge", pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):

        '''Clears Messages. Usage: m!purge <amount>'''
        if amount == 0:
            await ctx.send('Please specify amount.')
        else:
            await ctx.channel.purge(limit=amount+1)
            await ctx.send('I cleared ' + str(amount) + ' messages, ' + ctx.message.author.mention)
            time.sleep(3)
            await ctx.channel.purge(limit=1)

    @purge.error    
    async def purge_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            text = "Sorry," + ctx.message.author.mention + "you do not have permissions to do that!"
            await ctx.send(text)


    @commands.command()
    async def test(self, ctx):
        '''States The Channel Type'''
        await ctx.send("もしもし!  バトルバニーです :carrot:")



bot.add_cog(SFW(bot))
bot.add_cog(NSFW(bot))
bot.add_cog(Administration(bot))


bot.run(token)
