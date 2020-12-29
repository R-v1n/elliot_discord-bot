from discord.ext import commands
class Elliot(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
         print(f'Logged in as ::>> {self.bot.user.name} ')

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel=member.guild.system_channel
        if channel is not None:
            await channel.send(f"Hello Friend.I am elliot anderson. \n Welcome to team Faux <<{member}>>")

    @commands.command()
    async def help(self,ctx):
            await ctx.send(f'Hello i am Elliot.the following commands are available.\n1>!!help :- provide help menu \n2>!!info :- provide info on Team Faux\n3>!!search ex :- search exlpoit in exploit db \n4>!!search wiki :- search wikipedia\n5>!!search yt :- search youtube')

    @commands.command()
    async def info(self,ctx):
        await ctx.send("Team Faux is a CTF team and communty of people passionate in CTF and cybersecurity")

def setup(bot):
    bot.add_cog(Elliot(bot))
