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

class PathLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk, cwd: str, font: tuple) -> None:
        """
        Widget to display the path to the current working directory.
        """

        # widget setup
        super().__init__(master = master,
                         text = cwd,
                         font = font
                         )

    def update_label(self, cwd: str) -> None:
        """
        Updates the label's text to the current working directory.
        """

        self.configure(text = cwd)
