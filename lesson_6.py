#Функции, упр.1. Даны списки: Нужно вернуть список, который состоит из элементов, общих для этих двух списков
def big_list(*args):
  result = [i for i in b if i in a]
  print(result)
  return
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
big_list(a,b)
# Функции, упр.4.Hаписать функцию для определения наибольшего числа (реализовать свой max)
def biggest_number(*args):
    sorted_list = sorted(list)
    result = sorted_list[-1]
    print(result)
    return
list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
biggest_number(list)
# Декоратор упр.1: написать декоратор, который возвращает int вместо float (хотим получить 1 вместо 1.5 как в примере)
def int_decorator(func):
    def wrapper(*args):
        return int(func(*args))
    return wrapper
@int_decorator
def div(x, y):
    return x / y
print(div(3, 2))
# Декоратор упр.6:Написать декоратор, который будет просить пользователя ввести число до тех пор, пока он не введет положительное число
def positive_number_decorator(func):
    def wrapper():
        while True:
            number = int(input("Enter the number: "))
            if number > 0:
                break
        return func(number)
    return wrapper
@positive_number_decorator
def some_number(number):
    print("This is positive number!")
some_number()