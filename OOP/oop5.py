# 1. Создайте базовый класс Notification (Уведомление)
#    Атрибуты: title (заголовок), message (сообщение)
#    Методы:
#    - send() - абстрактный метод (должен быть переопределен)
#
# 2. Создайте дочерние классы:
#
#    EmailNotification - отправка по email
#    - send() возвращает "Email: {title} | {message}"
#
#    SMSNotification - отправка по SMS
#    - send() возвращает "SMS: {title} {message}"
#
#    PushNotification - отправка push-уведомления
#    - send() возвращает "Push: 🔔 {title} - {message}"
# #
# #    TelegramNotification - отправка в Telegram
# #    - send() возвращает "Telegram: {title}\n{message}"
# #
# # 3. Создайте список разных уведомлений
# # 4. Используя цикл, отправьте ВСЕ уведомления
# #    (полиморфизм - один цикл для всех типов!)
# #
# # Пример использования:
# # 
# # email = EmailNotification("Новый заказ", "У вас новый заказ #123")
# # sms = SMSNotification("Подтверждение", "Код: 12345")
# # push = PushNotification("Скидка", "Скидка 50% на все товары")
# # telegram = TelegramNotification("Напоминание", "Не забудьте о встречи!")
# #
# # notifications = [email, sms, push, telegram]
# #
# # for notification in notifications:
# #     print(notification.send())
# #
# # Вывод:
# # Email: Новый заказ | У вас новый заказ #123
# # SMS: Подтверждение Код: 12345
# # Push: 🔔 Скидка - Скидка 50% на все товары
# # Telegram: Напоминание
# # Напоминание о встречи!


# class Notification:
#     def __init__(self, title, message):
#         self.title = title
#         self.message = message

#     def send(self):
#         pass


# class EmailNotification(Notification):
#     def send(self):
#         return f"Email: {self.title} | {self.message}"


# class SMSNotification(Notification):
#     def send(self):
#         return f"SMS: {self.title} {self.message}"


# class PushNotification(Notification):
#     def send(self):
#         return f"Push: 🔔 {self.title} - {self.message}"


# class TelegramNotification(Notification):
#     def send(self):
#         return f"Telegram: {self.title}\n{self.message}"
    

# email = EmailNotification("Новый заказ", "У вас новый заказ #123")
# sms = SMSNotification("Подтверждение", "Код: 12345")
# push = PushNotification("Скидка", "Скидка 50% на все товары")
# telegram = TelegramNotification("Напоминание", "Не забудьте о встречи!")

# notifications = [email, sms, push, telegram]

# for notification in notifications:
#     print(notification.send())



# 1. Создайте базовый класс Payment (Оплата)
#    Атрибуты: amount (сумма), description (описание)
#    Методы:
#    - process() - обрабатывает платеж (полиморфный метод)
#    - get_info() - информация о платеже
#
# 2. Создайте дочерние классы платежных систем:
#
#    CreditCardPayment - оплата кредитной картой
#    - process() возвращает f"Платеж {amount} тенге обработан кредитной картой"
#    - get_info() возвращает f"Кредитная карта: {amount} тенге - {description}"
#
#    MobileWalletPayment - оплата мобильным кошельком
#    - process() возвращает f"Платеж {amount} тенге обработан мобильным кошельком"
#    - get_info() возвращает f"Мобильный кошелек: {amount} тенге - {description}"
#
#    BankTransferPayment - оплата банковским переводом
#    - process() возвращает f"Платеж {amount} тенге переведен банком"
#    - get_info() возвращает f"Банковский перевод: {amount} тенге - {description}"
#
#    CryptoPayment - оплата криптовалютой
#    - process() возвращает f"Платеж {amount} тенге принят в крипто"
#    - get_info() возвращает f"Крипто: {amount} тенге - {description}"
#
# 3. Создайте список платежей разными способами
# 4. Обработайте ВСЕ платежи используя ОДИН цикл (полиморфизм!)
# 5. Посчитайте общую сумму всех платежей
#
# Пример использования:
#
# payment1 = CreditCardPayment(5000, "Покупка товара")
# payment2 = MobileWalletPayment(2000, "Пополнение счета")
# payment3 = BankTransferPayment(10000, "Зарплата")
# payment4 = CryptoPayment(3000, "Инвестиция")
#
# payments = [payment1, payment2, payment3, payment4]
#
# # Обработка всех платежей одинаково
# for payment in payments:
#     print(payment.get_info())
#     print(payment.process())
#     print()
#
# # Общая сумма
# total = sum(p.amount for p in payments)
# print(f"Общая сумма платежей: {total} тенге")


