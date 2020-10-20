import djur
import foodmanager
import hygienmanager
import healthmanager

import sys

class Menu:

    
    def __init__(self, title, menu_items):
        self.__menu_items = (menu_items)

        self.__settings = ['dark/light mode']

        self.__title = title

        self.__darkMode = False

        self.__foodmanager = foodmanager.FoodManager()

        self.__hygienmanager = hygienmanager.HygienManager()

        self.__healthmanager = healthmanager.HealthManager()



    def show_menu(self):
        print(self.__title)

        for i, item in enumerate(self.__menu_items):
            print(f'{i+1}: {item}')
        request = input().lower()

        if request == 'status':
            Menu.printStatus()

        elif request == 'food':
            Menu.show_Food()

        elif request == 'hygene':
            Menu.show_Hygene()

        elif request == 'activities':
            Menu.show_Activities()

        elif request == 'settings':
            Menu.show_Settings()

        elif request == 'quit':
            sys.exit(0)

        else:
            print('I don\'t know what that means...')



    def printStatus(self):
        print(djur.status())
    


    def show_Food(self):
        for i, item in enumerate(self.__foodmanager.getOptions1()):
            print(f'{i+1}: {item}')

        foodRequest = input().lower()

        for i, item in enumerate(self.__foodmanager.getOptions2(foodRequest)):
            print(f'{i+1}: {item}')

        foodRequest = input().lower()

        self.__foodmanager.eat(foodRequest)

        Menu.printStatus()



    def show_Hygene(self):
        for i, item in enumerate(self.__hygienmanager.getOptions()):
            print(f'{i+1}: {item}')

        self.hygeneRequest = input().lower()

        self.__hygienmanager.do(self.hygeneRequest)

        Menu.printStatus()



    def show_Activities(self):
        for i, item in enumerate(self.__healthmanager.getOptions()):
            print(f'{i+1}: {item}')

        self.activityRequest = input().lower()

        self.__healthmanager.activity(self.activityRequest)

        Menu.printStatus()



    def show_Settings(self):
        for i, item in enumerate(self.__settings):
            print(f'{i+1}: {item}')

        self.settingRequest = input().lower()

        if self.settingRequest == 'dark/light mode' or self.settingRequest == 'darkmode' and self.__darkMode == False or self.settingRequest == 'lightmode' and self.__darkMode == True:
           self.__darkMode = not self.__darkMode 




main_menu = Menu('Main Menu', ['Status', 'Food', 'Hygene', 'Activities', 'Settings', 'Quit'])

djur = djur.Djur('Jure')

main_menu.show_menu()
