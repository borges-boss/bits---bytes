from content.game_save.models.game_save_model import GameSaveModel
from content.player.models.player_model import PlayerModel


class PlayerController:

    global_player = None

    @classmethod
    def load_player(cls):
        model = GameSaveModel()
        cls.global_player = model.get_player_info()

    @classmethod
    def save_player_state(cls):
        model = GameSaveModel()
        cls.global_player = model.save_game(cls.global_player)
        print("O jogo foi salvo.")

    @classmethod
    def get_player(cls):
        return cls.global_player
    
    @classmethod
    def set_player_state(cls, player):
        cls.global_player = player

    @classmethod
    def restore_full_health(cls):
        player_model = PlayerModel()
        cls.global_player.health(player_model.get_player_max_health(cls.global_player)) #Restaurar vida completa do jogador

    @classmethod
    def restore_full_mana(cls):
        player_model = PlayerModel()
        cls.global_player.mana(player_model.get_player_max_mana(cls.global_player)) 

    @classmethod
    def restore_full_stamina(cls):
        player_model = PlayerModel()
        cls.global_player.stamina(player_model.get_player_max_stamina(cls.global_player)) 

    @classmethod
    def equip_piece_of_armor(cls,wearable_item):
        player_model = PlayerModel()
        cls.set_player_state(player_model.equip_piece_of_armor(wearable_item, cls.get_player()))

    @classmethod
    def equip_item(cls,item):
        player_model = PlayerModel()
        cls.set_player_state(player_model.equip_item(item,cls.get_player()))

    @classmethod
    def use_consumable(cls,item):
        player_model = PlayerModel()
        cls.set_player_state(player_model.use_consumable(item,cls.get_player()))

    @classmethod
    def useAbility(cls, ability, target):
        player_model = PlayerModel()
        return player_model.useAbility(ability,target,cls.get_player())
    
    @classmethod
    def get_player_damage(cls):
        player_model = PlayerModel()
        return player_model.get_player_damage(cls.get_player())
    
    @classmethod
    def get_player_defence(cls):
        player_model = PlayerModel()
        return player_model.get_player_defence(cls.get_player())


        
    
