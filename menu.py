import djur
import foodmanager
import hygienmanager
import healthmanager

import sys

class Menu:

    
    def __init__(self, title, menu_items, food_items, hygene_Options, activities):
        self.__menu_items = (menu_items)
        self.__food_items = (food_items)
        self.__hygene_Options = (hygene_Options)
        self.__activities = (activities)
        self.__settings = ['dark/light mode']
        self.__title=title

        self.__darkMode = False

        self.__foodmanager = foodmanager.FoodManager()
        self.__hygienmanager = hygienmanager.HygienManager()
        self.__healthmanager = healthmanager.HealthManager()


    def show_menu(self):
        print(self.__title)

        for i, item in enumerate(self.__menu_items):
            print(f'{i+1}: {item}')

    def printStatus(self):
        print(djur.status())
    
    def show_Food(self):
        for i, item in enumerate(self.__food_items):
            print(f'{i+1}: {item}')
        foodRequest = input().lower()
        self.__foodmanager.eat(foodRequest)
        Menu.printStatus()

    def show_Hygene(self):
        for i, item in enumerate(self.__hygene_Options):
            print(f'{i+1}: {item}')
        self.hygeneRequest = input().lower()
        self.__hygienmanager.do(self.hygeneRequest)
        Menu.printStatus()

    def show_Activities(self):
        for i, item in enumerate(self.__activities):
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




main_menu = Menu('Huvudmeny', ['Status', 'Mat', 'Hygien', 'Aktiviteter', 'Inställningar', 'Avsluta'], ['candy', 'meat', 'water'], ['shower', 'hand sanitizer'], ['play', 'exercise'])

djur = djur.Djur('Jure')

main_menu.show_menu()

request = input().lower()

if request == 'status':
    Menu.printStatus()
elif request == 'mat':
    Menu.show_Food()
elif request == 'hygien':
    Menu.show_Hygene()
elif request == 'aktiviteter':
    Menu.showActivities()
elif request == 'inställningar':
    Menu.show_Settings
elif request == 'avsluta':
    sys.exit(0)
else:
    print('Jag vet inte vad det betyder...')
