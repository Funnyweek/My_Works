# Не Изменяемые
int 
float
str
bool
tuple

# Изменяемые
list
set 
dict

# a = [3,4,5,3,3,4,4,5,6,7,7,8,8,9,1,1,1,1,1,6]
# a = list(set(a))
# print(a)



# a = {3,4,5,3,3,4,4,5,6,7,7,8,8,9,6, 0, (2131, ), 123.123, 'asdasdsd' }
# a.add('wqeqwe')
# print(a)


# a = {3,4,5,3,3,4,4,5,6,7,7,8,8,9,6, 0, (2131, ), 123.123, 'asdasdsd' }
# a.remove(3)
# print(a)

# a = {3,4,5, 123.123, 'asdasdsd'}

# a.clear()
# print(a)

# a = set()

# a = {3,4,5, 123.123, 'asdasdsd'}

# a.remove(7)
# a.discard(7)
# print(a)
# print(a.p


# a = {1, 2, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(a.intersection(b))
# print(a.intersection(b))
# print(b.difference_update(a))

# print(b)
# print(b)
#########################################

# a = {1, 2, 4, 5}
# b = {4, 5, 6, 7, 8}
# a.update(b)
# print(a)



# foods = ["Coca-Cola", ['Potato', 'Cheeps']]
# foods = {
#     "drinks": "Coca-Cola",
#     "drinks": "Pepsi",
#     "snacks": ['Potato', 'Cheeps']
# }

# print(foods['drinks'])
# print(foods['snacks'][1])




# foods = {
#     "drinks": "Pepsi",
#     "snacks": ['Potato', 'Cheeps']
# }

# foods.update({'colas': 'Coca-Cola'})
# print(foods)
# foods['eda'] = 'Plov'

# print(foods)
# foods['snacks'].append('Burger')
# print(foods)





foods = {
    "drinks": "Pepsi",
    "snacks": ['Potato', 'Cheeps']
}

# foods.pop('snacks')
# print(foods)

# print(foods.get("drin"))
# print(foods["drin"])


# print(foods.keys(), foods.values(), foods.items())

# for key, value in foods.items():
#     print(f"{key=}, {value=}")

# salaries = {
#     'Aktan': 100,
#     'Sultan': 200,
#     'Aybek': 300,
#     'Jamal': 400,
#     'Abror': 500,
#     'Jamshid': 600,
#     'Ilana': 1000
# }

# print(min(salaries.items(), key=lambda x: x[1]))
# print(max(salaries.items(), key=lambda x: x[1]))
# sum_salay = sum(salaries.values())
# count_salary = len(salaries)

# print(f"Count salary: {count_salary} \nSum salary: {sum_salay} \nAverage salary: {sum_salay / count_salary}")
# import time
# import os




# for i in range(60):
#     for j in range(60):
#         # os.system('clear')
#         # print(f'{i}:{j}')
#         # time.sleep(0.3)





# a = {
#     'kuhnya1': {
#         'stol': 10,
#         'stul': 2
#     },
#     'kuhnya2': {
#         'stol': 10,
#         'stul': 2
#     }
# }

# area = 0
# for i in a:
#     area += sum(a[i].values())
# print(area)


# area = 0
# for i in a:
#     for j in a[i]:
#         print(j, a[i][j])
#         area += a[i][j]

# print(area)


# for i in range(1, 20+1):
#     for j in range(1, 20+1):
#         print(f'{i} ** {j} = {j**i}')
#     print()


# a = [1,2,3,4,5, 6, 7, 7,8,8]

# c = [{i:i**2} for i in a if i % 2 == 0]

# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append({i:i**2})

# print(b)
# print(c)

# a = []
# for i in range(100):
#     a.append(i)

# print(a)

# b = [i for i in range(100)]
# print(b)

# c = list(range(100))
# print(c)



# a = []
# for i in range(10):
#     if i % 2 == 0:
#         a.append(0)
#     else:
#         a.append(i)
# print(a)

# b = [0 if i % 2 == 0 else i for i in range(10)]
# print(b)

# c = [i for i in range(10) if i % 2 != 0]
# print(c)


# a = 0 if 5 % 5 != 0 else 5

# print(a)

# s = {i:i*2 for i in range(10)}

# print(s)

# cities = []
# current_city = None
# while True:
#     action = int(input("Выберите действие: \n"
#         " 1. Добавить новый город \n"
#         " 2. Отобразить список городов \n"
#         " 3. Заменить город \n"
#         " 4. Удалить город \n"
#         " 5. Посетить следующий город \n"
#         " 6. Выход \n"))
#     if action == 6:
#         print("Программа завершает работу!")
#         break
#     elif action == 1:
#         city = input("Введите название города: ")
#         if city in cities:
#             print(f"б. Такой город уже есть!, {cities[city]}")
#         elif city.isdigit():
#             print("в. Некорректное название!")
#         else:
#             cities.append(city)
#             print("a. Город добавлен!")
#     elif action == 2:
#         if cities == []:
#             print("Нет городов для вывода, заполните лист!")
#         else:
#             print(f"Список городов: \n", cities)
#     elif action == 3:
#         if cities == []:
#             print("Нет городов для изменения, заполните лист!")
#         else:
#             choice = int(input(f"Выберите город по номеру для замены (счет начинается с 0):{cities}: "))
#             city = input("Введите новый город: ")
#             print(f"Новый город: {city}")
#             if city not in cities:
#                 cities[choice] = city
#                 print("б. Город заменен")
#             elif cities[choice] == city:
#                 print(f"в. Такой город уже есть! {city} - 3")
#             elif city.isdigit() == True:
#                 print("г. Некорректное название!")
#     elif action == 4:
#         if cities == []:
#             print("Нет городов для удаления, заполните лист!")
#         else:
#             choice2 = int(input(f"Выберите город по номеру для удаления (счет начинается с 0):{cities}: "))
#             city = input("Введите название города, который вы хотите удалить: ")
#             if city != cities[choice2]:
#                 print("а. Текущий город отсутвует")
#             elif city.isdigit() == True:
#                 print("б. Некорректное название!")
#             elif city == cities[choice2]:
#                 cities.pop(choice2)
#                 print("в. Город удален!") 
#     elif action == 5:
        # if cities == []:
        #     print("Нет городов для выбора, заполните лист!")
        # else:
        #     city_choice = int(input(f"В каком городе вы хотите находится в данный момент? (счет начинается с 0) {cities}: "))
        #     print(f"На данный момент мы находимся в городе: {cities[city_choice]}")
            
        #     choice3 = int(input(f"Выберите, какой город вы хотите посетить следующим? (счет начинается с 0):{cities}: "))
            
        #     city = input("Введите название города, который вы хотите Посетить: ")
            
        #     current_city = cities[choice3]


        #     if city == cities[choice3]:
        #         print(f"а. Сейчас мы находися в городе: {cities[choice3]}")
        #     elif city.isdigit() == True:
        #         print("б. Некорректное название!")
        #     elif city != cities[choice3]:
        #         print("в. Вы выбрали разные значения пары значение/название!")



