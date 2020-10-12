class Menu:
    """
    (Docstring)
    En klass för att beskriva en meny.
    """    

    def __init__(self, title, menu_items):
        self.__menu_items=(menu_items)
        self.__title=title

    #Visar menyn
    def show_menu(self):
        print(self.__title)

        for i, item in enumerate(self.__menu_items):
            print(f'{i+1}: {item}')

main_menu = Menu('Huvudmeny', ['Status', 'Mat', 'Hygien', 'Aktiviteter', 'Inställningar', 'Avsluta'])

main_menu.show_menu()
help(Menu)
