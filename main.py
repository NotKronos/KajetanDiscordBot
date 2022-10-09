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


token = get_token()
