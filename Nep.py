import discord
from discord.ext import commands
import asyncio
import random
import os.path
import datetime
import time
import aiohttp
import dropbox
import dropbox.files
from urllib import request
from array import array

description = "A bot created by VorgunTheBeta"
utils = discord.utils
formatter = commands.HelpFormatter(show_check_failure=False)
game = discord.Game()
dbclient = dropbox.Dropbox('hLV5aeCyroAAAAAAAAAAHxfTb412mE0N_1rypf0CorlfWy6NXAtJvW3axbh1dq3Z')
bot = commands.Bot(command_prefix='?', description=description, formatter=formatter)

async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            await bot.send_message(ctx.message.channel, page)
    else:
         pages = bot.formatter.format_help_for(ctx, ctx.command)
         for page in pages:
            await bot.send_message(ctx.message.channel, page)
def owner():
    def predicate(ctx):
        return ctx.message.author.id == '127188004216373248'
    return commands.check(predicate)

def webDND():
    def predicate(ctx):
        return ctx.message.server.id=='154009582748827648'
    return commands.check(predicate)

def notWeb():
    def predicate(ctx):
        return ctx.message.server.id!='154009582748827648'
    return commands.check(predicate)
def blancship():
    def predicate(ctx):
        return ctx.message.server.id =='199045411640573954'
    return commands.check(predicate)

@bot.command(help="Says hello")
async def hello():
    result = "Hello there~"
    await bot.type()
    await asyncio.sleep(2)
    await bot.say(result)

@bot.command(pass_context=True)
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

@bot.command(pass_context=True,hidden=True)
@owner()
async def status(ctx):
        msg = ctx.message.content
        game.name = msg.replace("?status",'')
        await bot.change_status(game)

@bot.command()
async def info(ctx):
    await bot.type()
    embed = discord.Embed(colour=discord.Colour.magenta,url="https://github.com/VorgunTheBeta/Neppy",title="My Source")
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(name="Created by",value="VorgunTheBeta")
    embed.add_field(name="Made using",value="Python")
    embed.add_field(name="Server count",value=str(len(bot.servers)))
    embed.add_field(name="Command count",value=str(len(bot.commands)))
    about = ("I'm a simple bot made by VorgunTheBeta. I'm multi purpose.\r\n If you want to support Vorgun, go [here]({})").format("https://www.patreon.com/VorgunTheBeta?ty=h")
    embed.add_field(name="About Me",value=about,inline=False)

    await asyncio.sleep(2)
    await bot.say(embed)

@bot.command(pass_context=True)
@notWeb()
async def halp(ctx):
    user = ctx.message.server.get_member_named("VorgunTheBeta#9662")
    if user.nick == None:
        name = user.name
    else:
        name = user.nick
    await bot.type()
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
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "The moderators of this immaculate server highly recommend using Vivaldi~ \nhttps://vivaldi.com/?lang=en")

@rec.command()
async def txt_editor():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say("The moderators of this immaculate server highly recommend using Brackets~ \nhttp://brackets.io/")

@rec.command()
async def dev_site():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "The moderators of this immaculate server highly recommend using Mozilla Developer Network for all your coding help needs~ \nhttps://developer.mozilla.org/en-US/")

@bot.command()
@webDND()
async def reverb():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say("Ravenslofty recommends using this plugin for all your reverb needs~ \nhttp://magnus.smartelectronix.com/#Ambience")

@bot.command()
@webDND()
async def plug():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( Text("plug.txt"))

@bot.command()
@webDND()
async def shit():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( Text("shit.txt"))

@bot.command()
@owner()
async def nick(nickname :str):
    await bot.change_nickname(message.server.me, nickname)
    prtmsg = "Nickname changed to {0} on {1.name}"
    print(prtmsg.format(nickname, message.server))

@bot.command(hidden=True)
@owner()
async def join_server():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "So you want me in your server?~~~ Just use this link: https://goo.gl/NPrZRF")

@bot.command(aliases=['sauce'],help="Shows my source code")
async def source():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "So you want to see whats behind me huh~ https://github.com/VorgunTheBeta/Neppy")

@bot.command(help="Shows any relevant notices")
async def notice():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( Text("notice.txt"))

@bot.command(pass_context=True,aliases=['Google'],help="Google things")
async def google(ctx):
    src = ctx.message.content.replace("?google ",'').replace(" ", '+').replace("<", '%3C').replace(">", '%3E')
    send = 'https://google.com/search?q=' + src
    await bot.type()
    await asyncio.sleep(2)
    await bot.say(send)

@bot.command(help="Do you feel lucky?")
async def im_feeling_lucky(search: str):
    src = search.replace(" ", '').replace("<", '%3C').replace(">", '%3E')
    send = 'https://google.com/search?btnI=&q=' + src
    await bot.type()
    await asyncio.sleep(2)
    await bot.say(send)

