# Program №1
print('Создаем список с числами и сортируем их по возрастанию:')
list_1 = [1, 22, 14, 127, 19, 80]
list_1.sort()
print(list_1)


# Program №2
print('Создать словарь из 6 пар: int -> str, например {6: "6"}, вывести его в консоль попарно')
new_dict = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6'}
for i in new_dict:
    print(i, new_dict[i])

# Program №3
print('Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем: ')
new_tuple = (0.23, 12.76, 5.33, 0.33, 13.7, 45.3, 59.43, 59.4, 0.123, 22.03)

print('The max value in tuple is {} and the min value is {}'.format(max(new_tuple), min(new_tuple)))

# Program №4
print ('Создать лист из 3 слов: ["Earth", "Russia", "Moscow"], соеденить все слова в единую строку, чтобы получилось: "Earth -> Russia -> Moscow" ')

list_1 = ["Earth", "Russia", "Moscow"]
new_list = '->'.join(list_1)
print(new_list)


# Program №5
print('Взять строку "/bin:/usr/bin:/usr/local/bin" и разбить ее в список по символу ":" ')

string = '/bin:/usr/bin:/usr/local/bin '
new_list = string.split(':')
print(new_list)


# Program №6

print('Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет :')

true_division = []
false_division = []

for i in range(1, 101):
    if i % 7 == 0:
        true_division.append(i)
    else:
        false_division.append(i)

print('В указанном диапазоне на 7 делятся следующие числа : {}, а не делятся :{}'. format(true_division, false_division))

# Program №7

print('Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы ')

new_matrix = [[13, 56, 43],
              [43, 908, 0.6],
              [22, 321, 0],
              [9.5, 67, 14]]
m_str = []
a = []
b = []
c = []

for i in new_matrix:
    a.append(i[0])
    b.append(i[1])
    c.append(i[2])
    m_str.append(i)       

print('Строки текущей матрицы: {}'.format(m_str), 'Столбцы в текущей матрице: первый{}, второй{}, третий{}'.format(a, b, c))

# Program №8

print('Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс')
new_list = [345, 'Hello, world!', 0.32, True, (12, 13, 15), ['hello', 13, 0.27], {'key_1':'value_1', 12: '12'}]
for i in new_list:
    print(i, new_list.index(i))


# Program №9

print("Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'")

new_list = [345, 'Hello, world!', 0.32, 'to-delete', True, (12, 13, 15), 'to-delete', ['hello', 13, 0.27], {'key_1':'value_1', 12: '12'}, 'to-delete']

for i in new_list:
    if i == 'to-delete':
        new_list.remove(i)
        
print(new_list)


# Programm №10

print('Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль')

for i in range(10, 0, -1):
    print(i)

# or

new_list = []

for i in range(1, 11):
    new_list.append(i)

print(new_list[::-1])














