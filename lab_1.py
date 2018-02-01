# Write a function that give random of 3 error and except all of this:
def random_error():
        t_err = (ValueError, TypeError, RuntimeError)
        import random
        i = random.randint(0, 2)
        return t_err[i]

try:
        raise random_error()
except ValueError:
        print('Invalid value')
except TypeError:
        print('Invalid type')
except RuntimeError:
        print('runtime is over')


#Write a function that take a list. If all items of list is numbers sort it, another gives ValueError:

def is_int(lis):
    for i in lis:
        if type(i) != int:
            return ValueError
    lis.sort()
    return lis


#Write a function that changed all keys in dict to strin and return a new dict:

def change_keys(dic):
        new_dic = {}
        for key, value in dic.items():
                new_dic.update({str(key): value})
        return(new_dic)

# Write a function that takes list of numbers and gives they multyple

def multyple_list(list_numbers):
        result = list_numbers[0]
        for i in range(1, len(list_numbers)):
                result *= list_numbers[i]
        return result
