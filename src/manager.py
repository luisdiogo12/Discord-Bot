from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument, CommandInvokeError


class Manager(commands.Cog):
    '''Gerencia o bot'''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self): 
        print(f'logged as {self.bot.user}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send('Falta argumentos, digite >help')
        elif isinstance(error,CommandNotFound):
            await ctx.send('Comando inexistente, digite >help')
        else:
            raise error

   
def setup(bot):
    bot.add_cog(Manager(bot))