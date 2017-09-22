#HTML分析
import html.parser as h

class MyHTMLParser(h.HTMLParser):

    a_t=False
    b_t=False

    def handle_starttag(self, tag, attrs):
        if tag=='h3' and len(attrs) > 0 and attrs[0][1] == 'event-title':
            self.a_t=True

        if tag == 'span' and len(attrs) > 0 and attrs[0][1] == 'event-location':
            self.b_t=True
            
        for attr in attrs:
            if tag == 'time':
                print('时间:',attrs[0][1])
            
       
    def handle_data(self, data):
        if self.a_t is True:
            print('活动:',data)

        if self.b_t is True:
            print('地点:',data)
            print('\n')

    def handle_endtag(self, tag):
        self.a_t=False
        self.b_t=False


p=MyHTMLParser()

mystr = open('C://Users//Master//Python.html','rb').read().decode('utf-8')
p.feed(mystr)
p.close()
