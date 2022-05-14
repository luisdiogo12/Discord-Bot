import requests

from discord.ext import commands


class Cryptos(commands.Cog):
    """Descrição"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command( help = 'Mostra opreço relativo de duas moedas')
    async def binance(self, ctx, coin, base):
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

def setup(bot):
    bot.add_cog(Cryptos(bot))