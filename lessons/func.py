
# Created on Tue July 11 10:32:32 2023

# def hello():
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')


# for i in range(10):
#     print(i)
#     hello()


# def get_len(text: str) -> int:
#     count = 0
#     for _ in text:
#         count += 1
#     return count


# s = 'kashdkjgashjdjhashdcjhgcagjcasxghashkxcakshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# d = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'


# count = 0
# for i in s:
#     count += 1

# count_b = 0
# for i in b:
#     count_b += 1

# s_len = get_len(s)
# b_len = get_len(b)
# d_len = get_len(d)

# print(s_len == s_len == d_len)

# import string
# import random


# def generate_password(length: int) -> str:
#     symbols = string.ascii_letters + string.digits
#     password = ''
#     for _ in range(length):
#         password += random.choice(symbols)
#     return password


# p1 = generate_password(10) 
# p2 = generate_password(10) 
# p3 = generate_password(10) 
# p4 = generate_password(10) 
# print(p1,p2,p3,p4)







# def get_5(item: int, massiv: list) -> bool:
#     if type(massiv) not in [list, tuple]:
#         raise TypeError('Массив должен быть списком или картежом')
    
#     if item in massiv:
#         return True
#     return False

# print(get_5(2, 6))




# def fibonachi(n: int) -> list:
#     x1, x2 = 1, 1
#     lst = []
#     for _ in range(n):
#         lst.append(x1)
#         x1, x2 = x2, x1 + x2
#     return lst
# print(fibonachi(100))




# def main(n: int) -> int:
#     if n % 2 == 0:
#         return n
#     return n + 1

# a = main(4)
# print(a)







# def main(n: int = 10000) -> int:
#     if n % 2 == 0:
#         return n
#     return n + 1

# print(main(213213))



# def main(*args):
#     return sum(args)

# print(main(2, 3, 4, 5, 6, 7, 8, 9, 10))


# def main(**kwargs):
#     return list(kwargs.items())

# print(main(name='Ivan', age=23, city='Moscow', country='Russia'))




# def main(a, b=None, *args, **kwargs):
#     return f"{a=}, {b=}, {args=}, {kwargs=}"
# print(main(1, name='Ivan', age=23))


# def digital_root(n):
#     if n > 9:
#         return digital_root(eval('+'.join(str(n))))
#     return n

# print(digital_root(132189))

  