# Создайте программу для формирования отчёта по результатам автоматизированного тестирования.
# Исходные данные программа должна получать из JSON-файла, в котором для каждого теста указаны название, статус и время выполнения.
# Программа должна определить общее количество тестов, количество тестов со статусами PASS, FAIL и SKIP, сформировать список упавших тестов,
# определить самый длительный тест и рассчитать суммарное время выполнения.
# При обработке данных необходимо использовать минимум один генератор списка, lambda, filter() и reduce().
# Работу с файлом и входными данными необходимо защитить с помощью try/except: программа должна корректно обрабатывать отсутствие файла,
# некорректный JSON и неправильную структуру тестовых данных. Сформированный итоговый отчёт необходимо сохранить в отдельный JSON-файл.

# solution
import json
from functools import reduce

input_file = "tests.json"
output_file = "report.json"

try:
    # Открываем и читаем JSON-файл
    with open(input_file, "r", encoding="utf-8") as f:
        tests = json.load(f)
    # Проверяем, что это список
    if not isinstance(tests, list):
        raise ValueError("В файле должен быть список тестов")
    # Проверяем, что список не пустой
    if len(tests) == 0:
        raise ValueError("Список тестов пустой")
    # Проверяем структуру каждого теста
    for i, test in enumerate(tests, start=1):
        if not isinstance(test, dict):
            raise ValueError(f"Тест #{i} не является словарём")
        for field in ["name", "status", "time"]:
            if field not in test:
                raise ValueError(f"У теста #{i} отсутствует поле '{field}'")

    # --- Дальше считаем отчёт ---
    # Общее количество тестов
    total = len(tests)
    # Количество по статусам через генератор списка
    passed = len([t for t in tests if t["status"] == "PASS"])
    failed = len([t for t in tests if t["status"] == "FAIL"])
    skipped = len([t for t in tests if t["status"] == "SKIP"])
    # Список упавших тестов через filter() и map()
    failed_tests = list(filter(lambda t: t["status"] == "FAIL", tests))
    failed_names = list(map(lambda t: t["name"], failed_tests))
    # Самый длительный тест через max() и lambda
    longest = max(tests, key=lambda t: t["time"])
    longest_test = {"name": longest["name"], "time": longest["time"]}
    # Суммарное время через reduce()
    total_time = reduce(lambda acc, t: acc + t["time"], tests, 0)
    # Округляем на всякий случай
    total_time = round(total_time, 2)
    # Формируем отчёт
    report = {
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "failed_tests": failed_names,
        "longest_test": longest_test,
        "total_time": total_time
    }
    # Печатаем в консоль
    print("=== Отчёт по тестам ===")
    print("Всего тестов:", report["total_tests"])
    print("PASS:", report["passed"])
    print("FAIL:", report["failed"])
    print("SKIP:", report["skipped"])
    print("Упавшие тесты:", report["failed_tests"])
    print("Самый длительный тест:", report["longest_test"])
    print("Суммарное время:", report["total_time"])
    # Сохраняем отчёт в отдельный файл
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)
    print(f"Отчёт сохранён в файл: {output_file}")

except FileNotFoundError as e:
    print(f"Файл не найден: {e}")
except json.JSONDecodeError as e:
    print(f"Не удалось прочитать JSON: {e}")
except ValueError as e:
    print(f"Ошибка в данных: {e}")
except KeyError as e:
    print(f"Отсутствует поле: {e}")
except Exception as e:
    print(f"Непредвиденная ошибка: {e}")