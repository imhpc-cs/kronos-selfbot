# CONFIG
# ----
#-----
with open ("token.txt", "r") as f:
    tsucc = str(f.read())
with open ("prefix.txt", "r") as ff:
    psucc = str(ff.read())
token = tsucc 
prefix = psucc # This will be used at the start of commands.
# ----------

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
import pyPrivnote as pn
from gtts import gTTS
# Imports the needed libs.



print(f'''{Fore.RESET}
 ██ ▄█▀ ██▀███   ▒█████   ███▄    █  ▒█████    ██████ 
 ██▄█▒ ▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▒██▒  ██▒▒██    ▒ 
▓███▄░ ▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██░  ██▒░ ▓██▄   
▓██ █▄ ▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒▒██   ██░  ▒   ██▒
▒██▒ █▄░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░░ ████▓▒░▒██████▒▒
▒ ▒▒ ▓▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░ ░▒ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░
░ ░░ ░   ░░   ░ ░ ░ ░ ▒     ░   ░ ░ ░ ░ ░ ▒  ░  ░  ░  
░  ░      ░         ░ ░           ░     ░ ░        ░  
                                                      
                        
                        

    '''+Fore.RESET)



class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print(f"Connected to: [{self.user.name}]")
        print("Successfully Authed Into Token")
        print("This Is A Selfbot By imhpc On Instagram!")
        print("V1")
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")
# Declares the bot, passes it a prefix and lets it know to (hopefully) only listen to itself.

@bot.event
async def on_ready():
    print("Logged In")
#Prints when the bot is ready to be used.

async def self_check(ctx):
  if bot.user.id == ctx.message.author.id:
    return True
  else:
    return False
    # A secondary check to ensure nobody but the owner can run these commands.
        

@commands.check(self_check)
@bot.command(pass_context=True)
async def clearall(ctx: int):
            async for message in ctx.channel.history(limit=99999):
                if message.author == ctx.author:
                    await message.delete()
                    await asyncio.sleep(0)


commands.check(self_check)
@bot.command(pass_context=True)
async def kall(ctx):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    await ctx.guild.kick(user)
    print (f"{user.name} has been kicked from {ctx.guild.name}")
    print ("Action Completed: kall")
    # Kicks every member in a server.
    
    
    
@commands.check(self_check)
@bot.command(pass_context=True)
async def rape(ctx):
  await ctx.message.delete()
  while True:
    await ctx.send(".help")


        
@commands.check(self_check)
@bot.command(pass_context=True)
async def ball(ctx):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await ctx.guild.ban(user)
      print (f"{user.name} has been banned from {ctx.guild.name}")
    except:
      print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
      print ("Action Completed: ball")  

@commands.check(self_check)
@bot.command(pass_context=True)
async def rall(ctx, rename_to):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.edit(nick=rename_to)
      print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
    except:
      print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
      print ("Action Completed: rall")
    # Renames every member in a server.

@commands.check(self_check)
@bot.command(pass_context=True)
async def mall(ctx, *, message):
  await ctx.message.delete()
  for user in ctx.guild.members:
    try:
      await user.send(message)
      print(f"{user.name} has recieved the message.")
    except:
      print(f"{user.name} has NOT recieved the message.")
      print("Action Completed: mall")
    # Messages every member in a server.

@commands.check(self_check)
@bot.command(pass_context=True)
async def dall(ctx, condition):
  await ctx.message.delete()
  if condition.lower() == "channels":
    for channel in list(ctx.guild.channels):
      try:
        await channel.delete()
        print (f"{channel.name} has been deleted in {ctx.guild.name}")
      except:
        print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        print ("Action Completed: dall channels")
        if condition.lower() == "roles":
          for role in list(ctx.guild.roles):
            try:
              await role.delete()
              print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
              print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
              print ("Action Completed: dall roles")
            if condition.lower() == "emojis":
              for emoji in list(ctx.guild.emojis):
                try:
                  await emoji.delete()
                  print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                  print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
                  print ("Action Completed: dall emojis")
                if condition.lower() == "all":
                  for channel in list(ctx.guild.channels):
                    try:
                      await channel.delete()
                      print (f"{channel.name} has been deleted in {ctx.guild.name}")
                    except:
                      print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
                      for role in list(ctx.guild.roles):
                        try:
                          await role.delete()
                          print (f"{role.name} has been deleted in {ctx.guild.name}")
                        except:
                          print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
                          for emoji in list(ctx.guild.emojis):
                            try:
                              await emoji.delete()
                              print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                            except:
                              print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
                              print ("Action Completed: dall all")
    # Can  perform multiple actions that envolve mass deleting.