@bot.command(help="Google image search things")
async def image(search: str):
    img = search.replace(" ", '+')
    send= "https://google.com/search?tbm=isch&q=" + img
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( send)


@bot.command(help="Look things up on Wikipedia")
async def wiki(search: str):
    src = search.replace(" ",'_')
    send = "https://en.wikipedia.org/wiki/"+src
    await bot.type()
    await asyncio.sleep(2)
    await bot.say(send)

@bot.command(pass_context=True,help="Make notes that will be saved")
async def make_note(ctx):
    userid= ctx.message.author.id
    note = ctx.message.content.replace("?make_note ",'')
    fname = userid+'.txt'
    f = open(fname, 'a')
    f.write(note+"\n")
    f.close()
    g = open(fname, 'rb')
    result = dbclient.files_search('', fname, start=0, max_results=100)
    if result.matches == None:
        dbclient.files_upload(g.read(), "/" + fname, dropbox.files.WriteMode.add,
                              client_modified=datetime.datetime.now(), mute=True)
    else:
        dbclient.files_upload(g.read(), "/" + fname, dropbox.files.WriteMode.overwrite,
                              client_modified=datetime.datetime.now(), mute=True)

    g.close()
    print('Message written')

@bot.command(pass_context=True,help="View any notes that have been saved")
async def notes(ctx):
     userid= ctx.message.author.id
     fname = userid + ".txt"
     result = dbclient.files_search('', fname, start=0,max_results=100)
     if len(result.matches) == 0:
        await bot.say( "I'm so sorry, but I can't seem to find any notes for you~~~")
     else:
        dbclient.files_download_to_file(fname, '/'+fname)
        print("file downloaded")
        g = open(fname)
        mes = g.read()
        await bot.say( "Your saved notes are: "+mes)

@bot.command(help="If you want to help out Vorgun")
async def support():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say(
                           "You want to help out with keeping me and my sister up and running? Thanks!~~~ https://www.patreon.com/VorgunTheBeta?ty=h")
    await bot.type()
    await asyncio.sleep(2)
    await bot.say("Or if you prefer to make a single donation, go here: https://paypal.me/vorgunthebeta")

@bot.command(help="Show current supporters of the patreon")
async def supporters():
    highrank = "Noire.io"
    lowrank = "Games Von Dudemeister, blan"
    await bot.type()
    await asyncio.sleep(2)
    await bot.say("Here are the awesome people who support me: (High Ranks - $5 pledge) " + highrank + ", (Low Ranks - $1 pledge) " + lowrank)

@bot.command(help="Adds a techno playlist to Nep-Tunes' queue")
async def doof_doof():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say("!p https://www.youtube.com/playlist?list=PL1idN54yDQTQTHXHEydxzmTVcYffEtBiH")

@bot.command(help="Adds Dimension Tripper to Nep-Tunes' queue")
async def dtrip():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "!p https://www.youtube.com/watch?v=LHOEUrFOX4Y")

@bot.command(help="Adds Miracle Portable Mission to Nep-Tunes' queue")
async def mpm():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "!p https://www.youtube.com/watch?v=bGbdrLQWZpo")

@bot.command(help="Adds Neptune Sagashite to Nep-Tunes' queue")
async def sagashite():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say("!p https://www.youtube.com/watch?v=I7TUNfNGTzY")

@bot.command(aliases=['Blanc','White_Heart'], help="Shows pictures of Blanc/White Heart")
async def blanc():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("blanc.txt"))

@bot.command(aliases=['Nepgear','Purple_Sister'], help="Shows pictures of Nepgear/Purple Sister")
async def nepgear():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("nepgear.txt"))

@bot.command(aliases=['ploot','Plutia','Iris_Heart'], help="Shows pictures of Plutia/Iris Heart")
async def plutia():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("plutia.txt"))

@bot.command(aliases=['Noire', 'Black_Heart'], help="Shows pictures of Noire/Black Heart")
async def noire():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("noire.txt"))

@bot.command(aliases=['Vert','Green_Heart'], help="Shows pictures of Vert/Green Heart")
async def vert():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("vert.txt"))

@bot.command(aliases=['ram_and_rom','Rom_and_Ram', 'Ram_and_Rom', 'White_Sisters'], help="Shows pictures of Rom and Ram/White Sisters")
async def rom_and_ram():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("romandram.txt"))

@bot.command(aliases=['Uni','Black_Sister'], help="Shows pictures of Uni/Black Sister")
async def uni():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("uni.txt"))

@bot.command()
async def nepger():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "http://i.imgur.com/XHkYq9d.png")

@bot.command(aliases=['histy','Histoire','Histy'], help="Shows pictures of Histoire")
async def histoire():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("histoire.txt"))

@bot.command()
async def crying_nepgear():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "http://i.imgur.com/mvxtHrr.png")

@bot.command(aliases=['iffy','Iffy'], help="Shows pictures of IF")
async def IF():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("IF.txt"))

