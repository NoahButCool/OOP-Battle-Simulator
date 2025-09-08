from enemy import Enemy

class Florb(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500
        self.attack_power = 30

    def attack(self):
        return self.attack_power

