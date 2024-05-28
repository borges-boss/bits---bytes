from services.data_store import DataStore
from constants.constants import GAME_START_INTRO_TEXT_KEY

class GameOpeningModel:

   def __init__(self):
      self.data_store = DataStore()

   def get_opening_text(self):
        return self.data_store.find_by_key(GAME_START_INTRO_TEXT_KEY)