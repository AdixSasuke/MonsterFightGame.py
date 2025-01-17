import random
from Enemy import * 

class Ogre(Enemy):
    def __init__(self, health, damage):
        super().__init__(
            name="Ogre",
            health=health,
            damage=damage)

    def talk(self):
        print(f"{self._name} is slamming hands all around.")
        
    def ability(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.damage += 4
            print("Ogres's Atk Dmg +4 pts!")
            print(f"Ogre Damage:{self.damage}")