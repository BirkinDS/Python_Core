# Есть два списка:
# test_cases = ["Login", "Registration", "Checkout", "Logout"]
# statuses = ["PASS", "FAIL", "PASS", "SKIP"]
# Необходимо с помощью zip() объединить название каждого тест-кейса с его статусом.
# Создайте функцию print_report(test_cases, statuses), которая принимает два списка и выводит отчёт в формате Login — PASS.
# После формирования отчета программа должна определить количество успешных и неуспешных тестов и сообщить, можно ли считать тестовый
# запуск успешным: если есть хотя бы один FAIL, запуск считается неуспешным.

# solution
def print_report(test_cases, statuses):
    for name, status in zip(test_cases, statuses):
        print(name, "-", status)

    pass_count = 0
    fail_count = 0

    for status in statuses:
        if status == "PASS":
            pass_count = pass_count + 1
        elif status == "FAIL":
            fail_count = fail_count + 1

    print("Успешных тестов:", pass_count)
    print("Неуспешных тестов:", fail_count)

    if fail_count > 0:
        print("Тестовый запуск: неуспешный")
    else:
        print("Тестовый запуск: успешный")


test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

print_report(test_cases, statuses)