from math import floor, trunc
import random
import numpy as np


class HygieneManager:

    def __init__(self):
        #hygienvärdet
        self.hygiene = 40
        #antal piller gurkbert har tagit
        self.__pills_taken = 0
        #total tid inte använd i update funktionen
        self.__total_time = 0
        #ger meny-grabbarna en array för menyn
        self.get_options = {
            'Shower':self.shower, 
            'Hand Sanitiser': self.sanitiser, 
            'Take medicine': self.pills,
            'Use perfume' : self.perfume
            }


    def update(self, elapsed_time):
        """
        För varje sekund som gått har Gurkbert antingen blivit smutsigare eller inte.
        """
        #lägger ihop elapsed- och total_time
        self.__total_time = self.__total_time + elapsed_time
        
        #spontant önskar eller minskar Gurkberts hygien
        for x in range(floor(self.__total_time/10)):
            self.hygiene += random.choice([0.5,-1])
        
        #minskar total piller tagna
        self.__pills_taken = max(self.__pills_taken-(self.__total_time/10), 0)
                
        #om gurkbert tar över 10 piller för snabbt så dör han då värdet blir en dödsdom
        if self.__pills_taken > 10:
            self.hygiene = -69
        
        #tar bort tid från total time för den använts
        self.__total_time %= 10
            
        return 0
     

    def shower(self):
        """
        Gurkbert duschar med varmvatten och använder balsam, conditioner samt tvål.
        """
        self.hygiene += 20 * abs(np.random.normal(1,0.5))
        
        return 0
    
    def sanitiser(self):
        """
        Detta är handsprit så det är snabbare att skriva men get ett mindre värde.
        """
        self.hygiene += 5
        
        return 0


    def pills(self):
        """
        Detta gör så du tar ett piller, vilket spontant ändrar hans hygien
        """
        self.__pills_taken += 1
        #spontant ändrara hygien värdet
        
        self.hygiene += random.choice([40,10,20,30,-15])
        print('Gurkbert pops a Gurkoprofen')
        return 0


    def perfume(self):
        """
        Gurkbert poppar vätska från en container(???)
        """
        self.hygiene *= float('0.'+('9'*10))
        return 0