@commands.check(self_check)
@bot.command(pass_context=True)
async def destroy(ctx):
  await ctx.message.delete()
  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print (f"{emoji.name} has been deleted in {ctx.guild.name}")
    except:
      print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
      for channel in list(ctx.guild.channels):
        try:
          await channel.delete()
          print (f"{channel.name} has been deleted in {ctx.guild.name}")
        except:
          print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
          for role in list(ctx.guild.roles):
            try:
              await role.delete()
              print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
              print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
              for user in list(ctx.guild.members):
                try:
                  await ctx.guild.ban(user)
                  print (f"{user.name} has been banned from {ctx.guild.name}")
                except:
                  print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
                  print ("Action Completed: destroy")
    # Outright destroys a server.
  
@commands.check(self_check)
@bot.command(pass_context=True)
async def textnuke(ctx):
      guild = ctx.message.guild
      await guild.create_text_channel('imhpc ON IG')

@commands.check(self_check)
@bot.command()
async def dog(ctx: commands.Context):
  async with aiohttp.ClientSession(loop=ctx.bot.loop) as session:
    async with session.get("https://random.dog/woof.json") as r:
      data = await r.json()
      embed = discord.Embed()
      embed.set_image(url=data['url'])
      await ctx.send(embed=embed)

@commands.check(self_check)
@bot.command()
async def dogs(ctx: commands.Context):
  async with aiohttp.ClientSession(loop=ctx.bot.loop) as session:
    async with session.get("https://random.dog/woof.json") as r:
      data = await r.json()
      embed = discord.Embed()
      embed.set_image(url=data['url'])
      await ctx.send(embed=embed)
      
bad_words = ['fuck', 'shit', 'etc.']

@commands.check(self_check)
@bot.command()
async def censor(member):
  guild = client.get_guild(member.guild.id)
  for channel in guild.text_channels:
    async for message in channel.history(limit=search_depth):
      if message.author.id == member.id:
        await message.channel.purge(bad_words)

@commands.check(self_check)
@bot.command()
async def corona(ctx):
  async with aiohttp.ClientSession() as session:
    async with session.get(f'https://corona.lmao.ninja/v2/all') as r:
      if r.status == 200:
        js = await r.json()
        cases = js['cases']
        deaths = js['deaths']
        recovered = js['recovered']
        casestoday = js['todayCases']
        tests = js['tests']
        await ctx.send("**Coronavirus (COVID-19) STATS**" + "\n" + "```" + " Cases: " + str(cases) + "\n " + "Deaths: " + str(deaths) + "\n " + "Recovered: " + str(recovered) + "\n" + " Cases Today: " + str(casestoday) + "\n" + " Total Tested: " + str(tests) + "\n```")

@commands.check(self_check)
@bot.command()
async def meme(ctx):
  mem = str()
  meme = requests.get("https://meme-api.herokuapp.com/gimme/dankmemes")
  mem = str(meme.json()['url'])
  await ctx.send(mem)   
  await ctx.send("*Credit to imhpc*")

@commands.check(self_check)
@bot.command()
async def memes(ctx):
  mem = str()
  meme = requests.get("https://meme-api.herokuapp.com/gimme/dankmemes")
  mem = str(meme.json()['url'])
  await ctx.send(mem)    
  await ctx.send("*Credit to imhpc*")

@commands.check(self_check)
@bot.command()
async def iplookup(ctx, ipp):  
  async with aiohttp.ClientSession() as session:
    async with session.get(f'https://json.geoiplookup.io/{ipp}') as r:
      if r.status == 200:
        js = await r.json()
        ip = js['ip']
        isp = js['isp']
        org = js['org']
        lat = js['latitude']
        long = js['longitude']
        hostname = js['hostname']
        city = js['city']
        country_code = js['country_code']
        country_name = js['country_name']
        postal_code = js['postal_code']
        currency_code = js['currency_code']
        region = js['region']
        currency_name = js['currency_name']
        results=str("""
        *Looking It Up...BRB!*
        ```yaml
        //IP LOOKUP\\
        
        Results For """+ipp+""":
        
        IP: """ + ip + """
        
        HOSTNAME: """ + hostname + """
        
        ISP: """ + isp + """
        
        ORG: """ + org + """
        
        CITY: """ + city + """
        
        COUNTRY: """ + country_name + """
        
        REGION: """ + region + """
                
        POSTAL/ZIP CODE: """ + postal_code + """
        
        CURRENCY: """ + currency_name + """
        ```
        """)
        await ctx.send(results)


@commands.check(self_check)
@bot.command()
async def domainresolver(ctx, ip):  
  async with aiohttp.ClientSession() as session:
    async with session.get(f'https://json.geoiplookup.io/{ip}') as r:
      if r.status == 200:
        js = await r.json()
        domain = js['ip']
        await ctx.send("**Looking Up **" + ip)
        time.sleep(1)
        await ctx.send(ip + "** Resolves To: **" + domain)

