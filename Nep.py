import discord
from discord.ext import commands
import asyncio
import random
import os.path
import datetime
import time
import aiohttp
import dropbox
from urllib import request
from array import array

description = "A bot created by VorgunTheBeta"
utils = discord.utils
bot = commands.Bot(command_prefix='?', description=description)
game = discord.Game()
dbclient = dropbox.Dropbox('hLV5aeCyroAAAAAAAAAAHxfTb412mE0N_1rypf0CorlfWy6NXAtJvW3axbh1dq3Z')
def owner():
    def predicate(ctx):
        return ctx.message.author.id == '127188004216373248'
    return commands.check(predicate)

def webDND():
    def predicate(ctx):
        return ctx.message.server.id=='154009582748827648'
    return commands.check(predicate)

def notWebDND():
    def predicate(ctx):
        return ctx.message.server.id!='154009582748827648'
    return commands.check(predicate)

@bot.command()
async def hello():
    result = "Hello there~"
    await bot.type
    await asyncio.sleep(2)
    await bot.say(result)

@bot.command(pass_contect=True)
async def sleep(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    if member.id == '127188004216373248' or member.id == '126899976042184705' or member.id == '127010252934610944' or member.id == '146720848424861696':
        await bot.type()
        await asyncio.sleep(2)
        await bot.say( "What, you don't like me?")
        user = discord.User()
        user.id = 127188004216373248
        await bot.send_message(user, "I'm down")
        print('message recieved')
        bot.close()
        exit()
    else:
        await bot.type()
        await asyncio.sleep(2)
        await bot.say("http://www.ozsticker.com/ozebayimages/620_dave_product.jpg")

@bot.command()
@owner()
async def status(msg: str):
        game.name = msg
        await bot.change_status(game)

@bot.command(pass_context=True)
@webDND()
async def info(ctx):
    user = ctx.message.server.get_member_named("VorgunTheBeta#9662")
    if user.nick == None:
        name = user.name
    else:
        name = user.nick
    await bot.type
    msg = Text("info.txt")
    await asyncio.sleep(2)
    await bot.say(msg.format(name))

@bot.command(pass_context=True)
@notWebDND()
async def help(ctx):
    user = ctx.message.server.get_member_named("VorgunTheBeta#9662")
    if user.nick == None:
        name = user.name
    else:
        name = user.nick
    await bot.type
    msg = Text("help.txt")
    await asyncio.sleep(2)
    await bot.say( msg.format(name))

@bot.group(pass_context=True)
@webDND()
async def rec(ctx):
    if ctx.invoked_subcommand is None:
        await bot.type()
        await asyncio.sleep(2)
        await bot.say('What are you trying to do?')

@rec.command()
async def browser():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "The moderators of this immaculate server highly recommend using Vivaldi~ \nhttps://vivaldi.com/?lang=en")

@rec.command()
async def txt_editor():
    await bot.type
    await asyncio.sleep(2)
    await bot.say("The moderators of this immaculate server highly recommend using Brackets~ \nhttp://brackets.io/")

@rec.command()
async def dev_site():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "The moderators of this immaculate server highly recommend using Mozilla Developer Network for all your coding help needs~ \nhttps://developer.mozilla.org/en-US/")

@bot.command()
@webDND()
async def reverb():
    await bot.type
    await asyncio.sleep(2)
    await bot.say("Ravenslofty recommends using this plugin for all your reverb needs~ \nhttp://magnus.smartelectronix.com/#Ambience")

@bot.command()
@webDND()
async def plug():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( Text("plug.txt"))

@bot.command()
@webDND()
async def shit():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( Text("shit.txt"))

@bot.command()
@owner()
async def status(nickname :str):
    await bot.change_nickname(message.server.me, nickname)
    prtmsg = "Nickname changed to {0} on {1.name}"
    print(prtmsg.format(nickname, message.server))

@bot.command()
async def join_server():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "So you want me in your server?~~~ Just use this link: https://goo.gl/NPrZRF")

@bot.command(aliases=['source','sauce'])
async def source():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "So you want to see whats behind me huh~ https://github.com/VorgunTheBeta/Neppy")

@bot.command()
async def notice():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( Text("notice.txt"))

@bot.command(aliases=['google','Google'])
async def google(search: str):
    src = search.replace(" ", '+').replace("<", '%3C').replace(">", '%3E')
    send = 'https://google.com/search?q=' + src
    await bot.type
    await asyncio.sleep(2)
    await bot.say( send)

@bot.command()
async def im_feeling_lucky(search: str):
    src = search.replace(" ", '').replace("<", '%3C').replace(">", '%3E')
    send = 'https://google.com/search?btnI=&q=' + src
    await bot.type
    await asyncio.sleep(2)
    await bot.say( send)

