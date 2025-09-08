from enemy import Enemy

class baby_elf(Enemy):
    def cry():
        print("wahhh wahhh")

    def take_damage(self, damage):
        print("you should feel bad about yourself... attacking a baby")
        return super().take_damage(damage)