
# f = open('main.txt', 'r')
# text = f.read() # фаил открыт в режимах чтения и запаковки в переменновой text 
# f.close()

# print(text)


# f = open('main.txt', 'a')
# f.write('Hello world!\n')
# f.close()

# a = 'Hello world!\n'

# with open('main.txt', 'a') as file:
#     file.write('Hello world!\n')

# with open('/Users/kiri/python_mor/lessons/data/main.txt', 'r') as file:
#     text = file.read()
#     print(len(text.split('\n')))



# with open('/Users/kiri/Downloads/загруженное.png', 'rb') as file:
#     data = file.read()
#     print(data)





# with open('data/main.txt', 'a') as file:
#     for i in range(1, 101):
#         file.write(f'{i} \n')


# while True:
#     a = []
#     with open('data/main.txt', 'r') as file:
#         text = file.read()
#         login_confirm = input('Введите логин: ')
#         if login_confirm in text:
#             print('Такой логин уже есть введите другой логин')
#         else:
#             password1 = input('Введите пароль: ')
#             password2 = input('Повторите пароль: ')
#             if password1 == password2:
#                 with open('data/main.txt', 'a') as file:
#                     file.write(f'login: {login_confirm} \n password: {password1} \n')


# import os 

# path = '/Users/kiri/python_mor/lessons/day11.py'

# print(os.path.exists(path))

# os.system('cat day10.py')


