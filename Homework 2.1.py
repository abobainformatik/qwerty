class Sauce:
    def init(self, flavor):
        self.flavor = flavor

    def show_my_sauce(self, addition=""):
        if addition:
            print(f"Соус и {addition}")
        else:
            print("Майонез")

class Employee:
    def init(self, name, age, salary):
        self.name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0  

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def get_total_salary(self):
        return self.__salary + self.__bonus


class Recipe:
    def __init(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f"Ингредиенты для {self.name}:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        print(f"Сегодня мы готовим {self.name}.")
        print(f"Выполняем инструкцию по приготовлению блюда {self.name}...")
        print(f"Блюдо {self.name} готово!")



# Sauce Example
cheese_sauce = Sauce("Сырный")
cheese_sauce.show_my_sauce("грибы")  
cheese_sauce.show_my_sauce()        

# Employee Example
employee1 = Employee("Иван", 30, 50000)
print(f"Имя: {employee1.get_name()}")
print(f"Возраст: {employee1.get_age()}")
print(f"Зарплата: {employee1.get_salary()}")

employee1.set_bonus(10000)
print(f"Бонус: {employee1.get_bonus()}")
print(f"Итоговая зарплата: {employee1.get_total_salary()}")

# Recipe Examples

spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

spaghetti.print_ingredients()

spaghetti.cook()

cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

cake.print_ingredients()

cake.cook()