@commands.check(self_check)
@bot.command()
async def maclookup(ctx, mac):  
  await ctx.send("**Looking Up "+mac+"...**")
  link = str('https://api.macvendors.com/{}'.format(mac));r = requests.get(link)
  await ctx.send("```perl\n"+r.text+"\n```")  
@commands.check(self_check)  

@bot.command()
async def headerscrape(ctx, host):  
  await ctx.send("**Scraping "+host+"...**")
  link = str('https://api.hackertarget.com/httpheaders/?q={}'.format(host));r = requests.get(link)
  await ctx.send("```yaml\n"+r.text+"\n```")  
        
@commands.check(self_check)
@bot.command()
async def dm(ctx, member: discord.Member, *,content):
    channel = await member.create_dm()
    await channel.send(content)
    await ctx.send("**Sent!**")

@commands.check(self_check)
@bot.command()
async def kick(ctx, target : discord.Member, *, reason=None):
    await target.kick(reason=reason)
    await ctx.send("**SKID GOT KICKED!!**")

@commands.check(self_check)
@bot.command()
async def ban(ctx, target : discord.Member, *, reason=None):
    await target.ban(reason=reason)
    await ctx.send("**SKID GOT BANNED!!**")

@commands.check(self_check)
@bot.command()
async def mute(ctx, member: discord.Member):
  role = get(member.guild.roles, name="Muted") 
  await member.add_roles(role) 
  embed = discord.Embed(title="User Muted!", description="{0} was muted by {1}!".format(member, ctx.message.author), color=0xff00f6)
  await ctx.send(embed=embed)
  
@commands.check(self_check)
@bot.command()
async def addrole(ctx, member: discord.Member, role):
  role = get(member.guild.roles, name=role) 
  await member.add_roles(role) 
  embed = discord.Embed(title="User Muted!", description="{0} was muted by {1}!".format(member, ctx.message.author), color=0xff00f6)
  await ctx.send(embed=embed)


@commands.check(self_check)
@bot.command()
async def unmute(ctx, member: discord.Member):
  rolez = get(member.guild.roles, name="Muted") 
  await member.remove_roles(rolez) 
  embed = discord.Embed(title="User Unmuted!", description="{0} was unmuted by {1}!".format(member, ctx.message.author), color=0xff00f6)
  await ctx.send(embed=embed) 

@commands.check(self_check)
@bot.command()
async def admin(ctx, member): 
  await member.add_roles("Admin") 


@commands.check(self_check)
@bot.command()
async def makerole(ctx, role):
  guild = ctx.guild
  await guild.create_role(name=role, colour=discord.Colour(0xffffff), permissions=Permissions.all())
  await ctx.send("Created " + str(role))

@commands.check(self_check)
@bot.command()
async def purge(ctx, amount=100000):
  await ctx.channel.purge(limit=amount)
  await ctx.send("https://tenor.com/view/explosion-action-bird-run-running-gif-4877919")
  await ctx.send("**PURGED!!**")

@commands.check(self_check)
@bot.command()
async def annoy(ctx, member: discord.Member, *,content):
    channel = await member.create_dm()
    while True:
      await channel.send(content)
      time.sleep(2)

@commands.check(self_check)
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@commands.check(self_check)
@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)


@commands.check(self_check)
@bot.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(a/b)

@commands.check(self_check)
@bot.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(a-b)

@commands.check(self_check)
@bot.command()
async def textchannel(ctx, arg1):
  guild = ctx.message.guild
  await guild.create_text_channel(arg1)
  await ctx.send("**Ok, created channel**")
  
@commands.check(self_check)
@bot.command()
async def voicechannel(ctx, arg1):
  guild = ctx.message.guild
  await guild.create_voice_channel(arg1)
  await ctx.send("**Ok, created channel**")

@commands.check(self_check)
@bot.command()
async def cmd(ctx, *, cmd):
  async with ctx.typing():
    await ctx.send(f"Executing {cmd}") 
    function = subprocess.check_output(cmd, shell=True) 
    function = function.decode('utf-8') 
    await ctx.send(f"Output diff\n{function}")

@commands.check(self_check)
@bot.command()
async def kitty(ctx):
  async with aiohttp.ClientSession(loop=ctx.bot.loop) as session:
    async with session.get("https://aws.random.cat/meow") as r:
      data = await r.json()
      embed = discord.Embed()
      embed.set_image(url=data['file'])
      await ctx.send(embed=embed)


@commands.check(self_check)
@bot.command()
async def smiley(ctx):
  await ctx.send(":smile:")

