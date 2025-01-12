class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def get_info(self):
        return 'Марка: {}, Модель: {}'.format(self.make,self.model)

vehicle=Vehicle('BMW','m5')
print(vehicle.get_info())

class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make, model)
        self.fuel_type=fuel_type

    def get_info(self):
        base_info=super().get_info()
        return '{}, Топливо:{}'.format(base_info,self.fuel_type)

car=Car('BMW','x7','БЕНЗ')
print(car.get_info())

vehicle2=Vehicle('12','11')
print(vehicle2.get_info())