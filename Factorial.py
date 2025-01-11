from math import factorial


num = int(input("ENTER THE NUMBER YOU WANT FACTORIAL OFF : \n"))

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"THE FACTORIAL OF THIS NUMBER IS {factorial} ")
