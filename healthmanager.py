import random
class HealthManager:
    
    def __init__(self):
        self.happiness = 0
        self.__age = 0

    def update(self, elapsed_time):
        self.__age += elapsed_time
        self.happiness -= elapsed_time / 60
        return 0

    def funpill(self):
        """
        Gurkbert konsumerar ett piller för en god tid.
        """
        self.happiness += 3
        print("The pill brings Gurkbert a bit of joy.")
    
    def playnormal(self):
        """
        Gurkbert gör något lätt och roligt.
        """
        self.happiness += 5
        easygamechoice = random.randint(0,1)
        if easygamechoice == 0:
            print("Gurkbert skips the rope.")
        elif easygamechoice == 1:
            print("Gurkbert claps his hands joyously.")
        else:
            print("Gurkbert cheers.")
        
    def playhard(self):
        """
        Gurkbert gör något svårare med bättre vinster dock med risk för förlust.
        """
        winorlose = random.randint(0,6)
        if winorlose == 6:
            print("Gurkbert fails and runs into a table. Not a gamer move! :(")
            self.happiness -= 10
        elif winorlose != 6:
            self.happiness += 15
            hardgamechoice = random.randint(0,1)
            if hardgamechoice == 0:
                print("Gurkbert sets a new Pacman record!")
            elif hardgamechoice == 1:
                print("Gurkbert wins a match of Stalin Simulator!")
            else:
                print("Gurkbert wins a game of Fortnite!")
    def playgod(self):
        """
        Gurkbert utmanar Gud själv i en lek om liv och döden.
        """
        defeatzeus = random.randint(0,1)
        if defeatzeus == 0:
            print("Gurkbert was sheeple and is struck by lightning.")
            self.happiness = self.happiness * 0.6
        elif defeatzeus == 1:
            print("Gurkbert yells 'ABSORB BREAK!' and throws a thunderbolt at Zeus.)
            self.happiness += 30
          
    def get_options(self):
        return ['funpill', 'playnormal', 'playhard', 'playgod']

       



   