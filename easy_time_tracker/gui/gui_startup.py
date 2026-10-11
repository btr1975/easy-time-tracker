"""
GUI Startup
"""

import tkinter as tk
from easy_time_tracker.gui.main import MainFrame


def ett_gui() -> None:
    """Function to start the GUI

    :returns: Nothing
    """
    root = tk.Tk()
    root.title("Easy Time Tracker")
    # root.geometry("600x400")
    app = MainFrame(master=root)
    app.mainloop()
