# Декоратор для логирования автотестов. Напишите декоратор log_test, который перед запуском тестовой
# функции выводит её имя, после выполнения сообщает о завершении и выводит полученный результат.
# Декоратор должен поддерживать функции с произвольным количеством позиционных и именованных
# аргументов с помощью *args и **kwargs. Используйте functools.wraps(), чтобы сохранить метаданные исходной функции.

# solution
from functools import wraps

def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Тест завершён: {func.__name__}")
        print(f"Результат: {result}")
        return result
    return wrapper

@log_test
def test_1(username, password):
    return username == "admin" and password == "1234"
test_1("admin", "1234")