# class Payment:
#     def __init__(self, amount, description):
#         self.amount = amount
#         self.description = description

#     def process(self):
#         pass

#     def get_info(self):
#         pass


# class CreditCardPayment(Payment):
#     def process(self):
#         return f"Платеж {self.amount} тенге обработан кредитной картой"

#     def get_info(self):
#         return f"Кредитная карта: {self.amount} тенге - {self.description}"


# class MobileWalletPayment(Payment):
#     def process(self):
#         return f"Платеж {self.amount} тенге обработан мобильным кошельком"

#     def get_info(self):
#         return f"Мобильный кошелек: {self.amount} тенге - {self.description}"


# class BankTransferPayment(Payment):
#     def process(self):
#         return f"Платеж {self.amount} тенге переведен банком"

#     def get_info(self):
#         return f"Банковский перевод: {self.amount} тенге - {self.description}"


# class CryptoPayment(Payment):
#     def process(self):
#         return f"Платеж {self.amount} тенге принят в крипто"

#     def get_info(self):
#         return f"Крипто: {self.amount} тенге - {self.description}"
    

# payments = [
#     CreditCardPayment(5000, "Покупка товара"),
#     MobileWalletPayment(2000, "Пополнение счета"),
#     BankTransferPayment(10000, "Зарплата"),
#     CryptoPayment(3000, "Инвестиция")
# ]

# for payment in payments:
#     print(payment.get_info())
#     print(payment.process())
#     print()

# total = sum(p.amount for p in payments)
# print(f"Общая сумма платежей: {total} тенге")


# 1. Создайте базовый класс Animal (Животное)
#    Атрибуты: name (имя), age (возраст)
#    Методы:
#    - speak() - издает звук (полиморфный)
#    - eat(food) - ест пищу (полиморфный)
#    - get_info() - информация о животном
#
# 2. Создайте дочерние классы животных:
#
#    Lion (Лев) наследует Animal
#    - speak() возвращает f"{name} рычит: РРРРР!"
#    - eat() возвращает f"{name} ест {food}" (если это мясо)
#    - get_info() возвращает f"Лев {name}, {age} лет"
#
#    Elephant (Слон) наследует Animal
#    - speak() возвращает f"{name} трубит: ТУ-У-У!"
#    - eat() возвращает f"{name} ест {food}" (если это растения)
#    - get_info() возвращает f"Слон {name}, {age} лет"
#
#    Parrot (Попугай) наследует Animal
#    - speak() возвращает f"{name} кричит: Привет! Привет!"
#    - eat() возвращает f"{name} ест {food}" (если это семечки)
#    - get_info() возвращает f"Попугай {name}, {age} лет"
#
#    Monkey (Обезьяна) наследует Animal
#    - speak() возвращает f"{name} прыгает и кричит: УУУ-УУУ!"
#    - eat() возвращает f"{name} ест {food}" (если это фрукты)
#    - get_info() возвращает f"Обезьяна {name}, {age} лет"
#
# 3. Создайте список животных разных видов
# 4. Используя ОДИН цикл:
#    - Выведите информацию о каждом
#    - Заставьте каждое издать звук
#    - Накормите каждое животное разной пищей
#
# Пример использования:
#
# lion = Lion("Лео", 5)
# elephant = Elephant("Дамбо", 10)
# parrot = Parrot("Кеша", 3)
# monkey = Monkey("Чита", 4)
#
# animals = [lion, elephant, parrot, monkey]
#
# for animal in animals:
#     print(animal.get_info())
#     print(animal.speak())
#     if isinstance(animal, Lion):
#         print(animal.eat("мясо"))
#     elif isinstance(animal, Elephant):
#         print(animal.eat("траву"))
#     elif isinstance(animal, Parrot):
#         print(animal.eat("семечки"))
#     elif isinstance(animal, Monkey):
#         print(animal.eat("бананы"))
#     print()
#
# # УЛУЧШЕНИЕ: Переделайте так, чтобы методу eat() не нужно было
# # проверять тип животного. Используйте свой метод feed() с
# # правильной пищей для каждого животного!


# 

