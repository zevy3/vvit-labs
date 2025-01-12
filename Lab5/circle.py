class Circle:
    def __init__(self,radius):
        self.radius=radius

    def get_radius(self):
        return self.radius
    def set_radius(self,new_radius):
        try:
            if new_radius<0:
                raise ValueError
            self.radius=new_radius
        except:
            print('Ошибка, радиус не изменился')

circle2=Circle(12)
print('Изначальный радиус:',circle2.get_radius())
circle2.set_radius(-1)
print('Новый радиус:',circle2.get_radius())