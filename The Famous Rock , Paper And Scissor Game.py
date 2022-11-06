# The Famous Rock , Paper And Scissor Game Using Python

import random

def game(comp,you):
    if comp==you:
        return None
    elif comp== 'r' :
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp== 'p' :
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp== 's' :
        if you == 'r':
            return True
        elif you == 'p':
            return False
    
print("comuter: rock(r) paper(p) scissor(s) ")
rand=random.randint(1,3)
if rand==1:
    comp='r'
elif rand==2:
    comp='p'
elif rand==3:
    comp='s'

you=input("you: Rock(r) Paper(p) Scissor(s)")
x=game(comp,you)

print(f"Comp: {comp} \nyou : {you}")
if x== None:
    print("It's a TIE ! ")
elif x==True:
    print("YOU WIN !")
else:
    print("You Lose!")
