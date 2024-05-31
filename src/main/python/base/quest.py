from base.item import Item
from constants.constants import REWARD_TYPE_ITEM

class Quest:

    def __init__(self, name, description, reward, reward_type):
        self.name = name
        self.description = description
        self.reward = reward
        self._reward_type = reward_type
        self.is_completed = False

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_description(self):
        return self.description

    def set_description(self, value):
        self.description = value

    def get_reward(self):
        return self.reward

    def set_reward(self, value):
        self.reward = value

    @property
    def reward_type(self):
        return self._reward_type

    @reward_type.setter
    def reward_type(self, value):
        self._reward_type = value

        
    def complete_and_get_reward(self, player):
        if not self.is_completed:
            self.is_completed = True
            print(f'Quest "{self.name}" has been completed!')
            
        else:
            print(f'You have already completed the quest "{self.name}".')

    def display_quest_info(self):
        status = "Completed" if self.is_completed else "Not Completed"
        if self.reward_type == REWARD_TYPE_ITEM:
            print(f'Quest Name: {self.name}\nDescription: {self.description}\nReward: {self.get_reward_names()}\nStatus: {status}')
        else:
            print(f'Quest Name: {self.name}\nDescription: {self.description}\nReward: {self.reward} coins\nStatus: {status}')
            

    def get_reward_names(self):
        return ', '.join([item.name for item in self.reward])