#Program №1
print('Рассчитываем площадь прямоугольника')
x = input('Пожалуйста, введите длину первой стороны в см: ')
y = input('Пожалуйста, введите длину второй стороны в см: ')

print('Площадь прямоугольника составляет: ', int(x) * int(y) , 'см кв.')

# Program №2
print('Рассчитываем сумму или разность чисел')
x = input('Пожалуйста, введите первое число: ')
y = input('Пожалуйста, введите второе число: ')
z = input('Пожалуйста, введите знак + или - : ')

if z == '+':
    print('Сумма чисел равна: ', int(x) + int(y))
else:
    print('Разница чисел равна: ', int(x) - int(y))

# Program №3

print('Рассчитываем все простые числа между 0 и пользовательским числом')

user_input = int(input('Пожалуйста, введите целое число: '))

count_num = list()

for i in range(2, user_input+1):

    for j in range(2, i):
        
        if i % j == 0:
            break
    else:
            count_num.append(i)

print('Список простых чисел в заданном диапазоне: ', count_num)

# Program №4

print('Расчет чисел кратных 5 в заданном диапазоне')

num1 = int(input('Пожалуйста, введите первое число: '))
num2 = int(input('Пожалуйста, введите второе число: '))
num_list = list()

for i in range(num1, num2+1):
    if i % 5 == 0:
        num_list.append(i)

print( 'Числа, кратные 5 в указанном Вами диапазоне: ', num_list)


# Program №5

print('Игра "Загадки"')

quiz_content = ['Вопрос 1: Заполните пробел: Для преобразования числа в строку выполните "___(100)" :',
                'Для преобразования строки в число выполните "___(100)" :',
                'Какой тип данных будет у переменной f, если f = 12 + 2.5? :',
                'Как в Python обозначается истина? :', 
                'Цикл с пред-условием :',
                'Чему равна переменная b, если b = bool(51)? :',
                'Чему равно утверждение: (True or False) and True? :',
                'Чему равно утверждение 0 == None? :',
                'Что вернет выражение "Hello"[1]? :',
                'Что вернет выражение len("Hello world!") :']
quiz_answers = ['str', 'int', 'float', 'True', 'While', 'True', 'True', 'False', 'e', '12']
count_true = 0
count_false = 0

for i in range(0, len(quiz_content)):
    user_answer = input(quiz_content[i])
    true_answer = quiz_answers[i]
    
    
    if user_answer.upper() == true_answer.upper():
        count_true += 1
        
    else:
        count_false += 1
        
    

print('Вы ответили правильно на {} вопроса, а неверно на {} вопроса'.format(count_true, count_false))


