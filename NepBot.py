import discord
import asyncio

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
                    if message.author.id == '127188004216373248' or message.author.id == '126899976042184705' or message.author.id == '127010252934610944':
                          yield from bot.send_message(message.channel, "What, you don't like me?")
                          user.id = 127188004216373248
                          yield from bot.send_message(user, "Neppy is down")
                          print('message recieved')
                          bot.close()
                          exit()
                    else:
                          yield from bot.send_message(message.channel, "http://www.ozsticker.com/ozebayimages/620_dave_product.jpg")
        elif message.content.startswith('?status'):
                    if message.author.id == '127188004216373248' or message.author.id == '126899976042184705' or message.author.id == '127010252934610944':
                        msg = yield from bot.wait_for_message(timeout=5.0, author=message.author)
                        
                        game.name = msg.content
                        yield from bot.change_status(game)
                        return
                    else:
                        yield from bot.send_message(message.channel, "http://vignette1.wikia.nocookie.net/meme/images/8/8e/Nope.jpg")
        elif message.content.startswith('?pingvorg'):
            yield from bot.send_message(message.channel, "<@127188004216373248>")
        elif message.content.startswith('?rec browser') and message.author.server.id!='99333280020566016':
            yield from bot.send_message(message.channel, "The moderators of this immaculate server highly recommend using Vivaldi~ \nhttps://vivaldi.com/?lang=en")
        elif message.content.startswith('?rec txt editor'):
            yield from bot.send_message(message.channel, "The moderators of this immaculate server highly recommend using Brackets~ \nhttp://brackets.io/")
        elif message.content.startswith('?rec dev site'):
       	    yield from bot.send_message(message.channel, "The moderators of this immaculate server highly recommend using Mozilla Developer Network for all your coding help needs~ \nhttps://developer.mozilla.org/en-US/")
        elif message.content.startswith('?mods'):
            yield from bot.send_message(message.channel, "<@127010252934610944>, <@127188004216373248>, <@126899976042184705> you are needed!~")
        elif message.content.startswith('?info'):
            yield from bot.send_message(message.channel, "I was created by <@127188004216373248>~ \nHere are my commands =```?hello, ?shit, ?rec browser, ?rec txt editor, ?mods, ?rec dev site, ?reverb, ?plug, ?google```")
        elif message.content.startswith('?lol'):
            yield from bot.send_message(message.channel, "http://ta-sa.org/data/images/laughing_man_big_2.png")
        elif message.content.startswith('limewire'):
            yield from bot.send_message(message.channel, "https://www.youtube.com/watch?v=SAp0xO-LwFs")
       	elif message.content.startswith('?reverb'):
    	    yield from bot.send_message(message.channel, "Ravenslofty recommends using this plugin for all your reverb needs~ \nhttp://magnus.smartelectronix.com/#Ambience")
       	elif message.content.startswith('?plug'):
    	    yield from bot.send_message(message.channel, "https://valiantghost.com/ ~ Created by Summonee \nhttp://www.ldsgamers.com/ ~ Created by mechwd \nMessage <@127188004216373248> to have your site added~")
       	elif message.content.startswith('?shit'):
       	    yield from bot.send_message(message.channel, "Here are some sites that you should learn from what not to do ~ \nhttp://www.lingscars.com/ \nhttp://www.fentek-ind.com/ \nhttps://valiantghost.com/ \nhttp://memekifanwebsite.netlify.com/")
       	elif message.content.startswith('?google'):
            google = message.content.replace('?google ', '').replace(" ", '+').replace("<", '%3C').replace(">", '%3E')
            send = 'https://google.com/search?q=' + google
            yield from bot.send_message(message.channel, send)
        elif message.content.startswith('The More You Know'):
            yield from bot.send_message(message.channel, "http://cdn.theatlantic.com/assets/media/img/mt/2014/09/The_More_You_Know/lead_large.png")
        elif message.author.id=='127067362372354048':
            yield from bot.send_message(message.channel, "Are you trying to hurt me Dan? You are such a meany~")
        elif message.content.startswith('pudding'):
            yield from bot.send_message(message.channel, "http://img09.deviantart.net/336c/i/2013/317/e/3/nep_s_pudding_by_devilnekox-d6u5ae7.jpg \nPUDDING~")
       	    
       	    
       	    
       	    
       	    
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
    bot.change_status(null)



bot.run('vorgunthebeta@gmail.com', 'kazza10')
        
