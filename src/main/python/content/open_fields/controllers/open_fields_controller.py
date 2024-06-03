from content.open_fields.models.open_fields_model import OpenFieldsModel


class OpenFieldsController:
    def __init__(self):
        self.model = OpenFieldsModel()

    def explore(self):
        self.model.explore()

    def open_inventory(self):
        self.model.open_inventory()

    def open_journal(self):
        self.model.open_journal()

    def find_open_fields_by_city(self,city):
        return self.model.find_open_fields_by_city(city)