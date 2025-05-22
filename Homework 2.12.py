def find_elements_by_index(values, indices):
    """
    Функция для поиска элементов по индексам с обработкой исключений
    
    :param values: Список значений
    :param indices: Список индексов
    :return: Список найденных элементов или сообщение об ошибке
    """
    result = []
    try:
        for index in indices:
            result.append(values[index])
        return result
    except IndexError as e:
        return f"Ошибка индекса: {e}"

# Пример использования
numbers = [10, 20, 30, 40, 50]
index_list = [1, 3, 6]  # Обратите внимание, что индекс 6 выходит за границы

# Вызов функции
result = find_elements_by_index(numbers, index_list)
print(result)  # Выведет сообщение об ошибке

# Пример с корректными индексами
valid_indexes = [0, 2, 4]
print(find_elements_by_index(numbers, valid_indexes))  # Выведет [10, 30, 50]














import math

class Circle:
    """
    Класс, представляющий круг с радиусом и вычисляемыми свойствами
    """
    def __init__(self, radius):
        """
        Инициализация круга с заданным радиусом
        
        :param radius: Радиус круга (положительное число)
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = radius

    @property
    def radius(self):
        """Свойство для доступа к радиусу"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Сеттер для радиуса с проверкой значения"""
        if value <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = value

    @property
    def diameter(self):
        """Свойство для вычисления диаметра"""
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        """Сеттер для диаметра (автоматически изменяет радиус)"""
        if value <= 0:
            raise ValueError("Диаметр должен быть положительным числом")
        self._radius = value / 2

    def area(self):
        """Метод для вычисления площади круга"""
        return math.pi * self._radius ** 2

# Пример использования
circle = Circle(5)
print(f"Радиус: {circle.radius}")      # 5
print(f"Диаметр: {circle.diameter}")   # 10
print(f"Площадь: {circle.area():.2f}") # 78.54

# Изменение радиуса через диаметр
circle.diameter = 14
print(f"Новый радиус: {circle.radius}") # 7











class Employee:
    def __init__(self):
        """Инициализация класса с пустым списком сотрудников"""
        self.__employees = []
    
    def add_employee(self, name, salary):
        """
        Добавление нового сотрудника
        
        :param name: Имя сотрудника
        :param salary: Зарплата сотрудника (число)
        """
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Зарплата должна быть положительным числом")
        self.__employees.append({"name": name, "salary": salary})
    
    @property
    def average_salary(self):
        """
        Свойство для вычисления средней зарплаты
        
        :return: Средняя зарплата или 0 если нет сотрудников
        """
        if not self.__employees:
            return 0
        total_salary = sum(emp["salary"] for emp in self.__employees)
        return total_salary / len(self.__employees)
    
    def get_sorted_employees(self, reverse=False):
        """
        Возвращает список сотрудников, отсортированный по зарплате
        
        :param reverse: Если True - сортировка по убыванию
        :return: Отсортированный список сотрудников
        """
        return sorted(self.__employees, key=lambda emp: emp["salary"], reverse=reverse)
    
    def __str__(self):
        """Строковое представление списка сотрудников"""
        return "\n".join(f"{emp['name']}: {emp['salary']}" for emp in self.__employees)


# Пример использования
if __name__ == "__main__":
    company = Employee()
    
    # Добавляем сотрудников
    company.add_employee("Иван Иванов", 75000)
    company.add_employee("Петр Петров", 90000)
    company.add_employee("Анна Сидорова", 85000)
    company.add_employee("Мария Кузнецова", 80000)
    
    # Выводим среднюю зарплату
    print(f"Средняя зарплата: {company.average_salary:.2f}")
    
    # Получаем и выводим отсортированный список (по возрастанию)
    print("\nСотрудники по возрастанию зарплаты:")
    for emp in company.get_sorted_employees():
        print(f"{emp['name']}: {emp['salary']}")
    
    # Получаем и выводим отсортированный список (по убыванию)
    print("\nСотрудники по убыванию зарплаты:")
    for emp in company.get_sorted_employees(reverse=True):
        print(f"{emp['name']}: {emp['salary']}")
