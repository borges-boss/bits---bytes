import os
import textwrap
from utils.print_utils import PrintUtils

class GameOpeningView:
    def display_intro_text(self,text):
        terminal_width = os.get_terminal_size().columns

        PrintUtils.print_slowly("\n".join(textwrap.wrap(text, width=terminal_width)),0.06)

    def display_ascii_art(self,art):
        print(art)