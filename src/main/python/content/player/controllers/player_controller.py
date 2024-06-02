from content.game_save.models.game_save_model import GameSaveModel


class PlayerController:

    global_player = None

    @classmethod
    def load_player(cls):
        model = GameSaveModel()
        cls.global_player = model.get_player_info()

    @classmethod
    def save_player_state(cls):
        model = GameSaveModel()
        cls.global_player = model.save_game(cls.global_player)
        print("O jogo foi salvo.")

    @classmethod
    def get_player(cls):
        return cls.global_player
    
    @classmethod
    def set_player_state(cls, player):
        cls.global_player = player
    
