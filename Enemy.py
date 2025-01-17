class Enemy:
    def __init__(self, name, health, damage):
        self._name = name
        self.health = health
        self.damage = damage    

    def talk(self): 
        print(f"I am {self._name}, My health is {self.health}, I do Damage of {self.damage}")
        
    def get_type(self):
        return self._name
    
    def info(self):
        print(f"{self._name} has {self.health}HP and does damage of {self.damage}Pts")
        
    def attack(self):
        print(f"{self.damage}pts damage dealt by {self._name}")

    def ability(self):
        print("No special attack!")
