import time
from Enemy import *
from Enemy1 import *
from Enemy2 import *


print("Welcome To the Monster Fight Game.....")
time.sleep(1)
print("Enemy 1: Zombie...!")
time.sleep(1)
print("Enemy 2: Ogre...!")
time.sleep(1)
e1hp = int(input("Enter Zombie's HP:- "))
e2hp  = int(input("Enter Ogre's HP:- "))
e1dmg = int(input("Enter Zombie's Attack Power:- "))
e2dmg = int(input("Enter Ogre's Attack Power:- "))


e1 =  Zombie(e1hp, e1dmg)
e2 = Ogre(e2hp,e2dmg)

def battle(e1:Enemy, e2:Enemy):
    e1.info()
    time.sleep(1)
    e2.info()
    time.sleep(1)
    
    while e1.health > 0 and e2.health > 0:
        print(f"Zombie HP: {e1.health}\nOgre HP: {e2.health}")
        time.sleep(1)
        e1.ability()
        time.sleep(1)
        e2.ability()
        time.sleep(1)
        e2.attack()
        time.sleep(1)
        e1.health -= e2.damage
        time.sleep(1)
        e1.attack()
        time.sleep(1)
        e2.health -= e1.damage
        time.sleep(1)
        print("----------------------------")
    
    if e1.health > 0:
        print("Zombie Wins")
    else:
        print("Ogre Wins")
        
print("----------------------------")
battle(e1 ,e2)