@commands.check(self_check)
@bot.command()
async def cat(ctx):
  async with aiohttp.ClientSession(loop=ctx.bot.loop) as session:
    async with session.get("https://aws.random.cat/meow") as r:
      data = await r.json()
      embed = discord.Embed()
      embed.set_image(url=data['file'])
      await ctx.send(embed=embed)


#https://www.countryflags.io/{str(ip_data['country_code'])}/shiny/64.png


#@bot.command()
#
#async def announce(ctx, arg):
#  channel = bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)
#  await channel.send(arg)
#  await ctx.send("**Announcement made!**")
#  await ctx.message.delete()


@commands.check(self_check)
@bot.command()
async def portscan(ctx, host):
  await ctx.send("**Scanning "+host+"...**")
  link = str('https://api.hackertarget.com/nmap/?q={}'.format(host));r = requests.get(link)
  await ctx.send("```yaml\n"+r.text+"\n```")  

@commands.check(self_check)   
@bot.command()
async def chatbot(ctx,*, question):
  async with aiohttp.ClientSession() as session:
    async with session.get(f'https://some-random-api.ml/chatbot?message={question}') as r:
      if r.status == 200:
        js = await r.json()
        response = js['response']
        await ctx.send("**Reply: **")
        await ctx.send("```haskell\n"+response+"\n```")
        
@commands.check(self_check)
@bot.command()
async def whois(ctx, host):
  await ctx.send("**WHOIS Results For "+host+"...**")
  link = str('https://api.hackertarget.com/whois/?q={}'.format(host));r = requests.get(link)
  await ctx.send("```yaml\n"+r.text+"\n```")   

@commands.check(self_check)  
@bot.command()
async def revdns(ctx, host):
  await ctx.send("**Reverse DNS For "+host+"...**")
  link = str('https://api.hackertarget.com/reversedns/?q={}'.format(host));r = requests.get(link)
  await ctx.send("```yaml\n"+r.text+"\n```")   


@commands.check(self_check)  
@bot.command()
async def ping(ctx, host):
  await ctx.send("**Ping Results For "+host+"...**")
  link = str('https://api.hackertarget.com/nping/?q={}'.format(host));r = requests.get(link)
  await ctx.send("```yaml\n"+r.text+"\n```")   


@commands.check(self_check)  
@bot.command()
async def dnslookup(ctx, host):
  await ctx.send("**DNS Lookup Results For "+host+"...**")
  link = str('https://api.hackertarget.com/dnslookup/?q={}'.format(host));r = requests.get(link)
  await ctx.send("```yaml\n"+r.text+"\n```")   
  
@commands.check(self_check)
@bot.command()
async def crawl(ctx, host):
  await ctx.send("**Crawl Results For "+host+"...**")
  link = str('https://api.hackertarget.com/pagelinks/?q={}'.format(host));r = requests.get(link)
  await ctx.send("```yaml\n"+r.text+"\n```")   
  


@commands.check(self_check)
@bot.command()
async def hello(ctx):
    await ctx.send("**:wave:Ayooo Wassup {}**".format(ctx.message.author))

#@bot.command()
#
#async def cmd(ctx, cmd):
#    async with ctx.typing():
#      await ctx.send(f"**Executing `{cmd}`**")
#      function = subprocess.check_output(cmd, shell=True)
#      function = function.decode('utf-8')
#      await ctx.send(f"**__Output__**```diff\n{function}```")

@commands.check(self_check)
@bot.command()
async def invite(ctx):
    await ctx.send("")

bot.remove_command('help')

@commands.check(self_check)
@bot.command()
async def avatar(ctx, member: discord.Member): 
  show_avatar = discord.Embed(
  
  
    color = discord.Color.dark_blue()
  )
  show_avatar.set_image(url='{}'.format(member.avatar_url))
  await ctx.send("**Sending avatar..**")
  await ctx.send(embed=show_avatar)



@commands.check(self_check)
@bot.command()
async def tokengen(ctx):
  async with aiohttp.ClientSession() as session:
    async with session.get(f'https://some-random-api.ml/bottoken') as r:
      if r.status == 200:
        js = await r.json()
        token = js['token']
        await ctx.send("**Generating a Token...**")
        await ctx.send("```yaml\n"+token+"\n```")


