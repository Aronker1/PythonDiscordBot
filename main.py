import os
import random

import discord
from discord import app_commands
from tenor import getGif
from keep_alive import keep_aliveaa

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)


@client.event  #tells that the bot is online
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


#------------------------------msg events----------------------------
@client.event
async def on_message(message: discord.Message):
    if message.mention_everyone is True:  #if someone mentions everyone it prints out the message
        await message.channel.send(
            f'{message.author.mention} dont mention everyone idiot')
    elif message.author.id == 1053743721377697893 and random.randint(0,9) == 9:
        await message.channel.send('סתום תפה פלגמט', reference=message)
    elif message.author.id == 529333842482298900:
        await message.channel.send('https://cdn.discordapp.com/attachments/1024746822574555208/1173217822550278234/IMG_1432.jpg?ex=6563273e&is=6550b23e&hm=799f11beb9d6f0c954600121&')


#------------------------------commands----------------------------
@tree.command(name="test", description="dev test command")
async def test(ctx: discord.Interaction):
    print("test command run")
    await ctx.response.send_message("test", ephemeral=True)


@tree.command(name="react", description="sends a gif of user prompt")
@app_commands.describe(prompt="The prompt for the gif")
async def react(ctx: discord.Interaction, prompt: str):
    try:
        gif = getGif(prompt)
    except:
        await ctx.response.send_message("dumbass you sent something invalid")
    my_embed = discord.Embed(title=f"{ctx.user.name}'s honest reaction",color=discord.Color.random())
    my_embed.set_image(url=gif)
    new_msg = await ctx.response.send_message(content="", embed=my_embed)


@tree.command(name="sync",
              description="Syncs commands across all servers",
              guild=discord.Object(id=1173171412689768559))
@app_commands.describe(id="Id of the server to sync commands for")
async def sync(ctx: discord.Interaction, id: int):
    for guild in client.guilds:
        tree.copy_global_to(guild=guild)
        await tree.sync(guild=guild)


#----------------------------------activate the bot-----------------------------------
try:
    token = os.getenv("TOKEN") or ""
    keep_alive()
    client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
#----------------------------------activate the bot-----------------------------------
