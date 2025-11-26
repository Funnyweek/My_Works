# def rps(a, b):
#     if a == "Rock" and b == "Scissors":
#         return("player a win")
#     elif a == "Scissors" and b == "Paper":
#         return ("player a wim")
#     elif a == "Paper" and b == "Rock":
#         return("player a win")
#     elif a == "Scissors" and b == "Rock":
#         return("player b win")
#     elif a == "Paper" and b == "Scissors":
#         return("player b win")
#     elif a == "Rock" and b == "Paper":
#         return("player b win")
#     else:
#         return("eror")





# def is_palindrome(s:str):
#     if s.lower() == s[::-1].lower():
#         return "True"
#     else:
#         return "False"





# def sum_array(a:list):
#     if a == []:
#         return 0
#     else:
#         b = sum(a)
#         return b     
    
    
    
# def quarter_of(month):
#     if month <= 3:
#         return 1
#     elif month >= 4 and month <= 6:
#         return 2
#     elif month >= 7 and month <= 9:
#         return 3
#     elif month >= 10 and month <= 12:
#         return 4





# def human_years_cat_years_dog_years(human_years):
#     a = 15
#     b = 15
#     if human_years == 1:
#         return [human_years, a, b]
#     if human_years == 2:
#         return [human_years, a+9, b+9]
#     else:
#         return [human_years, a+9+(4*(human_years-2)), b+9+(5*(human_years-2))]



# def odd_ball(arr):
#     for i in arr:
#         if type(i) == int:
#             try:
#                 odd = arr[i]
#                 if odd == "odd":
#                     return True
#             except Exception:
#                 pass
#     return False


# def sing():
#     lin = []
#     def bottles(n):
#         if n == 0: return "no more bottles of beer"
#         if n == 1: return "1 bottle of beer"
#         else:
#             return f"{n} bottles of beer"
#     for i in range(99, 0, -1):
#         lin.append(f"{bottles(i)} on the wall, {bottles(i)}.")
#         next = i - 1
#         lin.append(f"Take one down and pass it around, {bottles(next)} on the wall.")
#     lin.append("No more bottles of beer on the wall, no more bottles of beer.")
#     lin.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
#     return lin


def stringify(node):
    if node is None:
        return "None"
    a = []
    while node is not None:
        a.append(str(node.data))
        node = node.next 
    return " -> ".join(a) + " -> None"
        
        
        
        
# class Maks:
#     name = 'Максим'
#     def tolk(self):
#         return 'Ayyy'
    

# a = Maks()

# print(a.tolk())
# print(a.name)

