from classes.npc import Npc
from classes.pacific_structure import PacificStructure
from base.quest import Quest
from typing import List

class Tavern(PacificStructure):

    def __init__(self, name, type, width, height, tavern_keeper:Npc, quests: List[Quest]):
        super().__init__(name, type, width, height, [])
        self._tavern_keeper = tavern_keeper
        self._quests = quests

    @property
    def tavern_keeper(self):
        return self._tavern_keeper

    @tavern_keeper.setter
    def tavern_keeper(self, value):
        self._tavern_keeper = value

    @property
    def quests(self):
        return self._quests

    @quests.setter
    def quests(self, value):
        self._quests = value

        