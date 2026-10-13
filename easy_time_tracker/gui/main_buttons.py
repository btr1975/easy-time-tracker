"""
Main buttons frame
"""

import tkinter as tk
from easy_time_tracker.gui.projects_frame import ProjectsFrame
from easy_time_tracker.gui.people_frame import PeopleFrame


class MainButtons(tk.Frame):
    """Main Buttons Frame

    :param master: The tkinter object
    """

    def __init__(self, master: tk.Misc, font: tuple[str, int]) -> None:
        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = font

        self.projects_button_object = tk.Button(self, height=1, width=10, font=self._font)
        self.people_button_object = tk.Button(self, height=1, width=10, font=self._font)

        self.projects_button()
        self.people_button()

        self.projects_frame: None | ProjectsFrame = None
        self.people_frame: None | PeopleFrame = None

    def projects_button_command_callback(self):
        """Callback for the projects button

        :returns: Nothing
        """
        self.clear_people_frame_callback()
        if self.projects_frame is None:
            self.projects_frame = ProjectsFrame(master=self, font=self._font)

    def other_button_command_callback(self):
        """Callback for the projects button

        :returns: Nothing
        """
        self.clear_projects_frame_callback()
        if self.people_frame is None:
            self.people_frame = PeopleFrame(master=self, font=self._font)

    def clear_projects_frame_callback(self) -> None:
        """Callback to destroy the projects frame

        :returns: Nothing
        """
        if self.projects_frame is not None:
            self.projects_frame.destroy()
            self.projects_frame = None

    def clear_people_frame_callback(self) -> None:
        """Callback to destroy the people frame

        :returns: Nothing
        """
        if self.people_frame is not None:
            self.people_frame.destroy()
            self.people_frame = None

    def projects_button(self) -> None:
        """The projects button

        :returns: Nothing
        """
        self.projects_button_object["text"] = "Projects"
        self.projects_button_object["command"] = self.projects_button_command_callback
        self.projects_button_object.pack(side="top")

    def people_button(self) -> None:
        """The people button

        :returns: Nothing
        """
        self.people_button_object["text"] = "People"
        self.people_button_object["command"] = self.other_button_command_callback
        self.people_button_object.pack(side="top")
