import os
import discord
from discord import app_commands
from discord.ext import commands
from tenor import getGif
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event  #tells that the bot is online
async def on_ready():
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')
  print('------')


#------------------------------msg events----------------------------
@bot.event
async def on_message(message):
  if message.mention_everyone == True:  #if someone mentions everyone it prints out the message
    await message.channel.send('dont mention everyone idiot')
  elif message.author.id == 1053743721377697893:
    await message.channel.send('סתום תפה פלגמט')

  await bot.process_commands(message)  #the msg will wait for the


#------------------------------commands----------------------------
#say command: $say hello
#prints hello
@bot.command()
async def test(ctx, arg):
  await ctx.send(arg)


@bot.command(name="react")
async def react(ctx, args):

  # Delete the users command
  await ctx.message.delete()
  # our test search
  await ctx.send(getGif(args))


#----------------------------------activate the bot-----------------------------------
try:
  token = os.getenv("TOKEN") or ""
  keep_alive()
  bot.run(token)
except discord.HTTPException as e:
  if e.status == 429:
    print(
        "The Discord servers denied the connection for making too many requests"
    )
    print(
        "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
    )
  else:
    raise e
#----------------------------------activate the bot-----------------------------------
