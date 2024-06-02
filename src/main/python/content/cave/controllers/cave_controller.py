

from content.cave.models.cave_model import CaveModel
from services.location_service import LocationService


class CaveController:
    def __init__(self):
        self.model = CaveModel()

    def explore(self):
        self.model.explore()

    def open_inventory(self):
        self.model.open_inventory()

    def open_journal(self):
        self.model.open_journal()

    def leave(self,previous_structure_view):
        LocationService.leave(previous_structure_view)