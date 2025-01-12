class Parrot:
    species='птица'
    def __init__(self,name,age):
        self.name=name
        self.age=age

kesha=Parrot('Кеша',10)
kuki=Parrot('Куки',15)

print('Кеша -- {}'.format(kesha.__class__.species))
print('Куки тоже {}'.format(kuki.__class__.species))

print("{} -- {}-летний попугай".format(kesha.name, kesha.age))