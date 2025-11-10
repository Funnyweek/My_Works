# sum()
# min()
# max()
# sorted()
# reversed()
# len()
# range()
# print()
# list()
# tuple()
# set(), dict(), int()
# input()
# slice()


# enumerate()
# map()
# filter()
# zip()
# all()
# any()
# eval()
# round()
# abs()
# pow()

# a = ['Asel', 'Mansur', 'Alim', 'Jahongir', 'Abdulloh', 'Alexandr', 'Vlad']

# for i, v in enumerate(a):
#     if i % 2 == 0:
#         print(i, v)

# print(list(enumerate(a)))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1
# c = [str(i) for i in a]

# 2
# b = []
# for i in a:
#     b.append(str(i))

# 3
# b = list(map(str, a))

# print(b)
# c = list(map(int, b))
# print(c)

# print(''.join(b))


# def main_pow(x):
#     return x ** 2

# print(main_pow(2))


# numbers = input("Введите числа через пробел: ").split()
# numbers = list(map(int, numbers))
# print(numbers)
# pow_numbers = list(map(lambda x: x ** 2, numbers))
# print(pow_numbers)



# numbers = [1, 2, 6, 3, 8, 5, 9, 4]

# b = []
# for i in numbers:
#     if i > 5:
#         b.append(i)
# print(b)

# b = [i for i in numbers if i > 5]
# print(b)

# def main_f(x):
#     if x % 3 == 0 or x % 5 ==0:
#         return True
# list_filter = list(filter(main_f, numbers))
# print(list_filter)

# list_filter = list(filter(lambda x: x % 3 == 0 or x % 5 ==0 , numbers))
# print(list_filter)





# a = [1,    3,   4,   5]
# b = ['a', 'b', 'c', 'd']

# print(list(zip(a,b)))




# all()
# any()
# eval()
# round()
# abs()


# a = [True, True, False]

# a = [12,3243,345,456,46,46]
# c = [True if i % 2 == 0 else False for i in a]

# print(c)
# print(all(c))
# print(any(c))

# a = -943
# print(abs(a))
# v = 23
# print(-v)

# s = 54.829234
# print(round(s, 2))

# while True: print(eval(input(">>> ")))


# problem1

# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)

# set_values = all([isinstance(value, (int, float, str, tuple)) for value in values])

# set_values = all([1 if type(i) in [str, list, tuple] else 0 for i in values])

# print(set_values)


# def string(obj):
#     vowels = 'aeiouyаеёиоуыэюя'
#     filtered_letters = len(list(filter(lambda letter: letter in vowels, obj.lower())))
#     return f"Количество гласных букв - {filtered_letters}"

# print(string('KJhjflh siuhdfiusdfhishdiшвагыршгцруашцрлрвадлорфыдоварлфыовралодуа'))
# 

# def is_prime(x):
#     for i in range(2, x): 
#         if x % i ==0: return False
#     return True

# print(list(filter(is_prime, range(1, 101))))

