#熟悉装饰器
def decor(func):
    print('adc()函数接收两个参数,以逗号隔开')
    def plhe(a,b):
        id = str(input('id=:'))
        sn = int(input('密码=:'))
        print('hello,%s,答案是'%(id))
        return func(a,b)
    return plhe

@decor
def adc(a,b):
    print(a+b)
