from discord.ext import commands
bot=commands.Bot(command_prefix="!!",help_command=None)
bot.load_extension("cogs.elliot")
bot.load_extension("cogs.exploit")
token="enter your token"
bot.run(token)
