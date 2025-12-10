# 1. Создайте базовый класс Shape (Фигура)
#    Атрибуты: name (название)
#    Методы: 
#    - get_info() - возвращает "{name} - это фигура"
#    - get_area() - возвращает 0 (базовая реализация)
#
# 2. Создайте дочерний класс Circle (Круг)
#    Атрибуты: radius (радиус)
#    Переопределите:
#    - get_info() - возвращает "{name} с радиусом {radius}"
#    - get_area() - вычисляет площадь круга (π * r²)
#    Используйте math.pi
#
# 3. Создайте дочерний класс Rectangle (Прямоугольник)
#    Атрибуты: width (ширина), height (высота)
#    Переопределите:
#    - get_info() - возвращает "{name} {width}x{height}"
#    - get_area() - вычисляет площадь (width * height)
#
# 4. Создайте дочерний класс Triangle (Треугольник)
#    Атрибуты: base (основание), height (высота)
#    Переопределите:
#    - get_info() - возвращает "{name} с основанием {base} и высотой {height}"
#    - get_area() - вычисляет площадь ((base * height) / 2)
#
# 5. Создайте по одному объекту каждой фигуры
# 6. Выведите информацию о каждой фигуре
# 7. Выведите площадь каждой фигуры
#
# # Пример использования:
# # circle = Circle("Круг", 5)
# # print(circle.get_info())   # Круг с радиусом 5
# # print(f"Площадь: {circle.get_area():.2f}")  # Площадь: 78.50
# #
# # rect = Rectangle("Прямоугольник", 4, 5)
# # print(rect.get_info())     # Прямоугольник 4x5
# # print(f"Площадь: {rect.get_area()}")  # Площадь: 20

# class Shape:
#     def __init__(self,name):
#         self.name = name
# class Circle(Shape):
#     def __init__(self, name, rad):
#         super().__init__ (name)
#         self.rad = rad
#     def rad1(self):
#         print(f"{3.14 * self.rad} = {3.14}* {self.rad}")
# class Rectangle(Shape):
#     def __init__(self, name, h, w):
#         super().__init__ (name)
#         self.h = h
#         self.w = w
#     def r(self):
#         print(self.h*self.w)
# class Triangle(Shape):
#     def __init__(self, name, h, w):
#         super().__init__ (name)
#         self.h = h
#         self.w = w
#     def r(self):
#         print((self.h*self.w)/2)
    
    
    
# a = Circle("circle", 4)
# b = Rectangle('ad', 3,6)
# c = Triangle("1231",1,6)
# a.rad1()
# b.r()
# c.r()





# 1. Создайте базовый класс Employee (Сотрудник)
#    Атрибуты: name (имя), salary (зарплата), position (должность)
#    Методы:
#    - get_info() - возвращает "{name} - {position}, зарплата: {salary}"
#    - get_bonus() - возвращает 10% от зарплаты (зарплата * 0.1)
#
# 2. Создайте дочерний класс Manager (Менеджер)
#    Атрибуты: team_size (размер команды)
#    Переопределите:
#    - get_info() - вызывает super().get_info() + " Команда: {team_size} человек"
#    - get_bonus() - возвращает 20% от зарплаты (зарплата * 0.2)
#
# 3. Создайте дочерний класс Developer (Разработчик)
#    Атрибуты: language (язык программирования)
#    Переопределите:
#    - get_info() - вызывает super().get_info() + " Язык: {language}"
#    - get_bonus() - возвращает 15% от зарплаты (зарплата * 0.15)
#
# 4. Создайте дочерний класс Director (Директор)
#    Переопределите:
#    - get_bonus() - возвращает 30% от зарплаты (зарплата * 0.3)
#
# 5. Создайте по одному объекту каждого типа
# 6. Для каждого выведите:
#    - Информацию (get_info())
#    - Зарплату
#    - Бонус (get_bonus())
#    - Общую зарплату с бонусом
#
# Пример использования:
# emp = Employee("Иван", 100000, "Секретарь")
# print(emp.get_info())              # Иван - Секретарь, зарплата: 100000
# print(f"Бонус: {emp.get_bonus()}")  # Бонус: 10000.0
#
# dev = Developer("Мария", 120000, "Разработчик", "Python")
# print(dev.get_info())  
# # Мария - Разработчик, зарплата: 120000 Язык: Python
# print(f"Бонус: {dev.get_bonus()}")  # Бонус: 18000.0

