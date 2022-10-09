import discord
from discord.ext import commands


def get_token() -> str:
    """
    Returns token as string
    Token should be located in token/.token
    """
    try:
        token_file = open(".token", "r")
        return token_file.readline()
    except IOError:
        print("Error reading token")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix="!", intents=intents)

token = get_token()

client.run(token)
