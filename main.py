# imports go here
import discord
import os
from discord.ext import commands
import datetime
 
# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))
 
# Change the current working directory to the script directory
# This is so the script operates in its directory making it OS and folder agnostic.
os.chdir(script_directory)
 
# copy the below section into a file named data.env and save it in the same directory the script is running in
 
# discord token
# [discord token goes here]
# random.org token
# [random.org token goes here]
 
 
# Open the 'data.env' file in read mode
with open("data.env", 'rt') as file:
    # Load secret keys
    content = file.readlines()
    discordToken = content[1] # 1 being the second line containing the discord token
    randomToken = content[3] # 3 being the fourth line containing the random.org token
 
intents = discord.Intents.all() # im lazy, i just enable everything because my primary bot does a hodgepodge of things 
 
# you can set the prefix to anything. This is still a python script, you can play with variables as you wish. 
# the comment is what i run on my bot. its just a line that changes the prefix if its on a windows pc.
 
# prefix = "!"
# if os.name == "nt": prefix = "@"
 
prefix = "!" 
bot = commands.Bot(command_prefix=prefix, intents=intents)
 
# global variables go here
################
 
guildCount = 0
# developer_channel = 0
 
################
 
@bot.event
async def on_ready():
    global guildCount
    for guild in bot.guilds: # not efficient, i just use it for my main bot to know how many servers its in
        guildCount += 1
    print(f'I have logged in as {bot.user.name} ({bot.user.id}).\nThere are {guildCount} active servers.')
 
    # uncomment the below code and add in one of your servers channels where the bot will post messages. I use this to alert me whenever the bot starts or restarts
    
    # global developer_channel
    # dev_channel = [dev channel id goes here]
    # developer_channel = bot.get_channel(dev_channel)
    # await developer_channel.send(f'<@{your user ID}> {datetime.now()},a different test')
    
 
'''
in the below def, ctx is the context the bot works with. ctx.message is the message contents, ctx.author is the author, ctx.author.id is the authors discord id. you can view the contents of ctx by print(ctx) to view all of its contents but its a beast to unfold.
ctx.guild
ctx.guild.id
there are many more but you just have to play around with it.
async def on_message runs for EVERY MESSAGE. on small servers and when the bot isnt used much this is fine. but when the bot gets more popular, running a def for every message will bog it down. you will then switch to 
 
ctx.channel.send only works in response to a message. see the above on_ready() def for info on how to send arbitrary messages to a channel
'''
@bot.event
async def on_message(ctx, member: discord.Member = None):
    if ctx.author == bot.user:
        return
    
    print(f"{ctx.content}")
    # this prints the message contents to the console
 
    # /tableflip in discord will trigger this
    if '(╯°□°)╯︵ ┻━┻' in ctx.content:
        await ctx.send('NO TABLE FLIPPING\n┬─┬ノ( º _ ºノ)')
 
    await bot.process_commands(ctx)  # Important! Process commands after handling events. Technically the on_message event stops the bot from processing anything else so this line will allow the bot to process anything that isnt caught by the on_message def. this does mean that the bot will respond to a trigger in the on_message def and a command so be mindful of that.
 
'''
as mentioned above, when you dont want the bot reading every single message, you will use "commands"
 
they are very straight forward, the bot listens for a certain flag on a message, which in the def below is "!date" and only then will it trigger the command
 
you will need a unique @bot.command for each command. 
'''
 
@bot.command(name='date')
async def test(ctx):
    current_date = datetime.date.today()
    await ctx.send(f"The date is {current_date}")
 
@bot.command(name='celebrate')
async def test(ctx):
    await ctx.send(f'Congratz {ctx.author} you have a functioning discord bot.')
 
# Run the bot with your token this must be at the very end. it starts the discord bot.
bot.run(discordToken)