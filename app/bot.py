# bot.py
import os
import discord
from discord import app_commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = 1301982775095590943                # Testing server
channel_id = 1302312626620989551           # ids channel

intents = discord.Intents.default()        # Start with default intents
intents.message_content = True             # Enable intent for reading message content
intents.members = True                     # Enable intent for accessing member data (needed for roles)

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# END OF HEADER

# runs at launch
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    # Lets the server op know that commands have loaded on the server(s)
    await tree.sync(guild=discord.Object(id=GUILD))
    print("Ready!")
    

    

# Will send a print to the server console when a user sends a message in the specified channel
@client.event
async def on_message(message):
    # Check if the message is from the specified channel and not from the bot itself
    if message.channel.id == channel_id and message.author != client.user:
        print(f"Message from {message.author}: {message.content}")


# Add the guild ids in which the slash command will appear.
# If it should be in all, remove the argument, but note that
# it will take some time (up to an hour) to register the
# command if it's for all guilds.
@tree.command(
    name="commandname",
    description="My first application Command",
    guild=discord.Object(id=GUILD)
)
async def first_command(interaction: discord.Interaction):
    await interaction.response.send_message("Text", ephemeral=True)

    





# Last line to run
client.run(TOKEN)