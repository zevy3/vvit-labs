def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age}")

describe_person("Иван")

def is_prime(number):
    number=int(input('Проверка простого числа: '))
    ans=[]
    for i in range(2,number**2+1):
        if number%i==0: ans.append(i)
    if len(ans)==1: return True
    else: return False

print(is_prime(''))