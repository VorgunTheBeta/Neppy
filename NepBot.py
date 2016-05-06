import discord
import asyncio
import random
import os.path
#Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 'oftivivyqtuiicu'
app_secret = 'igg65mw0d65duuk'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
dbclient = dropbox.client.DropboxClient("hLV5aeCyroAAAAAAAAAABxoK294BSQXMAqGwkCqQOK_LCnKle4EpDE0gplny4zcT")
description = "A bot created by VorgunTheBeta"
utils = discord.utils
bot = discord.Client()
game = discord.Game()
user = discord.User()
        

               
@bot.event
@asyncio.coroutine
def on_message(message):
        if message.content.startswith('?hello'):
                result = "Hello there~"
                yield from bot.send_message(message.channel, result)
        elif message.content.startswith('?sleep'):
                    if message.author.id == '127188004216373248' or message.author.id == '126899976042184705' or message.author.id == '127010252934610944' or message.author.id=='83677331951976448':
                          yield from bot.send_message(message.channel, "What, you don't like me?")
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
        elif message.content.startswith('?pingvorg'):
            yield from bot.send_message(message.channel, "<@127188004216373248>")
        elif message.content.startswith('?rec browser') and message.author.server.id!='99333280020566016':
            yield from bot.send_message(message.channel, "The moderators of this immaculate server highly recommend using Vivaldi~ \nhttps://vivaldi.com/?lang=en")
        elif message.content.startswith('?rec txt editor') and message.author.server.id!='99333280020566016':
            yield from bot.send_message(message.channel, "The moderators of this immaculate server highly recommend using Brackets~ \nhttp://brackets.io/")
        elif message.content.startswith('?rec dev site') and message.author.server.id!='99333280020566016':
       	    yield from bot.send_message(message.channel, "The moderators of this immaculate server highly recommend using Mozilla Developer Network for all your coding help needs~ \nhttps://developer.mozilla.org/en-US/")
        elif message.content.startswith('?mods') and message.author.server.id!='99333280020566016':
            yield from bot.send_message(message.channel, "<@127010252934610944>, <@127188004216373248>, <@126899976042184705> you are needed!~")
        elif message.content.startswith('?info') and message.author.server.id!='99333280020566016':
            yield from bot.send_message(message.channel, "I was created by <@127188004216373248>~ \nHere are my commands =```?hello, ?source, ?shit, ?rec browser, ?rec txt editor, ?mods, ?rec dev site, ?reverb, ?plug, ?google [search term], ?imfeelinglucky [search term]```")
        elif message.content.startswith('?help') and message.author.server.id!='154009582748827648':
            yield from bot.send_message(message.channel, "I was created by <@127188004216373248>~ \nHere are my commands =```?hello, ?source, ?google [search term], ?imfeelinglucky [search term], The More You Know, ?pudding, ?help, ?smug, ?shock```")
        elif message.content.startswith('?lol') and message.author.server.id!='99333280020566016':
            yield from bot.send_message(message.channel, "http://ta-sa.org/data/images/laughing_man_big_2.png")
        elif message.content.startswith('limewire') and message.author.server.id!='99333280020566016':
            yield from bot.send_message(message.channel, "https://www.youtube.com/watch?v=SAp0xO-LwFs")
       	elif message.content.startswith('?reverb') and message.author.server.id!='99333280020566016':
    	    yield from bot.send_message(message.channel, "Ravenslofty recommends using this plugin for all your reverb needs~ \nhttp://magnus.smartelectronix.com/#Ambience")
       	elif message.content.startswith('?plug') and message.author.server.id!='99333280020566016':
    	    yield from bot.send_message(message.channel, "https://github.com/VorgunTheBeta/Neppy ~ Hey thats me, Created by VorgunTheBeta \nhttps://valiantghost.com/ ~ Created by Summonee \nhttp://www.ldsgamers.com/ ~ Created by mechwd \nhttp://www.cibgraphics.com ~ Created by mechwd \nhttps://github.com/cibgraphics/Vanilla5 ~ Created by mechwd \nhttp://www.cyvercom.com/ ~ Created by orctamer \nhttp://xandsoftware.azurewebsites.net/ ~Created by XAND(Eric) \nMessage <@127188004216373248> to have your site added~")
       	elif message.content.startswith('?shit') and message.author.server.id!='99333280020566016':
       	    yield from bot.send_message(message.channel, "Here are some sites that you should learn from what not to do ~ \nhttp://www.lingscars.com/ \nhttp://www.fentek-ind.com/ \nhttps://valiantghost.com/ \nhttp://memekifanwebsite.netlify.com/")
       	elif message.content.startswith('?google'):
            google = message.content.replace('?google ', '').replace(" ", '+').replace("<", '%3C').replace(">", '%3E')
            send = 'https://google.com/search?q=' + google
            yield from bot.send_message(message.channel, send)
        elif message.content.startswith('?imfeelinglucky'):
            google = message.content.replace('?imfeelinglucky ', '').replace(" ", '').replace("<", '%3C').replace(">", '%3E')
            send = 'https://google.com/search?btnI=&q=' + google
            yield from bot.send_message(message.channel, send)
        elif message.content.startswith('The More You Know') or message.content.startswith('the more you know'):
            yield from bot.send_message(message.channel, "http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")
        elif message.content.startswith('?pudding'):
            image = random.choice(["http://img09.deviantart.net/336c/i/2013/317/e/3/nep_s_pudding_by_devilnekox-d6u5ae7.jpg", "https://gotgame.com/wp-content/uploads/2015/02/pudding.jpg", "https://53rg10.files.wordpress.com/2013/09/commie_hyperdimension_neptunia_the_animation_-_10_643170f6-mkv_snapshot_19-17_2013-09-14_16-22-45.jpg", "https://media.giphy.com/media/QfUwLcZ1cbaOQ/giphy.gif", "https://i.ytimg.com/vi/2I4Sjqn17QI/hqdefault.jpg", "https://31.media.tumblr.com/f89a86fff4d005aaeb2ff96afe166d86/tumblr_inline_ncxdqpuqSH1rejbig.gif"])
            msg = image + " \nPUDDING~"	
            yield from bot.send_message(message.channel, msg)
        elif message.content.startswith('?smug'):
            img = random.choice(["http://scontent-a.cdninstagram.com/hphotos-xaf1/t51.2885-15/10914676_1598608667029772_1771256047_a.jpg","http://41.media.tumblr.com/eae2e1da5f744b4058274b7f3ce93463/tumblr_nn129eZTXb1urtbs9o1_1280.png","https://i.warosu.org/data/jp/img/0140/65/1441685647187.jpg","https://cdn.discordapp.com/attachments/156523621240537088/177982860093816833/1435607123227.jpg"])
            yield from bot.send_message(message.channel, img)
        elif message.content.startswith('?dtrip'):
            yield from bot.send_message(message.channel, "!p https://www.youtube.com/watch?v=LHOEUrFOX4Y")
        elif message.content.startswith('?mpm'):
            yield from bot.send_message(message.channel, "!p https://www.youtube.com/watch?v=bGbdrLQWZpo")
        elif message.content.startswith('?shock'):
            yield from bot.send_message(message.channel, "https://cdn.discordapp.com/attachments/156523621240537088/176951338356178945/jeepers.gif")
        elif "neppy!" in message.content and message.author.id=='120980798550573056':
            msg = "{0.mention}!~"
            yield from bot.send_message(message.channel, msg.format(message.author))
        elif "neppy!" in message.content and message.author.id=='84554337220567040':
            msg = "{0.mention}!~"
            yield from bot.send_message(message.channel, msg.format(message.author))
        elif message.content.startswith('?source'):
            yield from bot.send_message(message.channel, "So you want to see whats behind me huh~ https://github.com/VorgunTheBeta/Neppy")
        elif message.content.startswith('?mknote'):
            userid= message.author.id
            f = open(userid+".txt", 'a')
            msg = message.content.replace('?mknote ','')
            f.write(msg+"\n")
            response = client.put_file(userid+".txt", f)
            f.close()
            print('Message written')
            print('uploaded', responce)
        elif message.content =="?notes":
            userid= message.author.id
            if os.path.isfile(userid+".txt"):
                f = open(userid+".txt")
                msg = f.read()
                f.close()
                yield from bot.send_message(message.channel, "Your saved notes are: "+msg)
            else:
            	yield from bot.send_message(message.channel, "I'm so sorry, but I can't seem to find any notes for you...~")

@bot.event
@asyncio.coroutine
def on_member_join(member):
	if member.server.id=='154009582748827648':
		channel = discord.Object(id='155225555598442496')
		message = "{0.name} has joined the server~ <@127010252934610944>"
		yield from bot.send_message(channel, message.format(member))

@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')



bot.run('MTY3OTgxOTA4OTE4MTQwOTI4.Cf7x5g.jzZYEW7CA_q4ooYXdMVUooFbJXM')
        
