class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if self._is_positive_amount(amount):
            self.__balance += amount
            return True
        else:
            print("Сумма пополнения должна быть положительной.")
            return False

    def withdraw(self, amount):
        if self._is_positive_amount(amount) and amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            print("Сумма снятия должна быть положительной и не превышать баланс.")
            return False

    def get_balance(self):
        return self.__balance

    @staticmethod
    def _is_positive_amount(amount):
        return amount > 0

    @classmethod
    def create_account_with_zero_balance(cls, account_number):
        return cls(account_number)


# Пример использования:
account1 = BankAccount("12345", 1000)

print(f"Баланс: {account1.get_balance()}")

account1.deposit(500)
print(f"Баланс после пополнения: {account1.get_balance()}")

account1.withdraw(200)
print(f"Баланс после снятия: {account1.get_balance()}")

account1.withdraw(2000)  # Попытка снять больше, чем есть на счете

account2 = BankAccount.create_account_with_zero_balance("67890")
print(f"Баланс нового счета: {account2.get_balance()}")


# Задача 2
class User:
    def __init__(self, username, password):
        self.__username = username
        if User._is_strong_password(password):
            self.__password = password
        else:
            raise ValueError("Пароль должен содержать не менее 6 символов.")

    def change_password(self, new_password):
        if User._is_strong_password(new_password):
            self.__password = new_password
            print("Пароль успешно изменен.")
        else:
            print("Новый пароль недостаточно сложный.")

    @staticmethod
    def _is_strong_password(password):
        return len(password) >= 6

    @classmethod
    def create_user_with_default_password(cls, username):
        return cls(username, "default_password")  # Небезопасно, просто для примера


# Пример использования:
try:
    user1 = User("john_doe", "123")  # Вызовет ошибку ValueError
except ValueError as e:
    print(e)

user2 = User("jane_doe", "password123")  # Создаст пользователя

user2.change_password("short")
user2.change_password("new_strong_password")

user3 = User.create_user_with_default_password("guest")
print(f"Пользователь {user3._User__username} создан с паролем по умолчанию.")  # Не рекомендуется обращаться к приватным атрибутам

# Задача 3
import datetime

class Book:
    def __init__(self, title, author, year):
        if not Book._is_valid_year(year):
            raise ValueError("Год издания должен быть целым числом и не в будущем.")
        self.__title = title
        self.__author = author
        self.__year = year

    def get_info(self):
        return f"Название: {self.__title}, Автор: {self.__author}, Год издания: {self.__year}"

    @staticmethod
    def _is_valid_year(year):
        current_year = datetime.datetime.now().year
        return isinstance(year, int) and year <= current_year

    @classmethod
    def create_book_without_year(cls, title, author):
        return cls(title, author, datetime.datetime.now().year) #Использовали текущий год, а не 2024, потому что сейчас не 2024

# Пример использования:

try:
    book1 = Book("Мастер и Маргарита", "Булгаков", 2025)
except ValueError as e:
    print(e)

book2 = Book("1984", "Оруэлл", 1949)
print(book2.get_info())

book3 = Book.create_book_without_year("Преступление и наказание", "Достоевский")
print(book3.get_info())


