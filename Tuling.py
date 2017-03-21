from wxpy import *

bot=Bot()

my_friend=ensure_one(bot.search('甘兆焯'))
tuling=Tuling(api_key='fde750b9c63b4bbc9c76950075138ab4')

@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)

bot.start()