import discord
from discord.ext import commands

# Define your bot and set your prefix
bot = commands.Bot(command_prefix="!")

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
TOKEN = 'YOUR_TOKEN_HERE'

# Replace this with the exact message and role you want to assign
trigger_message = "Lottness#2766890"
role_name = "SpecialRole"  # This role should already exist on your server

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore bot messages
    if message.author.bot:
        return

    # Check if the message content matches the trigger message
    if message.content == trigger_message:
        role = discord.utils.get(message.guild.roles, name=role_name)
        if role:
            await message.author.add_roles(role)
            await message.channel.send(f"{message.author.mention}, you have been assigned the '{role_name}' role!")
        else:
            await message.channel.send(f"Role '{role_name}' does not exist. Please create it first.")

# Start the bot
bot.run(TOKEN)
