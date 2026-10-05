# Дан файл вещественных чисел.
# Заменить в нем все элементы на их квадраты.

# solution
with open("file.txt") as f:
    numbers = list(map(float, f.read().split()))

squares = [n ** 2 for n in numbers]

with open("file.txt", "w") as f:
    for n in squares:
        f.write(str(n) + "\n")