@commands.check(self_check)
@bot.command()
async def lol(ctx):
    embed = discord.Embed(title=bot.user.name, description="**Moderation Menu (Admin Commands)**", color=800080)
    embed.add_field(name="+helpquarantine", value="**Gives this message**", inline=False)
    embed.add_field(name="+memes or +meme", value="**Sends back a random meme**", inline=False)
    embed.add_field(name="+chatbot <message>", value="**Asks the chat bot your question**", inline=False)
    embed.add_field(name="+smiley", value="**Sends smiley face, cuz why not?**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    
    await ctx.send(embed=embed)


@commands.check(self_check)
@bot.command()
async def help(ctx):
    embed = discord.Embed(title=bot.user.name, description="", color=0xff1493)
    embed.add_field(name="+help", value="**Gives this message**")
    embed.add_field(name="+helptools", value="**Gives you a list of all tools.**")
    embed.add_field(name="+helpmoderation", value="**Gives you a list of mod commands**")
    embed.add_field(name="+helpnetwork", value="**Networking Tools!**")
    embed.add_field(name="+helpfunny", value="**Funny Stuff!!**")
    embed.add_field(name="+helpquarantine", value="**Pass the time while in quarantine!**")
    embed.add_field(name="+setup", value="**Explains the requirements to have this bot in your server!**")
    embed.add_field(name="+invite", value="**Generates an invite link for SymphannyBot!**")
    
    await ctx.send(embed=embed)

@commands.check(self_check)
@bot.command()
async def helptools(ctx):
    embed = discord.Embed(title=bot.user.name, description="**Tools Menu!**", color=800080)
    embed.add_field(name="+helptools", value="**Gives this message**", inline=False)
    embed.add_field(name="+add <X Y>", value="**Gives the addition answer of *X* and *Y* **", inline=False)
    embed.add_field(name="+subtract <X Y>", value="**Gives the subtraction answer of *X* and *Y* **", inline=False)
    embed.add_field(name="+multiply <X Y>", value="**Gives the multiplication answer of *X* and *Y* **", inline=False)
    embed.add_field(name="+divide <X Y>", value="**Gives the division answer of *X* and *Y* **", inline=False)    
    embed.add_field(name="+dm <@person> <message>", value="**Sends a dm from the bot to a specified person**", inline=False)
    embed.add_field(name="+hello", value="**Prints a nice message!**", inline=False)
    embed.add_field(name="+info", value="**Gives a little info about the bot**", inline=False)
    embed.add_field(name="+tokengen", value="**Generates a random bot token!**", inline=False)
    
    await ctx.send(embed=embed)
    

@commands.check(self_check)
@bot.command()
async def helpmoderation(ctx):
    embed = discord.Embed(title=bot.user.name, description="**Moderation Menu (Admin Commands)**", color=800080)
    embed.add_field(name="+helpmoderation", value="**Gives this message**", inline=False)
    embed.add_field(name="+mute <@user>", value="**Mutes a specified user**", inline=False)
    embed.add_field(name="+unmute <@user>", value="**Unmutes a specified user**", inline=False)
    embed.add_field(name="+textchannel <name>", value="**Makes a text channel**", inline=False)
    embed.add_field(name="+voicechannel <name>", value="**Makes a voice channel**", inline=False)
    embed.add_field(name="+announce <message>", value="**Makes an announcement to #announcement**", inline=False)
    embed.add_field(name="+annoy <@person> <message>", value="**Spams a specified person's DMs!**", inline=False)
    embed.add_field(name="+dm <@person> <message>", value="**Sends a dm from the bot to a specified person**", inline=False)
    
    await ctx.send(embed=embed)
    

@commands.check(self_check)
@bot.command()
async def helpquarantine(ctx):
    embed = discord.Embed(title=bot.user.name, description="**Moderation Menu (Admin Commands)**", color=800080)
    embed.add_field(name="+helpquarantine", value="**Gives this message**", inline=False)
    embed.add_field(name="+memes or +meme", value="**Sends back a random meme**", inline=False)
    embed.add_field(name="+chatbot <message>", value="**Asks the chat bot your question**", inline=False)
    embed.add_field(name="+smiley", value="**Sends smiley face, cuz why not?**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    
    await ctx.send(embed=embed)


@commands.check(self_check)
@bot.command()
async def helpnetwork(ctx):
    embed = discord.Embed(title=bot.user.name, description="**Moderation Menu (Admin Commands)**", color=800080)
    embed.add_field(name="+helpnetwork", value="**Gives this message**", inline=False)
    embed.add_field(name="+iplookup <ip>", value="**Allows one to lookup results on a specific IP.**", inline=False)
    embed.add_field(name="+domainresolver <domain>", value="**See what IP a domain resolves to.**", inline=False)
    embed.add_field(name="+portscan <host>", value="**Checks for common ports on a host.**", inline=False)
    embed.add_field(name="+headerscrape <host>",value="**Checks the HTTP Headers on a host.**", inline=False)
    embed.add_field(name="+whois <website>", value="**Get the WHOIS Details for a website.**", inline=False)
    embed.add_field(name="+ping <host>", value="**Sends ICMP Probes to a host.**", inline=False)
    embed.add_field(name="+dnslookup <host>", value="**Runs a DNS Lookup for a host.**", inline=False)
    embed.add_field(name="+crawl https://<website>", value="**Crawls A Website.**", inline=False)
    embed.add_field(name="+revdns <website>", value="**Attempts to find all Reverse DNS Entries for a Domain.**", inline=False)
    embed.add_field(name="+maclookup <mac>", value="**Lookup the vendor for a mac address!**", inline=False)
    
    await ctx.send(embed=embed)
    
@commands.check(self_check)
@bot.command()
async def helpfunny(ctx):
    embed = discord.Embed(title=bot.user.name, description="**Moderation Menu (Admin Commands)**", color=800080)
    embed.add_field(name="+helpfunny", value="**Gives this message**", inline=False)
    embed.add_field(name="+cat or +cats", value="**Sends a random picture of a cat!**", inline=False)
    embed.add_field(name="+dog or +dogs", value="**Sends a random picture of a dog!**", inline=False)
    embed.add_field(name="+jokes", value="**Tells a joke**", inline=False)
    embed.add_field(name="+meme or +memes", value="**Prints a random meme using an api (Creds to Aero!)**", inline=False)
    embed.add_field(name="+chatbot", value="**Talk to a AI, responses are funny!**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    embed.add_field(name="+comingsoon", value="**comingsoon**", inline=False)
    
    await ctx.send(embed=embed)

@commands.check(self_check)
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=bot.user.name, description="", color=800080)

    # give info about you here
    embed.add_field(name="Made by", value="imhpc#0416")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server Count", value=f"{len(bot.guilds)}")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discord.gg/9HMQMPx")
    embed.add_field(name="Bot User ID", value=bot.user.id)
    embed.add_field(name="Server Hostname", value=socket.gethostname())
    embed.add_field(name="Prefix:", value="+")
    embed.add_field(name="Help Command:", value="+help")
    
    await ctx.send(embed=embed)
    


  
@commands.check(self_check)
@bot.command()
async def cookie(ctx, person):
  await ctx.send("**{} Do u want a cookie nigga? :cookie: **".format(person))

@commands.check(self_check)
@bot.command()
async def ascii(ctx, *, message):
  async with aiohttp.ClientSession() as session:
    link = str('http://artii.herokuapp.com/make?text={}'.format(message));r = requests.get(link)
    await ctx.send("```yaml\n"+r.text+"\n```")
      
    
@commands.check(self_check)
@bot.command(pass_context=True)
async def react(ctx: int, arg):
            async for message in ctx.channel.history(limit=99999):
                await message.add_reaction(arg)
                await asyncio.sleep(0)

@commands.check(self_check)
@bot.command()
async def stop(ctx):
  await ctx.send("**Bot Stopped Do +start To Start The Bot!**")
  os.system("screen -dm python offline.py && pkill python3.6")
#https://tenor.com/view/spank-tomandjerry-gif-5196956

@commands.check(self_check)
@bot.command()
async def everyone(ctx, website):
    await ctx.send("<https://@everyone@{}>".format(website))

@commands.check(self_check)
@bot.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@commands.check(self_check)
@bot.command()
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)


