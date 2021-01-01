from discord.ext import commands
import discord
#cog for providing list of important tools for CTF
class exp_tools(commands.Cog):
  def __init__(self,bot):
     self.bot=bot
  #create embeds with name and link of online tools      
  @commands.command(name="tools")
  async def tools_display(self,ctx):
    embed=discord.Embed(title="useful tools")
    embed.add_field(name="online Crypto tools",inline=False,value="[cyberchef](http://icyberchef.com/)\n[substitution ciphers](https://quipqiup.com/)")
    embed.add_field(name="hash cracking tools",inline=False,value="[crackstation](https://crackstation.net/)\n[online hash cracker](https://www.onlinehashcrack.com/)")
    embed.add_field(name="privesc check scripts",inline=False,value="[linEnum](https://github.com/rebootuser/LinEnum)\n[Linuxprivchecker](https://github.com/sleventyeleven/linuxprivchecker)\n[unix_privesc_check](https://github.com/pentestmonkey/unix-privesc-check)")
    embed.add_field(name="scripting frameworks",inline=False,value="[pwn_tools](https://github.com/Gallopsled/pwntools)\n[scapy](https://scapy.net/)\n[impacket](https://github.com/SecureAuthCorp/impacket)\n[requests](https://pypi.org/project/requests/)\n[Nmap](https://pypi.org/project/python-nmap/)")
    embed.add_field(name="code beautifier tools",inline=False,value="[code_beautify](https://codebeautify.org/)")
    embed.add_field(name="exploit search",inline=False,value="[Exploit db](https://www.exploit-db.com)\n[Rapid7 db](https://www.rapid7.com/db/)")
    embed.add_field(name="OSINT",inline=False,value="[shodan](https://www.shodan.io/)\n[spyse](https://spyse.com/)\n[G_dork db](https://www.exploit-db.com/google-hacking-database)")
    embed.add_field(name="misc",inline=False,value="[ngrok](https://ngrok.com/)\n[temp mail](https://temp-mail.org/en/)\n[online_exif_viewer](http://exif.regex.info/exif.cgi)\n[steg_online](https://stegonline.georgeom.net/upload)")
    await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(exp_tools(bot))
