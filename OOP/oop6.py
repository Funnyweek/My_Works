# 1. Создайте класс User (Пользователь)
#    PUBLIC атрибуты:
#    - username (имя пользователя)
#    
#    PROTECTED атрибуты:
#    - _email (email пользователя)
#    
#    PRIVATE атрибуты:
#    - __password (пароль - критичные данные!)
#    - __password_attempts (попытки входа)
#    - __is_blocked (заблокирован ли аккаунт)
#
#    Методы:
#    - get_username() - PUBLIC, возвращает имя
#    - _get_email() - PROTECTED, возвращает email (для дочерних классов)
#    - __validate_password(password) - PRIVATE, проверяет пароль (вспомогательный)
#    - login(password) - PUBLIC, попытка входа
#      * Если пароль неверный - увеличить попытки
#      * После 3 неверных попыток - заблокировать аккаунт
#      * Возвращает "Успешный вход" или сообщение об ошибке
#    - change_password(old_password, new_password) - PUBLIC
#      * Проверить старый пароль
#      * Проверить что новый пароль не короче 8 символов
#      * Изменить пароль
#    - is_account_blocked() - PUBLIC, возвращает статус блокировки
#    - unblock_account() - PUBLIC, разблокировать аккаунт (админ функция)
#
# 2. Использование:
#    - Создайте пользователя
#    - Попытайтесь войти с неправильным паролем 3 раза
#    - Проверьте что аккаунт заблокирован
#    - Разблокируйте аккаунт
#    - Измените пароль
#    - Успешно войдите с новым паролем
#
# Пример:
# user = User("alice", "alice@gmail.com", "password123")
# print(user.login("wrong"))      # ❌ Пароль неверный. Попытка 1 из 3
# print(user.login("wrong"))      # ❌ Пароль неверный. Попытка 2 из 3
# print(user.login("wrong"))      # ❌ Пароль неверный. Попытка 3 из 3
# print(user.is_account_blocked()) # True - аккаунт заблокирован
# user.unblock_account()
# user.change_password("password123", "newpassword123")
# print(user.login("newpassword123")) # ✓ Успешный вход



class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password
        self.__password_attempts = 0
        self.__is_blocked = False

    def get_username(self):
        return self.username

    def _get_email(self):
        return self._email

    def __validate_password(self, password):
        return password == self.__password

    def login(self, password):
        if self.__validate_password(password):
            self.__password_attempts = 0
            return "Успешный вход"
        else:
            self.__password_attempts += 1
            if self.__password_attempts >= 3:
                self.__is_blocked = True
            return f"❌ Пароль неверный. Попытка {self.__password_attempts} из 3"

    def change_password(self, old_password, new_password):
        if self.__validate_password(old_password):
            if len(new_password) >= 8:
                self.__password = new_password
                return "Пароль успешно изменен"
            else:
                return "Новый пароль должен быть не менее 8 символов"
        else:
            return "Старый пароль неверный"

    def is_account_blocked(self):
        return self.__is_blocked

    def unblock_account(self):
        self.__is_blocked = False
        return "Аккаунт разблокирован"

user = User("alice", "alice@gmail.com", "password123")
print(user.login("wrong"))      # ❌ Пароль неверный. Попытка 1 из 3
print(user.login("wrong"))      # ❌ Пароль неверный. Попытка 2 из 3
print(user.login("wrong"))      # ❌ Пароль неверный. Попытка 3 из 3
print(user.is_account_blocked()) # True - аккаунт заблокирован
user.unblock_account()
user.change_password("password123", "newpassword123")
print(user.login("newpassword123")) # ✓ Успешный вход