import random

def game(comp , you):
    if comp==you:
        return None 
    if comp == 's':
        if you =='w':
            return False
        elif 'g':
            return True

    if comp == 'w':
        if you =='g':
            return False
        elif 's':
            return True   

    if comp == 'g':
        if you =='s':
            return False
        elif 'w':
            return True

print("Computer Turn : Snake(s) Water(w) Gun(g)")
randNo = random.randint(1,3)
if randNo==1:
    comp = "s"
elif randNo==2:
    comp= 'w'
elif randNo==3:
    comp= 'g'


you = input("Your Turn : Snake(s) Water(w) Gun(g)")
a = game(you , comp)

print(f"Computer Choose  {comp}")
print(f"You Choose  {you}")

if a == None:
    print("The Game Is A Tie !")
elif a:
    print("You Win!")
else:
    print("You Lose!")    
