import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

discordToken = os.getenv('AAUXGibHrjkpBR1TK__-IqjbfCVz0PFv')  # Update to read from environment
bot.run(discordToken)
