

#Special thanks to the lads of the Tortoise Discord Bot Community for helping me create this wonderful piece of work. Check out their discord server: https://discord.gg/BSBMQ2n
#They are an awesome lot.
#Also special thanks to ShiftyWizard#4823 for teaching me Regex to allow nHentai Linker Function to work.
#imports


#Imports go here
import json
import re
import asyncio
import discord
import os
import random
import praw 

#sets working dirrectory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


#prefix for core commands
prefix = "m!"
prefix_2 = "momo"

#Set To False To allow bot to work outside of nsfw channels
n_universal = False

#Set to False to prevent bot from responding to basic messages
res_func = True

#Set to False if you don't want the other NSFW commands to work in DMs (Not Recommended)
nsfw_dm = True

#redgex scanner for the holy 6 digits
regular = r"(?:\D+?|^)(\d{6})(?=\D+?|$)"
compiled = re.compile(regular)


#the discord client
client = discord.Client()

#PRAW Stuff
with open("reddit_id.txt", "r") as f:
    with open("reddit_secret.txt", "r") as g:
        reddit = praw.Reddit(client_id=f.read(), client_secret=g.read(), user_agent='<Universal>:<Br12Ir5JUAlZSQ>:<v1> (by /u/WinterAmoeba514)')

def subreddit_image_embedder(subreddit, filter='hot'):
    subred = reddit.subreddit(subreddit)
    
    if filter == "hot":
        neewmeem = subred.hot(limit=50)
    elif filter == "top":
        neewmeem = subred.top('all', limit=50)
    elif filter == "new":

        neewmeem = subred.new(limit=50)
    lstmeem = list(neewmeem)
    randsub = random.choice(lstmeem)
    embed = discord.Embed(title=randsub.title,
                       description=f'',
                       url=randsub.url, colour=0x3498d)
    embed.set_image(url=randsub.url)
    return embed

def momo_self(m):
    return m.author == client.user

def bot_info():
    bot_info_embed = discord.Embed(title="Battle Bunny Info Card", url="https://github.com/Burri-Taco/Momo_Battle_Bunny",
                          description="Made by @ShiftyWizard#4823 & @_BurriTaco_#0889 because they'd rather do Python than VB.", color=0xfabcbd)
    bot_info_embed.set_thumbnail(url="https://i.redd.it/27bp6h2z55011.jpg")
    bot_info_embed.set_footer(text="(The code is like, really really bad)")
    return bot_info_embed

#Startup Process
@client.event
async def on_ready():
    #prints on terminal a message after a successful startup of program
    print("Watashi ga kita!")

    #The displayed game of the bot
    game = discord.Streaming(name="TED Talk: Bunny Girls, the Next Stage of Human Evolution",
                             url="https://www.twitch.tv/momothebattlebunny")
    await client.change_presence(status=discord.Status.online, activity=game)

    #This is the startup message, copy the channel ID for the channel where you want the bootup message to go to.
    #In this case I use a file called channel_id.txt to store the ID of the channel i want the message to be sent to
    with open("channel_id.txt", "r") as f:
        channels = f.readlines()
        channels = [int(x.strip()) for x in channels]
        
        for guild in client.guilds: 
            for channel in guild.channels:
                if channel.id in channels:
                    await channel.send("🥕Moshi moshi🥕 \n Batorubanī wa koko ni arimasu! \n Do m!help for available commands")

#This bit prevents multiple messages being sent if the same person shares more than 1 server with the bot
#Put discord ID on the file if u want to DM people when the bot startsup
    with open("user_id_list.txt", "r") as f:
        message_user_id = f.readlines()
        message_user_id = [int(x.strip()) for x in message_user_id]
        snakecaseboyimdown = []
        for guild in client.guilds:
            for user in guild.members:
                if user.id in message_user_id:
                    if not user in snakecaseboyimdown:
                        snakecaseboyimdown.append(user)
        #The message it sends on startup
        for user in snakecaseboyimdown:
            await user.send("Yo! someone turned me on, just letting you know.")
            await asyncio.sleep(2)
            await user.send("To stop receiving these messagers, type 'STOP'")
            
