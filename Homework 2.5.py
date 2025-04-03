import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self, h=1e-5):
        self.h = h #Шаг для вычисления производной

    def __call__(self, func, x):
        """Вычисляет производную функции func в точке x."""
        return (func(x + self.h) - func(x - self.h)) / (2 * self.h)

    def __get__(self, instance, owner):
        """Дескриптор: позволяет вызывать производную как атрибут класса ExponentialFunction."""
        if instance is None:
            return self
        return lambda x: self(instance, x)

class ExponentialFunction:
    def __init__(self, a):
        self.a = a
        self.derivative = Derivative() # Атрибут, являющийся экземпляром Derivative

    def __call__(self, x):
        """Вычисляет значение функции f(x) = a * e^x."""
        return self.a * np.exp(x)


# Пример использования и построение графиков:
a = 2 # Коэффициент перед экспонентой
f = ExponentialFunction(a)

# Интервал для графиков:
x = np.linspace(-2, 2, 100)
# Вычисляем значения функции и ее производной:
y = [f(xi) for xi in x]
y_derivative = [f.derivative(xi) for xi in x]

# Строим графики:
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'f(x) = {a} * e^x')
plt.plot(x, y_derivative, label="f'(x) =  Производная") #Сделана подпись, что это производная.
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции и ее производной")
plt.legend()
plt.grid(True)
plt.show()
