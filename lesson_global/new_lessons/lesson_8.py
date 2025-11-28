# students = {
#     "Artem":55,
#     "BOB": 11,
#     "victor":12,
#     "saniya": 33
# }
# n = 0
# with open("1234.txt", "w") as file:
#     for i in students:
#         file.write(f"{i}:{students[i]}\n")



# Задача 1: Преобразование содержимого файла

# 1. Создайте файл 'text.txt' с несколькими строками в РАЗНОМ регистре
#    Пример: "Привет МИР", "PyThOn", "файлы И ДАННЫЕ"
# 2. Откройте файл и прочитайте содержимое
# 3. Переведите весь текст в ВЕРХНИЙ регистр (используйте .upper())
# 4. Сохраните результат в новый файл 'text_upper.txt'
# 5. Откройте оба файла и выведите их содержимое
# Покажите исходный файл и результат

b = []
n = 0
with open("text.txt", "r") as file:
    for a in file:
        print(a.upper())
        a = a.upper()
        a = b.append(a)
print(b)
c = ()
c = str(b)
with open("text.txt", "w") as file_2:
    file_2.write(c)



