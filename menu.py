import djur
import pickle
import numpy as np

import sys
import os

class Menu:

    
    def __init__(self, title, menu_items):
        self.__menu_items = (menu_items)

        self.__title = title

        self.__djuret = None

        self.__name = None

    def start_menu(self):
        """
        När man startar spelet får man valet att starta ett nytt spel eller att ladda en sparfil.
        """

        os.system('cls')
        for i, item in enumerate(['New Animal', 'Load Animal', 'Quit']):
            print(f'{i+1}: {item}')
        startRequest = input().lower()

        if startRequest == 'new animal' or startRequest == 'new' or startRequest == '1':
            self.__name = input('What will you name your animal? ')

            self.__djuret = djur.Djur(self.__name)

            with open('Animals/' + self.__name + '.pickle', 'wb') as objektfilen:
                pickle.dump(self.__djuret, objektfilen)
            
            self.show_menu()

        elif startRequest == 'load animal' or startRequest == 'load' or startRequest == '2':
            temp = os.walk('Animals')
            names = None
            for i in temp:
                names = i
            temporary = None
            for name in names:
                temporary = name
            array = []
            for name in temporary:
                array.append(name.split('.')[0])
            os.system('cls')
            for i, item in enumerate(array):
                print(f'{i+1}: {item}')

            self.__name = input().lower()
            for name in array:
                if self.__name == name and not self.__name.isnumeric():
                    animalName = name
                    break
                elif self.__name.isnumeric():
                    animalName = array[int(self.__name) - 1]
                    break
                else:
                    self.start_menu()

            os.system('cls')
            with open('Animals/' + self.__name + '.pickle', 'rb') as objektfilen:
                self.__djuret = pickle.load(objektfilen)
            self.show_menu()


        elif startRequest == 'quit' or startRequest == '3':
            os.system('cls')
            sys.exit(0)

        else:
            os.system('cls')
            print('I don\'t know what that means...')
            input('Press enter to continue')
            self.start_menu()


    def show_menu(self):

        """
        Huvudmenyn visas upp och användaren får välja vad de vill göra.
        """

        os.system('cls')
        print(self.__title)

        for i, item in enumerate(self.__menu_items):
            print(f'{i+1}: {item}')
        request = input().lower()

        if request == self.__menu_items[0].lower() or request == '1':
            self.print_status()

        elif request == self.__menu_items[1].lower() or request == '2':
            self.show_food()

        elif request == self.__menu_items[2].lower() or request == '3':
            self.show_hygene()

        elif request == self.__menu_items[3].lower() or request == '4':
            self.show_activities()

        elif request == self.__menu_items[4].lower() or request == '5':
            self.show_tutorial()

        elif request == self.__menu_items[5].lower() or request == '6':
            os.system('cls')

            with open('Animals/' + self.__name + '.pickle', 'wb') as objektfilen:
                pickle.dump(self.__djuret, objektfilen)

            sys.exit(0)

        else:
            os.system('cls')
            print('I don\'t know what that means...')
            input('Press enter to continue')
            self.show_menu()



    def print_status(self):

        """
        Vi kallar statusen från djur.py
        """

        os.system('cls')

        print(self.__djuret.status())

        input('Press enter to continue')

        self.show_menu()
    


    def show_food(self):

        """
        Matgruppen gjorde en funktion som skriver ut alla deras maträtter, så vi kallar den. Vi behöver ändå en lista med alla valen,
        så vi fick skapa den manuellt.
        """

        os.system('cls')

        items = ['Water', 'Bannana', 'JojKotfärssås', 'GoldenApple', 'Tequila']

        self.__djuret.foodmanager.backpack()

        foodRequest = input().lower()

        for index, option in enumerate(items):
            if foodRequest == option.lower() or int(foodRequest) == index + 1:
                self.__djuret.foodmanager.use(index)

        self.print_status()
    
        input('Press enter to continue')

        self.show_menu()



    def show_hygene(self):

        """
        Hugiengruppen gjorde sin getoptions till en dictionary som låter oss kalla deras funktionen direkt från den.
        """

        os.system('cls')

        hygieneOptions = self.__djuret.hygienmanager.get_options

        for i, item in enumerate(hygieneOptions.keys()):
            print(f'{i+1}: {item}')


        hygeneRequest = input().lower()


        for index, option in enumerate(hygieneOptions.keys()):
            if hygeneRequest == option.lower() or int(hygeneRequest) == index + 1:
                hygieneOptions[option]()

        self.print_status()
        
        input('Press enter to continue')

        self.show_menu()



    def show_activities(self):

        """
        Hälsogruppen hade inte gjort någon getOptions funktion, så vi fick gå in i deras kod och skriva av alla valen manuellt.
        """

        os.system('cls')

        healthOptions = ['Funpill', 'Playnormal', 'Playhard', 'Playgod']
        healthFunctions = [self.__djuret.healthmanager.funpill(), self.__djuret.healthmanager.playnormal(), self.__djuret.healthmanager.playhard(), self.__djuret.healthmanager.playgod()]

        for i, item in enumerate(healthOptions):
            print(f'{i+1}: {item}')

        activityRequest = input().lower()

        for index, option in enumerate(healthOptions):
            if activityRequest == option.lower() or int(activityRequest) == index + 1:
                healthFunctions[index]

        self.print_status()

        input('Press enter to continue')
        
        self.show_menu()
    
    def show_tutorial(self):

        """
        Vi tyckte att spelet var lite svårt att förstå, så vi skrev en liten guide. För att hålla temat är den fortfarande lite kryptisk
        """

        os.system('cls')

        print('This game is played entirely using text!')
        print('As you play, numbered options will appear in the console.')
        print('By typing one of the options or its corresponding number and pressing enter,')
        print('that option will be selected.')
        print('')
        print('Your goal in this game is to keep your animal alive and happy for as long as possible.')
        print('To do this, you must open the game often and make sure your animal is fed, clean, and happy.')
        print('This may seem hard at first, but i\'m sure you\'ll get used to checking in on your animal in no time!')
        print('Good luck!')
        print('')

        
        input('Press enter to continue')

        self.show_menu()




main_menu = Menu('Main Menu', ['Status', 'Drink/Eat', 'Hygiene', 'Activities', 'How to play', 'Quit'])

main_menu.start_menu()
