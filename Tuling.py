from wxpy import *

bot=Bot()

ice=ensure_one(bot.search('图灵机器人'))
gan=ensure_one(bot.search('甘兆焯'))
tuling=Tuling(api_key='fde750b9c63b4bbc9c76950075138ab4')
tuling2=Tuling(api_key='7a7206d2d7714feaa6f70beaef6c3dc3')

@bot.register(ice)
def reply_my_friend(msg):
    tuling.do_reply(msg)

@bot.register(gan)
def reply_my_friend2(msg):
    tuling2.do_reply(msg)

embed()