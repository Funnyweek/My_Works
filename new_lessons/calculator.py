a = int(input("a = "))
c = input("Что вы хотите?(+ - * /) = ")
b = int(input("b = "))

if c == "+":
    print (f"{a} + {b} = {a+b}")
elif c == "-":
    print (f"{a} - {b} = {a-b}")
elif c == "*":
    print (f"{a} * {b} = {a*b}")
elif c == "/":
    print (f"{a} / {b} = {a/b}")
