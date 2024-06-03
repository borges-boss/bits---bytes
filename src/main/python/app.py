from content.menu.controllers.menu_controller import MenuController
from base.journal import Journal
from base.wallet import Wallet
from classes.damage_item import DamageItem
from classes.inventory import Inventory
from classes.open_fields import OpenFields
from classes.player import Player
from content.player.controllers.player_controller import PlayerController
from services.location_service import LocationService


if __name__ == '__main__':
     player = Player(200,100,300,1,"Test","Human","Warrior",[],20,2.2,Wallet(100),Inventory([],500.0),DamageItem("Hands","damage_item","Common",0,[],1),[],Journal([]),OpenFields("Open","open_fields",100,100, 10, [], [],"Test"),"Townsville")
     PlayerController.set_player_state(player)
     #PlayerController.display_player_hud()
     LocationService.travel()
    # monster = Monster(200,100,300,1,"Slime","", "",500,"It's a slime",[Ability("Pounce","","physical",3,1)],20)
     #BattleView(monster,OpenFieldsView(OpenFields("Green Meadows","open_fields",100,100, 10, [], [],"Townsville"))).init_view()
     #menu_controller = MenuController()
    #menu_controller.init_menu()
  