# class Employee:
#     def __init__(self, name, salary, position):
#         self.name = name
#         self.salary = salary
#         self.position = position

#     def get_info(self):
#         return f"{self.name} - {self.position}, зарплата: {self.salary}"

#     def get_bonus(self):
#         return self.salary * 0.1


# class Manager(Employee):
#     def __init__(self, name, salary, position, team_size):
#         super().__init__(name, salary, position)
#         self.team_size = team_size

#     def get_info(self):
#         return super().get_info() + f" Команда: {self.team_size} человек"

#     def get_bonus(self):
#         return self.salary * 0.2


# class Developer(Employee):
#     def __init__(self, name, salary, position, language):
#         super().__init__(name, salary, position)
#         self.language = language

#     def get_info(self):
#         return super().get_info() + f" Язык: {self.language}"

#     def get_bonus(self):
#         return self.salary * 0.15


# class Director(Employee):
#     def __init__(self, name, salary, position):
#         super().__init__(name, salary, position)

#     def get_bonus(self):
#         return self.salary * 0.3


# emp = Employee("Иван", 100000, "Секретарь")
# mgr = Manager("Ольга", 200000, "Менеджер", 5)
# dev = Developer("Мария", 120000, "Разработчик", "Python")
# dir = Director("Сергей", 300000, "Директор")

# employees = [emp, mgr, dev, dir]

# for e in employees:
#     print("──────────────────────────────")
#     print(e.get_info())
#     print(f"Зарплата: {e.salary}")
#     print(f"Бонус: {e.get_bonus()}")
#     print(f"Общая зарплата с бонусом: {e.salary + e.get_bonus()}")

# 1. Создайте базовый класс Transport (Транспорт)
#    Атрибуты: brand (марка), model (модель), max_speed (максимальная скорость)
#    Методы:
#    - get_info() - возвращает "{brand} {model}, макс скорость: {max_speed} км/ч"
#    - move() - возвращает "Транспортное средство движется"
#
# 2. Создайте дочерний класс Car (Автомобиль)
#    Атрибуты: fuel_type (тип топлива - бензин, дизель и т.д.)
#    Переопределите:
#    - move() - возвращает "{brand} {model} едет по дороге, топливо: {fuel_type}"
#    - get_info() - вызывает super().get_info() + " Топливо: {fuel_type}"
#
# 3. Создайте дочерний класс Bicycle (Велосипед)
#    Атрибуты: gear_count (количество передач)
#    Переопределите:
#    - move() - возвращает "{brand} {model} едет на {gear_count} передачах"
#    - get_info() - вызывает super().get_info() + " Передач: {gear_count}"
#
# 4. Создайте дочерний класс Boat (Лодка)
#    Переопределите:
#    - move() - возвращает "{brand} {model} плывет по воде"
#
# 5. Создайте по одному объекту каждого типа
# 6. Для каждого выведите:
#    - Информацию
#    - Результат метода move()
#
# Пример использования:
# car = Car("Toyota", "Camry", 200, "бензин")
# print(car.get_info())  # Toyota Camry, макс скорость: 200 км/ч Топливо: бензин
# print(car.move())      # Toyota Camry едет по дороге, топливо: бензин
#
# bike = Bicycle("Giant", "Escape", 40, 21)
# print(bike.move())     # Giant Escape едет на 21 передачах


# class Transport:
#     def __init__(self, brand, model, max_speed):
#         self.brand = brand
#         self.model = model
#         self.max_speed = max_speed

#     def get_info(self):
#         return f"{self.brand} {self.model}, макс скорость: {self.max_speed} км/ч"

#     def move(self):
#         return "Транспортное средство движется"


# class Car(Transport):
#     def __init__(self, brand, model, max_speed, fuel_type):
#         super().__init__(brand, model, max_speed)
#         self.fuel_type = fuel_type