@client.event   
async def on_message(message):

    #Prevents bot from triggering it's own commands
    if message.author == client.user:
        return
    #Will only work on NSFW channels
    #checks for the numbers on messages
    nums = re.findall(compiled, message.content)

    
    #commands that are only triggered if the message starts with the prefix stated before
    if message.content.startswith(prefix) or message.content.startswith(prefix_2):
        if "help" in message.content.lower() or "info" in message.content.lower():
            await message.channel.send(embed=bot_info())

        #Sh*tty Clear Chat Functions    
        elif "purge" in message.content.lower() or message.channel.is_nsfw:
            if (message.channel.type == discord.DMChannel):
                await message.channel.send("Sorry, that command is only available in server channels")
            elif "bot" in message.content.lower():
                num_self_purge_amount = message.content.split(' ')[2]
                to_be_deleted = await message.channel.purge(limit=int(num_self_purge_amount), check=momo_self)
                await message.channel.send('I Deleted {} message(s) from me'.format(len(to_be_deleted)))
            elif "msg" in message.content.lower():
                num_msg_purge_amount = message.content.split(' ')[2]
                deleted = await message.channel.purge(limit=int(num_msg_purge_amount))
                await message.channel.send('I Deleted {} message(s)'.format(len(deleted)))
            else:
                await message.channel.send("What? That's not how you do it. \n ```m!purge msg/bot <number> \n``` is the correct usage")

        #Subreddit image poster bit
        elif "kizuna" in message.content.lower() or "kzn" in message.content.lower():
            await message.channel.send(embed=subreddit_image_embedder('kizunA_Irl'))

        elif "anime_irl" in message.content.lower():
            await message.channel.send(embed=subreddit_image_embedder('anime_irl'))

        elif "wholesomeanimeme" in message.content.lower():
            await message.channel.send(embed=subreddit_image_embedder('wholesomeanimemes'))

        elif "animeme" in message.content.lower():
            await message.channel.send(embed=subreddit_image_embedder('animemes'))

        elif "wholesome" in message.content.lower():
            await message.channel.send(embed=subreddit_image_embedder('wholesome'))

        elif "reddit" in message.content.lower():
            sub = message.content.split(' ')[1]
            await message.channel.send(embed=subreddit_image_embedder(sub))
        elif "kemonomimi" in message.content.lower():
            await message.channel.send(embed=subreddit_image_embedder('kemonomimi'))
            

        #nsfw commands
        #checks if command was run in NSFW channel
        elif (message.channel.type != discord.DMChannel) or message.channel.is_nsfw:
            if "hentai_irl" in message.content.lower():
                await message.channel.send(embed=subreddit_image_embedder('hentai_irl'))
            elif "hentai_gif" or "animated hentai" in message.content.lower():
                await message.channel.send(embed=subreddit_image_embedder('hentai_GIF'))
            elif "rule34 gif" or "r34 g" in message.content.lower():
                await message.channel.send(embed=subreddit_image_embedder('rule34'))
            elif "rule34" or "r34" in message.channel.lower():
                await message.channel.send(embed=subreddit_image_embedder('rule34gifs'))
            elif "hentai" in message.channel.lower():
                await message.channel.send(embed=subreddit_image_embedder('hentai'))    
            elif "kitsunemimi" in message.channel.lower():
                await message.channel.send(embed=subreddit_image_embedder('kitsunemimi'))


         #If Command was not recognised       
        else:
            await message.channel.send("Unknown command, you can enable/disable some commands by editting the python file I use to work.")
            await message.channel.send("You can check out the available commands by checking out my GitHub Page, which can be found here:")
            await message.channel.send(embed=bot_info())

            


    #this bit makes bot respond to good bot and bad bot
    elif "bot" in message.content.lower():
        if message.content.startswith("good"):  
             await message.channel.send("Thank you :heart:")
        elif message.content.startswith("bad"):
             await message.channel.send("Hate you too, BB")
        else:
            await message.channel.send("Hai, Batorubanī desu")

    #Responses to basic messages
    elif res_func is True:
        if "oh no" in message.content.lower():
            await message.channel.send("Oh Yes U(ㅇㅅㅇ❀)U")
        elif "fuck" in message.content.lower() or "shit" in message.content.lower():
            await message.channel.send("Hey! None of that U( ÒㅅÓ)U")
        elif "cya" in message.content.lower() or "bye" in message.content.lower() or "bai" in message.content.lower() or "gtg" in message.content.lower():
            await message.channel.send("Sayonara U(⁎˃ᆺ˂)U")
        elif "dio" in message.content.lower() or "you thought it was me" in message.content.lower():
            embed = discord.Embed(title="KONO DIO DA!", color=0xf5ef07)
            embed.set_image(
                url="https://www.myinstants.com/media/instants_images/it-was-me-dio.jpg")
            await message.channel.send(embed=embed)
        
        #Suprisiingly this bit is only meant to work in DM's, when someone responds to the startup messages at the start. I'll eventually fix it up
        elif "stop" in message.content.lower():
            await message.channel.send("🥕lol no🥕")
            await asyncio.sleep(2)
            await message.channel.send("🥕Actually, let me see what I can do🥕")
            await asyncio.sleep(2)
            await message.channel.send("🥕Stopped just for you :heart:🥕")
            await asyncio.sleep(2)
            await message.channel.send("🥕Kidding, that doesn't actually work. You'd need to message my Devs. Sorry🥕")



    #nbot here
    if nums and message.channel.is_nsfw() or n_universal is True:
        nlinks = []
        nurl = "https://www.nhentai.net/g/{0}"
        for num in nums:
            nlinks.append(nurl.format(num))
            await message.channel.send("\n".join(nlinks))

#Bot Token Goes Here
#The Bot Token Was put in a text file, you may/may not need to create a new .txt file and put it there.
with open("server_key.txt", "r") as f:
    client.run(f.read())
    
