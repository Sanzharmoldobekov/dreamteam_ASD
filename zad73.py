# Задание 1:
    # Нужно создать обычный калькулятор состоящий из знаков +,-,*,/
    # 1. У пользователя просят выбрать знак
    # 2. Просят ввести 1-ое число
    # 3. Просят ввести 2-ое число
    # 4. Вывести результат
    # 5. После результата спросить у пользователя хочет он закончить или нет, 
    # если нет то калькулятор должен запускатся сначала
    # 6. Учесть то что деление на ноль невозможно

print('Ноль завершит работу программы')
while True:
    s = input('Выберите знак (+,-,*,/): ')
    if s == '0' : break
    if s in ('=','-','*','/'):
        x = float(input('Введите число 1'))
        y = float(input('Введите число 2'))    
    if s == '+':
        print('%.2f' % (x+y))
    elif s == '-':
        print('%.2f' % (x-y))        
    elif s == '*':
        print('%.2f' % (x*y))
    elif s == '/':
        print('%.2f' % (x/y))
        if y != 0:
             print('%.2f' % (x/y))
        else:
             print('Деление на ноль')
    else:
        print('не верный знак')
    if s == '0' : break
