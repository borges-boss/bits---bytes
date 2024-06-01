import time
import os
from base.entity import Entity

class PrintUtils:

    @staticmethod
    def print_slowly(text,delay):
        for character in text:
          print(character, end='', flush=True)
          time.sleep(delay)

          
    @staticmethod
    def print_entity_dialog(entity:Entity,text:str):
       PrintUtils.print_slowly(entity.name+": "+text, 0.05)
       print("\n")

    @staticmethod
    def print_separator_line():
        terminal_width = os.get_terminal_size().columns
        print("-" * terminal_width)
        print("\n")

    @staticmethod
    def print_centered(text):
        terminal_width = os.get_terminal_size().columns
        print(text.center(terminal_width))




       
    
