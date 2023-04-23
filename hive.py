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
        ctk.set_default_color_theme("green")
        ctk.set_appearance_mode("system")

        # layout
        self.grid_rowconfigure(0, weight = 0)
        self.grid_rowconfigure(1, weight = 0)
        self.grid_rowconfigure(2, weight = 0)
        self.grid_rowconfigure(3, weight = 0)
        self.grid_rowconfigure(4, weight = 1)
        self.grid_columnconfigure(0, weight = 0)
        self.grid_columnconfigure(1, weight = 1)

        # data
        self.cwd_var = ctk.StringVar(master = self,
                                 value = "/"
                                 )
        self.sys_files_var = ctk.IntVar(master = self,
                                        value = 0
                                        )

        # appearance widgets
        self.appearance_label = AppearanceLabel(self)
        self.appearance_label.grid(row = 0,
                                   column = 0,
                                   padx = PADX,
                                   pady = PADY,
                                   sticky = "w"
                                   )

        self.appearance_selector = AppearanceSelector(self)
        self.appearance_selector.grid(row = 1,
                                      column = 0,
                                      padx = PADX,
                                      pady = PADY,
                                      sticky = "w"
                                      )

        # sys files widgets
        self.sys_files_label = SysFilesLabel(self)
        self.sys_files_label.grid(row = 2,
                                     column = 0,
                                     padx = PADX,
                                     pady = PADY,
                                     sticky = "w"
                                     )

        self.sys_files_switch = SysFilesSwitch(self, self.sys_files_var)
        self.sys_files_switch.grid(row = 3,
                                      column = 0,
                                      padx = PADX,
                                      pady = PADY,
                                      sticky = "w"
                                      )

        # checks if any variables were updated
        self.sys_files_var.trace_add("write", self.update_tree)
        self.cwd_var.trace_add("write", self.update_tree)

        # file explorer widgets
        self.file_explorer = FileExplorer(self)
        self.file_explorer.grid(row = 0,
                                rowspan = 5,
                                column = 1,
                                columnspan = 1,
                                padx = PADX,
                                pady = PADY,
                                sticky = "nsew"
                                )

    def update_tree(self, *args): # pylint: disable=unused-argument
        """
        Updates the file explorer tree from the app itself. Could be done with 
        app.file_explorer.fill_tree, but this is a lot cleaner and easier to read.
        """
        self.file_explorer.fill_tree(self.cwd_var.get(), self.sys_files_var.get())

# create and run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
