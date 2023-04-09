# 1. напишите функцию для проверки на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево
def polindrom(str):
  string=input("Enter the number")
  for i in string:
   if string == string[::-1]:
    print("It's polindrom")
    return
  else:
    print("It's not polindrom")
    return
polindrom(str)
#2.посчитайте, сколько раз каждый символ встречается в строке (можно использовать словарь для хранения символов и кол-ва раз, которое они встречаются в тексте)
string = input("enter")
dict_1 = {}
for char in string:
    if char in dict_1:
        dict_1[char] += 1
    else:
        dict_1[char] = 1
print(dict_1)
#3.Написать функцию, которая принимает в себя заранее неизвестное количество списов и возвращает объединенный список (т е list_1 = [1, 2, 3], l2 = [4, 5, 6], result = [1, 2, 3, 4, 5, 6])
def add_list_function(*args):
  result = []
  for list in args:
      result+=list
      print(result)
      return
a,b,c=[6,8],[12,7],[9,6]
add_list_function(a,b,c)
#4. Hаписать функцию, которая принимает в себя словарь и меняет местами ключи и значения в нем.
def swap_dict(dict):
    my_dict={}
    return {v: k for k, v in dict.items()}
my_dict={"hh":18,"bkk":82, "cd":34}
new_dict=swap_dict(my_dict)
print(new_dict)
#Написать лямбду, которая определяет, четное число или нет
number=lambda x: x % 2 == 0
print(number(int(input("Enter the number"))))