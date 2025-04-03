class Soyc:
    def __init__(self, taste):
        self.taste = taste

    def show_my_sauce(self, addition=""):
        if addition:
            print(f"Соус: {self.taste} и {addition}")
        else:
            print("Майонез")


class Employee:
    def __init__(self, name, age, salary, bonus=0):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = bonus

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
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print("Ингредиенты для приготовления блюда:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        print(f"Блюдо '{self.name}' готово!")


# Пример использования
sauce1 = Soyc("Сырный")
sauce1.show_my_sauce("беконом")

sauce2 = Soyc("Чесночный")
sauce2.show_my_sauce()

employee1 = Employee("Иван", 30, 50000)
print(employee1.get_name())
print(employee1.get_total_salary())

employee1.set_bonus(10000)
print(employee1.get_total_salary())

recipe1 = Recipe("Борщ", ["Мясо", "Картофель", "Капуста", "Свекла"])
recipe1.print_ingredients()
recipe1.cook()
