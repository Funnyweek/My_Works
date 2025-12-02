# import requests
# from pprint import pprint
# # Ваш API ключ
# API_KEY = '60e65401d8710502c7983cf2'

# # Базовая валюта
# base_currency = ('USD', "KZT", "RUB", "EUR")

# for i in base_currency:
#     # URL запроса
#     url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{i}'

#     # Отправляем запрос
#     response = requests.get(url)
#     # Проверяем статус
#     if response.status_code == 200:
#         data = response.json()
#         kzt = data["conversion_rates"]["KZT"]
#         print(f"{i}: в тг {kzt}")
#         print(f"Min: {min(data["conversion_rates"])}")
#         print(f"Max: {max(data["conversion_rates"])}")
#     else:
#         print(f'Ошибка: {response.status_code}')
   
   
# 1. Попросите пользователя ввести сумму в долларах (USD)
# 2. Используйте функцию exchange() для конвертации в 3 валюты:
#    - KZT (Казахстанский тенге)
#    - RUB (Российский рубль)
#    - EUR (Евро)
# 3. Выведите результаты в красивом формате
#
# Пример использования:
# Введите сумму в USD: 100
#
# ════════════════════════════════════════════════════════
#                   КОНВЕРТАЦИЯ $100
# ════════════════════════════════════════════════════════
# 100 USD (Доллар США)
#
# Конвертировано в:
# 1. 47545.00 KZT (Казахстанский тенге)
# 2. 9325.00 RUB (Российский рубль)
# 3. 92.00 EUR (Евро)
# ════════════════════════════════════════════════════════

# import requests
# from pprint import pprint
# # Ваш API ключ
# API_KEY = '60e65401d8710502c7983cf2'

# # Базовая валюта
# base_currency = input(">>>")
# a = float(input(">>>>"))

#     # URL запроса
# url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'
#     # Отправляем запрос
# response = requests.get(url)
#     # Проверяем статус
# if response.status_code == 200:
#     data = response.json()
#     print("==========================================")
#     print(f"          convert {base_currency} {a}        ")
#     print("==========================================")
#     print("KZT=", data["conversion_rates"]["KZT"] *a)
#     print("RUB=", data["conversion_rates"]["RUB"] *a)
#     print("EUR=", data["conversion_rates"]["EUR"] *a)
# else:
#     print(f'Ошибка: {response.status_code}')




# 1. Покажите пользователю список доступных валют:
#    KZT, RUB, EUR, GBP, JPY, CNY, AED, INR
# 2. Попросите выбрать валюту
# 3. Попросите ввести сумму
# 4. Используйте функцию exchange() для конвертации в USD
# 5. Выведите результат с названием валют
#
# Пример использования:
# Доступные валюты:
# 1. KZT - Казахстанский тенге
# 2. RUB - Российский рубль
# 3. EUR - Евро
# 4. GBP - Британский фунт
# 5. JPY - Японская йена
# 6. CNY - Китайский юань
# 7. AED - Дирхам ОАЭ
# 8. INR - Индийская рупия
#
# Выберите валюту (введите номер): 1
# Введите сумму: 50000
#
# ════════════════════════════════════════════════════════
#                   КОНВЕРТАЦИЯ В USD
# ════════════════════════════════════════════════════════
# 50000.00 KZT (Казахстанский тенге)
#                    ↓
# 105.24 USD (Доллар США)
#
# Курс: 1 KZT = 0.00210 USD
# ════════════════════════════════════════════════════════

# import requests
# from pprint import pprint
# # Ваш API ключ
# API_KEY = '60e65401d8710502c7983cf2'

# # Базовая валюта
# print("KZT, RUB, EUR, GBP, JPY, CNY, AED, INR")
# base_currency = input(">>>")
# a = float(input(">>>>"))
# v = input(">>>>")

#     # URL запроса
# url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'
#     # Отправляем запрос
# response = requests.get(url)
#     # Проверяем статус
# if response.status_code == 200:
#     data = response.json()
#     print(base_currency, a)
#     print(v, a*data["conversion_rates"][f"{v}"])
# else:
#     print(f'Ошибка: {response.status_code}')



