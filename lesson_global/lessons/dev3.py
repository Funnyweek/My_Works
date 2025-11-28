# def find_min(arr):
#     print(arr)
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return min(arr[0], find_min(arr[1:]))
    
# print(find_min([42, 65]))


# def rec_len(list_l):
#     if not list_l:
#         return 0
#     return rec_len(list_l[1:]) + 1

# print(rec_len([1,2,3,4,5]))



# def obratnii_poryadok(spisok):

#     if len(spisok) == 1:
#         return [spisok[0]]
#     else:
#         return  [spisok[-1]] + obratnii_poryadok(spisok[:-1])

# print(obratnii_poryadok(['watermelon', 'pineapple', 'watermelon']))



# def chet(func):
#     def wrapper(n):
#         number = func(n)
#         if number % 2 == 0:
#             return number
#         return number + 1
#     return wrapper


# @chet
# def main(n):
#     return n


# print(main(7))
import time


# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         print(time.time() - start)
#         return result
#     return wrapper

# @timer
# def gen_num(n):
#     return [i for i in range(n)]




# print(gen_num(10))



def decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
        return 
    return wrapper


@decorator
def mainer():
    print('Hello')


# print(mainer())



a = (lambda s, xx: s*xx)(2, 3)
print(a)
