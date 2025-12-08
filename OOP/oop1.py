# # 1. Создайте класс Cat
# # 2. В __init__ сохраняйте: name (имя), age (возраст), color (цвет)
# # 3. Добавьте метод meow(), который возвращает "{name} говорит: Мяу!"
# # 4. Создайте 3 объекта и вызовите метод meow()
# #
# # Примеры:
# # cat1 = Cat("Васька", 3, "черный")
# # print(cat1.meow())  → Васька говорит: Мяу!
# #
# # cat2 = Cat("Мурка", 5, "белый")
# # print(cat2.meow())  → Мурка говорит: Мяу!

# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color

#     def meow(self):
#         return f"{self.name} говорит: Мяу!"

# cat1 = Cat("Васька", 3, "черный")
# print(cat1.meow())

# cat2 = Cat("Мурка", 5, "белый")
# print(cat2.meow())

# cat3 = Cat("Пушок", 7, "серый")
# print(cat3.meow())



# # 1. Создайте класс Student
# # 2. В __init__ сохраняйте: name (имя), grade (класс - 10, 11 и т.д.)
# # 3. Добавьте метод study(), который возвращает "{name} учится в {grade} классе"
# # 4. Создайте 3 объекта и вызовите метод study()
# #
# # Примеры:
# # student1 = Student("Алиса", 10)
# # print(student1.study())  → Алиса учится в 10 классе
# #
# # student2 = Student("Боб", 11)
# # print(student2.study())  → Боб учится в 11 классе

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def study(self):
#         return f"{self.name} учится в {self.grade} классе"

# student1 = Student("Алиса", 10)
# print(student1.study())

# student2 = Student("Боб", 11)
# print(student2.study())

# student3 = Student("Виктор", 12)
# print(student3.study())




#  1. Создайте класс Fruit
# 2. В __init__ сохраняйте: name (название), price (цена)
# 3. Добавьте метод get_info(), который возвращает "{name} стоит {price} тенге"
# 4. Добавьте метод is_cheap(), который:
#    - Возвращает "Дешево" если price < 100
#    - Возвращает "Дорого" если price >= 100
# 5. Создайте 3 объекта и используйте оба метода
#
# Примеры:
# fruit1 = Fruit("Яблоко", 50)
# print(fruit1.get_info())  → Яблоко стоит 50 тенге
# print(fruit1.is_cheap())  → Дешево
#
# fruit2 = Fruit("Манго", 200)
# print(fruit2.get_info())  → Манго стоит 200 тенге
# print(fruit2.is_cheap())  → Дорого


# class Fruit:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def get_info(self):
#         return f"{self.name} стоит {self.price} тенге"

#     def is_cheap(self):
#         if self.price < 100:
#             return "Дешево"
#         else:
#             return "Дорого"

# fruit1 = Fruit("Яблоко", 50)
# print(fruit1.get_info())  # Яблоко стоит 50 тенге
# print(fruit1.is_cheap())  # Дешево

# fruit2 = Fruit("Манго", 200)
# print(fruit2.get_info())  # Манго стоит 200 тенге
# print(fruit2.is_cheap())  # Дорого


# 1. Создайте класс Lamp
# 2. В __init__ сохраняйте: brand (марка), is_on (включена ли - True/False)
# 3. Добавьте метод turn_on(), который:
#    - Устанавливает is_on = True
#    - Возвращает "{brand} включена"
# 4. Добавьте метод turn_off(), который:
#    - Устанавливает is_on = False
#    - Возвращает "{brand} выключена"
# 5. Добавьте метод get_status(), который возвращает:
#    - "Лампа включена" если is_on == True
#    - "Лампа выключена" если is_on == False
# 6. Создайте 2 объекта и используйте все методы
#
# Примеры:
# lamp1 = Lamp("Philips", False)
# print(lamp1.get_status())  → Лампа выключена
# print(lamp1.turn_on())     → Philips включена
# print(lamp1.get_status())  → Лампа включена
# print(lamp1.turn_off())    → Philips выключена
# print(lamp1.get_status())  → Лампа выключена


class Lamp:
    def __init__(self, brand, is_on):
        self.brand = brand
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True
        return f"{self.brand} включена"

    def turn_off(self):
        self.is_on = False
        return f"{self.brand} выключена"

    def get_status(self):
        if self.is_on:
            return "Лампа включена"
        else:
            return "Лампа выключена"

lamp1 = Lamp("Philips", False)
print(lamp1.get_status())  # Лампа выключена
print(lamp1.turn_on())     # Philips включена
print(lamp1.get_status())  # Лампа включена
print(lamp1.turn_off())    # Philips выключена
print(lamp1.get_status())  # Лампа выключена