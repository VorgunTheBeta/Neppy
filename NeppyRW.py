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
game = discord.Game('placeholder')
dbclient = dropbox.Dropbox('hLV5aeCyroAAAAAAAAAAHxfTb412mE0N_1rypf0CorlfWy6NXAtJvW3axbh1dq3Z')
bot = commands.Bot(command_prefix='?', description=description, formatter=formatter)

async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            await ctx.send(page)
    else:
         pages = bot.formatter.format_help_for(ctx, ctx.command)
         for page in pages:
            await ctx.send(page)
def owner():
    def predicate(ctx):
        return ctx.author.id == 127188004216373248
    return commands.check(predicate)

def webDND():
    def predicate(ctx):
        return ctx.guild.id== 154009582748827648
    return commands.check(predicate)

def notWeb():
    def predicate(ctx):
        return ctx.guild.id!= 154009582748827648
    return commands.check(predicate)

def blancship():
    def predicate(ctx):
        return ctx.guild.id == 199045411640573954
    return commands.check(predicate)

@bot.command()
async def hello(ctx):
    result = "Hello there~"
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send(result)

@bot.command()
async def sleep(ctx):

    member = ctx.author
    trusted = [127188004216373248, 126899976042184705, 12701025934610944, 14672084824861696]
    if member.id in trusted:
        await ctx.trigger_typing()
        await asyncio.sleep(2)
        await ctx.send( "What, you don't like me?")
        user = discord.User()
        user.id = 127188004216373248
        await user.create_dm()
        await ctx.send("I'm down")
        print('message recieved')
        bot.close()
        exit()
    else:
        await ctx.trigger_typing()
        await asyncio.sleep(2)
        await ctx.send("http://www.ozsticker.com/ozebayimages/620_dave_product.jpg")

@bot.command()
@owner()
async def status(ctx):
        msg = ctx.message.content
        game.name = msg.replace("?status",'')
        await bot.change_presence(game=game)

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
    user = ctx.guild.get_member_named("VorgunTheBeta")
    if user.nick == None:
        name = user.name
    else:
        name = user.nick
    ctx.typing()
    msg = Text("help.txt")
    await asyncio.sleep(2)
    await ctx.send( msg.format(name))

