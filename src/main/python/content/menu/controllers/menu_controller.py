import sys
from content.menu.views.menu_view import MenuView
from content.menu.models.menu_model import MenuModel
from content.load_menu.controllers.load_menu_controller import LoadMenuController
from content.game_opening.controllers.game_opening_controller import GameOpeningController
from utils.console_utils import ConsoleUtils

class MenuController:
    def __init__(self):
        self.model = MenuModel()
        self.view = MenuView()
        self.load_menu_controller = LoadMenuController(self)
        self.game_opening_controller = GameOpeningController()

    def show_menu(self):
        ConsoleUtils.clear_terminal()
        self.view.show_menu(self.model.menu)

    def get_menu_option(self):
        option = ""
        while(option == ""):
         option = str(input("Digite uma das opções acima:"))
         option = option.strip().lower()

         match option:
            case "start":
               print("Voce tem certeza que deseja iniciar um novo jogo?")
               print("S- Sim")
               print("N- Nao")
               choice = str(input())

               if choice.lower().strip() == "s":
                self.game_opening_controller.show_intro()
               else:
                  option = ""
                  self.show_menu()
            case "load":
               self.load_menu_controller.init_menu()
            case "quit":
               sys.exit()
            case _:
               option = ""
               self.show_menu()


    def init_menu(self):
       self.show_menu()
       self.get_menu_option()
