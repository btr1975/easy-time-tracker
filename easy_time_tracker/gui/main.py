"""
Main Frame
"""

import tkinter as tk
from easy_time_tracker.gui.main_buttons import MainButtons


class MainFrame(tk.Frame):
    """The Main application frame

    :param master: The tkinter object
    """

    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = ("Courier", 14)

        MainButtons(master=self, font=self._font)