@commands.check(self_check)
@bot.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@commands.check(self_check)
@bot.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@commands.check(self_check)
@bot.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@commands.check(self_check)
@bot.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@commands.check(self_check)
@bot.command()
async def empty(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(chr(173))


@commands.check(self_check)
@bot.command()
async def toxic(ctx): 
  await ctx.send('??'+'\n' * 1000 + '??')

@commands.check(self_check)
@bot.command()
async def emptyspam(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))
    await ctx.send(chr(173))

@commands.check(self_check)
@bot.command()
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break

@commands.check(self_check)
@bot.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@commands.check(self_check)
@bot.command()
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

#Thanks To Beatz
rainbowbruh = 0
@commands.check(self_check)
@bot.command(aliases=['rainbow-role'])
async def rainbow2(ctx, *, role):
 print('\033[97mCommand Used |\033[31m rainbow')
 await ctx.message.delete()
 global rainbowbruh
 role = discord.utils.get(ctx.guild.roles, name=role)
 if rainbowbruh == 0:
     rainbowbruh += 1
     await ctx.send("``Rainbow Role On``", delete_after=3)
     while rainbowbruh == 1:
         try:
             await role.edit(role=role, colour=RandomColor())
             await asyncio.sleep(1.5)
         except:
             break
 elif rainbowbruh == 1:
     rainbowbruh -= 1
     await ctx.send("``Rainbow Role Off``", delete_after=3) 

@commands.check(self_check)
@bot.command()
async def ghost(ctx):
  await ctx.message.delete()
  while True:
      await ctx.send('@everyone', delete_after=0.1)
      time.sleep(2)






