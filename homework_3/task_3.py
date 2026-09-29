# Дан список тестов:
#tests = [
#"test_login",
#"test_logout",
#"test_registration",
#"test_profile",
#"test_payment",
#"test_search"
#]
# Пользователь вводит количество тестов, которые необходимо запустить.
# Программа должна случайным образом выбрать указанное количество уникальных тестов из списка и каждому выбранному тесту случайно назначить
# статус PASS, FAIL или SKIP. Результаты необходимо объединить и вывести в виде отчёта. Если пользователь запросил больше тестов,
# чем существует в списке, программа должна вывести сообщение об ошибке.

# solution
import random

tests = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]

count = int(input("Сколько тестов запустить? "))

if count > len(tests):
    print("Ошибка: в списке только", len(tests), "тестов")
else:
    chosen = random.sample(tests, count)
    statuses = ["PASS", "FAIL", "SKIP"]

    report = []
    for test in chosen:
        status = random.choice(statuses)
        report.append((test, status))

    print("Отчёт о запуске:")
    for test, status in report:
        print(test, "-", status)