@bot.command()
async def image(search: str):
    img = search.replace(" ", '+')
    send= "https://google.com/search?tbm=isch&q=" + img
    await bot.type
    await asyncio.sleep(2)
    await bot.say( send)

@bot.command(pass_context=True)
async def make_note(note: str):
    userid= ctx.message.author.id
    fname = userid+'.txt'
    f = open(fname, 'a')
    f.write(note+"\n")
    result = dbclient.files_search('', userid, start=0,max_results=100)
    f.close()
    if result.matches:
      dbclient.files_upload(msg, "/"+fname, dropbox.files.WriteMode.add, client_modified=datetime.datetime.now(),mute=True)
    else:
      g = open(fname)
      mes = g.read()
      dbclient.files_upload(mes, "/"+fname, dropbox.files.WriteMode.overwrite, client_modified=datetime.datetime.now(),mute=True)
    print('Message written')

@bot.command(pass_context=True)
async def notes():
     userid= ctx.message.author.id
     fname = userid + ".txt"
     result = dbclient.files_search('', userid, start=0,max_results=100)
     if result.matches[0] == '':
       await bot.say( "I'm so sorry, but I can't seem to find any notes for you~~~")
     else:
       dbclient.files_download_to_file('/'+fname,'/'+fname)
     g = open(fname)
     mes = g.read()
     await bot.say( "Your saved notes are: "+mes)

@bot.command()
async def support():
    await bot.type
    await asyncio.sleep(2)
    await bot.say(
                           "You want to help out with finding a host for my sister? Thanks!~~~ https://www.patreon.com/VorgunTheBeta?ty=h")
@bot.command()
async def supporters():
    highrank = "Lance, Noire.io"
    lowrank = "none"
    await bot.type
    await asyncio.sleep(2)
    await bot.say("Here are the awesome people who support me: (High Ranks - $5 pledge) " + highrank + ", (Low Ranks - $1 pledge) " + lowrank)

@bot.command()
async def doof_doof():
    await bot.type
    await asyncio.sleep(2)
    await bot.say("!p https://www.youtube.com/playlist?list=PL1idN54yDQTQTHXHEydxzmTVcYffEtBiH")

@bot.command()
async def dtrip():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "!p https://www.youtube.com/watch?v=LHOEUrFOX4Y")

@bot.command()
async def mpm():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "!p https://www.youtube.com/watch?v=bGbdrLQWZpo")

@bot.command()
async def sagashite():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say("!p https://www.youtube.com/watch?v=I7TUNfNGTzY")

@bot.command(aliases=['blanc','Blanc','White Heart'])
async def blanc():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("blanc.txt"))

@bot.command(aliases=['nepgear','Nepgear','Purple Sister'])
async def nepgear():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("nepgear.txt"))

@bot.command(aliases=['plutia','ploot','Plutia','Iris Heart'])
async def plutia():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("plutia.txt"))

@bot.command(aliases=['noire','Noire', 'Bleack Heart'])
async def noire():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("noire.txt"))

@bot.command(aliases=['vert','Vert','Green Heart'])
async def vert():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("vert.txt"))

@bot.command(aliases=['rom and ram','ram and rom','Rom and Ram', 'Ram and Rom', 'White Sisters'])
async def rom_and_ram():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("romandram.txt"))

@bot.command(aliases=['uni','Uni','Black Sister'])
async def uni():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("uni.txt"))

@bot.command()
async def nepger():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "http://i.imgur.com/XHkYq9d.png")

@bot.command(aliases=['histoire','histy','Histoire','Histy'])
async def histoire():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("histoire.txt"))

@bot.command()
async def crying_nepgear():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "http://i.imgur.com/mvxtHrr.png")

@bot.command(aliases=['if','IF','iffy','IFfy'])
async def IF():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("IF.txt"))

@bot.command(aliases=['compa', 'Compa'])
async def compa():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("compa.txt"))

@bot.command(aliases=['neptune','Neptune','Purple Heart', 'nep'])
async def neptune():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("neptune.txt"))

@bot.command(aliases=['marvy','Marvy'])
async def marvy():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("marvy.txt"))

@bot.command()
async def wallpaper():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("wallpapers.txt"))

@bot.command()
async def hug(member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    hugee = member
    user = utils.find(lambda m: hugee.lower() in m.display_name.lower(), message.server.members)
    msg = "*hugs {0.mention}*"
    await bot.type
    await asyncio.sleep(2)
    await bot.say( msg.format(user))

@bot.command()
@owner()
async def change_pic(image: str):
    await ChangePic(image)

@bot.command()
async def request(req: str):
    requestee = message.author
    server = message.server
    await MakeNepRequest(req, requestee, server)

@bot.command()
async def RNG():
    await bot.type
    await asyncio.sleep(2)
    await bot.say(
                           "https://cdn.discordapp.com/attachments/126696039733264384/176351354044940289/RNGesus.gif")

@bot.command()
@webDND()
async def lol():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "http://ta-sa.org/data/images/laughing_man_big_2.png")

