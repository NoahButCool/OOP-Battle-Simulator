from enemy import Enemy
import random

class Florb(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500
        self.attack_power = 30

    def attack(self):
        if random.randint(1,10) == 5:
            return (self.attack_power * 2)
        else:
            return self.attack_power

    def take_damage(self, damage):
        return super().take_damage(damage / 2)

