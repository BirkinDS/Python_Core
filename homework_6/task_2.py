# Замыкание для проверки времени выполнения. Напишите функцию create_time_checker(max_time),
# которая возвращает вложенную функцию для проверки времени выполнения теста.
# Вложенная функция принимает фактическое время выполнения и сообщает, превышен установленный лимит или нет.
# Создайте два независимых замыкания с разными значениями max_time и продемонстрируйте их работу.

# solution
def create_time_checker(max_time):
    def checker(real_time):
        if real_time > max_time:
            print("Установленный лимит превышен",{real_time})
        if real_time < max_time:
            print("Установленный лимит не превышен",{real_time})

    return checker


checker_4 = create_time_checker(4)

print("лимит 4")
checker_4(1)
checker_4(10)