@bot.group()
@webDND()
async def rec(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.trigger_typing()
        await asyncio.sleep(2)
        await ctx.send('What are you trying to do?')

@rec.command()
async def browser(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( "The moderators of this immaculate server highly recommend using Vivaldi~ \nhttps://vivaldi.com/?lang=en")

@rec.command()
async def txt_editor(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send("The moderators of this immaculate server highly recommend using Brackets~ \nhttp://brackets.io/")

@rec.command()
async def dev_site(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( "The moderators of this immaculate server highly recommend using Mozilla Developer Network for all your coding help needs~ \nhttps://developer.mozilla.org/en-US/")

@bot.command()
@webDND()
async def reverb(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send("Ravenslofty recommends using this plugin for all your reverb needs~ \nhttp://magnus.smartelectronix.com/#Ambience")

@bot.command()
@webDND()
async def plug(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( Text("plug.txt"))

@bot.command()
@webDND()
async def shit(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( Text("shit.txt"))

@bot.command()
@owner()
async def nick(ctx, nickname :str):
    member = ctx.me
    await member.edit(nick=nickname)
    prtmsg = "Nickname changed to {0} on {1.name}"
    print(prtmsg.format(nickname, ctx.guild))

@bot.command()
async def join_server(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( "So you want me in your server?~~~ Just use this link: https://goo.gl/NPrZRF")

@bot.command(aliases=['sauce'])
async def source(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( "So you want to see whats behind me huh~ https://github.com/VorgunTheBeta/Neppy")

@bot.command()
async def notice(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( Text("notice.txt"))

@bot.command(aliases=['Google'])
async def google(ctx, search: str):
    src = search.replace(" ", '+').replace("<", '%3C').replace(">", '%3E')
    send = 'https://google.com/search?q=' + src
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send(send)

@bot.command()
async def im_feeling_lucky(ctx, search: str):
    src = search.replace(" ", '').replace("<", '%3C').replace(">", '%3E')
    send = 'https://google.com/search?btnI=&q=' + src
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send(send)

@bot.command()
async def image(ctx, search: str):
    img = search.replace(" ", '+')
    send= "https://google.com/search?tbm=isch&q=" + img
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( send)


@bot.command()
async def wiki(ctx, search: str):
    src = search.replace(" ",'_')
    send = "https://en.wikipedia.org/wiki/"+src
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send(send)

@bot.command()
async def make_note(ctx, note: str):
    userid= ctx.author.id
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

@bot.command()
async def notes(ctx):
     userid= ctx.author.id
     fname = userid + ".txt"
     result = dbclient.files_search('', fname, start=0,max_results=100)
     if len(result.matches) == 0:
        await ctx.send( "I'm so sorry, but I can't seem to find any notes for you~~~")
     else:
        dbclient.files_download_to_file(fname, '/'+fname)
        print("file downloaded")
        g = open(fname)
        mes = g.read()
        await ctx.send( "Your saved notes are: "+mes)

@bot.command()
async def support():
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send("You want to help out with finding a host for my sister? Thanks!~~~ https://www.patreon.com/VorgunTheBeta?ty=h")

#@bot.command()
#async def supporters():
#    highrank = "Lance, Noire.io"
#    lowrank = "none"
#    await ctx.trigger_typing()
#    await asyncio.sleep(2)
#    await ctx.send("Here are the awesome people who support me: (High Ranks - $5 pledge) " + highrank + ", (Low Ranks - $1 pledge) " + lowrank)


@bot.command(aliases=['Blanc','White_Heart'])
async def blanc(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("blanc.txt"))

@bot.command(aliases=['Nepgear','Purple_Sister'])
async def nepgear(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("nepgear.txt"))

@bot.command(aliases=['ploot','Plutia','Iris_Heart'])
async def plutia(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("plutia.txt"))

@bot.command(aliases=['Noire', 'Black_Heart'])
async def noire(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("noire.txt"))

@bot.command(aliases=['Vert','Green_Heart'])
async def vert(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("vert.txt"))

@bot.command(aliases=['ram_and_rom','Rom_and_Ram', 'Ram_and_Rom', 'White_Sisters'])
async def rom_and_ram(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("romandram.txt"))

@bot.command(aliases=['Uni','Black_Sister'])
async def uni(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("uni.txt"))

@bot.command()
async def nepger(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( "http://i.imgur.com/XHkYq9d.png")

@bot.command(aliases=['histy','Histoire','Histy'])
async def histoire(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("histoire.txt"))

@bot.command()
async def crying_nepgear(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( "http://i.imgur.com/mvxtHrr.png")

@bot.command(aliases=['iffy','Iffy'])
async def IF(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("IF.txt"))

@bot.command(aliases=['Compa'])
async def compa(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("compa.txt"))

@bot.command(aliases=['Neptune','Purple_Heart', 'nep'])
async def neptune(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("neptune.txt"))

@bot.command(aliases=['Marvy'])
async def marvy(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("marvy.txt"))

@bot.command()
async def wallpaper(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("wallpapers.txt"))

@bot.command(help='Hug someone')
async def hug(ctx, name: str):
    hugee = name
    user = utils.find(lambda m: hugee.lower() in m.display_name.lower(), ctx.guild.members)
    msg = "*hugs {0.mention}*"
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( msg.format(user))

@bot.command()
@owner()
async def change_pic(image: str):
    await ChangePic(image)

@bot.command()
async def request(ctx,req: str):
    requestee = ctx.author
    server = ctx.guild
    await MakeNepRequest(req, requestee, server)

@bot.command()
async def RNG(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send("https://cdn.discordapp.com/attachments/126696039733264384/176351354044940289/RNGesus.gif")

@bot.command()
@webDND()
async def lol(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send("http://ta-sa.org/data/images/laughing_man_big_2.png")

@bot.command()
@webDND()
async def limewire(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send("https://www.youtube.com/watch?v=SAp0xO-LwFs")

@bot.command()
async def pudding(ctx):
    msg = RandomImage("pudding.txt") + " \nPUDDING~"
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( msg)

@bot.command()
async def smug(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("smug.txt"))

@bot.command()
async def shock(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send("https://cdn.discordapp.com/attachments/156523621240537088/176951338356178945/jeepers.gif")

@bot.command()
async def wat(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send("https://cdn.discordapp.com/attachments/156523621240537088/180092100199579650/1457714637653.gif WAT")

@bot.command(help="The story behind my creation")
async def story(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( Text("story.txt"))

@bot.command(aliases=['?'])
async def huh(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(2)
    await ctx.send( RandomImage("what.txt"))

@bot.command(hidden=True)
@blancship()
async def nsfw(ctx):
    member = ctx.author
    role = discord.Object(id=199082489598181377)
    await member.add_roles(role)


@bot.event
async def on_message(message):
        if bot.user.mentioned_in(message):
            if message.author.id == 192351191642931200:
                await ctx.trigger_typing()
                await asyncio.sleep(2)
                await ctx.send("Well aren't you a little tsundere?~")
            else:
                await ctx.trigger_typing()
                await asyncio.sleep(2)
                await ctx.send("Yes?~~~")

        elif message.content == "GO THE FUCK TO SLEEP":
            await ctx.trigger_typing()
            await asyncio.sleep(2)
            await ctx.send(RandomImage("GTFTS.txt"))
        elif message.content == "AAA":
            await ctx.trigger_typing()
            await asyncio.sleep(2)
            await ctx.send( "MOU")
        elif "The More You Know" in message.content:
            if message.author.id == bot.user.id:
                return
            else:
                await ctx.trigger_typing()
                await asyncio.sleep(2)
                await ctx.send("http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")
        elif "the more you know" in message.content:
            if message.author.id == bot.user.id:
                return
            else:
                await ctx.trigger_typing()
                await asyncio.sleep(2)
                await ctx.send("http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")
        elif "neppy!" in message.content:
            msg = "{0.mention}!~"
            await ctx.trigger_typing()
            await asyncio.sleep(2)
            await ctx.send(msg.format(message.author))
        elif "good nep" in message.content:
            msg = "Good nep {0.mention}, sweet dreams~~~"
            await ctx.trigger_typing()
            await asyncio.sleep(2)
            await ctx.send(msg.format(message.author))


        if message.content.startswith("?"):
            if " " in message.content and "?rec" not in message.content and "make_note" not in message.content and "google" not in message.content and "image" not in message.content and "status" not in message.content and "nick" not in message.content and "request" not in message.content and "change" not in message.content and "hug" not in message.content:
                message.content = message.content.replace(" ","_")
# end of text recog commands
        await bot.process_commands(message)



@bot.event
async def on_member_join(member):
        if member.guild.id=='154009582748827648':
                channel = discord.Object(id=160670845675634688)
                message = "{0.name} has joined the server~"
                await channel.send(message.format(member))
                user = discord.User()
                user.id = member.id
                await user.send(Text("greeting.txt").format(member))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    print("Number of connected guilds:")
    print(len(bot.guilds))
    user = bot.get_user(127188004216373248)
    await user.send("I'm up")
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
             await bot.user.edit(avatar=await resp.read())
             print("Profile pic changed")

async def MakeNepRequest(msg,requestee,source):
    pm = "{0} requested on {1} "+msg
    user = discord.User()
    user.id = 127188004216373248
    await user.send(pm.format(requestee, source.name))

#end of custom functions
bot.run(os.environ['API_KEY'])