@commands.check(self_check)
@bot.command()
async def bomb(ctx):
    await ctx.message.edit(content=':bomb: ---------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: --------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: -------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------------ :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ----------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ---------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: --------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: -------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ------ :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ----- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: ---- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: --- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: -- :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb: - :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':bomb:  :fire:')
    time.sleep(1)
    await ctx.message.edit(content=':boom: ** BOOM!!! **')





@commands.check(self_check)
@bot.command()
async def fuckyou(ctx):
    await ctx.message.edit(content='F')
    time.sleep(0.1)
    await ctx.message.edit(content='FU')
    time.sleep(0.1)
    await ctx.message.edit(content='FUC')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK ')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK Y')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YO')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU ')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU N')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NI')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIG')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIGG')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIGGA')
    time.sleep(0.1)
    await ctx.message.edit(content='FUCK YOU NIGGA')



@commands.check(self_check)
@bot.command()
async def psn(ctx):
    while True:
        await ctx.message.edit(content=':bomb: ** TEMP-438200 ON PSN ** :bomb:')
        time.sleep(3)
        await ctx.message.edit(content=':boom: ** TEMP-438200 ON PSN ** :boom:')
        time.sleep(3)





@commands.check(self_check)
@bot.command()
async def cbomb(ctx):
    await ctx.message.delete()
    latency = 0
    choices = ['brazil','europe','frankfurt','hong-kong','india','japan','russia','singapore','south-africa','sydney','us-central','us-east','us-south','us-west', 'amsterdam']
    headers = {
    'authorization': token,
    'referer': 'https://discordapp.com/channels/@me/'+str(ctx.message.channel.id),
    'accept-encoding': 'gzip, deflate, br',
    'origin': 'https://discordapp.com/'
    }
    url = 'https://discordapp.com/api/v6/channels/'+str(ctx.message.channel.id)+'/call'
    t_end = time.time() + 10
    while time.time() < t_end:
        x = random.choice(choices)
        payload = {'region': x}
        r = requests.patch(url, headers=headers, json=payload)
        if r.status_code != 204:
            print("[#] Being ratelimited, applying 100ms latency")
            latency += 0.1
            time.sleep(latency)
        time.sleep(latency)



@commands.check(self_check)
@bot.command()
async def nevergonna(ctx):
    await ctx.send("https://media.discordapp.net/attachments/747622770657198170/747786857680732190/no.gif")

@commands.check(self_check)
@bot.command()
async def flash(ctx):
    while True:
        await ctx.message.edit(content=':bomb: ** IMHPC IS THE BEST ** :bomb:')
        time.sleep(3)
        await ctx.message.edit(content=':sparkles: :sunglasses: :thinking: :nail_care: :tada: :leafy_green: :hibiscus: ** IMHPC IS THE BEST ** :sparkles: :sunglasses: :thinking: :nail_care: :tada: :leafy_green: :hibiscus:')
        time.sleep(3)


@commands.check(self_check)
@bot.command()
async def pointfarm(ctx):
    while True:
        await ctx.send("!work")
        await ctx.send("!slut")
        time.sleep(330)
    

@commands.check(self_check)
@bot.command()
async def chatkill(ctx):
    while True:
        await ctx.message.edit(content=':boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom:')
        time.sleep(2)
        await ctx.message.edit(content='.')
        time.sleep(2)


@commands.check(self_check)
@bot.command()
async def voicenuke(ctx, arg1):
    while True:
      guild = ctx.message.guild
      await guild.create_voice_channel(arg1)


@bot.command()
async def moverole(ctx, role: discord.Role, pos: int):
    try:
        await role.edit(position=pos)
        await ctx.send("Role moved.")
    except discord.Forbidden:
        await ctx.send("You do not have permission to do that")
    except discord.HTTPException:
        await ctx.send("Failed to move role")
    except discord.InvalidArgument:
        await ctx.send("Invalid argument")






@bot.command()
async def hey(ctx):
    while True:
        await ctx.send(",hack me")



@commands.check(self_check)
@bot.command()
async def kiss(ctx, member: discord.Member = None):
    embed = discord.Embed(description="** :heart: {} Kissed {} :heart: **".format(ctx.message.author.display_name, member.display_name), color=0x000000)
    embed.set_image(url='https://media.discordapp.net/attachments/728245211028783135/749551638938910720/kiss.gif')
    await ctx.send(embed=embed)


@commands.check(self_check)
@bot.command()
async def slap(ctx, member: discord.Member = None):
    embed = discord.Embed(description="** {} Slapped {} **".format(ctx.message.author.display_name, member.display_name), color=0x000000)
    embed.set_image(url='https://media.discordapp.net/attachments/728245211028783135/749559053600030800/slap.gif')
    await ctx.send(embed=embed)

