import os
import platform

class ConsoleUtils:

    @staticmethod
    def clear_terminal():
     current_os = platform.system()
    
     if current_os == "Windows":
        os.system('cls')
     else:
        os.system('clear')


