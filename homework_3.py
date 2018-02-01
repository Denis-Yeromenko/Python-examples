# Program №1
print('Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, если оно меньше 0 - TypeError, если оно больше 10 - IndexError.Обрабатываем ошибку, говорим пользователю, в чем его ошибка')

try:
        def error_func():
                user_input = int(input('Please, input a number :'))
                if user_input % 2 == 0:
                    return ValueError
                elif user_input < 0:
                    return TypeError
                elif user_input > 10:
                    return IndexError
                else:
                        return RuntimeError
        raise error_func()
except ValueError:
        print('Your number is odd')
except TypeError:
        print('Your number is below zero')
except IndexError:
        print('Your number is more than 10')
except RuntimeError:
        print('You have normal number')

# Program №2
print('Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть.Если все хорошо - пишите объект в консоль. Если нет - обработайте возмозможные ошибки и скажите ему, что не так')

try:
        
        l_list = ['Hello!', True, 123, 0.22, {'KAY':'VALUE'}, (1, 2, 3, 4)]
        user_input = int(input('Please, input an index number of object would you like to see: '))
        if type(user_input) == int:
            if (user_input <= len(l_list)) && (user_input >= 0):
                print(l_list[user_input])
            else:
                raise IndexError
except IndexError:
        print('Your number is not index range!')

except ValueError:
        print('That was not a number!')

# Program №3

print('Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0')

def sum_func(a, b):
        if a > 0 and b > 0:
                return a + b
        elif a < 0 and b < 0:
                return a - b
        elif (a > 0 and b < 0) or (a < 0 and b > 0):
                return 0
        else:
                return a, b

# Porgram №4

print('Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль')

def more_func(a, b, c):
        
        if a > c and b > c:
                return a, b
        elif a > b and c > b:
                return a, c
        elif b > a and c > a:
                return b, c

# Program №5

print('Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, если флаг отрицателен - возвращаем новый список с четными числами из входного списка')

