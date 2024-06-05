from base.entity import Entity

class Npc(Entity):

    def __init__(self, health, defence, race, type, name,description,role):
      super().__init__(name, health, 0, defence, 0, race, type)
      self._description = description
      self._role = role

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


    def to_dict(self):
        return {
            'name': self.name,
            'health': self.health,
            'defence': self.defence,
            'race': self.race,
            'type': self.type,
            'description': self.description,
            'role': self.role
        }

