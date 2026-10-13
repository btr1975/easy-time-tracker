"""
The Notes Frame
"""

from typing import Callable
import tkinter as tk

from easy_time_tracker.easy_time_tracker import EasyTimeTracker


class NotesFrame(tk.Frame):
    """The Notes Frame

    :param master: The master widget
    :param font: The font
    :param project: The project
    :param description: The description
    :param on_back: Callback to the parent
    """

    def __init__(
        self, master: tk.Misc, font: tuple[str, int], project: str, description: str, on_back: Callable
    ) -> None:
        self._client = EasyTimeTracker()

        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = font
        self.on_back = on_back

        self.project = project
        self.description = description

        self.note_text_box_label_object = tk.Label(self, font=self._font)
        self.note_text_box_object = tk.Entry(self, width=120)

        self.add_button_object = tk.Button(self, height=1, width=10, font=self._font)

        self.note_text_box()
        self.note_button()

    def note_text_box(self) -> None:
        """The note text box

        :returns: Nothing
        """
        label = tk.Label(self, font=self._font)
        label["text"] = f"Project: {self.project}"
        label.grid(row=0, column=0, padx=1, pady=1)

        self.note_text_box_label_object["text"] = "Note"
        self.note_text_box_label_object.grid(row=1, column=0, padx=1, pady=1)

        self.note_text_box_object.insert(tk.END, "")
        self.note_text_box_object.grid(row=2, column=0, padx=1, pady=1)

    def note_button_command_callback(self) -> None:
        """The note button command callback

        :returns: Nothing
        """
        self._client.add_note_to_project(
            name=self.project, description=self.description, note=self.note_text_box_object.get()
        )
        self.on_back()
        self.destroy()

    def note_button(self) -> None:
        """The note button

        :returns: Nothing
        """
        self.add_button_object["text"] = "Add"
        self.add_button_object["command"] = self.note_button_command_callback
        self.add_button_object.grid(row=3, column=0, padx=1, pady=1)
