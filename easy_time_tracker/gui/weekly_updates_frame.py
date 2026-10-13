"""
The Weekly Updates Frame
"""

import tkinter as tk
from tkinter import messagebox

from easy_time_tracker.easy_time_tracker import EasyTimeTracker


class WeeklyUpdatesFrame(tk.Frame):
    """The Weekly Updates Frame

    :param master: The master widget
    :param font: The font
    """

    def __init__(self, master: tk.Misc, font: tuple[str, int]) -> None:
        self._client = EasyTimeTracker()

        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = font

        self.worked_on_text_box_label_object = tk.Label(self, font=self._font)
        self.worked_on_text_box_object = tk.Entry(self, width=120)

        self.benefit_to_company_text_box_label_object = tk.Label(self, font=self._font)
        self.benefit_to_company_text_box_object = tk.Entry(self, width=120)

        self.add_button_object = tk.Button(self, height=1, width=10, font=self._font)
        self.home_button_object = tk.Button(self, height=1, width=10, font=self._font)

        self.worked_on_text_box()
        self.benefit_to_company_text_box()
        self.add_button()
        self.home_button()

    def worked_on_text_box(self) -> None:
        """The worked on text box

        :returns: Nothing
        """
        self.worked_on_text_box_label_object["text"] = "Worked On"
        self.worked_on_text_box_label_object.grid(row=0, column=0, padx=1, pady=1)

        self.worked_on_text_box_object.insert(tk.END, "")
        self.worked_on_text_box_object.grid(row=0, column=1, padx=1, pady=1)

    def benefit_to_company_text_box(self) -> None:
        """The benefit to company on text box

        :returns: Nothing
        """
        self.benefit_to_company_text_box_label_object["text"] = "Benefit to Company"
        self.benefit_to_company_text_box_label_object.grid(row=1, column=0, padx=1, pady=1)

        self.benefit_to_company_text_box_object.insert(tk.END, "")
        self.benefit_to_company_text_box_object.grid(row=1, column=1, padx=1, pady=1)

    def add_button_command_callback(self) -> None:
        """The add button command callback

        :returns: Nothing
        """
        if self.worked_on_text_box_object.get() == "" or self.benefit_to_company_text_box_object.get() == "":
            messagebox.showinfo(title="Information", message="Please enter both items")
            return

        self._client.create_weekly_update(
            worked_on=self.worked_on_text_box_object.get(),
            benefit_to_company=self.benefit_to_company_text_box_object.get(),
        )
        self.worked_on_text_box_object.delete(0, tk.END)
        self.benefit_to_company_text_box_object.delete(0, tk.END)

    def home_button_command_callback(self) -> None:
        """The home button command callback

        :returns: Nothing
        """
        self.destroy()
        self.master.clear_weekly_updates_frame_callback()

    def add_button(self) -> None:
        """The add button

        :returns: Nothing
        """
        self.add_button_object["text"] = "Add"
        self.add_button_object["command"] = self.add_button_command_callback
        self.add_button_object.grid(row=2, column=0, padx=1, pady=1)

    def home_button(self) -> None:
        """The add button

        :returns: Nothing
        """
        self.home_button_object["text"] = "Home"
        self.home_button_object["command"] = self.home_button_command_callback
        self.home_button_object.grid(row=2, column=1, padx=1, pady=1)
