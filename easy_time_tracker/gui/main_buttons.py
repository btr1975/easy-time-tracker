"""
Main buttons frame
"""

import tkinter as tk
from easy_time_tracker.gui.projects_frame import ProjectsFrame


class MainButtons(tk.Frame):
    """Main Buttons Frame

    :param master: The tkinter object
    """

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = ("Courier", 14)

        self.projects_button()
        self.other_button()

        self.projects_frame: None | ProjectsFrame = None

    def projects_button_command_callback(self):
        """Callback for the projects button

        :returns: Nothing
        """
        if self.projects_frame is None:
            self.projects_frame = ProjectsFrame(master=self)

    def clear_projects_frame_callback(self) -> None:
        """Callback to destroy the projects frame

        :returns: Nothing
        """
        if self.projects_frame is not None:
            self.projects_frame.destroy()
            self.projects_frame = None

    def projects_button(self) -> None:
        """The projects button

        :returns: Nothing
        """
        button = tk.Button(self, height=1, width=10, font=self._font, name="projects_button")
        button["text"] = "Projects"
        button["command"] = self.projects_button_command_callback
        button.pack(side="top")

    def other_button(self) -> None:
        """The other button

        :returns: Nothing
        """
        button = tk.Button(self, height=1, width=10, bg="green", font=self._font, name="other_button")
        button["text"] = "OTHER"
        button["command"] = self.clear_projects_frame_callback
        button.pack(side="top")
