# Пользователь одной строкой вводит результаты запуска автотестов через пробел, например: PASS FAIL PASS SKIP PASS FAIL.
# Программа должна преобразовать введенную строку в список, подсчитать количество тестов каждого типа и вывести общую статистику.
# Логику подсчета необходимо вынести в отдельную функцию get_test_statistics(results), которая возвращает результат в виде словаря.
# Дополнительно программа должна вывести процент успешно пройденных тестов относительно общего количества тестов.
#Пример вывода:
#Всего тестов: 6
#PASS: 3
#FAIL: 2
#SKIP: 1
#Успешно: 50.0%

# solution
def get_test_statistics(results):
    stats = {}
    for result in results:
        if result in stats:
            stats[result] = stats[result] + 1
        else:
            stats[result] = 1
    return stats

line = input("Введите результаты тестов: ")
results = line.split()

stats = get_test_statistics(results)

total = len(results)

print("Всего тестов:", total)

for key in ["PASS", "FAIL", "SKIP"]:
    print(key + ":", stats.get(key, 0))

for key in stats:
    if key not in ["PASS", "FAIL", "SKIP"]:
        print(key + ":", stats[key])

pass_count = stats.get("PASS", 0)
percent = pass_count / total * 100
print("Успешно:", str(percent) + "%")