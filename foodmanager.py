import random

class FoodManager:

    def __init__(self):
        self.hunger = random.randint(30,60)
        self.thirst = random.randint(30,60)
        self.happiness = random.randint(30,60)

        """ ToDo
        self.later = [

        ]
        """

        self.inventorty = {
            "GoldenApple": {
                "Level":        10,
                "Unlocked":     False,
                "Amount":       0,

                "Hunger":       -10,
                "Thirst":       -10,
                "Happiness":    +25
            },

            "Water": {
                "Level":        1,
                "Unlocked":     False,
                "Amount":       0,

                "Hunger":       -2,
                "Thirst":       +10,
                "Happiness":    0 
            },

            "Bannana": {
                "Level":        1,
                "Unlocked":     False,
                "Amount":       0,

                "Hunger":       +10,
                "Thirst":       -2,
                "Happiness":    0
            },

            "Tequila": {
                "Level":        18,
                "Unlocked":     False,
                "Amount":       0,

                "Hunger":       0,
                "Thirst":       0,
                "Happiness":    0 
            },

            "Joj kotfärssås": {
                "Level":        5,
                "Unlocked":     False,
                "Amount":       0,

                "Hunger":       +10,
                "Thirst":       +5,
                "Happiness":    -20
            },
        }

    def update(self, elapsed_time):
        return 0

    def use(self, item):
        if self.inventorty[item] and self.inventorty[item].Amount > 0:
            self.inventorty[item].Unlocked = True

            self.hunger += self.inventorty[item].Hunger
            self.thirst += self.inventorty[item].Thirst
            self.happiness += self.inventorty[item].Happiness