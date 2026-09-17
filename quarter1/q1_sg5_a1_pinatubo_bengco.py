class Hero:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount

arthur = Hero("Arthur")
morgana = Hero("Morgana")

arthur.take_damage(10)

print(arthur.hp)
print(morgana.hp)