from content.player.controllers.player_controller import PlayerController


class InventoryModel:

    def get_items(self):
        return PlayerController.get_player().inventory.items