# Дан список результатов автотестов. Для каждого теста известны его название, статус выполнения (PASS, FAIL или SKIP) и время выполнения.
# Напишите программу, которая с помощью filter() получает все упавшие тесты, с помощью map() формирует список их названий,
# а с помощью reduce() рассчитывает общее время выполнения всех тестов.
# Дополнительно с помощью генератор списка сформируйте список названий успешно пройденных тестов. В результате программа должна
# вывести количество тестов каждого статуса, список названий упавших тестов, список успешно пройденных тестов и общее время выполнения всех тестов.

# solution
from functools import reduce
# Список тестов
tests = [
    {"name": "test_1", "status": "PASS", "time": 1},
    {"name": "test_2", "status": "FAIL", "time": 2},
    {"name": "test_3", "status": "FAIL", "time": 3},
    {"name": "test_4", "status": "SKIP", "time": 4},
]
# Считаем количество тестов по статусам
pass_test = 0
fail_test = 0
skip_test = 0

for test in tests:
    if test["status"] == "PASS":
        pass_test = pass_test + 1
    elif test["status"] == "FAIL":
        fail_test = fail_test + 1
    else:
        skip_test = skip_test + 1

# Через filter() получаем все упавшие тесты
failed_tests = list(filter(lambda t: t["status"] == "FAIL", tests))
# Через map() формируем список названий упавших тестов
failed = list(map(lambda t: t["name"], failed_tests))
# Через reduce() считаем общее время всех тестов
total_time = reduce(lambda acc, t: acc + t["time"], tests, 0)

# Выводим результаты
print("Количество PASS:", pass_test)
print("Количество FAIL:", fail_test)
print("Количество SKIP:", skip_test)
print("Упавшие тесты:", failed)
print("Общее время выполнения:", total_time,"секунд")