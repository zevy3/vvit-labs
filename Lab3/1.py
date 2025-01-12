def f(filename,mode):
    if mode=='full':
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    elif mode=='lines':
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line)

f('example.txt','full')
f('example.txt','lines')