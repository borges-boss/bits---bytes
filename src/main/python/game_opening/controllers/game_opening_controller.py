from game_opening.models.game_opening_model import GameOpeningModel
from game_opening.views.game_opening_view import GameOpeningView
from utils.console_utils import ConsoleUtils

class GameOpeningController:

    def __init__(self):
      self.model = GameOpeningModel()
      self.view = GameOpeningView()


    def show_intro_text(self):
        ConsoleUtils.clear_terminal()
        intro_text = self.model.get_opening_text()
        if len(intro_text) > 0:
           intro_text = intro_text[0]

        self.view.display_intro_text(intro_text)