# Зачем нужно наследование.
class Animal(): # Животное
    def __init__(self, name, alive=True, fed=False):
        self.alive = alive# True (живой)
        self.fed = fed # False (накормленный)
        self.name = name

    def __repr__(self):
        return self.name

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        elif food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant(): # Растение
    def __init__(self, name, edible=False):
        self.edible = edible # False (съедобность)
        self.name = name

    def __repr__(self):
        return self.name


class Flower(Plant):
    def __init__(self, name, edible=False):
        super().__init__(name)  # связь с родительским классом
        self.edible = edible


class Fruit(Plant):
    def __init__(self, name, edible=True):
        super().__init__(name)  # связь с родительским классом
        self.edible = edible


class Mammal(Animal): # Млекопитающие
    def __init__(self, name, alive=True, fed=False, *edible):
        super(). __init__(name) # связь с родительским классом
        self.edible = edible


class Predator(Animal): # Хищник
    def __init__(self, name, alive=True, fed=False, *edible): #
        super(). __init__(name) # связь с родительским классом
        self.edible = edible


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)