# def sum(a, c):
#     return a + c
# b = int(input('>>>'))
# d = int(input('>>>'))

# z = sum(b , d)
# print(z) 

# print(z +  35)

# l = input('>>>')
# x = 'sadsadasdasdsadsadasd'
# z = input(">>>>>>>>")
# def ount(text):
#     q = 0
#     for i in text:
#         q += 1
#     return q
# print(ount(l))
# print(ount(x))
# print(ount(z))



# # Задача 2: Конвертер температуры

# # 1. Напишите функцию celsius_to_fahrenheit(celsius)
# # 2. Формула: F = C * 9/5 + 32
# # 3. Функция должна возвращать температуру в Фаренгейтах
# # 4. Вызовите функцию для температур: 0, 25, 100, -40
# #
# # Пример:
# # celsius_to_fahrenheit(0) → 32
# # celsius_to_fahrenheit(25) → 77.0
# # celsius_to_fahrenheit(100) → 212.0


# def celsiu(a: int):
#     return a * 9.5 + 32
# v = int(input(">>>"))
# print(celsiu(v))



# Задача 3: Проверка четности

# 1. Напишите функцию is_even(num), которая проверяет четность
# 2. Возвращает True если число четное, False если нечетное
# 3. Вызовите функцию для чисел: 4, 7, 10, 15, 20
#
# Пример:
# is_even(4) → True
# is_even(7) → False
# is_even(10) → True

# def even(numbers):
#     if numbers % 2 == 0:
#          return "True"
#     else:
#          return "Flase"
# print(even(4))
# print(even(7))



    # Задача 4: Подсчет гласных букв

# 1. Напишите функцию count_vowels(text)
# 2. Подсчитайте количество гласных букв (а, е, и, о, у, я)
# 3. Используйте цикл for для проверки каждого символа
# 4. Вызовите функцию для текстов: "hello", "Python", "яблоко"
#
# Пример:
# count_vowels("hello") → 2 (e, o)
# count_vowels("Python") → 1 (o)
# count_vowels("яблоко") → 3 (я, о, о)




# def cound(text: str):
#     a = "aeiоuаеiouяыэюё"
#     c = 0 
#     for i in text.lower():
#         if i in a: 
#             c += 1
#     return c
# print("hello →", cound("hello"))   
# print("Python →", cound("Python")) 
# print("яблоко →", cound("яблоко")) 



# Задача 5: Квадрат числа

# 1. Напишите функцию square(x), которая возвращает квадрат числа
# 2. Вызовите функцию для чисел: 2, 3, 5, 10
# 3. Выведите результаты
#
# Пример:
# square(2) → 4
# square(3) → 9
# square(5) → 25

# def sudo(n):
#     return n ** 2
# print(sudo(2))


# Задача 6: Проверка палиндрома

# 1. Напишите функцию is_palindrome(text)
# 2. Проверьте является ли текст палиндромом (читается одинаково в обе стороны)
# 3. Возвращает True если палиндром, False если нет
# 4. Вызовите функцию для: "радар", "уровень", "привет", "топот"
#
# Пример:
# is_palindrome("радар") → True
# is_palindrome("уровень") → True
# is_palindrome("привет") → False
# is_palindrome("топот") → True


# def a(n):
#     if n[::-1] == n:
#         return('true')
#     else:
#         return("NO")
# print(a('radar'))



# Задача 7: Максимум из двух чисел

# 1. Напишите функцию max_of_two(a, b), которая возвращает большее число
# 2. Не используйте встроенную функцию max()
# 3. Используйте if/else
# 4. Вызовите функцию для пар: (5, 9), (15, 3), (10, 10)
#
# Пример:
# max_of_two(5, 9) → 9
# max_of_two(15, 3) → 15
# max_of_two(10, 10) → 10



# def a(v, c):
#     if v > c:
#         return v
#     else:
#         return c
# print(a(4,6))



# Задача 8: Скидка на покупку

# 1. Напишите функцию apply_discount(price, discount_percent)
# 2. Функция должна рассчитать цену со скидкой
# 3. Возвращает новую цену
# 4. Вызовите функцию для цен: 1000, 500, 2500 со скидками 10%, 20%, 15%
#
# Пример:
# apply_discount(1000, 10) → 900 (скидка 10%)
# apply_discount(500, 20) → 400 (скидка 20%)
# apply_discount(2500, 15) → 2125 (скидка 15%)



# def a(b):
#     if b >= 1000:
#         b = b - b*15/100
#         return b
#     elif b <1000 and b >=500:
#         b = b - b*10/100
#         return b
#     elif b < 500 and b >= 0:
#         b = b - b*5/100
#         return b 
# print(a(100))


# Задача 9: Умножение трех чисел

# 1. Напишите функцию multiply_three(a, b, c), которая возвращает произведение
# 2. Функция должна умножить все три числа
# 3. Вызовите функцию для разных комбинаций
#
# Пример:
# multiply_three(2, 3, 4) → 24
# multiply_three(5, 2, 3) → 30
# multiply_three(1, 1, 1) → 1

# def a(c, v ,b):
#     return (c * v * b)
# print(a(3, 5, 17))


# Задача 10: Возрастная категория

# 1. Напишите функцию get_age_category(age)
# 2. Возвращает категорию по возрасту:
#    - Если < 13: "Ребенок"
#    - Если 13-17: "Подросток"
#    - Если 18-65: "Взрослый"
#    - Если > 65: "Пенсионер"
# 3. Вызовите функцию для возрастов: 8, 15, 25, 70
#
# Пример:
# get_age_category(8) → "Ребенок"
# get_age_category(15) → "Подросток"
# get_age_category(25) → "Взрослый"
# get_age_category(70) → "Пенсионер"

# def a(b):
#     if b <= 13:
#         return 'reb'
#     elif b > 13 and b <=17:
#         return 'pod'
#     elif b > 17 and b <= 65:
#         return "vzr"
#     else:
#         return "pensia"
# print(a(44))
