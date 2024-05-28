from utils.console_utils import ConsoleUtils

class NavigationUtils:

    def __init__(self,menu_controller):
        self.menu_controller = menu_controller
    
    def navigate_to_main_menu(self):
        ConsoleUtils.clear_terminal()
        self.menu_controller.init_menu()
        
