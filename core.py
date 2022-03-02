from discord.ext import commands
import discord,os,random
whale='''       .
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~'''
class WhaleFactBot(commands.Bot):
    async def on_ready(self):
        print(whale)
        self.whaleFacts = open(os.getcwd() + "\\facts.txt", "r", encoding='UTF-8').read().split('\n')

class WhaleFactCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.urls = ['https://i.imgur.com/ppHGJIj.png',
                     'https://i.imgur.com/YnY4Awz.png',
                     'https://i.imgur.com/NppQajt.png',
                     'https://i.imgur.com/Uea6Wkc.png',
                     'https://i.imgur.com/lQgp0QH.png',
                     'https://i.imgur.com/QWwPh9k.png',
                     'https://i.imgur.com/33ly8KC.png',
                     'https://i.imgur.com/7jFEUjQ.png',
                     'https://i.imgur.com/5VqhIRo.png']

    def get_urls(self):
        return self.urls
    @commands.cooldown(1, 30, discord.ext.commands.BucketType.guild)
    @commands.command(name='fact', pass_context=True)
    async def fact(self, ctx):
        if len(self.bot.whaleFacts) == 0:
            self.bot.whaleFacts = open(os.getcwd() + "\\facts.txt", "r", encoding='UTF-8').read().split('\n')
        fact = random.choice(self.bot.whaleFacts)
        self.bot.whaleFacts.pop(self.bot.whaleFacts.index(fact))
        whaleFact = discord.Embed(title='Did you know?', description=fact)
        whaleFact.set_author(name='Whale Fact',icon_url=random.choice(self.urls))
        print(len(self.bot.whaleFacts))
        await ctx.send(content='{0}'.format(ctx.author.mention), embed=whaleFact)
    @fact.error
    async def whale_error(self,ctx,error):
        if isinstance(error,discord.ext.commands.CommandOnCooldown):
            await ctx.send('Give me {:.2f}s to come up with another whale fact!'.format(error.retry_after))
    @commands.cooldown(1,30,discord.ext.commands.BucketType.guild)
    @commands.command()
    async def whale(self,ctx):
        await ctx.send("```{0}```".format(whale))
    @whale.error
    async def whale_error(self,ctx,error):
        if isinstance(error,discord.ext.commands.CommandOnCooldown):
            await ctx.send('You are on Cooldown, please try again in {:.2f}s'.format(error.retry_after))

bot = WhaleFactBot(command_prefix='w!')
bot.add_cog(WhaleFactCog(bot))
bot.run(token = open('token.txt','r').read())