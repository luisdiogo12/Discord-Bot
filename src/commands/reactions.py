from discord.ext import commands
from time import sleep



class Reactions(commands.Cog):
    """Descrição"""
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener() # antes: @bot.event 
    async def on_reaction_add(self, reaction, user): #adicionou self
        print(reaction.emoji)
        if reaction.emoji == '⬆️':
            role = user.guild.get_role(926179393527771136)
        elif reaction.emoji == '⬇️':
            role = user.guild.get_role(926179404235800596)
        await user.add_roles(role)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
    
        if "amd" in message.content.lower():
            print(message)
            await message.channel.send('CRIIINGE')
            await message.channel.send('Vou apagar esta merda')
            sleep(2)
            await message.delete()
        
    
        await self.bot.process_commands(message) 



def setup(bot):
    bot.add_cog(Reactions(bot))