


#imports

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

#Set To False To allow bot to work outside of nsfw channels
n_universal = False
#Set to False to prevent bot from responding to basic messages
res_func = True
#Set to False if you don't want the other NSFW commands to work in DMs (Not Recommended)
nsfw_dm = False

#redgex scanner thingy for 6 digiTS
regular = r"(?:\D+?|^)(\d{6})(?=\D+?|$)"
compiled = re.compile(regular)


#the discord client
client = discord.Client()

#PRAW Stuff
with open("reddit_id.txt", "r") as f:
    with open("reddit_secret.txt", "r") as g:
        reddit = praw.Reddit(client_id=f.read(), client_secret=g.read(), user_agent='<Universal>:<Br12Ir5JUAlZSQ>:<v1> (by /u/WinterAmoeba514)')




#Startup Process
@client.event
async def on_ready():
    #prints on terminal a message after a successful startup of program
    print("Watashi ga kita!")

    #The displayed game of the bot
    game = discord.Game("Usagi Simulator")
    await client.change_presence(status=discord.Status.online, activity=game)

    #This is the startup message, copy the channel ID for the channel where you want the bootup message to go to.
    #In this case I use a file called channel_id.txt to store the ID of the channel i want the message to be sent to
    with open("channel_id.txt", "r") as f:
        channels = f.readlines()
        channels = [int(x.strip()) for x in channels]
        
        for guild in client.guilds: 
            for channel in guild.channels:
                if channel.id in channels:
                    await channel.send("🥕Moshi moshi. Batorubanī wa koko ni arimasu!🥕 \n 🥕Do m!help for available commands🥕")

    with open("user_id_list.txt", "r") as f:
        message_user_id = f.readlines()
        message_user_id = [int(x.strip()) for x in message_user_id]
        
        snakecaseboyimdown = []


        for guild in client.guilds:
            for user in guild.members:
                if user.id in message_user_id:
                    if not user in snakecaseboyimdown:
                        snakecaseboyimdown.append(user)


        for user in snakecaseboyimdown:
            await user.send("🥕Yo! someone turned me on, just letting you know.🥕")
            await asyncio.sleep(2)
            await user.send("🥕To stop receiving these messagers, type 'STOP'🥕")
            await asyncio.sleep(2)
            await user.send("🥕I'm kidding, that actually doesn't work. You'd need to message my Devs to remove you from the list.🥕")


            

