#python challenge 6
import zipfile
import re
f = zipfile.ZipFile('C://channel.zip','r')


#n = f.read('90052.txt').decode()
li = []

name = '90052.txt'

while True:
    try:
        op = f.open(name)
        n = op.read().decode()
        op.close()
        name = re.findall(r'(\d+)',n)[0] + '.txt'
            #name = n.split()[-1] + '.txt'
        info = f.getinfo(name)
        comment =  info.comment.decode()
        li.append(comment)
        print(comment,end="")
        name = re.findall(r'\d+',n)[0] + '.txt'
    except:#IndexError:
        #print('It"s time to check manually',sep = '\n')  
        break

#print(''.join(li))
