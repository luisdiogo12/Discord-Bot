import discord

from discord.ext import commands


class Images(commands.Cog):
    """Descrição"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='foto') 
    async def get_random_image(self, ctx):
        url_image='https://picsum.photos/1920/1080'
        embed_image = discord.Embed(
            title = 'titulo',
            description = 'descrição',
            color = 0x000FF,
        )
        embed_image.set_author(name = self.bot.user.name, icon_url=self.bot.user.avatar_url ) #todos os bot passam a self.bot......
        embed_image.set_footer(text = 'Made by: ' + self.bot.user.name, icon_url=self.bot.user.avatar_url )
        embed_image.set_image(url = url_image)
        embed_image.add_field(name = 'api', value= 'usamos a api do https://picsum.photos')
        embed_image.add_field(name = 'parametros', value= '{largura}/{altura}')
        embed_image.add_field(name = 'exemplos', value = url_image, inline = False)

        await ctx.send(embed= embed_image)
    
def setup(bot):
    bot.add_cog(Images(bot))