@bot.command(aliases=['Compa'], help="Shows pictures of Compa")
async def compa():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("compa.txt"))

@bot.command(aliases=['Neptune','Purple_Heart', 'nep'], help="Shows pictures of Neptune/Purple Heart")
async def neptune():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("neptune.txt"))

@bot.command(aliases=['Marvy'], help="Shows pictures of MarvelousAQL")
async def marvy():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("marvy.txt"))

@bot.command(help="Sends a wallpaper")
async def wallpaper():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("wallpapers.txt"))

@bot.command(pass_context=True,help='Hug someone')
async def hug(ctx, name: str):
    hugee = name
    user = utils.find(lambda m: hugee.lower() in m.display_name.lower(), ctx.message.server.members)
    msg = "*hugs {0.mention}*"
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( msg.format(user))

@bot.command()
@owner()
async def change_pic(image: str):
    await ChangePic(image)

@bot.command(pass_context=True,help="For requesting the bot in your server, or a feature/command")
async def request(ctx,req: str):
    requestee = ctx.message.author
    server = ctx.message.server
    await MakeNepRequest(req, requestee, server)

@bot.command(help="Pray to the RNG gods")
async def RNG():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say(
                           "https://cdn.discordapp.com/attachments/126696039733264384/176351354044940289/RNGesus.gif")

@bot.command()
@webDND()
async def lol():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "http://ta-sa.org/data/images/laughing_man_big_2.png")

@bot.command(help="Posts an old programmer joke")
async def limewire():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( "https://www.youtube.com/watch?v=SAp0xO-LwFs")

@bot.command(help="PUDDING")
async def pudding():
    msg = RandomImage("pudding.txt") + " \nPUDDING~"
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( msg)

@bot.command(help="When in need of a smug face")
async def smug():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( RandomImage("smug.txt"))

@bot.command(help="When you need a shock gif")
async def shock():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say(
                           "https://cdn.discordapp.com/attachments/156523621240537088/176951338356178945/jeepers.gif")

@bot.command(help="For use when utterly confused")
async def wat():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say(
                           "https://cdn.discordapp.com/attachments/156523621240537088/180092100199579650/1457714637653.gif WAT")

@bot.command(help="To know the story behind me")
async def story():
    await bot.type()
    await asyncio.sleep(2)
    await bot.say( Text("story.txt"))

@bot.command(aliases=['?'])
async def huh():
    if(server.id==110373943822540800):
            return
    else:
     await bot.type()
     await asyncio.sleep(2)
     await bot.say( RandomImage("what.txt"))


@bot.command(hidden=True,pass_context=True)
@blancship()
async def nsfw(ctx):
    member = ctx.message.author
    role = discord.Object(id='199082489598181377')
    await bot.add_roles(member, role)


@bot.event
async def on_message(message):


        if message.content == "GO THE FUCK TO SLEEP":
            await bot.send_typing(message.channel)
            await asyncio.sleep(2)
            await bot.send_message(message.channel,RandomImage("GTFTS.txt"))
        elif message.content == "AAA":
            await bot.send_typing(message.channel)
            await asyncio.sleep(2)
            await bot.send_message(message.channel, "MOU")
        elif "The More You Know" in message.content:
            if message.author.id == bot.user.id:
                return
            else:
                await bot.send_typing(message.channel)
                await asyncio.sleep(2)
                await bot.send_message(message.channel,"http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")
        elif "the more you know" in message.content:
            if message.author.id == bot.user.id:
                return
            else:
                await bot.send_typing(message.channel)
                await asyncio.sleep(2)
                await bot.send_message(message.channel,"http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")
        elif "neppy!" in message.content:
            msg = "{0.mention}!~"
            await bot.send_typing(message.channel)
            await asyncio.sleep(2)
            await bot.send_message(message.channel,msg.format(message.author))
        elif "good nep" in message.content:
            msg = "Good nep {0.mention}, sweet dreams~~~"
            await bot.send_typing(message.channel)
            await asyncio.sleep(2)
            await bot.send_message(message.channel,msg.format(message.author))


        if message.content.startswith("?"):
            if " " in message.content and "?rec" not in message.content and "make_note" not in message.content and "google" not in message.content and "image" not in message.content and "status" not in message.content and "nick" not in message.content and "request" not in message.content and "change" not in message.content and "hug" not in message.content and "im_feeling_lucky" not in message.content and "wiki" not in message.content:
                message.content = message.content.replace(" ","_")
# end of text recog commands
        await bot.process_commands(message)



@bot.event
async def on_member_join(member):
        if member.server.id=='154009582748827648':
                channel = discord.Object(id='160670845675634688')
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
    print("I am currently in: "+str(count_iterable(bot.servers))+" servers.")
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

def count_iterable(i):
    return sum(1 for e in i)

#end of custom functions
bot.run(Text('token.txt'))
