import random

class FoodManager:

    def __init__(self):
        self.hunger = random.randint(30,60)
        self.thirst = random.randint(30,60)
        self.happiness = random.randint(30,60)


        self.inventory = [
            {
                "Name":         "Water",

                "Hunger":       -2,
                "Thirst":       +10,
                "Happiness":    0 
            },
            {
                "Name":         "Bannana",

                "Hunger":       +10,
                "Thirst":       -2,
                "Happiness":    0
            },
            {
                "Name":         "JojKotfärssås",

                "Hunger":       +10,
                "Thirst":       +5,
                "Happiness":    -20
            },
            {
                "Name":         "GoldenApple",

                "Hunger":       -10,
                "Thirst":       -10,
                "Happiness":    +25
            },
            {
                "Name":         "Tequila",

                "Hunger":       0,
                "Thirst":       0,
                "Happiness":    0 
            }
        ]
    def update(self, elapsed_time):
        return 0

    def backpack(self):
        for i, v in enumerate(self.inventory):
            item = v['Name']
            print(f'{i+1}: {item}')

    def use(self, item):
        self.hunger += self.inventory[item]['Hunger']
        self.thirst += self.inventory[item]['Thirst']
        self.happiness += self.inventory[item]['Happiness']