import sys
from menu.views.menu_view import MenuView
from menu.models.menu_model import MenuModel
from load_menu.controllers.load_menu_controller import LoadMenuController
from game_opening.controllers.game_opening_controller import GameOpeningController

class MenuController:
    def __init__(self):
        self.model = MenuModel()
        self.view = MenuView()
        self.load_menu_controller = LoadMenuController(self)
        self.game_opening_controller = GameOpeningController()

    def show_menu(self):
        self.view.show_menu(self.model.menu)

    def get_menu_option(self):
        option = ""
        while(option == ""):
         option = str(input("Digite uma das opções acima:"))
         option = option.strip().lower()

         match option:
            case "start":
               self.game_opening_controller.show_intro_text()
            case "load":
               self.load_menu_controller.init_menu()
            case "quit":
               sys.exit()


    def init_menu(self):
       self.show_menu()
       self.get_menu_option()
