from content.player.controllers.player_controller import PlayerController
from services.data_store import DataStore
from utils.print_utils import PrintUtils


class InnModel:
    def __init__(self):
        self.datastore = DataStore()

    def get_inns_by_player_current_city(self,player):
        return self.datastore.find_inns_by_city(player.city)


    def rest(self):
        player =  PlayerController.get_player()
        inn = self.get_inns_by_player_current_city(player)[0]

        if player.wallet.coins >= self.price_per_stay:
            PrintUtils.print_dot_loading_animation("Descansando")
            PrintUtils.print_slowly("\nVoce descansou!")
            print("\nSua vida, mana e stamina foram renovados")
            
            player.wallet.subtract_coins(self.price_per_stay)
            PlayerController.restore_full_health()
            PlayerController.restore_full_mana()
            PlayerController.restore_full_stamina()

            PlayerController.set_player_state(player)
            PlayerController.save_player_state()
        else:
            PrintUtils.print_entity_dialog(inn.inkeeper,"Só volte aqui quando tiver grana pra pagar pelo quarto!\n")
            print("Voce nao tem moedas o suficiente para pagar por um quarto")
        
        
        
    def leave(self):
        pass