#有道翻译
import urllib.request
import urllib.parse
import json

class FY():
    def __init__(self):
        self.flag = True
        self.content = input('请输入:')
    
    def fanyi(self):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom='
        data = {}
        data['type'] = 'AUTO'
        data['i'] = self.content
        data['doctype'] = 'json'
        data['xmlVersion:'] = '1.8'
        data['keyfrom'] = 'fanyi.web'
        data['ue'] = 'UTF-8'
        data['typoResult'] = 'true'
        data = urllib.parse.urlencode(data).encode('utf-8')

        response = urllib.request.urlopen(url,data)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        try:
            print("翻译结果:%s" %(''.join (i for i in target['smartResult']['entries'][1:])))
        except:
            print('未找到结果')
        self.content = input('请继续，或输入quit终止:')
        if self.content=='quit':
            self.flag = False
            print('再见')
        while self.flag:
            self.fanyi()
        

if __name__ == '__main__':
    x = FY()
    x.fanyi()
