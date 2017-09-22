#python challenge 4
import urllib
from urllib import request
import re
link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=96791'
nothing = '96791'
while True:
    a = request.urlopen(link)
    page = a.read()
    page = page.decode('utf-8')
    nothing_n = re.findall(r'\d+',page)
    print(nothing_n)
    link = link.replace(nothing,nothing_n[0])
    #print(link)
    nothing = nothing_n[0]