# 1. Попросите пользователя ввести две валюты (коды: USD, KZT, EUR и т.д.)
# 2. Попросите ввести сумму
# 3. Используйте функцию exchange() для конвертации
# 4. Выведите курс обмена и результат конвертации
# 5. Обработайте ошибки если валюта не найдена
#
# Пример использования:
# Введите валюту ИЗ (например USD): EUR
# Введите валюту В (например KZT): JPY
# Введите сумму: 100
#
# ════════════════════════════════════════════════════════
#                КОНВЕРТАЦИЯ EUR → JPY
# ════════════════════════════════════════════════════════
# 100.00 EUR (Евро)
# Курс: 1 EUR = 150.50 JPY
#                    ↓
# 15050.00 JPY (Японская йена)
# ════════════════════════════════════════════════════════



# import requests

# API_KEY = '60e65401d8710502c7983cf2'

# def get_exchange_rate(base_currency, target_currency):
#     """
#     Получает курс обмена между двумя валютами
    
#     Args:
#         base_currency: Базовая валюта (например 'USD')
#         target_currency: Целевая валюта (например 'KZT')
    
#     Returns:
#         float: Курс обмена (1 базовая валюта = ? целевая валюта)
#         None: Если произошла ошибка
#     """
    
#     url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'
    
#     try:
#         response = requests.get(url, timeout=5)
        
#         if response.status_code == 200:
#             data = response.json()
            
#             # Проверяем успешность запроса
#             if data['result'] == 'success':
#                 # Получаем курс
#                 rate = data['conversion_rates'].get(target_currency)
#                 return rate
#             else:
#                 print(f'Ошибка API: {data["result"]}')
#                 return None
#         else:
#             print(f'Ошибка HTTP: {response.status_code}')
#             return None
            
#     except requests.exceptions.RequestException as e:
#         print(f'Ошибка подключения: {e}')
#         return None

# # Использование
# a = input(">>>")
# b= input(">>>>>")
# c = float(input(">>>"))
# rate = get_exchange_rate(f'{a}', f'{b}')
# rate = rate * c
# if rate:
#     print(f'{c} {a} = {rate} {b}')
# else:
#     print('Не удалось получить курс')


# 1. Допустим, товар стоит:
#    - 50 USD в США
#    - 5000 KZT в Казахстане
#    - 4500 RUB в России
#    - 45 EUR в Европе
#
# 2. Конвертируйте все цены в USD
# 3. Найдите самую дешевую и самую дорогую цену
# 4. Выведите все цены в формате таблицы
#
# Ожидаемый результат:
# ════════════════════════════════════════════════════════
#              СРАВНЕНИЕ ЦЕН ТОВАРА
# ════════════════════════════════════════════════════════
# Страна          | Цена        | В USD
# ─────────────────────────────────────
# США (USD)       | 50.00 USD   | 50.00 USD ✓
# Казахстан (KZT) | 5000.00 KZT | 10.52 USD
# Россия (RUB)    | 4500.00 RUB | 48.39 USD
# Европа (EUR)    | 45.00 EUR   | 48.91 USD
# ─────────────────────────────────────
#
# ✓ Самая дешевая цена: 10.52 USD (Казахстан)
# ✗ Самая дорогая цена: 50.00 USD (США)
# ════════════════════════════════════════════════════════


# import requests

# API_KEY = '60e65401d8710502c7983cf2'

# def get_exchange_rate(base_currency, target_currency):
#     url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'
#     try:
#         response = requests.get(url, timeout=5)
#         if response.status_code == 200:
#             data = response.json()
#             if data['result'] == 'success':
#                 return data['conversion_rates'].get(target_currency)
#             else:
#                 print(f'Ошибка API: {data["result"]}')
#                 return None
#         else:
#             print(f'Ошибка HTTP: {response.status_code}')
#             return None
#     except requests.exceptions.RequestException as e:
#         print(f'Ошибка подключения: {e}')
#         return None

