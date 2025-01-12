# file=open('user.txt','w',encoding='utf-8')
# a=input('Введите текст: ')
# file.write(a)

def wrr(a,mode):
    mode=input('Введите, что хотите сделать\nперезаписать - полностью стереть файл и записать введенное'
               '\nдописать - дописать текст в конец\n')
    if mode=='перезаписать':
        file=open('user.txt','w',encoding='utf-8')
        a=input('Введите текст: ')
        file.write(a+" ")
    elif mode=='дописать':
        file = open('user.txt', 'a', encoding='utf-8')
        a = input('Введите текст: ')
        file.write(a+" ")

wrr('','')