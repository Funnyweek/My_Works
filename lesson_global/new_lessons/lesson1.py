# f = int(input("number"))
# d = int(input("number2"))

# # If: f > d
# # print( "f is bigger") 
# # if f < d: 
# #     print("d is bigger")

# a = input("number")
# b = input("number2")

# print( a + "  " + b)
def main():
	try:
		f = int(input("Введите первое число: "))
		d = int(input("Введите второе число: "))
	except ValueError:
		print("Ошибка: введите целые числа")
		return

	if f > d:
		print(f"{f} больше, чем {d}")
	elif f < d:
		print(f"{d} больше, чем {f}")
	else:
		print("Числа равны")


if __name__ == "__main__":
	main()
