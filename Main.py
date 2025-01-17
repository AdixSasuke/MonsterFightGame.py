from Enemy import *
from Zombie import *
from Ogre import *

e1 =  Zombie(10, 1)
e2 = Ogre(20,3)

def battle(e1:Enemy, e2:Enemy):
    e1.info()
    e2.info()

    
    while e1.health > 0 and e2.health > 0:
        print(f"Zombie HP: {e1.health}\nOgre HP: {e2.health}")
        e1.ability()
        e2.ability()
        e2.attack()
        e1.health -= e2.damage
        e1.attack()
        e2.health -= e1.damage
        print("--------------------")
    
    if e1.health > 0:
        print("Zombie Wins")
    else:
        print("Ogre Wins")
        
print("--------------------")
battle(e1 ,e2)
