import discord
from discord.ext.commands import Bot, has_permissions, bot_has_permissions, guild_only
from discord.ext import commands
import random
import json
import aiohttp
from pyjokes import get_joke, get_jokes
import os


client = Bot(command_prefix="!")


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.idle, activity=discord.Game("Penguin Simulator")
    )
    print("We have logged in as {0.user}".format(client))


@client.command()
async def test(ctx, arg):
    """this function test to see if the bot works"""
    await ctx.send(arg)


# these commands respond with text
@client.command()
async def Hello_There(message):
    """this function responds with General Kenobi"""
    await message.channel.send("General Kenobi!")


@client.command()
async def HAPPY(message):
    """this function responds with Aye Aye Sir"""
    await message.channel.send("Aye Aye Sir")


@client.command()
async def pyjoke(ctx):
    """This function gets a random python joke from pyjoke"""
    await ctx.send(get_joke())


@client.command()
async def ask(ctx, *, arg=None):
    """This function takes an argument and gives a magic outcome"""
    if arg == None:
        await ctx.send("please ask a question")
    else:
        x = random.randint(0, 19)
        magic = [  # positive answers
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes! definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most Likely.",
            "The Outlook looks good.",
            "Yes!",
            "Signs point to yes.",
            # neutral answers
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "ask again.",
            # negative answers
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook is not so good.",
            "very doubtful.",
        ]
        await ctx.send(magic[x])


# random number commands
@client.command()
async def cf(message):
    """this function flips a coin and prints heads or tails"""
    c_flip = random.randint(0, 1)
    print(c_flip)
    if c_flip == 1:
        await message.channel.send(f"The coin flipped Heads")
    else:
        await message.channel.send(f"The coin flipped Tails")


@client.command()
async def rtd(message):
    """this function rolls a dice and prints the dice number"""
    dice = random.randint(1, 6)
    print(dice)
    await message.channel.send(f"The dice rolled a {dice}")


# these commands respond with pictures
@client.command()
async def pika(ctx):
  """This function returns a random image or gif of pikachu from some-random api"""
  async with aiohttp.ClientSession() as session:
      request = await session.get("https://some-random-api.ml/img/pikachu")
      pika_json = await request.json()

  embed = discord.Embed(title="Pikachu!", color=discord.Color.gold())
  embed.set_image(url=pika_json['link'])
  await ctx.send(embed=embed)


@client.command()
async def meme(ctx):
  """This function returns a random meme image from some-random api"""
  async with aiohttp.ClientSession() as session:
      request = await session.get("https://some-random-api.ml/meme")
      meme_json = await request.json()

  embed = discord.Embed(title="Have a meme", color=discord.Color.green())
  embed.set_image(url=meme_json['image'])
  await ctx.send(embed=embed)


@client.command()
async def panda(ctx):
  """This function returns a random panda image and fact from some-random api"""
  async with aiohttp.ClientSession() as session:
      request1 = await session.get("https://some-random-api.ml/img/panda")
      panda_json = await request1.json()
      request2 = request2 = await session.get("https://some-random-api.ml/facts/panda")
      fact_json = await request2.json()

  embed = discord.Embed(title="Panda!", color=discord.Color.lighter_grey())
  embed.set_image(url=panda_json["link"])
  embed.set_footer(text=fact_json["fact"])
  await ctx.send(embed=embed)


@client.command()
async def dog(ctx):
  """This function returns a random dog image and fact from some-random api"""
  async with aiohttp.ClientSession() as session:
      request1 = await session.get("https://some-random-api.ml/img/dog")
      dog_json = await request1.json()
      request2 = await session.get("https://some-random-api.ml/facts/dog")
      fact_json = await request2.json()

  embed = discord.Embed(title="Doggo!", color=discord.Color.blue())
  embed.set_image(url=dog_json["link"])
  embed.set_footer(text=fact_json["fact"])
  await ctx.send(embed=embed)


# these are moderator commands
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    """this function kicks a member"""
    await member.kick(reason=reason)
    await ctx.send(f"User {member} has kicked.")


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    """this function bans a member"""
    await member.ban(reason=reason)
    await ctx.send(f"User {member} has banned.")


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")

        else:
            await ctx.send(member + " was not found")


@client.command()
async def clear100(ctx, amount=100):
    """this function deletes 100 messages"""
    print("deleted 100 messages")
    await ctx.channel.purge(limit=amount)


@client.command()
async def clear(ctx, amount=5):
    """this function deletes 5 messages"""
    print("deleted 5 messages")
    await ctx.channel.purge(limit=amount)


#list of commands
@client.command()
async def commands(ctx):
  em = discord.Embed(title = "List of Bot Commands")

  em.add_field(name= "!Test (message)", value ="takes a message, then bot send message back")
  em.add_field(name= "!Hello_There", value ="sends a response")
  em.add_field(name= "!HAPPY", value ="sends a response")
  em.add_field(name= "!pyjoke", value ="replies with a python joke")
  em.add_field(name= "!ask (message)", value ="takes a message, replies with magic 8 ball response")
  em.add_field(name= "!cf", value ="flips a coin")
  em.add_field(name= "!rtd", value ="rolls a dice")
  em.add_field(name= "!pika", value ="sends a pikachu gif or image")
  em.add_field(name= "!meme", value ="sends a meme")
  em.add_field(name= "!panda", value ="sends a panda picture and fact")
  em.add_field(name= "!dog", value ="sends a dog picture and fact")
  em.add_field(name= "!kick @user", value ="kicks a user from the discord server")
  em.add_field(name= "!ban @user", value ="bans a user from the discord server")
  em.add_field(name= "!unban @user", value ="unbans a user from the server")
  em.add_field(name= "!clear", value ="clears the last 5 messages")
  em.add_field(name= "!clear100", value ="clears the last 100 messages")

  await ctx.send(embed = em)

client.run(${{secrets.TOKEN}})
