import discord
import os
import random
from keepalive import keep_alive
from replit import db
from discord.ext import commands



Token = os.environ['Token']
NEM = db["aranyk"]
SERVER_ID = int(os.environ['id'])
client = commands.Bot(command_prefix = "%")

@client.event
async def on_ready():
  print('A bot be van jelentkezve mint: {0.user}'.format(client))
  activity = discord.Activity(type=discord.ActivityType.listening, name="%parancsok")
  await client.change_presence(activity=activity)

@client.command()
async def aranyk(ctx, *, arg,):
  if arg == "sors":
    aranyk_nyitva = open("aranykopesek.txt", "r")
    sorsolt_aranyk = random.choice(aranyk_nyitva.readlines())
    await ctx.send(sorsolt_aranyk)
    aranyk_nyitva.close()
  if arg == "all":
    aranyk_fajl = open("aranykopesek.txt", "r")
    for idezet in aranyk_fajl.readlines():
      await ctx.send(idezet)
    aranyk_fajl.close()
  if arg.startswith("add"):
    idezet = arg[3:]
    aranyk_fajl = open("aranykopesek.txt", "a")
    aranyk_fajl.write(f"{idezet}\n")
    await ctx.send("Az idézet sikeresen hozzá lett adva: ")
    await ctx.send(idezet)
    aranyk_fajl.close()
  if arg == "del":
    aranyk_fajl = open("aranykopesek.txt")
    yes = []
    for no in aranyk_fajl.readlines():
      yes.append(no)
    aranyk_fajl.close()
    aranyk_fajl = open("aranykopesek.txt", "w")
    aranyk_fajl.close()
    aranyk_fajl = open("aranykopesek.txt", "a")
    del yes[-1]
    for vlami in yes:
      aranyk_fajl.write(vlami)
    aranyk_fajl.close()
    ctx.send("A legutóbb hozzáadott idézet el lett távolítva!")
  if arg.startswith("keres"):
    keresett = arg[5:]
    talalatok_szama = 0
    aranyk_fajl = open("aranykopesek.txt")
    for sor in aranyk_fajl.readlines():
      if keresett in sor:
        talalatok_szama += 1
        await ctx.send(sor)
    await ctx.send(f"Találatok száma: {talalatok_szama}")
    aranyk_fajl.close()


@client.command()
async def rand(ctx, *, arg):
  if arg == "champ":
    await ctx.message.delete()
    fajl = open("champ.txt", "r")
    random_champ = random.choice(fajl.readlines())
    fajl.close()
    await ctx.send(f"{ctx.author} használta **Random champ**: {random_champ}")
  if arg.startswith("tournament"):
    nevek = arg[11:].split(" ")
    if len(nevek) % 2 == 0:
      while len(nevek) > 0:
        nev1 = random.choice(nevek)
        nevek.remove(nev1)
        nev2 = random.choice(nevek)
        nevek.remove(nev2)
        await ctx.send(f"{nev1}, {nev2} ellen!")
    else: 
      while len(nevek) != 1:
        nev1 = random.choice(nevek)
        nevek.remove(nev1)
        nev2 = random.choice(nevek)
        nevek.remove(nev2)
        await ctx.send(f"{nev1}, {nev2} ellen!")
      await ctx.send(f"{nevek[0]} most várni fog.")

@client.command()
async def parancsok(ctx):
  for command in client.commands:
	  await ctx.send(command)
      
    

""""@client.command()
async def harc(ctx, arg):
  player1 = ""
  player2 = ""
  for user_mentioned in ctx.message.mentions:
    player1 = user_mentioned.id
  player2 = "<@" + str(ctx.author.id) + ">"
  await ctx.send(f"<@{player1}> kihívta {player2}-t")
  await"""
    
      
    

keep_alive()
client.run(Token)