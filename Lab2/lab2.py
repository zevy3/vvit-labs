def greet(name):
    name=str(input('Введите имя: '))
    return print('Привет,',name,"!")
greet('')
def square(number):
    number=int(input("Введите число: "))
    return number**2

print(square(''))
def max_of_two(x, y):
    x=int(input("Введите первое число: "))
    y=int(input("Введите второе число: "))
    if x>y: return x
    else: return y

print(max_of_two('',''))
