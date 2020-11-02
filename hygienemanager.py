import random
class HygieneManager:

    def __init__(self):
        self.hygiene = 40
        self.__pills_taken = 0
        self.__total_time = 0
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
        self.total_time = self.total_time + elapsed_time
        
        for x in range(self.total_time/10):
            self.hygiene += random.shuffle([0.5,-1])[0]
        
        self.__pills_taken = max(self.__pills_taken-(self.total_time/10), 0)
                
        if self.__pills_taken > 10:
            self.hygiene = -69
        
        self.total_time /= 10
            
        return 0
     

    def shower(self):
        """
        Gurkbert duschar med varmvatten och använder balsam, conditioner samt tvål.
        """
        self.hygiene += 10
        
        return 0

    
    def sanitiser(self):
        """
        Detta är handsprit så det är snabbare att skriva men get ett mindre värde.
        """
        self.hygiene += 2
        
        return 0


    def pills(self):
        """
        Detta gör så du tar ett piller, vilket sänker chansen till disease och ökar hygiene med 40
        """
        self.__pills_taken +=1
        self.hygiene += random.shuffle[40,10,20,30,-15][0]
        print('Gurkbert pops an ibuprofen')


    def perfume(self):
        return 0