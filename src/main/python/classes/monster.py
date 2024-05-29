from base.entity import Entity

class Monster(Entity):

    def __init__(self, health, defence,stamina, race, type, name, mana, description, abilities, level):
        super().__init__(health, defence, stamina, race, type)
        self._name = name
        self._mana = mana
        self._description = description
        self._abilities = abilities
        self._level = level


    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def abilities(self):
        return self._abilities

    @abilities.setter
    def abilities(self, value):
        self._abilities = value

    def useAbility(self,ability,target):
        print("Ability")
