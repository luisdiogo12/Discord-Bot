#pip install discord
#python -m pip install requests
#python -m pip show requests 
#pip install python-decouple



from tkinter import N
import discord
import discord.ext
import random
import requests
import time
import json
from decouple import config
from time import sleep
from discord.ext import commands, tasks
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument, CommandInvokeError


#-----
bot = commands.Bot(command_prefix = '>')


#-----
@bot.event 
async def on_ready(): 
    print(f'logged as {bot.user}')

#-----
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "amd" in message.content.lower():
        print(message)
        await message.channel.send('CRIIINGE')
        await message.channel.send('Vou apagar esta merda')
        sleep(2)
        await message.delete()
        
    
    await bot.process_commands(message) 
#-----
@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    if reaction.emoji == '⬆️':
        role = user.guild.get_role(926179393527771136)
    elif reaction.emoji == '⬇️':
        role = user.guild.get_role(926179404235800596)
    await user.add_roles(role)
#-----
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,MissingRequiredArgument):
        await ctx.send('Falta argumentos, digite <help')
    elif isinstance(error,CommandNotFound):
        await ctx.send('Comando inexistente, digite <help')
    else:
        raise error


#-----
@bot.command(name = 'estasca', help = 'Verifica presença')
async def presence(ctx): 
    name = ctx.author.nick
    response = 'Vai chatear outro ' + name
    await ctx.send(response) 

@bot.command(name = 'caraoucoroa')
async def caraoucoroa(ctx): 
    n = random.randint(0,1)
    if n == 1:
      response = 'cara'
    else:
      response = 'coroa'
    await ctx.send(response) 

#-----
@bot.command(name = 'mandaroleandroparaocrl')
async def mandaroleandroparaocrl(ctx): 
    n = 5
    i = 0
    while i < n:
        response = "Vai para o caralho Leandro"
        await ctx.send(response)
        i += 1
#-----

@bot.command(name = 'monke')
async def monke(ctx): 
    n = random.randint(0,5)
    def sw(n):
        return {
            0: "https://tenor.com/view/axanar-alecpeters-axamonitor-monkey-ape-gif-18121300",
            1: "https://tenor.com/view/monkey-gif-22052185",
            2: 'https://tenor.com/view/monki-flip-flip-monkey-gif-18797173',
            3: 'https://tenor.com/view/chimp-ak47-gif-24574916',
            4: 'https://tenor.com/view/krach-boursier-calculate-monkey-silly-gif-14808948',
            5: 'https://tenor.com/view/monkey-artificialbloom-monkey-hulahoop-monkey-dancing-gif-23688613'
        }[n]
    print(n)
    response = sw(n)
    await ctx.send(response)


@bot.command(name = 'guipocrl')
async def mandaroleandroparaocrl(ctx): 
    n = 5
    i = 0
    while i < n:
        response = "Vai para o caralho Gui^2"
        await ctx.send(response)
        i += 1
@bot.command( help = 'Mostra opreço relativo de duas moedas')
async def binance(ctx, coin, base):
    try:
        link = f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}'
        response = requests.get(link)
        data = response.json()
        price = data['price']
        if price:
            await ctx.send(f'O valor da {coin} relativamente a {base} é {price}')
        else:
            await ctx.send(f'O valor do par {coin}/{base} não foi encontrado')
    except Exception as error:
        await ctx.send('Deu erro')
        print(error)


#-----    
@bot.command(name = 'calcular', help = 'calcula uma expressao, ex:2**2')
async def calculate_expression(ctx, *expression): # (*expression) <calcular 1+1 --> expressao = ('1','+','1')
    expression = ''.join(expression)
    response = eval(expression) #fraqueza: conseguem alterar dentro do eval, até para fechar o programa
    await ctx.send('Resposta. ' + str(response))
#-----
@bot.command(name = 'enviar' , help = 'envia por privado a mensagem ao autor')
async def personal(ctx, mensagem): 
    try:
        await ctx.author.send(mensagem)
    except discord.errors.Forbidden:
        await ctx.send('Mensagens do server desabilitadas')
#-----
@bot.command(name='foto') 
async def get_random_image(ctx):
    url_image='https://picsum.photos/1920/1080'
    embed_image = discord.Embed(
        title = 'titulo',
        description = 'descrição',
        color = 0x000FF,
    )
    embed_image.set_author(name = bot.user.name, icon_url=bot.user.avatar_url )
    embed_image.set_footer(text = 'Made by: ' + bot.user.name, icon_url=bot.user.avatar_url )
    embed_image.set_image(url = url_image)
    embed_image.add_field(name = 'api', value= 'usamos a api do https://picsum.photos')
    embed_image.add_field(name = 'parametros', value= '{largura}/{altura}')
    embed_image.add_field(name = 'exemplos', value = url_image, inline = False)

    await ctx.send(embed= embed_image)
TOKEN = config('TOKEN_BOT') #TOKEN fica em maiusculas para ser uma constante
bot.run(TOKEN)
