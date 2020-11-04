import foodmanager
import hygienmanager
import healthmanager

import datetime
import random

class Djur:

    def __init__(self, namn):
        self.__namn = namn
        
        self.__birth = datetime.datetime.now()
        self.__last_updated = datetime.datetime.now()
        
        self.foodmanager = foodmanager.FoodManager()
        self.hygienmanager = hygienmanager.HygienManager()
        self.healthmanager = healthmanager.HealthManager()

        self.__faces = ('XP', ":'(", ':(', ':|', ':)', ':D')



    def update(self):
        """
        Uppdaterar djurets delar.
        """

        elapsed_seconds = (datetime.datetime.now() - self.__last_updated).total_seconds()
        self.__last_updated = datetime.datetime.now()

        self.foodmanager.update(elapsed_seconds)
        self.hygienmanager.update(elapsed_seconds)
        self.healthmanager.update(elapsed_seconds)


    def status(self):
        """
        Uppdaterar, beräknar status och returnerar en ansiktsstring.
        """
        
        self.update()

        status = min(self.foodmanager.hunger, self.hygienmanager.hygien, self.healthmanager.happiness)

        status = random.uniform(0, 100)
        if status <= 0:
            return self.__faces[0]
        elif status <= 20:
            return self.__faces[1]
        if status <= 40:
            return self.__faces[2]
        if status <= 60:
            return self.__faces[3]
        if status <= 80:
            return self.__faces[4]
        else:
            return self.__faces[5]
        