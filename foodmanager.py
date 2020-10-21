import random

class FoodManager:

    def __init__(self):
        self.hunger = random.randint(30,60)
        self.thirst = random.randint(30,60)
        self.happiness = random.randint(30,60)


        self.inventory = [
            {
                "Name":         "Water",
                "Level":        1,

                "Hunger":       -2,
                "Thirst":       +10,
                "Happiness":    0 
            },
            {
                "Name":         "Bannana",
                "Level":        1,

                "Hunger":       +10,
                "Thirst":       -2,
                "Happiness":    0
            },
            {
                "Name":         "JojKotfärssås",
                "Level":        5,

                "Hunger":       +10,
                "Thirst":       +5,
                "Happiness":    -20
            },
            {
                "Name":         "GoldenApple",
                "Level":        10,

                "Hunger":       -10,
                "Thirst":       -10,
                "Happiness":    +25
            },
            {
                "Name":         "Tequila",
                "Level":        18,

                "Hunger":       0,
                "Thirst":       0,
                "Happiness":    0 
            }
        ]
    def update(self, elapsed_time):
        return 0

    def backpack(self):
        for i, v in enumerate(self.inventory):
            print(i, ": ", v["Name"])

    def use(self, item):
        if self.inventory[item] and self.inventory[item].Amount > 0:
            self.inventory[item].Unlocked = True

            self.hunger += self.inventory[item].Hunger
            self.thirst += self.inventory[item].Thirst
            self.happiness += self.inventory[item].Happiness