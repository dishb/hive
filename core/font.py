#
#    A whole new file explorer for macOS. Finder, but better.
#    Copyright (C) 2023  Dishant B. (@dishb) <code.dishb@gmail.com> and
#    contributors.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import customtkinter as ctk

from .popup import Popup
from .helper import get_all_fonts
from .config import SCRIPT_DIR, FONT_PATH

class FontLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        Widget that explains what the menu below it is for/does.
        """

        # widget setup
        super().__init__(master = master,
                         text = "Font:",
                         font = font
                         )

class FontMenu(ctk.CTkOptionMenu):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        Widget that allows the user to select a theme from several options.
        """

        # font setup
        self.font = font

        # widget setup
        self.master = master
        self.options = get_all_fonts(f"{SCRIPT_DIR}/source/fonts/")
        super().__init__(self.master,
                         values = self.options,
                         command = self.change_font,
                         font = self.font
                         )

    def change_font(self, new_font: str) -> None:
        """
        Changes the theme of the app.
        """

        Popup(f"{SCRIPT_DIR}/source/misc/popup.png",
              "Popup: Please restart\nfor changes to the\nfont to take effect.",
              self.font
              )

        self.master.font = (new_font, 13)

        if " " in new_font:
            new_font = new_font.replace(" ", "_")

        ctk.FontManager.load_font(f"{FONT_PATH}/{new_font.lower()}")

        self.master.save_recent()
