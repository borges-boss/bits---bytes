from content.game_save.models.game_save_model import GameSaveModel


class GameSaveController:
    def __init__(self):
        self.model = GameSaveModel()

    def get_saves(self):
        return self.model.get_saves()

    def save_game(self, player):
        self.model.save_game(player)


    def get_player_info(self):
        return self.model.get_player_info()