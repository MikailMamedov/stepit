import time

class Hero:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack


    def attack_enemy(self, enemy):
        enemy.health = enemy.health - self.attack
        print(f"{self.name} attacks {enemy.name}!  {enemy.name} has {enemy.health} health")

hero1 = Hero("Knight", 100, 20)
hero2 = Hero("Warrior", 120, 15)

print("The fight begins!")
print()
time.sleep(1)

while hero1.health > 0 and hero2.health > 0:
    hero1.attack_enemy(hero2)
    if hero2.health <= 0:
        print(f"\n{hero1.name} wins!")
        break

    time.sleep(1)

    hero2.attack_enemy(hero1)
    if hero1.health <= 0:
        print(f"\n{hero2.name} wins!")
        break
    
    time.sleep(1)

print("\nThe battle over")