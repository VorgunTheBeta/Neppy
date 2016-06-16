import discord
import asyncio
import random
import os.path
import datetime
import time
from array import array

description = "A bot created by VorgunTheBeta"
utils = discord.utils
bot = discord.Client()
game = discord.Game()

        

               
@bot.event
@asyncio.coroutine
def on_message(message):
        if message.content.startswith('?hello'):
                result = "Hello there~"
                yield from bot.send_message(message.channel, result)
        elif message.content.startswith('?sleep'):
                    if message.author.id == '127188004216373248' or message.author.id == '126899976042184705' or message.author.id == '127010252934610944' or message.author.id=='83677331951976448':
                        yield from bot.send_message(message.channel, "What, you don't like me?")
                        user = discord.User()
                        user.id = 127188004216373248
                        yield from bot.send_message(user, "Neppy is down")
                        print('message recieved')
                        bot.close()
                        exit()
                    else:
                          yield from bot.send_message(message.channel, "http://www.ozsticker.com/ozebayimages/620_dave_product.jpg")
        elif message.content.startswith('?status'):
                    if message.author.id == '127188004216373248' or message.author.id == '126899976042184705' or message.author.id == '127010252934610944' or message.author.id=='83677331951976448':
                        msg = message.content.replace('?status ', '')
                        game.name = msg
                        yield from bot.change_status(game)
                        return
                    else:
                        yield from bot.send_message(message.channel, "http://vignette1.wikia.nocookie.net/meme/images/8/8e/Nope.jpg")
        elif message.content.startswith('?rec browser') and message.author.server.id=='154009582748827648':
            yield from bot.send_message(message.channel, "The moderators of this immaculate server highly recommend using Vivaldi~ \nhttps://vivaldi.com/?lang=en")
        elif message.content.startswith('?rec txt editor') and message.author.server.id=='154009582748827648':
            yield from bot.send_message(message.channel, "The moderators of this immaculate server highly recommend using Brackets~ \nhttp://brackets.io/")
        elif message.content.startswith('?rec dev site') and message.author.server.id=='154009582748827648':
            yield from bot.send_message(message.channel, "The moderators of this immaculate server highly recommend using Mozilla Developer Network for all your coding help needs~ \nhttps://developer.mozilla.org/en-US/")
        elif message.content.startswith('?mods') and message.author.server.id=='154009582748827648':
            yield from bot.send_message(message.channel, "<@127010252934610944>, <@127188004216373248>, <@126899976042184705> you are needed!~")
        elif message.content.startswith('?info') and message.author.server.id=='154009582748827648':
            user = message.server.get_member_named("VorgunTheBeta#9662")
            if user.nick == None:
               name = user.name
            else:
               name = user.nick
            fname = "Text Stuff/info.txt"
            yield from bot.send_message(message.channel, Text("Text Stuff/info.txt").format(name))
        elif message.content.startswith('?help') and message.author.server.id!='154009582748827648':
            user = message.server.get_member_named("VorgunTheBeta#9662")
            if user.nick == None:
               name = user.name
            else:
               name = user.nick
            yield from bot.send_message(message.channel, Text("Text Stuff/help.txt").format(name))
        elif message.content.startswith('?lol') and message.author.server.id=='154009582748827648':
            yield from bot.send_message(message.channel, "http://ta-sa.org/data/images/laughing_man_big_2.png")
        elif message.content.startswith('limewire') and message.author.server.id=='154009582748827648':
            yield from bot.send_message(message.channel, "https://www.youtube.com/watch?v=SAp0xO-LwFs")
        elif message.content.startswith('?reverb') and message.author.server.id=='154009582748827648':
            yield from bot.send_message(message.channel, "Ravenslofty recommends using this plugin for all your reverb needs~ \nhttp://magnus.smartelectronix.com/#Ambience")
        elif message.content == '?plug' and message.author.server.id=='154009582748827648':
            yield from bot.send_message(message.channel, Text("Text Stuff/plug.txt"))
        elif message.content.startswith('?shit') and message.author.server.id=='154009582748827648':
            yield from bot.send_message(message.channel, Text("Text Stuff/shit.txt"))
        elif message.content.startswith('?google') or message.content.startswith('?Google'):
            google = message.content.replace('?google ', '').replace(" ", '+').replace("<", '%3C').replace(">", '%3E')
            send = 'https://google.com/search?q=' + google
            yield from bot.send_message(message.channel, send)


        elif message.content.startswith('?imfeelinglucky'):
            google = message.content.replace('?imfeelinglucky ', '').replace(" ", '').replace("<", '%3C').replace(">", '%3E')
            send = 'https://google.com/search?btnI=&q=' + google
            yield from bot.send_message(message.channel, send)


        elif "The More You Know" in message.content:
                if message.author.id == bot.user.id:
                    return
                else:
                    yield from bot.send_message(message.channel, "http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")

        elif  "the more you know" in message.content:
                if message.author.id == bot.user.id:
                    return
                else:
                    yield from bot.send_message(message.channel, "http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")

        elif message.content.startswith('?pudding'):
            msg = random.choice(FileToArray("Text Stuff/pudding.txt")) + " \nPUDDING~"
            yield from bot.send_message(message.channel, msg)

        elif message.content.startswith('?smug'):
            yield from bot.send_message(message.channel, random.choice(FileToArray("Text Stuff/smug.txt")))


        elif message.content.startswith('?dtrip'):
            yield from bot.send_message(message.channel, "!p https://www.youtube.com/watch?v=LHOEUrFOX4Y")


        elif message.content.startswith('?mpm'):
            yield from bot.send_message(message.channel, "!p https://www.youtube.com/watch?v=bGbdrLQWZpo")


        elif message.content.startswith('?shock'):
            yield from bot.send_message(message.channel, "https://cdn.discordapp.com/attachments/156523621240537088/176951338356178945/jeepers.gif")


        elif "neppy!" in message.content:
            msg = "{0.mention}!~"
            yield from bot.send_message(message.channel, msg.format(message.author))

        elif message.content.startswith('?source') or message.content.startswith('?sauce'):
            yield from bot.send_message(message.channel, "So you want to see whats behind me huh~ https://github.com/VorgunTheBeta/Neppy")


        elif message.content.startswith('?wat'):
            yield from bot.send_message(message.channel, "https://cdn.discordapp.com/attachments/156523621240537088/180092100199579650/1457714637653.gif WAT")




        elif message.content.startswith('?notice'):
            yield from bot.send_message(message.channel, Text("Text Stuff/notice.txt"))


        elif message.content.startswith('?mknote'):
            note = message.content.replace("?mknote ", '')
            yield from bot.send_message(message.author, note)


            #yield from bot.send_message(message.channel, "Please do not use this command, it does not work properly~~~")
            #userid= message.author.id
            #fname = userid+'.txt'
            #f = open(fname, 'a')
            #msg = message.content.replace('?mknote ','')
            #f.write(msg+"\n")
            #result = dbclient.files_search('', userid, start=0,max_results=100)
            #f.close()
            #if result.matches[0] == '':
            #   dbclient.files_upload(msg, "/"+fname, dropbox.files.WriteMode.add, client_modified=datetime.datetime.now(),mute=True)
            #else:
            #   g = open(fname)
            #   mes = g.read()
            #   dbclient.files_upload(mes, "/"+fname, dropbox.files.WriteMode.overwrite, client_modified=datetime.datetime.now(),mute=True)
            #print('Message written')

        elif message.content =="?notes":
            yield from bot.send_message(message.channel, "Please do not use this command, it does not work properly~~~")
            #userid= message.author.id
            #fname = userid + ".txt"
            #result = dbclient.files_search('', userid, start=0,max_results=100)
            #if result.matches[0] == '':
             #   yield from bot.send_message(message.channel, "I'm so sorry, but I can't seem to find any notes for you~~~")    
            #else:
             #   dbclient.files_download_to_file('/'+fname,'/'+fname)
                #  g = open(fname)
                # mes = g.read()
                # yield from bot.send_message(message.channel, "Your saved notes are: "+mes)
            

        elif message.content.startswith('?nick'):
                if message.author.id=="127188004216373248":
                        if message.content == '?nick':
                                nickname = None
                        else:
                                nickname = message.content.replace('?nick ','')
                        yield from bot.change_nickname(message.server.me, nickname)
                        prtmsg = "Nickname changed to {0} on {1.name}"
                        print(prtmsg.format(nickname, message.server))
                else:
                        yield from bot.send_message(message.channel, "https://cdn.discordapp.com/attachments/180764185205014530/191021728191873025/youre_gonna_die_now.jpg")

        elif bot.user.mentioned_in(message):
            if message.author.id == '192351191642931200':
                yield from bot.send_message(message.channel, "Well aren't you a little tsundere?~")
            else:
                yield from bot.send_message(message.channel, "Yes?~~~")


        elif message.content.startswith("?joinserver"):
            yield from bot.send_message(message.channel, "So you want me in your server?~~~ Just use this link: https://goo.gl/NPrZRF")


        elif message.content == "?support":
            yield from bot.send_message(message.channel, "You want to help out with finding a host for my sister? Thanks!~~~ https://www.patreon.com/VorgunTheBeta?ty=h")


        elif message.content == "?supporters":
            highrank = "Lance, Noire.io"
            lowrank = "none"
            yield from bot.send_message(message.channel, "Here are the awesome people who support me: (High Ranks - $5 pledge) "+highrank+", (Low Ranks - $1 pledge) "+lowrank)


        elif message.content =="?RNG":
            yield from bot.send_message(message.channel, "https://cdn.discordapp.com/attachments/126696039733264384/176351354044940289/RNGesus.gif")


        elif message.content =="?doof doof":
            yield from bot.send_message(message.channel, "!p https://www.youtube.com/playlist?list=PL1idN54yDQTQTHXHEydxzmTVcYffEtBiH")


        elif message.content.startswith("?image "):
            image = message.content.replace("?image ", '').replace(" ", '+')
            search = "https://google.com/search?tbm=isch&q="+image
            yield from bot.send_message(message.channel, search)


        elif "good nep" in message.content:
            msg = "Good nep {0.mention}, sweet dreams~~~"
            yield from bot.send_message(message.channel, msg.format(message.author))


        elif message.content == "fucking heroku":
            yield from bot.send_message(message.channel, "It sucks, I know.")


        elif message.content == "?blanc":
            yield from bot.send_message(message.channel, random.choice(FileToArray("Text Stuff/blanc.txt")))

        elif message.content == "?nepgear":
            yield from bot.send_message(message.channel, random.choice(FileToArray("Text Stuff/nepgear.txt")))

        elif message.content == "?plutia":
            yield from bot.send_message(message.channel, random.choice(FileToArray("Text Stuff/plutia.txt")))

        elif message.content == "?noire":
            yield from bot.send_message(message.channel, random.choice(FileToArray("Text Stuff/noire.txt")))

        elif message.content =="?vert":
            yield from bot.send_message(message.channel, random.choice(FileToArray("Text Stuff/vert.txt")))

        elif message.content == "?rom and ram":
            yield from bot.send_message(message.channel, random.choice(FileToArray("Text Stuff/romandram.txt")))

        elif message.content == "?uni":
            yield from bot.send_message(message.channel, random.choice(FileToArray("Text Stuff/uni.txt")))
        elif message.content == "?nepger":
            yield from bot.send_message(message.channel, "http://i.imgur.com/XHkYq9d.png")


@bot.event
@asyncio.coroutine
def on_member_join(member):
        if member.server.id=='154009582748827648':
                channel = discord.Object(id='155225555598442496')
                message = "{0.name} has joined the server~ <@127010252934610944>"
                yield from bot.send_message(channel, message.format(member))
                user = discord.User()
                user.id = member.id
                yield from bot.send_message(user, Text("Text Stuff/greeting.txt").format(member))
                f.close()

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    print("Connected Servers:")
    for s in bot.servers:
        print(s.name)

def FileToArray(filename):
    b = open(filename)
    pictures = b.read().split('\n')
    b.close()
    return pictures

def Text(filename):
    f = open(filename)
    notice = f.read()
    f.close()
    return notice

bot.run('MTY3OTgxOTA4OTE4MTQwOTI4.Cf7x5g.jzZYEW7CA_q4ooYXdMVUooFbJXM')
        
