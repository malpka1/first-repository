#Часть_1
#1. Oтфильтруйте список строк таким образом, чтобы остались строки, которые состоят только из букв
list_ = ['hy', 'pi', 'ly8', '1']
list_1=list(filter(lambda x: x.isalpha(), list_))
print(list_1)
#2. Посчитайте среднее арифметическое чисел list_ = [10, 20, 30, 40] (тут нужно разбить задачу на два этапа - посчитать сумму, а потом поделить на кол-во элементов)
list_ = [10, 20, 30, 40]
result = sum(list_)/len(list_)
print(int(result))
#3.Eсть список людей, нужно каждому добавить возраст (посчитать исходя из года рождения)
persons = [
 {"name": "Vasya", "birth_year": 1999},
 {"name": "Valentin", "birth_year": 1934},
 {"name": "Petr", "birth_year": 2005}]
for i in persons:
    i.update({"age":2023-i["birth_year"]})
print(persons)
#Часть_2. Работа с декораторами. Написать декоратор для функции, который будет возвращать Lena если пользователь введет lena, то есть делать capitalize
def decorator_capitalize(func):
    def wrapper():
        return func().capitalize()
    return wrapper

@decorator_capitalize
def decorator_capitalize():
    return input("Enter the name")

print(decorator_capitalize())