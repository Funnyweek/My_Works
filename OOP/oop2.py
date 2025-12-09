# class Book:
#     def __init__(self, title, author=None):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"'{self.title}'" + (f" by {self.author}" if self.author else "")


# class Chest:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         if isinstance(book, Book):
#             if book.title not in [b.title for b in self.books]:
#                 self.books.append(book)
#                 print(f"Книга {book} добавлена в сундук")
#             else:
#                 print(f"Книга {book.title} уже есть в сундуке")
#         else:
#             print("Можно добавлять только объекты класса Book")

#     def list_books(self):
#         if self.books:
#             print("Список книг в сундуке:")
#             for book in self.books:
#                 print(f" - {book}")
#         else:
#             print("Сундук пуст")

# book1 = Book("Война и мир", "Лев Толстой")
# book2 = Book("Приключения", "Неизвестный автор")
# book3 = Book("Проект Главдина")

# chest1 = Chest()
# chest1.add_book(book1)
# chest1.add_book(book2)
# chest1.add_book(book3)
# chest1.add_book(book1)  # проверка на дубликат

# chest1.list_books()


# 1. Создайте класс Product
#    Атрибуты: name (название), price (цена), stock (количество на складе)
#    Метод: get_info() - информация о товаре
#
# 2. Создайте класс ShoppingCart
#    Атрибуты: 
#    - owner (владелец корзины - имя покупателя)
#    - items (список товаров с количеством)
#    Методы:
#    - add_product(product, quantity) - добавить товар в определенном количестве
#    - remove_product(product) - удалить товар из корзины
#    - get_total_price() - общая стоимость всех товаров в корзине
#    - get_item_count() - общее количество товаров (всех)
#    - show_cart() - показать содержимое корзины
#
# 3. Создайте 5-6 товаров (пример: Яблоко, Молоко, Хлеб, Масло, Сыр, Йогурт)
# 4. Создайте 2 корзины разным людям (Алиса, Боб)
# 5. Добавьте товары в корзины
# 6. Покажите корзины с информацией:
#    - Что купил каждый
#    - Сколько всего товаров
#    - Сколько стоит
# 7. Удалите один товар из корзины
# 8. Покажите обновленную корзину
#
# Пример использования:
# 
# product1 = Product("Яблоко", 50, 100)
# product2 = Product("Молоко", 300, 50)
# 
# cart_alice = ShoppingCart("Алиса")
# cart_bob = ShoppingCart("Боб")
# 
# cart_alice.add_product(product1, 5)     # 5 яблок
# cart_alice.add_product(product2, 2)     # 2 молока
# 
# cart_bob.add_product(product1, 3)       # 3 яблока
# cart_bob.add_product(product2, 1)       # 1 молоко
# 
# cart_alice.show_cart()
# print(f"Всего в корзине: {cart_alice.get_item_count()} товаров")
# print(f"Сумма: {cart_alice.get_total_price()} тенге")
#
# cart_alice.remove_product(product1)     # Удаляем яблоки
# cart_alice.show_cart()                  # Показываем обновленную корзину


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_info(self):
        return f"{self.name} стоит {self.price} тенге, осталось {self.stock} штук"

class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add_product(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product):
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)
                break

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item["product"].price * item["quantity"]
        return total_price

    def get_item_count(self):
        total_count = 0
        for item in self.items:
            total_count += item["quantity"]
        return total_count

    def show_cart(self):
        print(f"Корзина {self.owner}:")
        for item in self.items:
            print(f" - {item['product'].name} x {item['quantity']}")
        print(f"Всего товаров: {self.get_item_count()}")
        print(f"Сумма: {self.get_total_price()} тенге")

product1 = Product("Яблоко", 50, 100)
product2 = Product("Молоко", 300, 50)

cart_alice = ShoppingCart("Алиса")
cart_bob = ShoppingCart("Боб")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

cart_alice.add_product(product1, 5)     # 5 яблок
cart_alice.add_product(product2, 2)     # 2 молока

cart_bob.add_product(product1, 3)       # 3 яблока
cart_bob.add_product(product2, 1)       # 1 молоко

cart_alice.show_cart()
print(f"Всего в корзине: {cart_alice.get_item_count()} товаров")
print(f"Сумма: {cart_alice.get_total_price()} тенге")

cart_alice.remove_product(product1)     # Удаляем яблоки
cart_alice.show_cart()                  # Показываем обновленную корзину