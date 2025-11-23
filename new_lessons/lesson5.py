# list = ['banana', 'apple', 'cherry', 'date', 'elderberry']
# b = []
# C = ("a, e, i, o, u, y, A, E, I, O, U, Y")
# list.sort()
# print(list)
# list.reverse()
# print(list)

# for a in list:
#     print(a.upper())
#     for letter in C:
#         if a.startswith(letter):
#             b.append('a')
#             break

# print(len(b))


# list = [" hello ", " hi ", " bye "]
# word = []
# word_1 = ""
# for word_edit in list:
#     word_edit = word_edit.strip()
#     word.append(word_edit)
# print(word)
# print("_".join(word))

# list_num = [1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
# count = 0
# indices = []
# for i in range(len(list_num)):
#     if list_num[i] == 5:
#         indices.append(i)
# print(list_num.count(5))
# print(indices)
# list_num.remove(5)
# print(list_num)


# names = ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# for name in range(len(names)):
#    print(name, names[name])
# print(names.index('Виктор'))
# names.insert(2, ' Edutyq')
# for name in range(len(names)):
#    print(name, names[name])

# numbers = [2, 4, 6, 8, 10, 12, 15, 18, 20]
# list_5 = []
# for number in numbers:
#     print(number * 5)
# print("----------------")
# for number_2 in numbers:
#     print(number_2 ** 2)
# print("----------------")
# for number_3 in numbers:
#     if number_3 % 3 == 0:
#         list_5.append(number_3)
# print(list_5)

# list = ['python', 'javascript', 'go', 'rust', 'java', 'cpp']
# a = []
# v= []
# word = max(list, key=len)
# print(word)
# word_1 = min(list, key=len)
# print(word_1)
# print("----------------")
# for s in list:
#     s = list.index(s)
#     print(f"{list[s][0]}")
#     print(f"{list[s][-1]}")
#     print(f"{list[s]} {len(list[s])}")
# for d in list:
#     c = d.capitalize()
#     a.append(c)
# print(a)
# for m in list:
#     if "p" in m:
#         v.append(m)
# print(v)


# Задача 8: Комплексная работа с методами

# Создайте список: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 1. Отсортируйте список
# 2. Разверните в обратном порядке
# 3. Подсчитайте все элементы
# 4. Подсчитайте сколько раз встречается число 5
# 5. Найдите индекс первого числа 1
# 6. Удалите первое число 1
# 7. Выведите список после каждой операции

# list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# list.sort()
# print(list)
# list.reverse()
# print(list)
# print(len(list))
# print(list.count(5))
# print(list.index(1))
# list.remove(1)
# print(list)


# Задача 9: Поиск и фильтрация текста

# Создайте список фраз:
# ['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']
# 1. Найдите все фразы, которые содержат букву 'о'
# 2. Создайте новый список фраз длиной > 20 символов
# 3. Замените все пробелы на подчеркивания в каждой фразе
# 4. Создайте новый список с первым словом каждой фразы
# 5. Подсчитайте общее количество слов во всех фразах


# list = ['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']
# list_1 = []
# for i in list:
#     if "о" in i:
#         list_1.append(i)
# print(list_1)
# list_2 = []
# for i in list:
#     if len(i) > 20:
#         list_2.append(i)
# print(list_2)
# list_3 = []
# for i in list:
#     i = i.replace(" ", "_")
#     list_3.append(i)
# print(list_3)
# list_4 = []
# for i in list:
#     i = i.split(" ")
#     list_4.append(i[0])
# print(list_4)
# list_5 = []
# for i in list:
#     i = i.split(" ")
#     list_5.append(len(i))
# print(sum(list_5))

# Задача 10: Вложенные циклы и комбинирование данных

# Создайте списки:
# numbers = [1, 2, 3, 4]
# letters = ['a', 'b', 'c']
#
# 1. Создайте новый список, где каждое число соединено с каждой буквой
#    Результат: ['1a', '1b', '1c', '2a', '2b', '2c', ...]
#
# 2. Создайте новый список со строками "число-буква" для пар:
#    ['1-a', '2-b', '3-c', '4-?']
#    (если букв меньше, пропустите оставшиеся числа)
#
# 3. Для каждой пары выведите информацию
#
# 4. Используйте extend() для объединения списков


numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c']
a = []
b = []
for i in numbers:
    for j in letters:
        a.append(i)
        b.append(j)
print(a)
print(b)
for i in range(len(a)):
    print(f"{a[i]}-{b[i]}")