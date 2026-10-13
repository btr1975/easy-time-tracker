"""
Main buttons frame
"""

import tkinter as tk
from easy_time_tracker.gui.projects_frame import ProjectsFrame
from easy_time_tracker.gui.people_frame import PeopleFrame
from easy_time_tracker.gui.weekly_updates_frame import WeeklyUpdatesFrame


class MainButtons(tk.Frame):
    """Main Buttons Frame

    :param master: The tkinter object
    :param font: The font
    """

    def __init__(self, master: tk.Misc, font: tuple[str, int]) -> None:
        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = font

        self.button_heights = 1
        self.button_widths = 20

        self.projects_button_object = tk.Button(
            self, height=self.button_heights, width=self.button_widths, font=self._font
        )
        self.people_button_object = tk.Button(
            self, height=self.button_heights, width=self.button_widths, font=self._font
        )
        self.weekly_updates_button_object = tk.Button(
            self, height=self.button_heights, width=self.button_widths, font=self._font
        )

        self.projects_button()
        self.people_button()
        self.weekly_updates_button()

        self.projects_frame: None | ProjectsFrame = None
        self.people_frame: None | PeopleFrame = None
        self.weekly_updates_frame: None | WeeklyUpdatesFrame = None

    def projects_button_command_callback(self):
        """Callback for the projects button

        :returns: Nothing
        """
        self.clear_weekly_updates_frame_callback()
        self.clear_people_frame_callback()
        if self.projects_frame is None:
            self.projects_frame = ProjectsFrame(master=self, font=self._font)

    def people_button_command_callback(self):
        """Callback for the people button

        :returns: Nothing
        """
        self.clear_weekly_updates_frame_callback()
        self.clear_projects_frame_callback()
        if self.people_frame is None:
            self.people_frame = PeopleFrame(master=self, font=self._font)

    def weekly_updates_button_command_callback(self):
        """Callback for the weekly updates button

        :returns: Nothing
        """
        self.clear_people_frame_callback()
        self.clear_projects_frame_callback()
        if self.weekly_updates_frame is None:
            self.weekly_updates_frame = WeeklyUpdatesFrame(master=self, font=self._font)

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

    def clear_weekly_updates_frame_callback(self) -> None:
        """Callback to destroy the weekly updates frame

        :returns: Nothing
        """
        if self.weekly_updates_frame is not None:
            self.weekly_updates_frame.destroy()
            self.weekly_updates_frame = None

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
        self.people_button_object["command"] = self.people_button_command_callback
        self.people_button_object.pack(side="top")

    def weekly_updates_button(self) -> None:
        """The weekly updates button

        :returns: Nothing
        """
        self.weekly_updates_button_object["text"] = "Weekly Updates"
        self.weekly_updates_button_object["command"] = self.weekly_updates_button_command_callback
        self.weekly_updates_button_object.pack(side="top")
