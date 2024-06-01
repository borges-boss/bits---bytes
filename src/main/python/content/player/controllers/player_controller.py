from content.game_save.models.game_save_model import GameSaveModel

class PlayerController:

    global_player = None

    def __init__(self):
        self.model = GameSaveModel()


    def get_player(self):
        return self.model.get_player_info()