import djur
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
            temp = os.walk('Animals')
            names = None
            for i in temp:
                #print(i)
                names = i
            #print (names)
            temporary = None
            for name in names:
                #print(os.path)
                temporary = name
            #print (temporary)
            array = []
            for name in temporary:
                array.append(name.split('.')[0])
            #print(array)
            os.system('cls')
            for i, item in enumerate(array):
                print(f'{i+1}: {item}')

            animalName = input().lower()
            for name in array:
                if animalName == name and not animalName.isnumeric():
                    animalName = name
                    break
                elif animalName.isnumeric():
                    animalName = array[int(animalName) - 1]
                    break
                else:
                    self.start_menu()

            os.system('cls')
            with open('Animals/' + animalName + '.pickle', 'rb') as objektfilen:
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

        print(self.__djuret.status())

        input('Press enter to continue')

        self.show_menu()
    


    def show_food(self):
        os.system('cls')

        for i, item in enumerate(self.__djuret.foodmanager.get_options()):
            print(f'{i+1}: {item}')

        foodRequest = input().lower()

        self.__djuret.foodmanager.use(foodRequest)

        self.print_status()
    
        input('Press enter to continue')

        self.show_menu()



    def show_hygene(self):
        os.system('cls')

        hygieneOptions = self.__djuret.hygienmanager.get_options

        for i, item in enumerate(hygieneOptions.keys()):
            print(f'{i+1}: {item}')

        hygeneRequest = input().lower()

        #if self.hygeneRequest == self.__djuret.hygienmanager.get_options.keys()[0] or self.hygeneRequest == '1':
        #    self.__djuret.hygienmanager.get_options[self.__djuret.hygienmanager.get_options.keys()[0]]()

        for option in hygieneOptions:
            if hygeneRequest == option.keys().lower():
                hygieneOptions.option()

        self.print_status()
        
        input('Press enter to continue')

        self.show_menu()



    def show_activities(self):
        os.system('cls')

        for i, item in enumerate(self.__djuret.healthmanager.get_options()):
            print(f'{i+1}: {item}')

        self.activityRequest = input().lower()

        self.__djuret.healthmanager.activity(self.activityRequest)

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
