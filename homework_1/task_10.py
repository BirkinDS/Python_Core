#task description
# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного:
# [1, 5, 2, 9, 2, 9, 1] => 5 | Напишите программу, которая будет выводить уникальное число

# solution
array_numbers = [1, 5, 2, 9, 2, 9, 1]
for number in array_numbers:
    if array_numbers.count(number) == 1:
        print(number)