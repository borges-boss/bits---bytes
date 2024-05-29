from services.data_store import DataStore
from content.game_save.mappings.game_save_log_mapping import GameSaveLogMapper
from constants.constants import GAME_SAVES_KEY

class LoadMenuModel:
    def __init__(self):
        self.datastore = DataStore()

    def get_save_logs(self):
       save_logs = self.datastore.find_by_key(GAME_SAVES_KEY)
       return GameSaveLogMapper.map_to_model(save_logs)

