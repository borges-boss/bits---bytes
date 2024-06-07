from content.game_opening.models.game_opening_model import GameOpeningModel
from content.game_opening.views.game_opening_view import GameOpeningView
from content.player.controllers.player_controller import PlayerController
from content.race_selection.views.race_selection_view import RaceSelectionView
from utils.console_utils import ConsoleUtils
import keyboard

class GameOpeningController:

    def __init__(self):
      self.model = GameOpeningModel()
      self.view = GameOpeningView()

    def start_game(self):
       PlayerController.init_new_player_instance()
       ConsoleUtils.clear_terminal()
       RaceSelectionView().init_view()
    
    def show_ascii_art(self):
       art = self.model.get_ascii_art()
       print(art)

    def show_transition_key(self):
        print("")
        print("Pressione Espaco para continuar...")
        keyboard.wait("space")
        self.start_game()

    def show_intro_text(self):
        ConsoleUtils.clear_terminal()
        intro_text = self.model.get_opening_text()
        if len(intro_text) > 0:
           intro_text = intro_text[0]

        self.view.display_intro_text(intro_text)
        


    def show_intro(self):
       self.show_intro_text()
       self.show_transition_key()
       