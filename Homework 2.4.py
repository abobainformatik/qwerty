class Fraction:
    
    def new(cls, numerator, denominator):
       
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Числитель и знаменатель должны быть целыми числами.")
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен 0.")
        return super().new(cls)

    def init(self, numerator, denominator):
      
        self.numerator = numerator
        self.denominator = denominator
        self.value = round(numerator / denominator, 3) # Вычисляем значение при инициализации

    def __str(self):
     
        return f"{self.numerator}/{self.denominator}"

    def add(self, other):
       
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def sub(self, other):
        
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def mul(self, other):
        
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def truediv(self, other):
       
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    @property
    def value(self):
       
        return self.__value


    @staticmethod
    def is_valid_fraction(numerator, denominator):
    
      return isinstance(numerator, int) and isinstance(denominator, int) and denominator != 0


    @classmethod
    def from_float(cls, float_value):
       
        if not isinstance(float_value, float):
             raise TypeError("Аргумент должен быть float.")
        integer_part, decimal_part = str(float_value).split('.')
        denominator = 10 ** len(decimal_part)
        numerator = int(integer_part + decimal_part)

        return cls(numerator, denominator)


# Пример использования
try:
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    print(f1 + f2)  # 5/4
    print(f1 - f2)  # -1/4
    print(f1 * f2)  # 3/8
    print(f1 / f2)  # 2/3
    print(f1.value) # 0.5

    f3 = Fraction(5, 0)
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")

try:
    f4 = Fraction("a", 2)
except TypeError as e:
    print(f"Ошибка: {e}")

f5 = Fraction.from_float(0.75)
print(f5)  # 75/100
print(f5.value)  # 0.75

print(Fraction.is_valid_fraction(5,2)) #True
print(Fraction.is_valid_fraction(5,0)) #False
print(Fraction.is_valid_fraction("a",2)) #False
