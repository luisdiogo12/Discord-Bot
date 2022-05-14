import random

from discord.ext import commands



class Smarts(commands.Cog):
    """Descrição"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = 'calcular', help = 'calcula uma expressao, ex:2**2')
    async def calculate_expression(self, ctx, *expression): # (*expression) <calcular 1+1 --> expressao = ('1','+','1')
        expression = ''.join(expression)
        response = eval(expression) #fraqueza: conseguem alterar dentro do eval, até para fechar o programa
        await ctx.send('Resposta. ' + str(response))

    @commands.command(name = 'caraoucoroa')
    async def caraoucoroa(self, ctx): 
        n = random.randint(0,1)
        if n == 1:
          response = 'cara'
        else:
          response = 'coroa'
        await ctx.send(response) 

def setup(bot):
    bot.add_cog(Smarts(bot))