@bot.command()
@webDND()
async def limewire():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( "https://www.youtube.com/watch?v=SAp0xO-LwFs")

@bot.command()
async def pudding():
    msg = RandomImage("pudding.txt") + " \nPUDDING~"
    await bot.type
    await asyncio.sleep(2)
    await bot.say( msg)

@bot.command()
async def smug():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("smug.txt"))

@bot.command()
async def shock():
    await bot.type
    await asyncio.sleep(2)
    await bot.say(
                           "https://cdn.discordapp.com/attachments/156523621240537088/176951338356178945/jeepers.gif")

@bot.command()
async def wat():
    await bot.type
    await asyncio.sleep(2)
    await bot.say(
                           "https://cdn.discordapp.com/attachments/156523621240537088/180092100199579650/1457714637653.gif WAT")

@bot.command()
async def story():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( Text("story.txt"))

@bot.command(aliases=['?'])
async def huh():
    await bot.type
    await asyncio.sleep(2)
    await bot.say( RandomImage("what.txt"))
async def on_message(message):

        if bot.user.mentioned_in(message):
            if message.author.id == '192351191642931200':
                await bot.type
                await asyncio.sleep(2)
                await bot.say( "Well aren't you a little tsundere?~")
            else:
                await bot.type
                await asyncio.sleep(2)
                await bot.say( "Yes?~~~")

        elif message.content == "GO THE FUCK TO SLEEP":
            await bot.type
            await asyncio.sleep(2)
            await bot.say( RandomImage("GTFTS.txt"))
        elif message.content == "AAA":
            await bot.type
            await asyncio.sleep(2)
            await bot.say( "MOU")
        elif "The More You Know" in message.content:
            if message.author.id == bot.user.id:
                return
            else:
                await bot.type
                await asyncio.sleep(2)
                await bot.say("http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")
        elif "the more you know" in message.content:
            if message.author.id == bot.user.id:
                return
            else:
                await bot.type
                await asyncio.sleep(2)
                await bot.say("http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")
        elif "neppy!" in message.content:
            msg = "{0.mention}!~"
            await bot.type
            await asyncio.sleep(2)
            await bot.say( msg.format(message.author))
        elif "good nep" in message.content:
            msg = "Good nep {0.mention}, sweet dreams~~~"
            await bot.type
            await asyncio.sleep(2)
            await bot.say( msg.format(message.author))
        elif message.content.startswith("FUCKING"):
            await bot.type
            await asyncio.sleep(2)
            await
            bot.say( "It sucks, I know.")
        elif message.content.upper() == "JUST":
            await bot.type
            await asyncio.sleep(2)
            await bot.say(random.choice(
                ["DO IT http://i.imgur.com/Vav0hU0.jpg", "FUCK MY SHIT UP http://i.imgur.com/ygbXO2F.gif"]))


# end of text recog commands

@bot.event
async def on_member_join(member):
        if member.server.id=='154009582748827648':
                channel = discord.Object(id='155225555598442496')
                message = "{0.name} has joined the server~"
                await bot.send_message(channel, message.format(member))
                user = discord.User()
                user.id = member.id
                await bot.send_message(user, Text("greeting.txt").format(member))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    print("Connected Servers:")
    for s in bot.servers:
        print(s.name)
    user = discord.User()
    user.id = 127188004216373248
    await bot.send_message(user, "I'm up")
#start of custom fucntions
def FileToArray(filename):
    fname = "Text Stuff/"+filename
    b = open(fname)
    pictures = b.read().split('\n')
    b.close()
    return pictures

def Text(filename):
    fname = "Text Stuff/"+filename
    f = open(fname)
    notice = f.read()
    f.close()
    return notice

def RandomImage(filename):
    pics = FileToArray(filename)
    image = random.choice(pics)
    return image

async def ChangePic(image):
    print(image)
    with aiohttp.ClientSession() as session:
        async with session.get(image) as resp:
             await bot.edit_profile(avatar=await resp.read())
             print("Profile pic changed")

async def MakeNepRequest(msg,requestee,source):
    pm = "{0} requested on {1} "+msg
    user = discord.User()
    user.id = 127188004216373248
    await bot.send_message(user, pm.format(requestee, source.name))

#end of custom functions
bot.run(os.environ['API_KEY'])


