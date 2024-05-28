import shutil

class LoadMenuView:
    def __init__(self):
        self.columns, self.rows = shutil.get_terminal_size()
        self.margin = 16
        self.box_width = self.columns - (2 * self.margin)

    def create_box(self, game_text, time_text):
        box = (
            f"{' ' * self.margin}┌{'─' * (self.box_width - 2)}┐\n" +
            f"{' ' * self.margin}│{game_text:^{self.box_width - 2}}│\n" +
            f"{' ' * self.margin}│{' ' * (self.box_width - 2)}│\n" +
            f"{' ' * self.margin}│{'Last saved:':^{self.box_width - 2}}│\n" +
            f"{' ' * self.margin}│{time_text:^{self.box_width - 2}}│\n" +
            f"{' ' * self.margin}└{'─' * (self.box_width - 2)}┘\n"
        )
        return box

    def display(self, header, game_boxes):
        full_screen_output = header + ''.join(game_boxes)
        print(full_screen_output)