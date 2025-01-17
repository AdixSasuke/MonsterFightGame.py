from Enemy import *
import random

class Zombie(Enemy):
    
    def __init__(self, health, damage):
        super().__init__(
            name = "Zombie",
            health = health,
            damage = damage)
    
    def attack1(self):
        print(f"{self._name} is Spreading Disease")
    
    def talk(self):
        print(f"Grumbling....!")
        
    def ability(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health +=5
            print("Zombie HP +5 Pts")
            print(f"Zombie HP: {self.health}")