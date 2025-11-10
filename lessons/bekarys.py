
products = ['яблока','груша','арбуз','банан','мандарин']
print(products)
i = int(input('i: '))
if i > 4:
    print('не правильный индекс')
else:
    products.pop(i)
    print(products)

    


#problem 2(day5)
# list = []
# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
# d = int(input('d:'))
# e = int(input('e:'))
# list.append(a)
# list.append(b)
# list.append(c)
# list.append(d)
# list.append(e)
# print(list)
# di = len(list)
# s = sum(list) / di
# print(s)

#list.extend([a,b,c,d,e])
#max1 = max(list)
#min1= min(list)


#print('maximum',max1)
#print('minimum',min1)


# problem 1(day5)
# list_1 = []
# list_2 = []
# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
# d = int(input('d:'))
# e = int(input('e:'))
# if a%2==0:
#     list_1.append(a)
# else:
#     list_2.append(a)

# if b%2==0:
#     list_1.append(b)
# else:
#     list_2.append(b)

# if c%2==0:
#     list_1.append(c)
# else:
#     list_2.append(c)

# if d%2==0:
#     list_1.append(d)
# else:
#     list_2.append(d)

# if e%2==0:
#     list_1.append(e)
# else:
#     list_2.append(e)
# print(list_1)
# print(list_2)