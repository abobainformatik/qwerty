class BankAccount:
    def init(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if self._is_positive(amount):
            self.__balance += amount
            print(f"Внесено {amount}. Новый баланс: {self.__balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if self._is_positive(amount):
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Снято {amount}. Новый баланс: {self.__balance}")
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Сумма снятия должна быть положительной.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self): 
        return self.__account_number

    @staticmethod
    def _is_positive(amount):  
        return amount > 0

    @classmethod
    def create_empty_account(cls, account_number):
        return cls(account_number)  

# --- Example Usage ---
acc = BankAccount.create_empty_account("123456789")
print(f"Account number: {acc.get_account_number()}")  
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())  
acc.withdraw(-100) 
acc.withdraw(500) 
acc.deposit(0)  

acc2 = BankAccount("987654321", 1000)
print(f"Account number: {acc2.get_account_number()}")
print(f"Initial balance: {acc2.get_balance()}")

acc2.deposit(200)
acc2.withdraw(500)
print(f"New balance: {acc2.get_balance()}")

# Задача 2
class User:
    def __init(self, username, password):
        self.username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_password(self, new_password):
        if User._is_strong_password(new_password):
            self.__password = new_password
            print("Пароль успешно изменён")
        else:
            print("Ошибка: пароль слишком короткий")

    def get_password(self):
        return self.__password 

    @staticmethod
    def _is_strong_password(password):
        return len(password) >= 6

    @classmethod
    def create_default_user(cls, username):
        default_password = "defaultPassword"
        if not User._is_strong_password(default_password):
            raise ValueError("The default password is not secure enough!")
        return cls(username, default_password)

# --- Example Usage ---
user = User.create_default_user("Alice")
print(user.get_username())

user.set_password("12345")
user.set_password("securePass")
print(user.get_password()) 

# Задача 3
class Book:
   
    def __init(self, title, author, year):
       
        if not Book.is_valid_year(year):
            raise ValueError("Некорректный год издания.")
        self.__title = title
        self.__author = author
        self.__year = year

    @staticmethod
    def is_valid_year(year):
       
        import datetime

        current_year = datetime.datetime.now().year
        return isinstance(year, int) and year <= current_year

    @classmethod
    def create_book_without_year(cls, title, author):
       
        return cls(title, author, 2024)

    def get_info(self):
        
        return f"Название: {self.__title}, Автор: {self.__author}, Год: {self.__year}"


# Example Usage
try:
    book1 = Book("Мастер и Маргарита", "Булгаков", 1967)
    print(book1.get_info())  

    book2 = Book.create_book_without_year("1984", "Оруэлл")
    print(book2.get_info())  

    
    book3 = Book("Незнайка на Луне", "Носов", 2025)
except ValueError as e:
    print(f"Ошибка: {e}")  # Ошибка: Некорректный год издания.

try:
    book4 = Book("Незнайка на Луне", "Носов", "строка")
except ValueError as e:
    print(f"Ошибка: {e}")
