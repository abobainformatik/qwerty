class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = ('x', 'y', '_z')  # Ограничиваем допустимые атрибуты
    
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z  # Приватный атрибут для z
    
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, value):
        raise AttributeError("Изменение координаты z запрещено")


# Тестовый сценарий
if __name__ == "__main__":
    # Создаем экземпляр Point3D
    pt = Point3D(10, 20, 30)
    
    # Выводим значения x, y и z
    print(f"x: {pt.x}, y: {pt.y}, z: {pt.z}")
    
    # Пробуем изменить z (должно вызвать исключение)
    try:
        pt.z = 40
    except AttributeError as e:
        print(f"Ошибка при попытке изменить z: {e}")
    
    # Пробуем добавить новый атрибут (должно вызвать исключение)
    try:
        pt.extra = 100
    except AttributeError as e:
        print(f"Ошибка при попытке добавить атрибут: {e}")
    
    # Проверяем отсутствие __dict__
    try:
        print(pt.__dict__)
    except AttributeError as e:
        print(f"Ошибка при обращении к __dict__: {e}")







import sys
import timeit
from random import randint

class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class SlotPoint:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

def create_points(cls, count):
    return [cls(randint(0, 100), randint(0, 100)) for _ in range(count)]

def test_performance():
    # Создаем по 1000 экземпляров каждого класса
    normal_points = create_points(NormalPoint, 1000)
    slot_points = create_points(SlotPoint, 1000)
    
    # Тестируем производительность метода move
    normal_time = timeit.timeit(
        'for p in points: p.move(1, 1)',
        setup='from __main__ import normal_points as points',
        number=1000
    )
    
    slot_time = timeit.timeit(
        'for p in points: p.move(1, 1)',
        setup='from __main__ import slot_points as points',
        number=1000
    )
    
    print(f"Время выполнения для NormalPoint: {normal_time:.6f} сек")
    print(f"Время выполнения для SlotPoint: {slot_time:.6f} сек")
    print(f"Разница: {normal_time - slot_time:.6f} сек (SlotPoint быстрее на {(normal_time - slot_time)/normal_time*100:.2f}%)")

def test_memory_usage():
    # Создаем по одному экземпляру каждого класса
    normal_point = NormalPoint(10, 20)
    slot_point = SlotPoint(10, 20)
    
    # Добавляем динамический атрибут для NormalPoint
    normal_point.z = 30
    
    print("\nРазмеры объектов в памяти:")
    print(f"NormalPoint: {sys.getsizeof(normal_point)} байт")
    print(f"SlotPoint: {sys.getsizeof(slot_point)} байт")
    
    # Пытаемся добавить атрибут к SlotPoint
    try:
        slot_point.z = 30
    except AttributeError as e:
        print(f"\nПопытка добавить атрибут к SlotPoint: {e}")

if __name__ == "__main__":
    print("=== Тестирование производительности ===")
    test_performance()
    
    print("\n=== Тестирование использования памяти ===")
    test_memory_usage()
    













class Student:
    __slots__ = ['name', 'age', 'grade']
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def calculate_average_grade(students):
    if not students:
        return 0
    total = sum(student.grade for student in students)
    return total / len(students)

# Создаем коллекцию студентов
students = [
    Student("Кирилл Дорофеев", 20, 4.5),
    Student("Максим Щербаков", 21, 3.8),
    Student("Лиза староста", 19, 4.2),
    Student("Илюха бакулин", 20, 4.9),
    Student("Роман", 22, 3.5)
]

# Вычисляем и выводим среднюю оценку
average = calculate_average_grade(students)
print(f"Средняя оценка студентов: {average:.2f}")













class Product:
    __slots__ = ['name', 'price', 'quantity']
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def get_products_above_price(products_dict, threshold):
    return [name for name, product in products_dict.items() if product.price > threshold]

# Создаем словарь товаров
products = {
    "Ноутбук": Product("Ноутбук", 50000, 10),
    "Смартфон": Product("Смартфон", 30000, 25),
    "Планшет": Product("Планшет", 25000, 15),
    "Наушники": Product("Наушники", 5000, 50),
    "Монитор": Product("Монитор", 20000, 12)
}

# Демонстрируем работу функции
threshold_price = 25000
expensive_products = get_products_above_price(products, threshold_price)
print(f"Товары дороже {threshold_price} руб.: {', '.join(expensive_products)}")
