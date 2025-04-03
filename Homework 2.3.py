class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, item):
        return "This attribute is not available"


# Пример использования:
my_car = Car("Toyota", "Prius")

print(my_car.make)   # Toyota
print(my_car.model)  # Corolla
print(my_car.color)  # This attribute is not available
print(my_car.year)   # This attribute is not available


# Задача 2
class Rectangle:
    __slots__ = ('width', 'height') # Важно: Ограничиваем возможные атрибуты

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key not in Rectangle.__slots__:  # Теперь проверяем __slots__
            raise AttributeError("Local attributes are not allowed")
        super().__setattr__(key, value)

# Пример использования:
rect = Rectangle(10, 5)

print(rect.width)   # 10
print(rect.height)  # 5

try:
    rect.color = "red"  # Вызовет исключение AttributeError
except AttributeError as e:
    print(e)

try:
    rect.width = 20      # Теперь вызовет исключение, т.к. это не новое значение
    print(rect.width)
except AttributeError as e:
    print(e)
