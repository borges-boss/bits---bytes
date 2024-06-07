import time
from base.ability import Ability
from classes.damage_item import DamageItem
from classes.dungeon import Dungeon
from classes.monster import Monster
from constants.constants import ITEM_RARITY_COMMON, ITEM_TYPE_DAMAGE, RACE_TYPE_DEMON, STRUCTURE_TYPE_DUNGEON
from content.battle.views.battle_view import BattleView
from content.city_structure.views.city_structure_view import CityStructureView
from content.player.controllers.player_controller import PlayerController
from services.data_store import DataStore
from utils.console_utils import ConsoleUtils
from utils.print_utils import PrintUtils


class PrisonView:

    def __init__(self):
        PlayerController.init_player_abilities()
        PlayerController.init_player_attributes()
        self.prison = Dungeon("Prisao",STRUCTURE_TYPE_DUNGEON,1,0,1,[],1,[])
        self.player = PlayerController.get_player()
        self.player.location = self.prison
        self.player.city = "Rivendell"
        PlayerController.silent_save(self.player)
        ConsoleUtils.clear_terminal()
        self.is_battle_finished = False

    

    def wake_up(self):
        PrintUtils.print_slowly("A escuridão da cela de prisão é interrompida abruptamente por um estrondo ensurdecedor. O chão frio e úmido treme sob você enquanto sons de luta e gritos ecoam pelos corredores de pedra.\n"+
                                "Você se levanta, os olhos lutando para se ajustar à fraca luz que se infiltra através das barras enferrujadas da cela. O ar está carregado com uma tensão palpável, uma sensação de medo e urgência que faz seu coração acelerar.\n"
                                +"De repente, a porta da sua cela é arremessada aberta com um estrondo. Um guarda da prisão entra, ofegante e coberto de suor.\n")
        
        PrintUtils.print_slowly("\nGuarda: Os exércitos do rei demônio estão aqui! Eles estão matando todos...")
        PrintUtils.print_slowly("\nGuarda: Fuja!")

        PrintUtils.print_slowly("\nVocê pega as chaves, a realidade da situação começando a afundar. A prisão está sendo invadida. E se você não agir rápido, pode ser o próximo.\nCom um ultimo olhar para a cela que foi sua casa por tanto tempo, voce sai correndo para o corredor, pronto para enfrentar o desconhecido. A aventura esta apenas começando.")
        time.sleep(2)
        name = None
        ConsoleUtils.clear_terminal()
        while name == None:
             print("\nDigite o seu nome:")
             name = str(input())
             print(f"\nEntao voce quer ser chamado de {name}? (s/n)")
             confirm = str(input())
             if confirm.lower() == "s":
                 self.player.name = name
                 PlayerController.silent_save(self.player)
                 ConsoleUtils.clear_terminal()
             else:
                 ConsoleUtils.clear_terminal()
                 name = None

        PrintUtils.print_slowly("Passando pelos corredores da prisão voce se depara com dois corpos mutilados e um Soldado Infernal que acabou de fazer mais uma vitima bem na sua frente!")
        print("\n")
        PrintUtils.print_slowly("A visão do Soldado Infernal é assustadora. Ele é uma criatura imponente, com chifres retorcidos e olhos que brilham com um fogo maligno. Seu corpo é coberto por uma armadura negra e ele empunha uma espada que parece feita de sombras sólidas.")
        print("\n")
        PrintUtils.print_slowly("Você sente o medo se infiltrar em seu peito, mas sabe que não pode se dar ao luxo de hesitar. Você tem que lutar. Com as mãos trêmulas, você pega uma espada caída ao lado de um dos corpos e se prepara para o confronto...")
        sword = DamageItem("Espada de Ferro",ITEM_TYPE_DAMAGE,ITEM_RARITY_COMMON,4.0,[],3.4)
        self.player.inventory.add_item(sword)
        self.player.equipped_item = sword 
        PlayerController.silent_save(self.player)

        monster = Monster(110,10,40,50,RACE_TYPE_DEMON,RACE_TYPE_DEMON,"Soldado Infernal",70,"Um soldado dos exercitos do rei demonio",[],1)
        slash = Ability("Corte", "Um ataque básico com a espada.", "physical", 20, 5)
        fireball = Ability("Bola de Fogo", "Um ataque mágico de fogo.", "magic", 30, 10)
        monster.abilities.append(slash)
        monster.abilities.append(fireball)
        
        datastore = DataStore()
        city = datastore.find_city_by_name(self.player.city)[0]
        city_open_fields = datastore.find_open_fields_by_city(self.player.city) # Lembrar de cadastrar essa cidade nos arquivos json

        BattleView(monster, CityStructureView(city_open_fields[0],city.structures)).init_view()
            
                 
     
                 
    


    