# 1. Создайте класс Student (Студент)
#    Атрибуты: name (имя), student_id (ID студента), gpa (средний балл)
#    Методы:
#    - get_info() - информация о студенте
#    - update_gpa(new_gpa) - обновить GPA
#
# 2. Создайте класс Course (Курс)
#    Атрибуты: 
#    - name (название курса)
#    - instructor (преподаватель)
#    - max_students (максимум студентов)
#    - students (список студентов на курсе)
#    Методы:
#    - add_student(student) - добавить студента на курс
#    - remove_student(student) - удалить студента с курса
#    - is_full() - полон ли курс?
#    - get_students_count() - сколько студентов на курсе?
#    - show_students() - показать всех студентов на курсе
#    - get_average_gpa() - средний GPA всех студентов на курсе
#
# 3. Создайте класс University (Университет) - НАСЛЕДОВАНИЕ
#    Наследует от: ничего (базовый класс)
#    Атрибуты:
#    - name (название университета)
#    - courses (список курсов)
#    Методы:
#    - add_course(course) - добавить курс
#    - find_course(course_name) - найти курс по названию
#    - get_statistics() - вывести статистику (всего студентов, всего курсов и т.д.)
#
# 4. Сценарий:
#    - Создайте университет
#    - Создайте 3 курса
#    - Добавьте курсы в университет
#    - Создайте 10 студентов
#    - Добавьте студентов в разные курсы
#    - Выведите информацию о каждом курсе
#    - Выведите средний GPA каждого курса
#    - Выведите статистику университета
#
# Пример:
# uni = University("КазНУ имени аль-Фараби")
#
# python_course = Course("Python", "Иван Петров", 30)
# java_course = Course("Java", "Мария Сидорова", 25)
# js_course = Course("JavaScript", "Петр Иванов", 20)
#
# uni.add_course(python_course)
# uni.add_course(java_course)
# uni.add_course(js_course)
#
# students = [
#     Student("Алиса", 1, 4.5),
#     Student("Боб", 2, 3.8),
#     ...
# ]
#
# python_course.add_student(students[0])
# python_course.add_student(students[1])
# ...
#
# print(python_course.get_students_count())  # 3
# print(python_course.get_average_gpa())     # 4.1
# print(uni.get_statistics())



# class Student:
#     def __init__(self, name, student_id, gpa):
#         self.name = name
#         self.student_id = student_id
#         self.gpa = gpa

#     def get_info(self):
#         return f"Name: {self.name}, Student ID: {self.student_id}, GPA: {self.gpa}"

#     def update_gpa(self, new_gpa):
#         self.gpa = new_gpa

# class Course:
#     def __init__(self, name, instructor, max_students):
#         self.name = name
#         self.instructor = instructor
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

#     def remove_student(self, student):
#         if student in self.students:
#             self.students.remove(student)
#             return True
#         return False

#     def is_full(self):
#         return len(self.students) == self.max_students

#     def get_students_count(self):
#         return len(self.students)

#     def show_students(self):
#         for student in self.students:
#             print(student.get_info())

#     def get_average_gpa(self):
#         if self.students:
#             return sum(student.gpa for student in self.students) / len(self.students)
#         return 0

# class University:
#     def __init__(self, name):
#         self.name = name
#         self.courses = []

#     def add_course(self, course):
#         self.courses.append(course)

#     def find_course(self, course_name):
#         for course in self.courses:
#             if course.name == course_name:
#                 return course
#         return None

#     def get_statistics(self):
#         total_students = sum(course.get_students_count() for course in self.courses)
#         total_courses = len(self.courses)
#         return f"Total Students: {total_students}, Total Courses: {total_courses}"

# # Пример использования
# uni = University("КазНУ имени аль-Фараби")

# python_course = Course("Python", "Иван Петров", 30)
# java_course = Course("Java", "Мария Сидорова", 25)
# js_course = Course("JavaScript", "Петр Иванов", 20)

# uni.add_course(python_course)
# uni.add_course(java_course)
# uni.add_course(js_course)

# students = [
#     Student("Алиса", 1, 4.5),
#     Student("Боб", 2, 3.8),
#     ...
# ]

# python_course.add_student(students[0])
# python_course.add_student(students[1])
# ...

