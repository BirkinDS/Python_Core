# Дан файл целых чисел. Создать два новых файла, первый из которых содержит четные числа
# из исходного файла, а второй — нечетные (в том же порядке).
# Если четные или нечетные числа в исходном файле отсутствуют, то соответствующий результирующий файл оставить пустым.

# solution
with open("one_file.txt") as f:
    numbers = list(map(int, f.read().split()))

with open("result/file1.txt", "w") as f1, open("result/file2.txt", "w") as f2:
    for n in numbers:
        if n % 2 == 0:
            f1.write(str(n) + "\n")
        else:
            f2.write(str(n) + "\n")