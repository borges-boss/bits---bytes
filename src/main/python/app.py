from content.menu.controllers.menu_controller import MenuController 
from content.tavern.controllers.tavern_controller import TavernController
from content.journal.controllers.journal_controller import JournalController

if __name__ == '__main__':
    TavernController("City").list_available_quests() 
    #JournalController().show_my_quests()
     #menu_controller = MenuController()
     #menu_controller.init_menu()
  