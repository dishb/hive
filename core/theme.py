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

from .config import *

class ThemeLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk) -> None:
        """
        Widget that explains what the menu below it is for/does.
        """

        # widget setup
        super().__init__(master,
                         text = "Theme:"
                         )

class ThemeMenu(ctk.CTkOptionMenu):
    def __init__(self, master: ctk.CTk) -> None:
        """
        Widget that allows the user to select a theme from several options.
        """

        super().__init__(master,
                         values = ["Blue", "Green", "Dark Blue"],
                         command = self.change_theme
                         )

    def change_theme(self, new_theme: str) -> None:
        """
        Changes the theme of the app.
        """

        if new_theme.lower() != "dark blue":
            ctk.set_default_color_theme(f"{THEME_PATH}/{new_theme.lower()}.json")
        else:
            ctk.set_default_color_theme(f"{THEME_PATH}/dark_blue.json")