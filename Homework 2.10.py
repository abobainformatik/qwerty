class Animal:
    def sound(self):
        return ""  # По умолчанию звук не определен

class Dog(Animal):
    def sound(self):
        return "Гав-гав"

class Cat(Animal):
    def sound(self):
        return "Мяу"

class Cow(Animal):
    def sound(self):
        return "Муу"

# Создаем список животных
animals = [Dog(), Cat(), Cow()]

# Выводим звуки, которые они издают
for animal in animals:
    print(animal.sound())
