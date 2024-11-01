import os
import discord
from discord.ext import commands

# Retrieve the Discord bot token from the environment variable
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Initialize Discord bot
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Example command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == '__main__':
    # Run the bot
    bot.run(DISCORD_TOKEN)
