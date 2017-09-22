#下载小说
import urllib
import urllib.request
import re
import time
import threading

class HTML_Tool(object):
    beginchar = re.compile('(\t|\n| |<a.*?>|<img.*?>)')
    endchar = re.compile('(<.*?>)')
    beginpart = re.compile('<p.*?>')
    newline = re.compile('(<br/>|</p>|<tr>|<div>|</div>)')
    newtab = re.compile('(<td>)')

    def replace_char(self,x):
        x = self.beginchar.sub('',x)
        x = self.beginpart.sub("\n    ",x)
        x = self.newline.sub("\n",x)
        x = self.newtab.sub("\t",x)
        x = self.endchar.sub("",x)
        
        x = re.sub(r'&nbsp;&nbsp;&nbsp;&nbsp;', '   ', x)  
        return x
class novel:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.tool = HTML_Tool()
        self.flag = False

    def getpage(self,page):
        url = 'http://m.biquge.vip/1_1497_'
        myurl = url + page +'/'
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Sa0fari/537.36'}
        req = urllib.request.Request(myurl,headers=headers)
        response = urllib.request.urlopen(req)
        mypage = response.read()
        page = mypage.decode('gbk',errors='ignore')
        items = re.findall(r'<li>\s*<a\s*href="(/1_\d+/\d+).html"\s*class="xbk">(.*?)</a>',page)
        return items

    def getchap(self,pg):
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Sa0fari/537.36'}
        req = urllib.request.Request(pg,headers=headers)
        response = urllib.request.urlopen(req)
        mypage = response.read()
        page = mypage.decode('gbk',errors='ignore')
        #print(page)
        items = re.findall(r'<article id="nr">(.*?)<div id="zuoyoufy">',page,re.S)
        return items

    def loadpage(self):
        while self.flag:
            if len(self.pages) < 2:
                try:
                    mypage = self.getpage(str(self.page))
                    self.page +=1
                    self.pages.append(mypage)
                except:
                    print('404 no found')
                    self.flag = False
            else:
                time.sleep(1)


    def downpage(self,nowpage):
        #print(nowpage)
        title = ''
        content = ''
        chapter = ''
        for items in nowpage:
            pg1 = 'http://m.biquge.vip' + items[0] +'.html'
            pg2 = 'http://m.biquge.vip' + items[0] +'_2'+'.html'
            content += self.getchap(pg1)[0] + self.getchap(pg2)[0]
            print('ok')
            content = self.tool.replace_char(content)
            #title += items[1]+'\n'
            '''
            for item in items:
                item = self.tool.replace_char(item)
            '''
            with open('C:/Users/Master/Desktop/msj.txt','a') as f:
                f.write(content)


    def start(self):
        self.flag = True
        page = self.page
        print('loading...')
        t = threading.Thread(target=self.loadpage,args=())
        t.start()

        while self.flag:
            if self.pages and (page<6):
                nowpage = self.pages[0]
                del self.pages[0]
                self.downpage(nowpage)
                page += 1

mynovel = novel()
mynovel.start()
