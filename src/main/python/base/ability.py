class Ability:

    def __init__(self, name, description, type:str, value, ability_cost):
        self._name = name
        self._description = description
        self._type = type
        self._value = value
        self._ability_cost = ability_cost



    @property
    def ability_cost(self):
        return self._ability_cost

    @ability_cost.setter
    def ability_cost(self, value):
        self._ability_cost = value

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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
