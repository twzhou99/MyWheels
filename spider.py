#爬取糗百
import urllib
import urllib.request
import re
import threading
import time

class HTML_Tool(object):
    beginchar = re.compile('(\t|\n| |<a.*?>|<img.*?>)')
    endchar = re.compile('(<.*?>)')
    beginpart = re.compile('<p.*?>')
    newline = re.compile('(<br/>|</p>|<tr>|<div>|</div>)')
    newtab = re.compile('(<td>)')

    def replace_char(self,x):
        x = self.beginchar.sub('',x)
        x = self.beginpart.sub("\n    ",x)
        x = self.newline.sub("\n",x)
        x = self.newtab.sub("\t",x)
        x = self.endchar.sub("",x)
        
        #x = re.sub(r'<br/>', '\n', x)  
        return x

class HTML_Model(object):

    def __init__(self):
        self.page = 1
        self.pages = []
        self.mytool =HTML_Tool()
        self.enable = False

    def Getpage(self,page):
        myurl = 'https://qiushibaike.com/hot/page/' + page
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        req = urllib.request.Request(myurl, headers=headers)
        myResponse = urllib.request.urlopen(req)
        mypage = myResponse.read()
        page = mypage.decode('utf-8')

        items = re.findall(r'<div\s*class="content">\s*<span>\s*(.*?)\s*</span>\s*</div>',page,re.S)
        return items

    def loadpages(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    mypage = self.Getpage(str(self.page))
                    self.page +=1
                    self.pages.append(mypage)
                except:
                    print('404 no found')
                    self.enable = False
            else:
                time.sleep(1)

    def showpage(self,q,page):
        for items in q:
            print('Page%d\n'%page)
            for item in items:
                item = self.mytool.replace_char(item)
                print(item,end='\n\n\n')
            
            myinput = input()
            if myinput == 'quit':
                print('see you next time!')
                self.enable = False
                break


    def start(self):
        self.enable = True
        page = self.page
        print('loading...')
        t = threading.Thread(target=self.loadpages,args=())
        t.start()

        while self.enable:
            if self.pages:
                nowpage = self.pages
                #del self.pages
                self.showpage(nowpage,page)
                page += 1
                

input('press enter to start:')
myModel = HTML_Model()
myModel.start()
