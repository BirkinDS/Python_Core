# Рекурсивный подсчет результатов тестов. Дан список результатов автотестов со статусами PASS, FAIL и SKIP.
# Напишите рекурсивную функцию, которая подсчитывает количество тестов со статусом PASS.
# Функция должна обрабатывать список с помощью рекурсии. Использовать циклы for и while нельзя.

# solution

# Список тестов
def count_passed(tests):
    if not tests:
        return 0
    if tests[0] == "PASS":
        return 1 + count_passed(tests[1:])
    else:
        return count_passed(tests[1:])


tests = ["PASS", "FAIL", "PASS", "SKIP"]

print("Тестов PASS:", count_passed(tests))
