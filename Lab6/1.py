class UserAccount:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.__password=password

    def set_password(self,new_password):
        self.__password=new_password
        # try:
        #     if new_password==self.__password:
        #         raise ValueError
        #     self.__password = new_password
        # except ValueError:
        #     print('ошибка')
    def check_password(self,password):
        return self.__password == password

class Surname(UserAccount):
    def __init__(self,username,email,password,surname):
        super().__init__(self,username,email,password)
        self.surname=surname

user=UserAccount('z3vy4','my.zona@bk.ru','seva2006')

user.set_password('bebra')
print(user.check_password('seva2006'))
print(user.check_password('bebra'))
print(user.__dict__)
# user.set_password('seva2001')



