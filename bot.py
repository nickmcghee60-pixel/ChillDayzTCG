import discord
from discord.ext import commands
import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Load cogs
for cog in [
    "cogs.cards",
    "cogs.match",
]:
    try:
        bot.load_extension(cog)
        print(f"Loaded {cog}")
    except Exception as e:
        print(f"Failed to load {cog}: {e}")

bot.run(config.TOKEN)
