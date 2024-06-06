from content.player.controllers.player_controller import PlayerController
from services.data_store import DataStore
from utils.print_utils import PrintUtils


class InnModel:
    def __init__(self,inn):
        self.datastore = DataStore()
        self.inn = inn

    def rest(self, player):

        if player.wallet.coins >= self.inn.price_per_stay:
            PrintUtils.print_dot_loading_animation("Descansando")
            PrintUtils.print_slowly("\nVoce descansou!")
            print("\nSua vida, mana e stamina foram renovados")
            
            player.wallet.subtract_coins(self.inn.price_per_stay)
            player = PlayerController.restore_full_health()
            player = PlayerController.restore_full_mana()
            player = PlayerController.restore_full_stamina()

            PlayerController.save_player_state(player)
        else:
            PrintUtils.print_entity_dialog(self.inn.inkeeper,"Só volte aqui quando tiver grana pra pagar pelo quarto!\n")
            print("Voce nao tem moedas o suficiente para pagar por um quarto")
        