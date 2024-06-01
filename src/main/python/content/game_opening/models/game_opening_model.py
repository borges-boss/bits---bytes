from services.data_store import DataStore
from constants.constants import GAME_START_INTRO_TEXT_KEY
from services.file_reader import FileReader

class GameOpeningModel:

   def __init__(self):
      self.data_store = DataStore()
      self.file_reader = FileReader()

   def get_opening_text(self):
        return self.data_store.find_data_by_key(GAME_START_INTRO_TEXT_KEY)
   
   def get_ascii_art(self):
       return self.file_reader.read_file_contents("src\main\\res\\demon_face.txt")