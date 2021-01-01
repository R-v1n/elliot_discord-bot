from discord.ext import commands
#intro cog
#defining general fns
#cogs are used by creating class and inheriting from commands.Cog
#cogs need to be setup using the setup fn
#the extensions are then loaded in bot.py
#asynchronous fns reqiure asyn while declaration and await while calling
#note:-ctx refers to context class in dircord.ext.commands
#ctx is passed in async fns to prove interactions with the server
#ctx attributes can be viewed in official docs:-https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context
#note:-various decorator are used {starts with @} including @commands.Cog.listener() , @commands.command which registers the given fn below in the commands objects
#new commands can be registered by adding command decorator and then fn definition
#commands are invoke with command_prefix{in our case "!!"} and fn name command name can be changed by creating alias by passing name parameter in command decorator
class Elliot(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    #print console output on bot intialization
    async def on_ready(self):
         print(f'Logged in as ::>> {self.bot.user.name} ')

    @commands.Cog.listener()
    #alert when new members join
    async def on_member_join(self,member):
        #fetch member channel
        channel=member.guild.system_channel
        await channel.send(f"Hello Friend.I am Elliot Alderson. \n Welcome to team Faux <<{member}>>")


    @commands.command()
    #basic help fn to send help menu
    async def help(self,ctx):
            await ctx.send(f'Hello i am Elliot.the following commands are available.\n1>!!help :- provide help menu \n2>!!info :- provide info on Team Faux\n3>!!search ex :- search exlpoit in exploit db \n4>!!search wiki :- search wikipedia\n5>!!search yt :- search youtube')

    @commands.command()
    #fn to send info on team Faux
    async def info(self,ctx):
        await ctx.send("Team Faux is a CTF team and community of people passionate in CTF and cybersecurity")
#setup fn to setup cog
#note:-setup fns are declared outside class
def setup(bot):
    bot.add_cog(Elliot(bot))
