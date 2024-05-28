from load_menu.models.load_menu_model import LoadMenuModel
from load_menu.views.load_menu_view import LoadMenuView
from utils.console_utils import ConsoleUtils

class LoadMenuController:
    def __init__(self,menu_controller):
        self.model = LoadMenuModel()
        self.view = LoadMenuView()
        self.menu_controller = menu_controller

    def get_input_option(self,saves_count):
        input_string = "Digite uma opção de 1 a "+str(saves_count)+" para carregar"

        while True:
          option = int(self.input_value(input_string))
          #Numero maximo de save slots é 4
          if option in range(saves_count+1) and (option > 0 and option <= 4):
              print("Voce tem certeza que quer carregar o save "+str(option)+" ?")
              print("S - Sim")
              print("N - Não")
              decision = str(input())
              if decision == "S":
                print("Loaded option: ",option)
                break
              else:
                  ConsoleUtils.clear_terminal()
                  self.display_menu()
          else:
              ConsoleUtils.clear_terminal()
              self.display_menu()
              print("Por favor digite uma opção de 1 a ",saves_count)
              
              
    def display_menu(self):
        header_text = "Games in progress"
        dashed_line = "-" * self.view.box_width
        header = f"{header_text:^{self.view.columns}}\n{' ' * self.view.margin}{dashed_line}\n"

        game_saves = self.model.get_save_logs()
        game_boxes = [self.view.create_box(f"{game_saves[i].title}", game_saves[i].last_save) for i in range(len(game_saves))]

        self.saves_count = len(game_saves)
        self.view.display(header, game_boxes)
        

    
    def init_menu(self):
        self.display_menu()
        self.get_input_option(self.saves_count)


    def input_value(self,message): 
        value = input(message+" (Ou digite 'menu' para voltar):")
        
        if value.strip().lower() == "menu":
            self.menu_controller.init_menu()
            return
        
        return int(value)
