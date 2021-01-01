from discord.ext import commands
import discord
import urllib.parse,urllib.request,re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as BS
from time import sleep
import wikipedia
#create tools to help in ctfs
#define search fns
#yoiutube search fn
#define exploit search fn


class hax0r_tools(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
#defing web scraping fn
    def exploitdb_scrape(self,keyword):
      print("Fetching exploits")
      #creating hedless webdriver using selenium
      #option for setting headless browser
      options = Options()
      options.headless = True
      exploit_list=[]
      #create webdriver with gecko driver <firefox>
      #note:-any webdriver can be used
      #path of webdriver should be specified during inintialization or path should be added to env PATH variable.
      browser=webdriver.Firefox(options=options)
      browser.get("https://www.exploit-db.com/")
      #sleep command to completely load webpage elements
      sleep(3)
      #fetching search box using relative xml path
      search=browser.find_element_by_xpath("//input[@type='search']")
      #sending search key word to browser
      search.send_keys(keyword)
      sleep(3)
      #get page source for web scraping
      webpage=browser.page_source
      #quit browser
      browser.quit()
      #initalise BeautifulSoup object with lxml parser.
      soup=BS(webpage,"lxml")
      #finding table with exploits
      exploit_table=soup.find("table",attrs={"id":"exploits-table"})
      #fetching table rows
      exploit_table_rows=exploit_table.tbody.find_all("tr")
      #checking if no results are found
      no_exp=exploit_table_rows[0].text
      if no_exp=="No matching records found":
          return 0
      else:
          #getting all a href attribute in html using BeautifulSoup
          for elements in exploit_table_rows:
             exploit=elements.find_all("a")
             #if the elements are empty break
             if not exploit[1].text :
                   break
             #appending to list of touple of exploit name and exploit url
             #adding complete string of url
             exploit_list.append((exploit[1].text,"https://www.exploit-db.com"+exploit[1].get('href')))
          print("fetched exploit list")
          return exploit_list

    async def yt_search(self,ctx,keyword,nor):
        #url encodeing search query
        query = urllib.parse.urlencode({'search_query':keyword})
        #opening url
        url= urllib.request.urlopen('http://www.youtube.com/results?' + query)
        #using re to find all result list
        search_results = re.findall(r'/watch\?v=(.{11})',url.read().decode())
        #if required no of results==1 send it else send link in loop
        if nor==1:
            await ctx.send('http://www.youtube.com/watch?v=' + search_results[1])
            return
        for i in range(int(nor)):
            url_keys='http://www.youtube.com/watch?v=' + search_results[i]
            print(url_keys)
            await ctx.send(url_keys)
    #wikipedia search fn
    async def wiki_search(self,ctx,keyword):
        #use wikipedia module to search summary of given search term
        try:
            wiki_summary=wikipedia.summary(keyword)
            await ctx.send(wiki_summary)
        #if multiple results are found will send exception containing list of realted pages
        except Exception as Err:
            await ctx.send(Err)

    #expoit search fn
    async def exploit_search(self,ctx,key,nor):
    #use web scraping to retun a list of exploits
        exploit_list=self.exploitdb_scrape(key)
    #if no results were vound send response
        if exploit_list==0:
            await ctx.send("No matching records found")
            return
        exp_len=int(len(exploit_list))
    #check if list from web scrape fn contains less no of results than required
    #change required no to available result number
        if exp_len<int(nor):
            nor=exp_len
    #create embed to send to server
    #adding embed title
        embed=discord.Embed(title=f"{key} search results")
    #accessing elements from exploit list where index 0 gives name and 1 is url
    #looping for mulitple no of results
        for ele in range(int(nor)):
            exp_name=exploit_list[ele][0]
            exp_link=exploit_list[ele][1]
            #creating href ie value="[the text to be shown](url)"
            embed.add_field(name=f"result no : {ele+1}",value=f"[{exp_name}]({exp_link})")
        await ctx.send(embed=embed)



    @commands.command(name='search')
    #creating command with name search
    #checking which search fn is to be used by checking 2nd parameter
    async def search_engine(self,ctx,*arg):
        #the check is performed to check if no of arguments are less than required and send proper usage insruction
        if len(arg)<2:
           await  ctx.send("usage :  !!search <-> {ex,yt} <-> keyword <-> no_of_Results[max:- 5,default:-1]")
           await  ctx.send("usage :  !!search <-> wiki <-> keyword")
           return
        #setting default no of required results to 1
        nor=1
        #s_type arg contains which fns to use
        s_type=arg[0]
        #key is the search term
        key=str(arg[1])
        #check if no of args are 3
        if len(arg)==3:
        #fetch the number of required results
            nor=arg[2]
        #check if no of results is less than 5 and send usage insruction
        if int(nor)>=5:
           ctx.send("maximum no_of_Results are 5 ")
           return
        #check the  search fn to use
        if s_type=="ex":
             await self.exploit_search(ctx,key,nor)
        elif s_type=="wiki":
             #wiki fn doesn't require no of results
             await self.wiki_search(ctx,key)
        elif s_type=="yt":
             await self.yt_search(ctx,key,nor)
        else:
            #if check fails send usage instruction
            await  ctx.send("usage :  !!search <-> {ex,yt} <-> keyword <-> no_of_Results[max:- 5,default:-1]")
            await  ctx.send("usage :  !!search <-> wiki <-> keyword")
            return
#cog setup fn
def setup(bot):
    bot.add_cog(hax0r_tools(bot))
