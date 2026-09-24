class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"{self.year} {self.make} {self.model}"

car1 = Car("Toyota", "Corolla", 2020)
print(car1.describe())

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

b1 = BankAccount()
b1.deposit(100)
b1.withdraw(150)

car2 = Car("Honda", "Civic", 2022)
car3 = Car("Ford", "Mustang", 2021)
print(car2.describe())
print(car3.describe())