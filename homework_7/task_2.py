# Создайте класс ATM, описывающий работу банкомата. Банкомат должен хранить количество купюр номиналом 20, 50 и 100.
# Начальное количество купюр каждого номинала передается при создании объекта через __init__().
# Реализуйте метод add_money(), позволяющий добавить в банкомат купюры каждого номинала.
# Также реализуйте метод withdraw(amount) для снятия указанной суммы.
# Метод должен определить, может ли банкомат выдать запрошенную сумму имеющимися купюрами.
# Если операция возможна, необходимо уменьшить количество купюр в банкомате, вывести,
# сколько купюр каждого номинала было выдано, и вернуть True.
# Если указанную сумму выдать невозможно — вернуть False и оставить содержимое банкомата без изменений.
# Создайте объект ATM, добавьте в него несколько купюр и выполните несколько операций снятия денег.

# solution
class ATM:
    def __init__(self, banknotes20, banknotes50, banknotes100):
        self.banknotes20 = banknotes20
        self.banknotes50 = banknotes50
        self.banknotes100 = banknotes100

    def add_money(self, banknotes20=0, banknotes50=0, banknotes100=0):
        self.banknotes20 += banknotes20
        self.banknotes50 += banknotes50
        self.banknotes100 += banknotes100

    def withdraw(self, amount):
        for count100 in range(min(amount // 100, self.banknotes100), -1, -1):
            after_100 = amount - count100 * 100

            for count50 in range(min(after_100 // 50, self.banknotes50), -1, -1):
                rest = after_100 - count50 * 50

                if rest % 20 != 0:
                    continue

                count20 = rest // 20

                if count20 > self.banknotes20:
                    continue

                self.banknotes100 -= count100
                self.banknotes50 -= count50
                self.banknotes20 -= count20

                print(f"Выдано: 100 — {count100}, 50 — {count50}, 20 — {count20}")
                return True

        print(f"Сумму {amount} выдать невозможно")
        return False

    def show_info(self):
        print(f"Остаток: 20 — {self.banknotes20}, "
              f"50 — {self.banknotes50}, "
              f"100 — {self.banknotes100}")


atm = ATM(5, 3, 2)
atm.add_money(2, 10, 20)

atm.withdraw(170)
print()
atm.withdraw(80)
print()
atm.withdraw(777)
print()
atm.withdraw(1000)
print()
atm.withdraw(10000)
print()

atm.show_info()
