from content.load_menu.views.load_menu_view import LoadMenuView
from content.game_save.models.game_save_model import GameSaveModel
from constants.constants import STRUCTURE_TYPE_CAVE, STRUCTURE_TYPE_DUNGEON, STRUCTURE_TYPE_INN, STRUCTURE_TYPE_OPEN_FIELD, STRUCTURE_TYPE_SHOP, STRUCTURE_TYPE_TAVERN
from content.cave.views.cave_view import CaveView
from content.city_structure.views.city_structure_view import CityStructureView
from content.dungeon.views.dungeon_view import DungeonView
from content.inn.views.inn_view import InnView
from content.open_fields.views.open_fields_view import OpenFieldsView
from content.player.controllers.player_controller import PlayerController
from content.shop.views.shop_view import ShopView
from content.tavern.views.tavern_view import TavernView
from services.data_store import DataStore
from utils.console_utils import ConsoleUtils

class LoadMenuController:
    def __init__(self,menu_controller):
        self.model = GameSaveModel()
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
              if decision.lower() == "s":
                PlayerController.load_player()
                datastore = DataStore()
                
                current_player_location = PlayerController.get_player().location
                city_open_field = datastore.find_open_fields_by_city(PlayerController.get_player().city)
                city = datastore.find_city_by_name(PlayerController.get_player().city)[0]
                
                if current_player_location.type == STRUCTURE_TYPE_DUNGEON:
                    DungeonView(OpenFieldsView(city_open_field[0]),current_player_location).init_view()
                elif current_player_location.type == STRUCTURE_TYPE_CAVE:
                    CaveView(CityStructureView(city_open_field[0],city.structures),current_player_location).init_view()
                elif current_player_location.type == STRUCTURE_TYPE_INN:
                    InnView(CityStructureView(city_open_field[0],city.structures),current_player_location).init_view()
                elif current_player_location.type == STRUCTURE_TYPE_OPEN_FIELD:
                    OpenFieldsView(city_open_field[0]).init_view()
                elif current_player_location.type == STRUCTURE_TYPE_SHOP:
                    ShopView(CityStructureView(city_open_field[0],city.structures),current_player_location).init_view()
                elif current_player_location.type == STRUCTURE_TYPE_TAVERN:
                    TavernView(CityStructureView(city_open_field[0],city.structures),current_player_location).init_view()
                else:
                    print("Local desconhecido")

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

        game_saves = self.model.get_saves()
        game_saves.sort(key=lambda x: x['last_save'])
        game_boxes = [self.view.create_box(f"{game_saves[i]['title']}", game_saves[i]['last_save']) for i in range(len(game_saves))]

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
