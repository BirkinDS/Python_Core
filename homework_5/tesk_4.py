#Создайте собственное исключение InvalidTestStatusError, наследуемое от Exception.
# Напишите функцию, которая принимает статус теста и проверяет его значение.
# Допустимыми считаются только PASS, FAIL и SKIP. Если передан любой другой статус, функция должна с помощью raise создать
# InvalidTestStatusError и передать в него сообщение с некорректным значением.
# В основной программе обработайте это исключение через try/except и выведите понятное сообщение пользователю.
# Проверьте программу как с корректными, так и с некорректными статусами.

# solution
# Создаём собственное исключение, наследуемся от Exception
class InvalidTestStatusError(Exception):
    pass
def check_status(status):
    # Список допустимых статусов
    allowed = ["PASS", "FAIL", "SKIP"]

    # Если статус не входит в список — поднимаем свою ошибку
    if status not in allowed:
        raise InvalidTestStatusError(f"Недопустимый статус теста: '{status}'. Разрешены только: PASS, FAIL, SKIP")

    # Если всё хорошо — возвращаем статус
    return status

# 1. Корректный статус
try:
    result = check_status("PASS")
    print("Статус принят:", result)
except InvalidTestStatusError as e:
    print("Ошибка:", e)
# 2. Ещё один корректный статус
try:
    result = check_status("SKIP")
    print("Статус принят:", result)
except InvalidTestStatusError as e:
    print("Ошибка:", e)
# 3. Некорректный статус
try:
    result = check_status("DONE")
    print("Статус принят:", result)
except InvalidTestStatusError as e:
    print("Ошибка:", e)
# 4. Ещё один некорректный статус (например, пустая строка)
try:
    result = check_status("")
    print("Статус принят:", result)
except InvalidTestStatusError as e:
    print("Ошибка:", e)