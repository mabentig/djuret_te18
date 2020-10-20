import random
class HygienManager:


    def __init__(self):
        self.hygiene = 40
        self.__pills_taken = 0
    

    def update(self, elapsed_time):
        """
        För varje sekund som gått har Gurkbert antingen blivit smutsigare eller inte.
        """
        for x in range(elapsed_time):
            
            self.hygiene -= random.shuffle([0,1])[0]
        
        self.__pills_taken = max(self.__pills_taken-elapsed_time/10, 0)
                
        if self.__pills_taken > 10:
            self.hygiene = -69
            
        return 0


    def shower(self):
        """
        Gurkbert duschar med varmvatten och använder balsam, conditioner samt tvål.
        """
        self.hygiene += 10
        
        return 0


    def hand_sanitiser(self):
        """
        Detta är handsprit så det är snabbare att skriva men get ett mindre värde.
        """
        self.hygiene += 2
        
        return 0
    

    def take_pills(self):
        """
        Detta gör så du tar ett piller, vilket sänker chansen till disease och ökar hygiene med 40
        """
        self.__pills_taken +=1
        self.hygiene += 40
        print('Gurkbert pops an ibuprofen')