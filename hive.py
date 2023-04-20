#
#    A whole new file explorer for macOS. Finder, but better.
#    Copyright (C) 2023  Dishant B. (@dishb)
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

from core import *

class App(ctk.CTk):
    def __init__(self):
        """
        Main app class that contains all the widgets and logic. To run, simply create an instance of 
        the class and call the ".mainloop()" method on the instance.
        """

        # window setup
        super().__init__()
        self.title("hive")
        self.iconbitmap("./src/icon.ico")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False)
        ctk.set_appearance_mode("system")

        # layout
        self.columnconfigure((0, 1), weight = 0)
        self.rowconfigure((0, 1), weight = 0)

        # appearance widgets
        self.appearance_selector = AppearanceSelector(self)
        self.appearance_selector.grid(row = 1, column = 0, padx = PADX, pady = PADY)

        self.appearance_label = AppearanceLabel(self)
        self.appearance_label.grid(row = 0, column = 0, padx = PADX, pady = PADY)

        # system files widgets
        self.system_files_switch = SystemFilesSwitch(self)
        self.system_files_switch.grid(row = 3, column = 0, padx = PADX, pady = PADY)

        self.system_files_label = SystemFilesLabel(self)
        self.system_files_label.grid(row = 2, column = 0, padx = PADX, pady = PADY)

# create and run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