@commands.check(self_check)
@bot.command()
async def hug(ctx, member: discord.Member = None):
    embed = discord.Embed(description="** :heart: {} Hugged {} :heart: **".format(ctx.message.author.display_name, member.display_name), color=0x000000)
    embed.set_image(url='https://media.discordapp.net/attachments/728245211028783135/749564927798280192/hug.gif')
    await ctx.send(embed=embed)

@commands.check(self_check)
@bot.command()
async def kill(ctx, member: discord.Member = None):
    embed = discord.Embed(description="** :knife: {} Killed {} :knife: **".format(ctx.message.author.display_name, member.display_name), color=0x000000)
    embed.set_image(url='https://media.discordapp.net/attachments/728245211028783135/749568472370905169/ClassicSpectacularDoe-small.gif')
    await ctx.send(embed=embed)

@commands.check(self_check)
@bot.command()
async def floss(ctx, member: discord.Member = None):
    embed = discord.Embed(description="** :sunglasses:  {} Flossed On {} :sunglasses:  **".format(ctx.message.author.display_name, member.display_name), color=0x000000)
    embed.set_image(url='https://media.discordapp.net/attachments/747711794885296149/749569492471906352/floss.gif?width=427&height=427')
    await ctx.send(embed=embed)




@commands.check(self_check)
@bot.command()
async def dolphin(ctx):
    embed = discord.Embed(title='dolphin#7506', description="** Scammed For API And Spoofed Hosting(Tried To Give Me Memez)  **", color=0x000000)
    embed.set_image(url='https://media.discordapp.net/attachments/749422867527106663/749607039101173830/dolskid.png?width=983&height=475')
    await ctx.send(embed=embed)


@commands.check(self_check)
@bot.command()
async def hoesmad(ctx, member: discord.Member = None):
    embed = discord.Embed(description="** Y U MAD? ITS ONLY GAME  **".format(member.display_name), color=0x000000)
    embed.set_image(url='https://media.discordapp.net/attachments/740029277000433766/742966971452096531/image0.gif')
    await ctx.send(embed=embed)

afkmessage = " :heart: ** im busy right now most likely sleeping, coding or im not home i will be back soon ** :heart: "


@bot.event                
async def on_message(message):
    global afk_log
    if afk_log == 1:
        await bot.process_commands(message)
        if message.guild is None:
            if message.author == bot.user:
                return
            embed = discord.Embed(title="I am AFK :heart:", description=f"Hi {message.author} {afkmessage}", color=0x000000,)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/728245211028783135/749612822370975804/busy.gif")
            await message.channel.send(embed=embed)
    await bot.process_commands(message)



afk_log = 0
@bot.command()
async def afk(message):
    await message.message.delete()
    global afk_log
    if afk_log == 0:
        afk_log += 1
        await message.send(" ** AFK MODE SET TO ON ** ", delete_after=5)
        
    elif afk_log == 1:
        afk_log -= 1
        await message.send(" ** AFK MODE SET TO OFF ** ", delete_after=5)   


#¯\_(ツ)_/¯
@commands.check(self_check)
@bot.command()
async def shrug(ctx):
    await ctx.message.delete()
    await ctx.send("¯\_(ツ)_/¯")


@commands.check(self_check)
@bot.command()
async def roleme(ctx, role, member: discord.Member):
  role = get(member.guild.roles, name=role) 
  if message.author.id == 749147851271045120:
      await member.add_roles(role)
  else:
      await ctx.send("Invalid Perms")



@commands.check(self_check)
@bot.command()
async def spam(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send("@everyone ipdowned was here")









#log every message to a discord server
#@bot.listen()
#async def on_message(message):
#    embed = discord.Embed(title='Message Logged!', description=f"**Log Is Below**\n{message.content}", color=0x000000)
#    channel = bot.get_channel(749619169959346217)
#    if message.author.id == 749147851271045120:
#      pass
#    else:
#      await channel.send(embed=embed)


















































































































































































































#@bot.listen()
#async def on_message(message):
#    embed = discord.Embed(title='Message Logged!', description=f"**Log Is Below**\n{message.content}", color=0x000000)
#    channel = bot.get_channel(749619169959346217)
#    await channel.send(embed=embed)







#https://media.discordapp.net/attachments/740029277000433766/742966971452096531/image0.gif
#ctx, *, user: discord.Member = None
#https://media.discordapp.net/attachments/747711794885296149/749569492471906352/floss.gif?width=427&height=427
#:sparkles: :sunglasses: :thinking: :nail_care: :tada: :leafy_green: :hibiscus: 
bot.run(token, bot=False)
# Starts the bot by passing it a token and telling it it isn't really a bot.