# def ask(x):

#     results = {}
#     target = "USD"
#     for base, amount in x.items():
#         rate = get_exchange_rate(base, target)
#         if rate:
#             converted = rate * float(amount)
#             results[base] = converted
#             print(f"{amount} {base} = {converted:.2f} {target}")
#         else:
#             print(f"Не удалось получить курс для {base}")
#     # найти минимальный результат
#     if results:
#         min_currency = min(results, key=results.get)
#         print(f"\nСамый маленький результат: {min_currency} = {results[min_currency]:.2f} {target}")

# x1 = {
#         "USD": 50,
#         "KZT": 5000,
#         "RUB": 4500,
#         "EUR": 45
#     }
# ask(x1)

    #  50 USD в США
#    - 5000 KZT в Казахстане
#    - 4500 RUB в России
#    - 45 EUR в Европе





# Дан список пользователей с балансом в USD:

# users = [
#     {'name': 'Алиса', 'balance_usd': 100},
#     {'name': 'Боб', 'balance_usd': 250},
#     {'name': 'Виктор', 'balance_usd': 500},
#     {'name': 'Галина', 'balance_usd': 150},
#     {'name': 'Дмитрий', 'balance_usd': 300}
# ]

# 1. Обновите список добавив для каждого пользователя балансы в валютах:
#    - KZT (Казахстанский тенге)
#    - KGS (Киргизский сом)
#    - RUB (Российский рубль)
#
# 2. Результат должен выглядеть так:
# users = [
#     {
#         'name': 'Алиса',
#         'balance_usd': 100,
#         'balance_kzt': 47545.00,
#         'balance_kgs': 8945.50,
#         'balance_rub': 9325.00
#     },
#     ...
# ]
#
# 3. Выведите таблицу со всеми балансами:
#
# ════════════════════════════════════════════════════════════════════════
#              БАЛАНСЫ ПОЛЬЗОВАТЕЛЕЙ В РАЗНЫХ ВАЛЮТАХ
# ════════════════════════════════════════════════════════════════════════
# Имя      | USD      | KZT         | KGS        | RUB
# ──────────────────────────────────────────────────────────
# Алиса    | 100.00   | 47545.00    | 8945.50    | 9325.00
# Боб      | 250.00   | 118862.50   | 22363.75   | 23312.50
# Виктор   | 500.00   | 237725.00   | 44727.50   | 46625.00
# Галина   | 150.00   | 71317.50    | 13418.25   | 13987.50
# Дмитрий  | 300.00   | 142635.00   | 26836.50   | 27975.00
# ════════════════════════════════════════════════════════════════════════
#
# 4. Найдите пользователя с максимальным балансом в каждой валюте
# 5. Сохраните обновленный список в файл 'users_with_currencies.txt'





import requests

API_KEY = '60e65401d8710502c7983cf2'

def get_exchange_rate(base_currency, target_currency):
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['result'] == 'success':
                return data['conversion_rates'].get(target_currency)
            else:
                print(f'Ошибка API: {data["result"]}')
                return None
        else:
            print(f'Ошибка HTTP: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Ошибка подключения: {e}')
        return None

def ask(users):
    results = {}
    target = "USD"
    for user in users:
        base = "USD"  # у всех баланс в долларах
        amount = user["balance_usd"]
        rate = get_exchange_rate(base, target)
        if rate:
            converted = rate * float(amount)
            results[user["name"]] = converted
            print(f"{user['name']}: {amount} {base} = {converted:.2f} {target}")
        else:
            print(f"Не удалось получить курс для {base}")

users = [
    {'name': 'Алиса', 'balance_usd': 100},
    {'name': 'Боб', 'balance_usd': 250},
    {'name': 'Виктор', 'balance_usd': 500},
    {'name': 'Галина', 'balance_usd': 150},
    {'name': 'Дмитрий', 'balance_usd': 300}
]

ask(users)

