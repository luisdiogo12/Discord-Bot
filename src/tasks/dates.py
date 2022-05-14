#n pus no bot primário
import datetime

from discord.ext import commands, tasks


class Dates(commands.Cog):
    """Work with dates"""

    def __init__(self, bot):
        self.bot = bot

    #comando para ligar a task
    @commands.Cog.listener(name = 'tempo') #quando ausente nos () o nome do comando fica igual ao da def
    async def on_ready(self):
        self.current_time.start() # tal como bot põe-se o self. antes

    @tasks.loop(seconds=1)
    async def current_time(self):
        
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel(874894819846139928) # bot passa a self.bot

        await channel.send("Data atual: " + now)


def setup(bot):
    bot.add_cog(Dates(bot))