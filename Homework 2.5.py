import matplotlib.pyplot as plt
import numpy as np

class Derivative:
    def init(self, h=1e-5):
        self.h = h

    def get(self, instance, owner):
        if instance is None:
            return self  # Возвращаем сам дескриптор, если доступ через класс

        self.instance = instance  # Сохраняем ссылку на экземпляр

        return self  # Возвращаем сам дескриптор

    def call(self, x):
        if self.instance is None:
             raise AttributeError("Derivative must be accessed via an ExponentialFunction instance.")
        return (self.instance(x + self.h) - self.instance(x - self.h)) / (2 * self.h)


class ExponentialFunction:
    def init(self, a=1):
        self.a = a
        self.derivative = Derivative()  # Создаем экземпляр дескриптора

    def call(self, x):
        return self.a * np.exp(x)

    def plot(self, x_range=(-2, 2), num_points=100):
        x = np.linspace(x_range[0], x_range[1], num_points)
        y = [self(xi) for xi in x]
        y_prime = [self.derivative(xi) for xi in x] # Используем дескриптор правильно

        plt.plot(x, y, label=f'f(x) = {self.a} * e^x')
        plt.plot(x, y_prime, label=f"f'(x) = {self.a} * e^x")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('График функции и её производной')
        plt.legend()
        plt.grid(True)
        plt.show()


# Пример использования
exp_func = ExponentialFunction(a=2)
print(exp_func(0))
print(exp_func.derivative(0)) # Используем дескриптор правильно

# Построение графиков
exp_func.plot()