# print(python_course.get_students_count())  # 3
# print(python_course.get_average_gpa())     # 4.1
# print(uni.get_statistics())
# 1. Создайте класс Person (Человек) - базовый класс
#    Атрибуты: name (имя), age (возраст)
#    Методы: get_info()
#
# 2. Создайте класс Book (Книга)
#    Атрибуты: title (название), author (автор), isbn (код), available (доступна ли)
#    Методы:
#    - get_info()
#    - borrow() - взять книгу (available = False)
#    - return_book() - вернуть книгу (available = True)
#
# 3. Создайте класс Reader(Person) - наследует от Person! НАСЛЕДОВАНИЕ!
#    Атрибуты: 
#    - name, age (от Person)
#    - reader_id (номер читателя)
#    - borrowed_books (список взятых книг)
#    Методы:
#    - borrow_book(book) - взять книгу
#    - return_book(book) - вернуть книгу
#    - get_borrowed_books() - показать все взятые книги
#    - get_info() - переопределить (использовать super()!)
#
# 4. Создайте класс Librarian(Person) - наследует от Person! НАСЛЕДОВАНИЕ!
#    Атрибуты:
#    - name, age (от Person)
#    - library_id (ID библиотекаря)
#    - books_count (количество книг в библиотеке)
#    Методы:
#    - add_book(book) - добавить книгу в библиотеку
#    - remove_book(book) - удалить книгу
#    - check_availability(book) - проверить доступность книги
#    - get_info() - переопределить (использовать super()!)
#
# 5. Создайте класс Library (Библиотека) - КОМПОЗИЦИЯ!
#    Атрибуты:
#    - name (название)
#    - books (список книг)
#    - readers (список читателей)
#    - librarians (список библиотекарей)
#    Методы:
#    - add_reader(reader) - добавить читателя
#    - add_librarian(librarian) - добавить библиотекаря
#    - get_statistics() - статистика библиотеки
#
# 6. Сценарий:
#    - Создайте библиотеку
#    - Добавьте книги
#    - Добавьте читателей
#    - Добавьте библиотекарей
#    - Читатели берут книги
#    - Библиотекари проверяют наличие книг
#    - Выведите статистику
#
# Пример:
# library = Library("Городская библиотека")
#
# # Создание и добавление книг
# book1 = Book("1984", "Джордж Оруэлл", "ISBN123", True)
# book2 = Book("О дивный новый мир", "Олдос Хаксли", "ISBN456", True)
#
# library.add_book(book1)
# library.add_book(book2)
#
# # Создание читателя (наследует от Person!)
# reader1 = Reader("Алиса", 20, 1)
# library.add_reader(reader1)
#
# # Читатель берет книгу
# reader1.borrow_book(book1)
# print(reader1.get_borrowed_books())  # Список взятых книг
#
# # Создание библиотекаря (наследует от Person!)
# librarian1 = Librarian("Иван", 35, 1)
# library.add_librarian(librarian1)
#
# # Библиотекарь проверяет наличие
# librarian1.check_availability(book2)  # Доступна
#
# # Статистика
# print(library.get_statistics())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Book:
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.available else 'No'}"

class Reader(Person):
    def __init__(self, name, age, reader_id):
        super().__init__(name, age)
        self.reader_id = reader_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"Book '{book.title}' has been borrowed by {self.name}")
        else:
            print(f"Book '{book.title}' is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"Book '{book.title}' has been returned by {self.name}")
        else:
            print(f"Book '{book.title}' has not been borrowed by {self.name}")

    def get_borrowed_books(self):
        return self.borrowed_books

class Librarian(Person):
    def __init__(self, name, age, librarian_id):
        super().__init__(name, age)
        self.librarian_id = librarian_id

    def add_book(self, book):
        print(f"Book '{book.title}' has been added by {self.name}")

    def remove_book(self, book):
        print(f"Book '{book.title}' has been removed by {self.name}")

    def check_availability(self, book):
        print(f"Book '{book.title}' is {'available' if book.available else 'not available'}")

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.readers = []
        self.librarians = []

    def add_book(self, book):
        self.books.append(book)

    def add_reader(self, reader):
        self.readers.append(reader)

    def add_librarian(self, librarian):
        self.librarians.append(librarian)

    def get_statistics(self):
        return f"Library: {self.name}, Books: {len(self.books)}, Readers: {len(self.readers)}, Librarians: {len(self.librarians)}"

    def get_info(self):
        return f"Library: {self.name}, Books: {len(self.books)}, Readers: {len(self.readers)}, Librarians: {len(self.librarians)}"

# Пример использования
library = Library("Городская библиотека")

book1 = Book("1984", "Джордж Оруэлл", "ISBN123", True)
book2 = Book("О дивный новый мир", "Олдос Хаксли", "ISBN456", True)

library.add_book(book1)
library.add_book(book2)

reader1 = Reader("Алиса", 20, 1)
library.add_reader(reader1)

reader1.borrow_book(book1)

librarian1 = Librarian("Иван", 35, 1)
library.add_librarian(librarian1)

print(library.get_statistics())
