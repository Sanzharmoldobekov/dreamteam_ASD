
# Задание 4:
# Дан список  целых чисел:
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# Создайте новый лист и замените отрицательные числа на -1, положительные на число 1, ноль оставить без изменения.

numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
numbers1 = []
for item in numbers:
    if item > 0:
        numbers1.append(1)
    elif item < 0:
        numbers1.append(-1)
    else:
        numbers1.append(0)
print(numbers)
print(numbers1)

