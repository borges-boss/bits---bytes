from classes.player import Player
from constants.constants import REWARD_TYPE_ITEM

class Quest:

    def __init__(self, name, description, reward, reward_type, is_completed = False):
        self._name = name
        self._description = description
        self._reward = reward
        self._reward_type = reward_type
        self._is_completed = is_completed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def reward(self):
        return self._reward

    @reward.setter
    def reward(self, value):
        self._reward = value

    @property
    def reward_type(self):
        return self._reward_type

    @reward_type.setter
    def reward_type(self, value):
        self._reward_type = value

    @property
    def is_completed(self):
        return self._is_completed

    @is_completed.setter
    def is_completed(self, value):
        self._is_completed = value

        
    def complete_and_get_reward(self, player:Player):
        if not self.is_completed:
            self.is_completed = True
            print(f'A quest "{self.name}" foi concluida!')

            if self.reward_type == REWARD_TYPE_ITEM:
                print(f'Voce ganhou "{self.reward.name}" como recompensa.')
                player.inventory.add_item(self.reward)
            else:
                print(f'Voce ganhou "{self.reward}" moedas como recompensa.')
                player.wallet.add_coins(self.reward)
            
        else:
            print(f'You have already completed the quest "{self.name}".')