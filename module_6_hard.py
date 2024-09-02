# Дополнительное практическое задание по модулю: "Наследование классов."
import math
class Figure():
    def __init__(self, __color=(1, 1, 1), __sides=1, filled=False):
        self.__sides = __sides # длина стороны
        self.__color = __color # список цветов RGB
        self.filled = filled # закрашенность

    def get_color(self):
        if self.__color == (1, 1, 1):
            return list(self.__color)
        else:
            return list(self.__color)

    def __is_valid_color(self, r, g, b): # проверка на правильность
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, valid):
        if valid >= 0 and valid == self.__sides:
            return True
        else:
            return False

    def get_sides(self):
        if self.sides_count == 12 or self.sides_count == 3:
            self.sides = self.__sides
            a = [self.__sides for i in range(self.sides_count)]
            return f'{a}'
        return f'{self.__sides}'


    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
            self.sides = self.__sides
            return f'{new_sides}'

    def __str__(self):
        return f'{self.__color}'

    def __len__(self):
        return self.__sides[0]

class Circle(Figure):
    def __init__(self, color, sides, sides_count=1):
        super().__init__(color, sides)
        self.color = color
        self.sides = sides
        self.sides_count = sides_count

    def __radius(self):
        rad = self.sides/(2 * math.pi)
        return f'{rad}'

    def get_square(self):
        pl = math.pi * self.__radius() ** 2
        return pl


class Triangle(Figure):
    def __init__(self, color, sides, sides_count=3):
        super().__init__(color, sides)
        self.color = color
        self.sides = sides
        self.sides_count = sides_count

    def get_square(self):
        a = self.sides
        b = self.sides
        c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return f'{area}'


class Cube(Figure):
    def __init__(self, color, sides, sides_count=12):
        super().__init__(color, sides)
        self.color = color
        self.sides = sides
        self.sides_count = sides_count

    def __sides(self):
        return Figure.get_sides()

    def get_volume(self):
        return self.sides ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())