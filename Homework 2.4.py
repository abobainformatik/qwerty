class Fraction:
    def __new__(cls, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Числитель и знаменатель должны быть целыми числами")
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        return super().__new__(cls)

    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

    @property
    def value(self):
        return round(self._numerator / self._denominator, 3)

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    @staticmethod
    def is_valid_fraction(numerator, denominator): #Возвращает True если дробь валидна, False - если нет
        return isinstance(numerator, int) and isinstance(denominator, int) and denominator != 0

    @classmethod
    def create_fraction_from_float(cls, float_number):
      """Имплементирует создание дроби из вещественного числа. Это сложная тема
      по причине неточности представления вещественных чисел в памяти компьютера.
      В реальности требует более сложного алгоритма для преобразования."""

      # Простейший пример, подходящий не для всех случаев, но для демонстрации:
      integer_part = int(float_number)
      fractional_part = float_number - integer_part
      return cls(int(fractional_part * 1000), 1000) #Примерное преобразование

# Пример использования:

try:
    fraction1 = Fraction(1.5, 2) # Вызовет TypeError
except TypeError as e:
    print(e)

try:
    fraction2 = Fraction(1, 0) # Вызовет ZeroDivisionError
except ZeroDivisionError as e:
    print(e)

fraction3 = Fraction(3, 4)

print(fraction3.value) # 0.75
print(fraction3)       # 3/4

print(Fraction.is_valid_fraction(1, 2))    # True
print(Fraction.is_valid_fraction(1, 0))    # False

fraction4 = Fraction.create_fraction_from_float(0.625)
print(fraction4) # 625/1000


