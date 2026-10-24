# Создайте класс CreditCard, описывающий кредитную карту.
# При создании объекта необходимо передавать номер счёта и начальный баланс карты.
# Реализуйте метод deposit(amount), который пополняет баланс на указанную сумму,
# метод withdraw(amount), который снимает указанную сумму, и метод show_info(),
# который выводит номер счёта и текущий баланс.
# Создайте три объекта класса CreditCard с разными номерами счетов и начальными балансами.
# Пополните баланс первой и второй карты, а с третьей карты снимите некоторую сумму.
# После выполнения операций выведите информацию о состоянии всех трёх карт.

# solution
class CreditCard:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостаточно средств")
        else:
            self.__balance -= amount
        return self.__balance

    def show_info(self):
        print(f"Номер счета: {self.__account_number}")
        print(f"Баланс: {self.__balance}")


first_card = CreditCard(12345, 100)
second_card = CreditCard(54321, 50)
third_card = CreditCard(1001, 400)

first_card.deposit(100)
second_card.deposit(50)
third_card.withdraw(100)

third_card.show_info()
print()
first_card.show_info()
print()
second_card.show_info()
