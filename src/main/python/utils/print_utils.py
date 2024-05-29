import time

class PrintUtils:

    @staticmethod
    def print_slowly(text,delay):
        for character in text:
          print(character, end='', flush=True)
          time.sleep(delay) 
    
