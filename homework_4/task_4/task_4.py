# Даны два файла произвольного типа.
# Поменять местами их содержимое.
# Файлы должны быть бинарного типа.

# solution
with open("file1.bin", "rb") as f1, open("file2.bin", "rb") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("file1.bin", "wb") as f1, open("file2.bin", "wb") as f2:
    f1.write(data2)
    f2.write(data1)

with open("file1.bin", "rb") as f1:
    print("file1:", f1.read().decode())

with open("file2.bin", "rb") as f2:
    print("file2:", f2.read().decode())