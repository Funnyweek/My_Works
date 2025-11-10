#1
ponits = 0

# for num in range(1, 10+1):
#     print(num)

ponits += 1

#2

# words = ["bmw", "mecedes", "subaru", "suzuki", "nissan"]

# for i in words:
#     if len(i) > 5:
#         print(i)

ponits += 1

#3

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
ponits += 1

# #4
# user_str = input("Enter a word: ")
# reversed_str = "".join(reversed(list(user_str)))
# # reversed_str = ''.join(reversed(list(user_str)))
# print(reversed_str)

ponits += 1



#5


# numbers = [24,23,15,67,45,90,74,36,37,46]

# for i in numbers:
#     if i % 3 == 0:
#         print(i)
ponits += 0.5


#6

# text = input('Введите слово: ')

# if text == text[::-1]:
#     print('Это слово палиндром')
# else:
#     print('Это слово не палиндром')

ponits += 1


#7. 

# text = input('Введите предложение: ')
# print(text.upper())

ponits += 1

#8.
# p = []
# for i in range(1, 21):
#      p.append(i)
#      if i % 2 == 0 and i % 3 != 0:
#          print(i)
# print(p)
ponits += 1


#9


# sum_numbers = 0
# for i in range(1, 101):
#     sum_numbers += i
# print(sum_numbers)

ponits += 1
#10

# s = input("Введите слово: ")
# s = s.split(" ")
# for i in s:
#     print(i)

ponits += 1
#  (Второй блок)


#1

# words = ['Anna', 'civic', 'kayak', 'Level', 
# 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 
# 'еще', 'кабак', 'шалаш', 'лишил','language', 
# 'which', 'means', 'vendor', 'слова', 'фраза', 
# 'введите', 'слово', 'кнопку',]
# for i in words:
#     if i == i[::-1]:
#         print(i)

ponits += 1

#2
# sum = 0
# for i in range (0,1001):
#     if i % 3 == 0 or i % 5 == 0:
#         sum+=i
# print(sum)

ponits += 1

#3

# str = "4729461084"
# a = 0

# for i in str:
#     if i.isdigit():
#         a += int(i)

# print(a)
ponits += 1





        
#4

# while True:
#     a = int(input("1 san = "))
#     b = int(input("2 san = "))
#     c = input("amaldar = ")
#     if c == "+":
#         print(a + b)
#     elif c == "-":
#         print(a - b)
#     elif c == "*":
#         print(a * b)
#     elif c == "/":
#         if a == 0 or b == 0:
#             print("error")
#         else: print(a / b)
#     elif c == "%":
#         print(a % b)
#     elif c == "":
#         print(a,b)
#     elif c == "//":
#         print(a // b)
#     else: print("error")
#     p = input("Вы хотите выйти = Y/N: ")
#     if p == "N": continue
#     elif p == "Y": break

ponits += 0.8

#5

# q = int(input("Введите число = "))
# for i in range(1, q+1):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)
ponits += 0


#6

# list = ["Apple", "banana", "orange", "lemon", "grape","iren"]
# letter = ('a', 'e', 'i', 'o', 'u','y')
# count = 0

# for i in list:
#     if i.startswith(letter):
#         count += 1
#         print(i)

ponits += 1


#7

# solem = input('Enter: ')
# solem_1 = solem.split(" ")
# per = len(solem_1[0])
# for i in solem_1:
#     if per < len(i):
#         print(i)

ponits += 1


# 8

# sum = 0
# solem = input()
# solem_1 = solem.split(".")
# sum_o = len(solem_1)
# for i in solem_1:
#     soz = i.split(" ")
#     sum += len(soz)
# print(sum/sum_o)
# "Программирование - это интересная и творческая деятельность. В программировании используются различные языки программирования. Python - один из самых популярных языков программирования."

ponits += 1
#9

# soz = input(" = ")
# list_s = set(soz)
# #считаем буквы
# arip = []
# for i in list_s:
#     arip.append((soz.count(i), i))
# arip.sort(reverse=True)
# print(arip)
# print(arip[0][1], arip[0][0])


ponits += 0.8









# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 
#          'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 
#          'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
# max = int(len(words[0]))
# for i in words:
#     if len(i) > max:
#         max = len(i)
#         max_s = i
# print("слово", max_s, ", самый длинный, состоит из = ", max,  " слов")


ponits += 1

from team1_2 import ponits as ponits_team1
import time
import os

for i in range(5, 0, -1):
    os.system("clear")
    print(i)
    time.sleep(1)



if ponits_team1 > ponits:
    print('Team 1 WIN', ponits_team1)
elif ponits == ponits_team1:
    print('Nichia Team')
else:
    print('Ibragim WIN', ponits, ponits_team1)


