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

list = ['python', 'javascript', 'go', 'rust', 'java', 'cpp']
a = []
v= []
word = max(list, key=len)
print(word)
word_1 = min(list, key=len)
print(word_1)
print("----------------")
for s in list:
    s = list.index(s)
    print(f"{list[s][0]}")
    print(f"{list[s][-1]}")
    print(f"{list[s]} {len(list[s])}")
for d in list:
    c = d.capitalize()
    a.append(c)
print(a)
for m in list:
    if "p" in m:
        v.append(m)
print(v)