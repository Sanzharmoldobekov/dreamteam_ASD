# Какое слово нужно сложить 5 раз чтобы получить число 5?
# Какое слово нужно умножить на 7 чтобы получить 7?
a=('5'+'5'+'5'+'5'+'5')
a1=1
b='7'
print(a1*b)
print (len(a))

# Задача 3
# Здесь замешаны разные типы данных.
# Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1.
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)

spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
x=[]
for i in spisok_1 :
	for j in spisok_2:
		if i!=j:
			x.append(i)
			break# Задание 6:
# Дан список чисел:
# numbers = [1,0,-2,4,3,6,6,3,5,8,4,2] 
# Выведите все элементы списка, которые больше предущего элемента
# Пример: (numbers: 1,5,2,4,3 Результат: 5,4)numbers = [1,0,-2,4,3,6,6,3,5,8,4,2] 
numbers = [1,0,-2,4,3,6,6,3,5,8,4,2] 
x=[]
for i in range(len(numbers)-1):
	n=numbers[i]
	i+=1
	m=numbers[i]
	if m>n:
		x.append(m)
print(x)

print(x)

a=[x for x in range(1,1000) if x%3==0 or x%5==0]
print(sum(a))











