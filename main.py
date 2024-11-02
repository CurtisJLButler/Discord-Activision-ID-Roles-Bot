# bot.py
import os
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = 1301982775095590943
channel_id = 1302312626620989551

intents = discord.Intents.default()       # Start with default intents
intents.message_content = True             # Enable intent for reading message content
intents.members = True                     # Enable intent for accessing member data (needed for roles)

client = discord.Client(intents=intents)

user_roles = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    

    # Fetch the guild using fetch_guild
    guild = await client.fetch_guild(GUILD)
    
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    # Iterate over each member in the guild and store their roles
    for member in guild.members:
        roles = [role.name for role in member.roles if role.name != "@everyone"]  # Exclude @everyone role
        user_roles[member.name] = roles  # Store the roles in the dictionary

    # Print out the roles for each user
    print("User Roles:")
    for user, roles in user_roles.items():
        print(f'{user}: {", ".join(roles) if roles else "No roles"}')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    # Check if the message is from the specified channel and not from the bot itself
    if message.channel.id == 1302312626620989551 and message.author != client.user:
        print(f"Message from {message.author}: {message.content}")

client.run(TOKEN)
