# Создайте собственный модуль test_data.py. В нём реализуйте функции generate_login(), generate_age(), generate_status() и generate_user().
# generate_user() должна использовать остальные функции и возвращать готового тестового пользователя в виде словаря.
# Создайте второй файл main.py. Импортируйте в него созданный модуль, запросите у пользователя количество необходимых тестовых пользователей и сформируйте их список.
# После генерации выведите пользователей и статистику по статусам ACTIVE, BLOCKED и INACTIVE.

# solution
import test_data

count = int(input("Сколько пользователей сгенерировать? "))
users = []
for i in range(count):
    users.append(test_data.generate_user())
print("Сгенерированные пользователи:")
for user in users:
    print(user)

stats = {}
for user in users:
    status = user["status"]
    if status in stats:
        stats[status] = stats[status] + 1
    else:
        stats[status] = 1

print("Статистика по статусам:")
for key in stats:
    print(key + ":", stats[key])
