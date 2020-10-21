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

        if request == 'status' or request == "1":
            self.print_status()

        elif request == 'food' or request == "2":
            self.show_Food()

        elif request == 'hygene' or request == "3":
            self.show_Hygene()

        elif request == 'activities' or request == "4":
            self.show_Activities()

        elif request == 'settings' or request == "5":
            self.show_Settings()

        elif request == 'quit' or request == "6":
            sys.exit(0)

        else:
            print('I don\'t know what that means...')



    def print_status(self):
        print(djur.status())
    


    def show_food(self):
        for i, item in enumerate(self.__foodmanager.get_options1()):
            print(f'{i+1}: {item}')

        foodRequest = input().lower()

        for i, item in enumerate(self.__foodmanager.get_options2(foodRequest)):
            print(f'{i+1}: {item}')

        foodRequest = input().lower()

        self.__foodmanager.eat(foodRequest)

        self.print_status()



    def show_hygene(self):
        for i, item in enumerate(self.__hygienmanager.get_options()):
            print(f'{i+1}: {item}')

        self.hygeneRequest = input().lower()

        self.__hygienmanager.do(self.hygeneRequest)

        self.print_status()



    def show_activities(self):
        for i, item in enumerate(self.__healthmanager.get_options()):
            print(f'{i+1}: {item}')

        self.activityRequest = input().lower()

        self.__healthmanager.activity(self.activityRequest)

        self.print_status()



    def show_settings(self):
        for i, item in enumerate(self.__settings):
            print(f'{i+1}: {item}')

        self.settingRequest = input().lower()

        if self.settingRequest == 'dark/light mode' or self.settingRequest == 'darkmode' and self.__darkMode == False or self.settingRequest == 'lightmode' and self.__darkMode == True:
           self.__darkMode = not self.__darkMode 




main_menu = Menu('Main Menu', ['Status', 'Food', 'Hygene', 'Activities', 'Settings', 'Quit'])

djur = djur.Djur('Jure')

main_menu.show_menu()
