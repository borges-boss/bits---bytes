import time
from python.base.entity import Entity

class PrintUtils:

    @staticmethod
    def print_slowly(text,delay):
        for character in text:
          print(character, end='', flush=True)
          time.sleep(delay)

          
    @staticmethod
    def print_entity_dialog(self,entity:Entity,text):
       self.print_slowly(entity.name+": "+text, 0.05)
       
    
