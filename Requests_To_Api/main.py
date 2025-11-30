# import requests

# # r = requests.get("https://google.com")
# # print(r.status_code)
# # print(r.text)

# with open('dogs.txt','a') as file:
#     for _ in range(10):
#         url = 'https://dog.ceo/api/breeds/image/random'
#         r = requests.get(url)
#         print(r.json())
#         data =r.json()
#         file.write(data["message"] + '\n')
    



# 1. Используя API: https://dog.ceo/api/breeds/list/all
# 2. Получите список всех пород собак
# 3. API вернет словарь где ключи - породы, значения - подпороды
# 4. Выведите первые 10 пород
# 5. Подсчитайте всего пород
# 6. Сохраните в файл 'all_breeds.txt' в формате:
#    1. affenpinscher
#    2. african
#    3. airedale
#    и т.д.
#
# API: https://dog.ceo/api/breeds/list/all
# Ответ: {"message": {"affenpinscher": [], "african": [], ...}, "status": "success"}
#
# Ожидаемый результат:
# Первые 10 пород:
# 1. affenpinscher
# 2. african
# ...
# Всего пород: 197
# ✓ Все породы сохранены в all_breeds.txt


# import requests
# url ='https://dog.ceo/api/breeds/list/all'
# response = requests.get(url)
# data = response.json()

# dic = data["message"]
# dogs = list(dic.keys())
# for i, a in enumerate(dogs[:10], start=1):
#     print(i, a)
# print(len(dogs))

# with open("all_dogs.txt","a") as file:
#     for i,a in enumerate(dogs, start=1):
#         file.write(f"{i}: {a}\n")


# 1. Попросите пользователя ввести название породы
# 2. Используя API: https://dog.ceo/api/breed/{breed}/images
# 3. Получите все фотографии этой породы
# 4. Выведите количество фотографий
# 5. Выведите первые 5 ссылок
# 6. Сохраните все ссылки в файл 'breed_photos.txt'
#
# API: https://dog.ceo/api/breed/labrador/images
# Ответ: {"message": ["https://...", "https://...", ...], "status": "success"}
#
# Пример использования:
# Введите породу: labrador
# Найдено 297 фотографий
# Первые 5:
# 1. https://images.dog.ceo/breeds/labrador/n02099712_1003.jpg
# 2. https://images.dog.ceo/breeds/labrador/n02099712_1004.jpg
# ...
# ✓ 297 фотографий сохранено в breed_photos.txt

import requests

dog = input(">>>").strip().lower()
url = f"https://dog.ceo/api/breed/{dog}/images"

resp = requests.get(url)
data = resp.json()

if data["status"] != "success":
    print("NO")
else:
    photos = data["message"]
    print(f"{len(photos)}")
    for i,a in enumerate(photos[:5], start=1):
        print(f"{i}:{a}")
    with open("photo.txt", "a") as file:
        for s in photos:
            file.write(f"{s} \n")