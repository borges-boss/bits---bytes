from constants.constants import CLASS_TYPE_ASSASIN, CLASS_TYPE_BATTLE_MAGE, CLASS_TYPE_BERSERKER, CLASS_TYPE_MAGE, CLASS_TYPE_WARRIOR
from classes.player import Player
from content.player.controllers.player_controller import PlayerController
from content.player.models.player_model import PlayerModel
from content.prison.views.prison_view import PrisonView
from utils.print_utils import PrintUtils


class ClassSelectionView:


    def __init__(self) -> None:
        self.available_classes = [CLASS_TYPE_WARRIOR, CLASS_TYPE_MAGE, CLASS_TYPE_ASSASIN, CLASS_TYPE_BERSERKER, CLASS_TYPE_BATTLE_MAGE]
        self.player_model = PlayerModel()
        self.is_running = True

    def select_class(self):
        PrintUtils.print_centered("Available races:")
        print("\n")
        PrintUtils.print_separator_line()

        for i, class_type in enumerate(self.available_classes, start=1):
            temp_player = Player(game_class=class_type) 

            base_health = self.player_model.get_base_health(temp_player)
            base_mana = self.player_model.get_base_mana(temp_player)
            base_stamina = self.player_model.get_base_stamina(temp_player)
            base_damage = self.player_model.get_base_damage(temp_player)
            base_defence = self.player_model.get_base_defence(temp_player)

            print(f"{i}. {class_type}")
            print(f"   Saude: {base_health}")
            print(f"   Mana: {base_mana}")
            print(f"   Stamina: {base_stamina}")
            print(f"   Dano: {base_damage}")
            print(f"   Defesa: {base_defence}\n")

        while self.is_running:
            try:
                class_choice = int(input("Digite o numero da classe que voce deseja escolher: "))
                if 1 <= class_choice <= len(self.available_classes):
                    chosen_class = self.available_classes[class_choice - 1]
                    print(f"Você escolheu a classe {chosen_class}.")

                    confirm = input("Voce tem certeza que quer escolher essa classe? (s/n): ")
                    if confirm.lower() == 's':
                        self.stop_view()
                        PlayerController.get_player().game_class = chosen_class
                        PrisonView().wake_up()
                    else:
                        print("Ok, vamos tentar novamente.")
                        
                else:
                    print("Escolha invalida. Por favor digite um numero correspondente qs classes listadas acima.")
            except ValueError:
                print("Entrada invalida. Por favor digite apenas numeros.")



    def init_view(self):
        self.is_running = True
        self.select_class()


    def stop_view(self):
        self.is_running = False
