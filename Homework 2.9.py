import math

class Shape:
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределен в подклассе")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() должен быть переопределен в подклассе")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Пример использования
circle = Circle(5)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())
