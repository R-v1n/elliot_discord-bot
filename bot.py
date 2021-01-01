from discord.ext import commands
#intializing bot with command_perfix and removing stock help command
#more info is giving in the elliot cog script
bot=commands.Bot(command_prefix="!!",help_command=None)
#using extensions for better modularity,extentions in cogs folder
bot.load_extension("cogs.elliot")
bot.load_extension("cogs.search_fns")
#use bot token from your discord dev account
token="Enter your token"
bot.run(token)
