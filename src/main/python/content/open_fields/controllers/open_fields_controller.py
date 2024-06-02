from content.open_fields.models.open_fields_model import OpenFieldsModel


class OpenFieldsController:
    def __init__(self, open_fields):
        self.model = OpenFieldsModel(open_fields)

    def explore(self):
        self.model.explore()

    def open_inventory(self):
        self.model.open_inventory()

    def open_journal(self):
        self.model.open_journal()

    def travel(self):
        self.model.leave()