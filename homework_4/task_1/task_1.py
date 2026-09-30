# Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного файла.
# Если чисел меньше 3 выводить ошибку.

# solution
with open("numbers.txt") as file:
    line = file.read().strip()

numbers = [int(ch) for ch in line if ch.isdigit()]
if len(numbers) < 3:
    print("Ошибка: в файле меньше 3-х чисел")
else:
    print(numbers[0], numbers[1], numbers[-2], numbers[-1])