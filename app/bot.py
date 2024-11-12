import os
import discord
from discord import app_commands

from dotenv import load_dotenv
import pymongo
import sys
import log
import mongoAPI
import re




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
    pattern = r"^[A-Za-z0-9]+#[0-9]{7}$"
    match = re.match(pattern, activisionid)

    if interaction.channel.id != channel_id:
        await interaction.response.send_message("This command can only be used in the specified channel.", ephemeral=True)
        return
    if match:
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
    result = mongoAPI.getID(member.name)
    if result is not None:
        log.log_message(f"{interaction.user}: got {member}'s ID  <Placeholder>")
        await interaction.response.send_message(f"{member}'s Activision ID is: {mongoAPI.getID(member.name)}", ephemeral=True)
    else:
        await interaction.response.send_message(f"{member} hasn't added their Activision ID to the bot", ephemeral=True)
        



@tree.command(
    name="getallids",
    description="Grabs all user id's from the database",
    guild=discord.Object(id=GUILD)
)
async def getCodId(interaction: discord.Interaction):
    act_ids = mongoAPI.getAll()  # Get the dictionary of user IDs
    if act_ids:
        # Format the dictionary into a string for easy display
        ids_message = "\n".join([f"{user}: {id}" for user, id in act_ids.items()])
        await interaction.response.send_message(f"User IDs:\n{ids_message}", ephemeral=True)
    else:
        await interaction.response.send_message("No user IDs found.", ephemeral=True)
    


@tree.command(
    name="help",
    description="Displays information about the Discord-Activision-ID-Roles-Bot",
    guild=discord.Object(id=GUILD)
)
async def help(interaction: discord.Interaction, command: str = None):
    if command is None:
        message = """
**Discord-Activision-ID-Roles-Bot**
Creates roles for users to display Activion IDs

**/setid** *(ActivisionID)*
This saves the username of the account you use the command along with your Activision ID (replace `(ActivisionID)` with your actual Activision ID).

**/getid** *(optional:username)*
This grabs the Activision ID of the discord user (Has to be someone in this server that has set their Activision ID using `/setid` as above).
If you type `/getid` without specifying a user, it will return your Activision ID instead of someone else's.

**/updateid** *(ActivisionID)*
This allows users to update their Activision IDs if they were incorrectly inputted into the database, or if they have updated their username on Call of Duty.

**/delid** *(ActivisionID)*
This allows users to delete their Activision ID from the database.
You still need to enter your Activision ID to prevent accidental deletion.

---

**Future Features**
I plan to add a semi-feature-rich log applet to this.
To avoid exceeding monthly limits on the free server, I’ll add limits on database access frequency.
Logs will be stored locally and are unaffected.

All app files are stored in the `app` folder.
"""
        await interaction.response.send_message(content=message, ephemeral=True)






# Last line to run
client.run(TOKEN)