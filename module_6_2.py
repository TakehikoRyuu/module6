# Доступ к свойствам родителя. Переопределение свойств.
class Vehicle:
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        return print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: {self.owner}')

    def set_color(self, new_color):
        low_color = new_color.lower()
        if low_color in self.__COLOR_VARIANTS:
            self.__color = low_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    def __init__(self, owner, __model, __color, __engine_power, __PASSENGERS_LIMIT=5):
        super().__init__(owner, __model, __color, __engine_power)  # связь с родительским классом
        self.__PASSENGERS_LIMIT = __PASSENGERS_LIMIT



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
# vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()