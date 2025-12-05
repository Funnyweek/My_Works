# 1. Напишите функцию show_info(**kwargs)
# 2. Принимает именованные аргументы
# 3. Выводит информацию в формате "ключ: значение"
#
# Пример:
# show_info(name='Алиса', age=20, city='Алматы')
# Вывод:
# name: Алиса
# age: 20
# city: Алматы

# def show_info(**kwargs):
#     la={
        
#     }
#     la.update(**kwargs)
#     print(la)
# show_info(city="almaty", age=22, name="Maxim")

# 1. Создайте декоратор add_suffix(func)
# 2. Добавляет " ✓" в конец результата
# 3. Примените к функции status(text)
#
# Пример:
# @add_suffix
# def status(text):
#     return text
#
# status('Ready') → "Ready ✓"
# status('Complete') → "Complete ✓"

# def start(func):
#     a = (f"{func} ✓")
#     return a
# print(start("Ready"))



# 1. Напишите функцию is_palindrome_number(num)
# 2. Проверяет является ли число палиндромом
# 3. Например 121 = 121 (палиндром)
#
# Примеры:
# is_palindrome_number(121) → True
# is_palindrome_number(12321) → True
# is_palindrome_number(123) → False
# is_palindrome_number(1) → True

# def il(num):
#     if num == num[::-1]:
#         print("True")
#     else:
#         print("False")

# il("121")
# il("123")


# 1. Создайте декоратор logger(func)
# 2. Логирует название функции, аргументы и результат
# 3. Выводит в формате: "[LOG] Функция: {name}, Аргументы: {args}, Результат: {result}"
#
# Пример:
# @logger
# def add(a, b):
#     return a + b
#
# add(5, 3)
# Вывод:
# [LOG] Функция: add, Аргументы: (5, 3), Результат: 8
# Результат: 8
#
# @logger
# def greet(name):
#     return f"Hello, {name}!"
#
# greet("Alice")
# Вывод:
# [LOG] Функция: greet, Аргументы: ('Alice',), Результат: Hello, Alice!
# Результат: Hello, Alice!

# def loger(func):
#     def wraper(*args, **kwargs):
#         v={
#         }
#         c = args[0]+args[1]
#         v.update(num=args,results=c)
#         print (v)
#         print(f"Result {c}")
#     return wraper

# def loger1(func):
#     def wraper(*args, **kwargs):
#         v={
#         }
#         c = args
#         v.update(num=args,results=c)
#         print (v)
#         print(f"Result {c}")
#     return wraper

# @loger
# def add(a,b):
#     c = a+b
#     print(c)
# @loger1
# def gree(a):
#     print(f"Hello,{a}")

# add(4,6)
# gree("OLEG")


# 1. Напишите функцию calculator(*numbers, **operations)
# 2. *numbers - числа для вычисления
# 3. **operations - операции:
#    - 'sum': выполнить сумму
#    - 'multiply': выполнить произведение
#    - 'power': возвести в степень (указать степень в value)
#    - 'round': округлить до N знаков
#
# Примеры:
# calculator(2, 3, 4, sum=True)
# → Сумма: 9
#
# calculator(2, 3, 4, multiply=True)
# → Произведение: 24
#
# calculator(2, 3, 4, sum=True, round=1)
# → Сумма: 9.0, Округлено до 1 знака
#
# calculator(2, power=3)
# → 2 в степени 3 = 8
#
# Детали:
# - Обработайте ошибки если нет нужной операции
# - Выведите результат в красивом формате
# - Используйте try/except для валидации

# def calculator(*numbers, **assas):
#     if assas.keys()=="sum":
#         print(sum(numbers))

            
# calculator(1,2,3, )



# 1. Напишите функцию concat_strings(*args)
# 2. Объединяет все строки в одну
# 3. Разделяет пробелом
#
# Примеры:
# concat_strings('Hello', 'World') → "Hello World"
# concat_strings('Python', 'is', 'awesome') → "Python is awesome"
# concat_strings('Test') → "Test"

def con(*args):
        a = ()
        a = args
        print(a)
con('Hello', 'World')
