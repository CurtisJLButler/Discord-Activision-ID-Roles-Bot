# bot.py
import os
import discord
from discord import app_commands

from dotenv import load_dotenv
import pymongo
import sys
import log
import mongoAPI


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

activision_id = {}
usageLog = {}

def post():
    log.log_message("Posting")



# Discord API stuff

# runs at launch
@client.event
async def on_ready():
    log.log_message(f'{client.user} has connected to Discord!')

    # Lets the server op know that commands have loaded on the server(s)
    await tree.sync(guild=discord.Object(id=GUILD))
    log.log_message("Bot is ready!")
    


# Will send a print to the server console when a user sends a message in the specified channel
@client.event
async def on_message(message):
    # Check if the message is from the specified channel and not from the bot itself
    if message.channel.id == channel_id and message.author != client.user:
        log.log_message(f"Message from {message.author}: {message.content}")


# Saves a users Activision ID to the database
@tree.command(
    name="setid",
    description="Saves your Activision ID to the server database",
    guild=discord.Object(id=GUILD)
    
)
async def setCodId(interaction: discord.Interaction, activisionid: str = None):
    if interaction.channel.id != channel_id:
        await interaction.response.send_message("This command can only be used in the specified channel.", ephemeral=True)
        return
    if(activision_id == "yes"):
        mongoAPI.post(str(interaction.user), str(activisionid))  # Call your database interaction function
        await interaction.response.send_message(f"{interaction.user}'s Activision ID is now set to {activisionid}", ephemeral=True)
    else:
        await interaction.response.send_message(f"Please enter a valid Activision ID", ephemeral=True)

# Gets a users Activision ID from the database
@tree.command(
    name="getid",
    description="Grabs a users Activision ID from the server database",
    guild=discord.Object(id=GUILD)
)
async def getCodId(interaction: discord.Interaction, member: discord.Member = None):
    if member is None:
        member = interaction.user
    log.log_message(f"{interaction.user}: got {member}'s ID  <Placeholder>")
    await interaction.response.send_message(f"Text {member}", ephemeral=True)

    





# Last line to run
client.run(TOKEN)