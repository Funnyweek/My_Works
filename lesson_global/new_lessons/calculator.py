while True:
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
    else:
        print("Error")
    exit = input("Exit? (yes/no) = ")   
    if exit == "yes" or exit == "y" or exit == "exit" or exit == "EXIT" or exit == "Exit":
        print("Goodbye")    
        break