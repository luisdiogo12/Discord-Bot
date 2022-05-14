#pip install discord
#pip install python-decouple

import os

from decouple import config
from discord.ext import commands

bot = commands.Bot(command_prefix = '>')

def load_cogs(bot):
    bot.load_extension('manager')
    bot.load_extension("tasks.dates")
    for file in os.listdir("commands"):
        print(file)
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")
load_cogs(bot)

#o codigo em cima em vez do codigo em baixo por extenso

'''
bot.load_extension('manager')
print('manager load')
bot.load_extension('commands.cryptos')
print('cryptos load')
bot.load_extension('commands.images')
print('images load')
bot.load_extension('commands.reactions')
print('reactions load')
bot.load_extension('commands.smarts')
print('smarts load')
bot.load_extension('commands.talks')
print('talks load')
bot.load_extension('tasks.dates')
print('dates load')'''


TOKEN = config('TOKEN_BOT') #TOKEN fica em maiusculas para ser uma constante
bot.run(TOKEN)
