from base.entity import Entity

class Npc(Entity):

    def __init__(self, health, defence, race, type,name,description,role):
      super().__init__(health, defence, race, type)
      self._name = name
      self._description = description
      self._role = role

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
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    
    def interact_with(self):
        print("Interact")

