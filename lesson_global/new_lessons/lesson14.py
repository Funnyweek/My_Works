
import requests
# import random

# def sort(func):
#     def war():
#         v = func()
#         v.sort()
#         return v
#     return war
    


# @sort
# def generate():
#     a = []
#     for _ in range(10):
#         c = random.randint(1,10)
#         a.append(c)
#     return a
        
# print(generate())



# Задача 1: Декоратор для добавления префикса

# 1. Создайте декоратор add_prefix(func)
# 2. Декоратор должен добавить "★ " перед результатом функции
# 3. Примените декоратор к функции greeting(name)
# 4. Функция greeting возвращает "Привет, {name}!"
#
# Пример:
# @add_prefix
# def greeting(name):
#     return f"Привет, {name}!"
#
# greeting('Алиса') → "★ Привет, Алиса!"
# greeting('Боб') → "★ Привет, Боб!"


# def add_prefix(func):
#     def wrapper(name):
#         return f"★ {func(name)}"
#     return wrapper



# @add_prefix
# def gree(name):
#     return f"Привет, {name}!"
# print(gree('Алиса'))




# Задача 2: Декоратор для проверки положительного числа

# 1. Создайте декоратор check_positive(func)
# 2. Декоратор должен проверить что число > 0
# 3. Если число положительное — вызвать функцию
# 4. Если число отрицательное — вернуть "Ошибка: число должно быть положительным"
# 5. Примените к функции square(x)
#
# Пример:
# @check_positive
# def square(x):
#     return x ** 2
#
# square(5) → 25
# square(-3) → "Ошибка: число должно быть положительным"




# def num(func):
#     def wr(a):
#         if a > 0:
#             return a**2
#         else:
#             return "eror"
#     return wr


# @num 
# def w(a):
#     return(w)
# print(w(-223))
        
        
# Задача 3: Декоратор для преобразования в ВЕРХНИЙ РЕГИСТР

# 1. Создайте декоратор uppercase(func)
# 2. Декоратор должен преобразовать результат в ВЕРХНИЙ РЕГИСТР
# 3. Используйте .upper()
# 4. Примените к функции message(text)
#
# Пример:
# @uppercase
# def message(text):
#     return text
#
# message('привет мир') → "ПРИВЕТ МИР"
# message('hello') → "HELLO"



# def upper(func):
#     def wr(a):
#         a = func(a)
#         return a.upper()
#     return wr

# @upper
# def les(a):
#     return a
# print(les("hello"))




# Задача 4: Декоратор для подсчета вызовов

# 1. Создайте декоратор count_calls(func)
# 2. Декоратор должен подсчитать количество вызовов функции
# 3. Перед каждым вызовом выводить "Вызов номер X"
# 4. Примените к функции multiply(a, b)
#
# Пример:
# @count_calls
# def multiply(a, b):
#     return a * b
#
# multiply(3, 4)  → Вызов номер 1 / 12
# multiply(5, 6)  → Вызов номер 2 / 30
# multiply(2, 7)  → Вызов номер 3 / 14



# def num(func):
#     cou = [0]
#     def wr(b, n):
#         func = b, n 
#         cou[0] += 1
#         c = b*n
#         print(cou)
#         return c
#     return wr

# @num
# def a(v, d):
#     return(v,d)



# print(f'{a(2, 5)}')
# print(f'{a(2, 5)}')
# print(f'{a(2, 5)}')





# Задача 5: Декоратор для добавления скобок вокруг результата

# 1. Создайте декоратор add_brackets(func)
# 2. Декоратор должен обвести результат в скобки: [результат]
# 3. Примените к функции concat(a, b)
#
# Пример:
# @add_brackets
# def concat(a, b):
#     return a + b
#
# concat('hello', ' world') → "[hello world]"
# concat('Python', ' is cool') → "[Python is cool]"
# concat('1', '2') → "[12]"



# def add(func):
#     def wr(*args, **kwargs):
#         r = func(*args, **kwargs)
#         return(f"[{r}]")
#     return wr
# @add
# def name(a, b):
#     return(a+b)


# print(name('hello',' world'))