#     def get_info(self):
#         return super().get_info() + f" Топливо: {self.fuel_type}"

#     def move(self):
#         return f"{self.brand} {self.model} едет по дороге, топливо: {self.fuel_type}"


# class Bicycle(Transport):
#     def __init__(self, brand, model, max_speed, gear_count):
#         super().__init__(brand, model, max_speed)
#         self.gear_count = gear_count

#     def get_info(self):
#         return super().get_info() + f" Передач: {self.gear_count}"

#     def move(self):
#         return f"{self.brand} {self.model} едет на {self.gear_count} передачах"


# class Boat(Transport):
#     def __init__(self, brand, model, max_speed):
#         super().__init__(brand, model, max_speed)

#     def move(self):
#         return f"{self.brand} {self.model} плывет по воде"


# # --- Пример использования ---
# car = Car("Toyota", "Camry", 200, "бензин")
# bike = Bicycle("Giant", "Escape", 40, 21)
# boat = Boat("Yamaha", "WaveRunner", 80)

# vehicles = [car, bike, boat]

# for v in vehicles:
#     print("──────────────────────────────")
#     print(v.get_info())
#     print(v.move())

# 1. Создайте базовый класс BankAccount (Банковский счет)
#    Атрибуты: owner (владелец), balance (баланс)
#    Методы:
#    - get_info() - возвращает "{owner}: {balance} тенге"
#    - get_commission() - возвращает 1% от баланса (комиссия за операцию)
#    - withdraw(amount) - снятие денег (баланс -= amount + комиссия)
#    - deposit(amount) - пополнение (баланс += amount)
#
# 2. Создайте дочерний класс SavingsAccount (Сбережения)
#    Переопределите:
#    - get_commission() - возвращает 0.5% от баланса (меньше комиссия)
#    - get_info() - вызывает super().get_info() + " (Сбережения)"
#
# 3. Создайте дочерний класс BusinessAccount (Бизнес счет)
#    Переопределите:
#    - get_commission() - возвращает 2% от баланса (больше комиссия)
#    - get_info() - вызывает super().get_info() + " (Бизнес)"
#
# 4. Создайте по одному счету каждого типа
# 5. Для каждого счета:
#    - Выведите информацию
#    - Пополните на 10000 тенге
#    - Выведите баланс
#    - Снимите 5000 тенге
#    - Выведите новый баланс
#    - Выведите комиссию за последнюю операцию
#
# Пример использования:
# acc = BankAccount("Алиса", 5000)
# print(acc.get_info())              # Алиса: 5000 тенге
# acc.deposit(10000)
# print(acc.get_info())              # Алиса: 15000 тенге
# acc.withdraw(5000)
# print(acc.get_info())              # Алиса: 9850 тенге (5000 + 150 комиссия)
# print(f"Комиссия: {acc.get_commission()}")  # Комиссия: 98.5

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.last_commission = 0  

    def get_info(self):
        return f"{self.owner}: {self.balance} тенге"

    def get_commission(self):
        return self.balance * 0.01

    def withdraw(self, amount):
        commission = self.get_commission()
        total = amount + commission
        if total > self.balance:
            print("Недостаточно средств для снятия")
            return
        self.balance -= total
        self.last_commission = commission

    def deposit(self, amount):
        self.balance += amount
        self.last_commission = 0  


class SavingsAccount(BankAccount):
    def get_commission(self):
        return self.balance * 0.005

    def get_info(self):
        return super().get_info() + " (Сбережения)"


class BusinessAccount(BankAccount):
    def get_commission(self):
        return self.balance * 0.02

    def get_info(self):
        return super().get_info() + " (Бизнес)"


accounts = [
    BankAccount("Алиса", 5000),
    SavingsAccount("Боб", 10000),
    BusinessAccount("Виктор", 20000)
]

for acc in accounts:
    print("──────────────────────────────")
    print(acc.get_info())
    acc.deposit(10000)
    print("После пополнения:", acc.get_info())
    acc.withdraw(5000)
    print("После снятия:", acc.get_info())
    print(f"Комиссия за последнюю операцию: {acc.last_commission:.2f}")

