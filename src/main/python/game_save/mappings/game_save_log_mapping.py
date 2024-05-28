from game_save.models.game_save_log_model import GameSaveLogModel

class GameSaveLogMapper:
    @staticmethod
    def map_to_model(data):
        return [GameSaveLogModel(item['title'], item['last_save']) for item in data]