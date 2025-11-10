int 
float
bool
str

# a = 'int'
# a = "float"
# a = ''' ksdhkfjhsdjkfhkh '''
# a = """ ksdhkfjhsdjkfhkh """


# n = True
# n = 1
# n = 2 == 2 
# n = True or False
# n = True and True
# n = not False
# n = "sajhkh" 
# n = "True".startswith("T")
# n = "True".endswith("e")
# n = "True".isalpha()
# n = "234".isdigit()

# if n:
#     print("true")
# else:
#     print("false")


# n = 342231

# if n % 2 == 0:
#     print("Делится на 2")
# else:
#     print("Не делится на 2")

# if n % 3 == 0:
#     print("Делится на 3")
# else:
#     print("Не делится на 3")

# if n % 4 == 0:
#     print("Делится на 4")
# else:
#     print("Не делится на 4")


# a = 0

# if a > 0:
#     print("Положительное")  
# else:
#     print("Число <= 0")






# a = 6

# if a % 2 == 0:
#     print("четное")
#     if a == 6:
#         print("Это число 6")
#     else:
#         print("Это число не 6")
# else:
#     print("Это число нечетное")

# a = "hello world world hello"
# mid = len(a) // 2
# b = a[:mid][::-1] + a[mid:]
# print(b)

# PROBLEM 15:
# Есть три числа 17391, 546, 934.
# Если каждое из них поделить на 17 по модулю, где остаток меньше всего?


# a = 17391 % 17
# b = 546 % 17
# c = 934 % 17

# if c > a and a < b:
#     print(a , 'naimenshii ostatok u chisla 17391')
# elif a > b and b < c:
#     print('naimenshii ostatok u chisla 546')
# else:
#     print('naimenshii ostatok u chisla 934')




# aaa = 5
# aab = 6
# aac = 7

# if aaa >= aab and aaa >= aac:
#     print("Максимальное число а: " + str(aaa))
# elif aab >= aaa and aab >= aac:
#     print("Максимальное число b: " + (aab))
# else:
#     print("Максимальное число c: " + str(aac))

# a = int(input("Enter: "))
# b = int(input("Enter: "))
# c = int(input("Enter: "))

# min_num = a if a < b < c else b if b < a < c else c
# max_num = a if a > b > c else b if b > a > c else c

# print(f"min_num = {min_num} max_num = {max_num}")

# if a > b > c:
#     print("А больше всех", a)
# elif b > a > c:
#     print("Б больше всех", b)
# else:
#     print ("С больше всех", c)

# if a < b < c:
#     print("А меньше всех", a)
# elif b < a < c:
#     print("Б меньше всех", b)
# else:
#     print ("С меньше всех", c)



# a = int(input("Enter: "))
# n = a if a % 2 == 0 else a + 1
# print(n)


# a = int(input("Год рождения: "))
# if 2023-a>=18:
#     print ("Совершеннолетний")
# elif 2023-a<=4:
#     print ("Несовершеннолетний")


# year_of_birth = int(input("Ввведите ваш год рождения: "))

# if 2023 - year_of_birth >= 18:
#     print("Совершеннолетний")
# elif 2023 - year_of_birth <= 4:
#     print("Ребенок")
# else:
#     print("Несовершеннолетний")

# a = -23
# if a > 0:
#     print(-a)
# else:
#     print(a)

# y = int(input("Enter: "))

# if y == 2023:
#     print("Current year")
# elif y > 2023:
#     print("Future")
# else:
#     print("Past")

# from math import pi
# from math import sqrt

# a = int(input("Enter: "))
# b = int(input("Enter: "))
# c = sqrt(a ** 2 + b ** 2)

# print(c)
