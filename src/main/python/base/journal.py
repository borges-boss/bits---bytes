class Journal: 

    def __init__(self,quests):
        self._quests = quests


    @property
    def quests(self):
        return self._quests

    @quests.setter
    def quests(self, value):
        self._quests = value


    def add_quest(self,quest):
        self.quests.append(quest)


    def to_dict(self):
        return {
            'quests': [quest.to_dict() for quest in self._quests]
        }

