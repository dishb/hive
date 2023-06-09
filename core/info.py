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

import os
from subprocess import check_output

import customtkinter as ctk

from .config import PADX, PADY

class InfoPopup(ctk.CTkToplevel):
    def __init__(self, font: tuple, cwd: str) -> None:
        """
        A popup window displaying information about a directory.
        """

        # window setup
        super().__init__()
        self.title("info")
        self.geometry("250x150")
        self.resizable(False, False)

        # attributes
        self.cwd = cwd
        self.font = font

        # grid setup
        self.grid_rowconfigure(0, weight = 0)
        self.grid_rowconfigure(1, weight = 0)

        self.grid_columnconfigure(0, weight = 0)

        # Git label widget
        self.git_repo = GitLabel(self, self.cwd, self.font)
        self.git_repo.grid(row = 0,
                           column = 0,
                           padx = PADX,
                           pady = PADY,
                           sticky = "w"
                           )

        # size label widget
        self.size = SizeLabel(self, self.cwd, self.font)
        self.size.grid(row = 1,
                       column = 0,
                       padx = PADX,
                       pady = PADY,
                       sticky = "w"
                       )

class GitLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTkToplevel, cwd: str, font: tuple) -> None:
        """
        A label to display whether the directory is a Git repository.
        """

        # widget setup
        super().__init__(master = master,
                         font = font,
                         text = "Git Repository: "
                         )

        if os.path.exists(f"{cwd}/.git"):
            self.configure(require_redraw = True,
                           text = self.cget("text") + "Yes"
                           )
        else:
            self.configure(require_redraw = True,
                           text = self.cget("text") + "No"
                           )

class SizeLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTkToplevel, cwd: str, font: tuple) -> None:
        """
        A label to display the size of a directory
        """

        # widget setup
        super().__init__(master = master,
                         font = font,
                         text = "Size: "
                         )

        self.get_size(cwd)

    def get_size(self, path: str) -> str:
        """
        Gets the size of a directory in bytes.
        """

        total_size = check_output(['du','-shx', path]).split()[0].decode('utf-8')
        total_size = str(total_size)

        # make it human readable
        if "K" in total_size:
            total_size = total_size.replace("K", "") + " kilo"
        elif "M" in total_size:
            total_size = total_size.replace("M", "") + " mega"
        elif "G" in total_size:
            total_size = total_size.replace("G", "") + " giga"

        self.configure(require_redraw = True,
                       text = self.cget("text") + total_size + "bytes"
                       )
