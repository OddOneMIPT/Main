class Shape:
    _width = 0
    _height = 0
    def __init__(self,width,height):
        Shape._height = height
        Shape._width = width


class Triangle(Shape):
    def area(self):
        return self._width * self._height / 2


class Rectangle(Shape):
    def area(self):
        return self._width * self._height

print('Введите высоту')
height = int(input())
print('Введите длину')
other_data = int(input())
Triangle = Triangle(height, other_data)
Rectangle = Rectangle(height, other_data)



print('Площадь треугольника',Triangle.area())
print('Площадь квадрата', Rectangle.area())


