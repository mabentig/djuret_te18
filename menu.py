import djur
import foodmanager
import hygienmanager
import healthmanager
import pickle

import sys
import os

class Menu:

    
    def __init__(self, title, menu_items):
        self.__menu_items = (menu_items)

        self.__settings = ['dark/light mode']

        self.__title = title

        self.__darkMode = False

        self.__djuret = None

        #self.__foodmanager = foodmanager.FoodManager()

        #self.__hygienmanager = hygienmanager.HygienManager()

        #self.__healthmanager = healthmanager.HealthManager()

    def start_menu(self):
        os.system('cls')
        for i, item in enumerate(['New Animal', 'Load Animal', 'Quit']):
            print(f'{i+1}: {item}')
        startRequest = input().lower()

        if startRequest == 'new animal' or startRequest == 'new' or startRequest == '1':
            name = input('What will you name your animal? ')

            self.__djuret = djur.Djur(name)

            with open('Animals/' + name + '.pickle', 'wb') as objektfilen:
                pickle.dump(self.__djuret, objektfilen)
            
            self.show_menu()

        elif startRequest == 'load animal' or startRequest == 'load' or startRequest == '2':
            print('poggers')
            temp = os.walk('Animals')
            names = None
            for i in temp:
                print(i)
                names = i
            for name in names:
                print(os.path)

        elif startRequest == 'quit' or startRequest == '3':
            os.system('cls')
            sys.exit(0)

        else:
            os.system('cls')
            print('I don\'t know what that means...')
            input('Press enter to continue')
            self.start_menu()


    def show_menu(self):
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
            self.show_settings()

        elif request == self.__menu_items[5].lower() or request == '6':
            os.system('cls')
            #Save self.__djuret
            sys.exit(0)

        else:
            os.system('cls')
            print('I don\'t know what that means...')
            input('Press enter to continue')
            self.show_menu()



    def print_status(self):
        os.system('cls')

        print(djur.status())

        input('Press enter to continue')

        self.show_menu()
    


    def show_food(self):
        os.system('cls')

        for i, item in enumerate(djur.__foodmanager.get_options()):
            print(f'{i+1}: {item}')

        foodRequest = input().lower()

        self.__foodmanager.use(foodRequest)

        self.print_status()
    
        input('Press enter to continue')

        self.show_menu()



    def show_hygene(self):
        os.system('cls')

        for i, item in enumerate(self.__hygienmanager.get_options.keys()):
            print(f'{i+1}: {item}')

        self.hygeneRequest = input().lower()

        if self.hygeneRequest == self.__hygienmanager.get_options.keys()[0] or self.hygeneRequest == '1':
            self.__hygienmanager.get_options[self.__hygienmanager.get_options.keys()[0]]()

        self.print_status()
        
        input('Press enter to continue')

        self.show_menu()



    def show_activities(self):
        os.system('cls')

        for i, item in enumerate(self.__healthmanager.get_options()):
            print(f'{i+1}: {item}')

        self.activityRequest = input().lower()

        self.__healthmanager.activity(self.activityRequest)

        self.print_status()

        input('Press enter to continue')
        
        self.show_menu()



    def show_settings(self):
        os.system('cls')

        for i, item in enumerate(self.__settings):
            print(f'{i+1}: {item}')

        self.settingRequest = input().lower()

        if self.settingRequest == 'dark/light mode' or self.settingRequest == 'darkmode' and self.__darkMode == False or self.settingRequest == 'lightmode' and self.__darkMode == True:
           self.__darkMode = not self.__darkMode 
        
        input('Press enter to continue')
        
        self.show_menu()




main_menu = Menu('Main Menu', ['Status', 'Drink/Eat', 'Hygene', 'Activities', 'Settings', 'Quit'])

#djur = djur.Djur('Jure')

main_menu.start_menu()
