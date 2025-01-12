def f(filename,mode):
    filename=input("Введите имя файла:\n")
    # mode=input("Введите режим чтения\nfull - полностью\nlines - построчно\n")
    try:
        mode = input("Введите режим чтения\nfull - полностью\nlines - построчно\n")
        if mode=='full':
            with open(filename, 'r', encoding='utf-8') as file1:
                content = file1.read()
                print(content)
        elif mode=='lines':
            with open(filename, 'r', encoding='utf-8') as file1:
                for line in file1:
                    print(line)
        else:
            print('Введено неверное значение режима')
    except FileNotFoundError:
        print(f'Файл {filename} не найден, попробуйте дописать расширение или проверьте ошибки в названии')

# f('example.txt','full')
# f('example.txt','lines')

f('','')