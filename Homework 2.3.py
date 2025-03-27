class Car:
   

    def init(self, make, model):
       
        self.make = make
        self.model = model

    def getattr(self, item):
       
        return "This attribute is not available"


# Пример использования
c = Car("Toyota", "Corolla")
print(c.make)
print(c.model)
print(c.color)

# Задача 2
class Rectangle:
    

    def init(self, width, height):
        
        self.width = width
        self.height = height

    def setattr(self, name, value):
        
        if name not in self.dict:
            raise AttributeError("Local attributes are not allowed")
        super().setattr(name, value)

# Пример использования
r = Rectangle(10, 5)
print(r.width)
print(r.height)

try:
    r.color = 'red' 
except AttributeError as e:
    print(e) 

r.width = 20 
print(r.width)
