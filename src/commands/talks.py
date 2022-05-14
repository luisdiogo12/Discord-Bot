from discord.ext import commands
import discord


class Talks(commands.Cog):
    """Talks with user"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='oi', help='Verifica presença') # antes: @bot.command(name = 'estasca' , help = 'Verifica presença')
    async def presence(self, ctx): #adicionou self
        name = ctx.author.nick
        response = 'Vai chatear outro ' + name
        await ctx.send(response) 

    @commands.command(name = 'enviar' , help = 'envia por privado a mensagem ao autor')
    async def personal(self, ctx, mensagem): 
        try:
            await ctx.author.send(mensagem)
        except discord.errors.Forbidden:
            await ctx.send('Mensagens do server desabilitadas')

def setup(bot):
    bot.add_cog(Talks(bot))