@client.event   
async def on_message(message):

    #Prevents bot from triggering it's own commands
    if message.author == client.user:
        return
    #Will only work on NSFW channels
    #checks for the numbers on messages
    nums = re.findall(compiled, message.content)

    
    #commands that are only triggered if the message starts with the prefix stated before
    if message.content.startswith(prefix):
        if "help" in message.content.lower() or "info" in message.content.lower():
            embed = discord.Embed(title="Battle Bunny Info Card", url="https://github.com/Burri-Taco/Momo_Battle_Bunny",
                                  description="Made by @ShiftyWizard#4823 & @_BurriTaco_#0889 because they'd rather do Python than VB.", color=0xfabcbd)
            embed.set_thumbnail(url="https://i.redd.it/27bp6h2z55011.jpg")
            embed.set_footer(text="(The code is like, really really bad)")
            await message.channel.send(embed=embed)

        #Shitty Clear Chat Functions    
        elif "clear" in message.content.lower():
            await message.channel.send("Not Clearing Messages \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n  \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n Cleared Messages")

        #This bit was made possible by Fwiz and Hideki Ryuga and their Tortoise Discord Bot (https://github.com/fwizzz/Tortoise-Discord-Bot)

        elif "kizuna" in message.content.lower() or "kzn" in message.content.lower():
                subred = reddit.subreddit('KizunaA_Irl')
                neewmeem = subred.hot(limit=100)
                lstmeem = list(neewmeem)
                randsub = random.choice(lstmeem)
                embed = discord.Embed(title=randsub.title,
                                      description=f'',
                                      url=randsub.url, colour=0x3498d)
                embed.set_image(url=randsub.url)
                await message.channel.send(embed=embed)

        elif "wholesomeanimeme" in message.content.lower():
                subred = reddit.subreddit('wholesomeanimemes')
                neewmeem = subred.hot(limit=100)
                lstmeem = list(neewmeem)
                randsub = random.choice(lstmeem)
                embed = discord.Embed(title=randsub.title,
                                      description=f'',
                                      url=randsub.url, colour=0x3498d)
                embed.set_image(url=randsub.url)
                await message.channel.send(embed=embed)

        elif "animeme" in message.content.lower():
                subred = reddit.subreddit('animemes')
                neewmeem = subred.hot(limit=100)
                lstmeem = list(neewmeem)
                randsub = random.choice(lstmeem)
                embed = discord.Embed(title=randsub.title,
                                      description=f'',
                                      url=randsub.url, colour=0x3498d)
                embed.set_image(url=randsub.url)
                await message.channel.send(embed=embed)
        elif "wholesome" in message.content.lower():
                subred = reddit.subreddit('wholesome')
                neewmeem = subred.hot(limit=100)
                lstmeem = list(neewmeem)
                randsub = random.choice(lstmeem)
                embed = discord.Embed(title=randsub.title,
                                      description=f'',
                                      url=randsub.url, colour=0x3498d)
                embed.set_image(url=randsub.url)
                await message.channel.send(embed=embed)

        elif "meme" in message.content.lower():
                subred = reddit.subreddit('memes')
                neewmeem = subred.hot(limit=100)
                lstmeem = list(neewmeem)
                randsub = random.choice(lstmeem)
                embed = discord.Embed(title=randsub.title,
                                      description=f'',
                                      url=randsub.url, colour=0x3498d)
                embed.set_image(url=randsub.url)
                await message.channel.send(embed=embed)

        #nsfw command
        elif "hentai" in message.content.lower():
            #checks if command was run in NSFW channel
            if nsfw_dm is True:
                subred = reddit.subreddit('hentai') 
                neewmeem = subred.hot(limit=100)
                lstmeem = list(neewmeem)
                randsub = random.choice(lstmeem)
                embed = discord.Embed(title=randsub.title,
                                      description=f'',
                                      url=randsub.url, colour=0x3498d)
                embed.set_image(url=randsub.url)
                await message.channel.send(embed=embed)
            elif message.channel.is_nsfw():
                subred = reddit.subreddit('hentai')
                neewmeem = subred.hot(limit=100)
                lstmeem = list(neewmeem)
                randsub = random.choice(lstmeem)
                embed = discord.Embed(title=randsub.title,
                                      description=f'',
                                      url=randsub.url, colour=0x3498d)
                embed.set_image(url=randsub.url)
                await message.channel.send(embed=embed)

            else:
                #return if it isn't
                await message.channel.send("🥕Sorry, that command is only available to be used in NSFW channels.🥕")


         #If Command was not recognised       
        else:
            await message.channel.send("🥕Unknown command, you can enable/disable some commands by editting the python file I use to work.🥕")
            await message.channel.send("You can check out the available commands by checking out my GitHub Page, which can be found here:")

            embed = discord.Embed(title="Battle Bunny Info Card", url="https://github.com/Burri-Taco/Momo_Battle_Bunny",
                                  description="Made by @ShiftyWizard#4823 & @_BurriTaco_#0889 because they'd rather do Python than VB.", color=0xfabcbd)
            embed.set_thumbnail(url="https://i.redd.it/27bp6h2z55011.jpg")
            embed.set_footer(text="(The code is like, really really bad)")
            await message.channel.send(embed=embed)


    #this bit makes bot respond to good bot and bad bot
    elif "bot" in message.content.lower():
        if message.content.startswith("good"):  
             await message.channel.send("Thank you :heart:")
        elif message.content.startswith("bad"):
             await message.channel.send("Hate you too, BB")
        else:
            await message.channel.send("Hai, Batorubanī desu")

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

            
    elif "stop" in message.content.lower():
        await message.channel.send("🥕lol no🥕")
        await asyncio.sleep(2)
        await message.channel.send("🥕Actually, let me see what I can do🥕")
        await asyncio.sleep(2)
        await message.channel.send("🥕Stopped just for you :heart:🥕")



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
