"""
A simple GUI
"""
import tkinter as tk  # pylint: disable=import-error
from tkinter import messagebox  # pylint: disable=import-error
from .easy_time_tracker import EasyTimeTracker


class Gui(tk.Frame):  # pylint: disable=too-many-instance-attributes
    """Class to run the Easy Time Tracker GUI

    :type master: tk.Tk
    :param master: The tkinter object

    :rtype: None
    :returns: None
    """
    start_group = []
    stop_group = []

    def __init__(self, master: tk.Tk = None) -> None:
        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self.start_button = None
        self.stop_button = None
        self.description_text_box_label = None
        self.description_text_box = None
        self.comments_text_box_label = None
        self.comments_text_box = None
        self.people_text_box_label = None
        self.people_text_box = None
        self.create_description_text_box()
        self.create_people_text_box()
        self.create_comments_text_box()
        self.create_stop_button()
        self.create_start_button()

        self.ett_obj = EasyTimeTracker()

    def create_start_button(self) -> None:
        """Method to create the start button and hide the stop group

        :rtype: None
        :returns: None
        """
        self.start_button = tk.Button(self, height=2, width=80, bg='green')
        self.start_button['text'] = 'START'
        self.start_button['command'] = self.start_button_callback
        self.start_button.pack(side='top')
        self.start_group.append(self.start_button)
        self.hide(self.stop_group)

    def create_stop_button(self) -> None:
        """Method to create the stop button

        :rtype: None
        :returns: None
        """
        self.stop_button = tk.Button(self, height=2, width=80, bg='red')
        self.stop_button['text'] = 'STOP'
        self.stop_button['command'] = self.stop_button_callback
        self.stop_button.pack(side='top')
        self.stop_group.append(self.stop_button)

    def create_description_text_box(self) -> None:
        """Method to create the description text box and label for it

        :rtype: None
        :returns: None
        """
        self.description_text_box_label = tk.Label(self, font=20)
        self.description_text_box_label['text'] = 'Description'
        self.description_text_box_label.pack(side='bottom')
        self.description_text_box = tk.Entry(self, width=120, font=20)
        self.description_text_box.pack(side='bottom')
        self.start_group.append(self.description_text_box_label)
        self.start_group.append(self.description_text_box)

    def create_people_text_box(self) -> None:
        """Method to create the people text box and label for it

        :rtype: None
        :returns: None
        """
        self.people_text_box_label = tk.Label(self, font=20)
        self.people_text_box_label['text'] = 'People'
        self.people_text_box_label.pack(side='bottom')
        self.people_text_box = tk.Entry(self, width=120, font=20)
        self.people_text_box.pack(side='bottom')
        self.start_group.append(self.people_text_box_label)
        self.start_group.append(self.people_text_box)

    def create_comments_text_box(self) -> None:
        """Method to create the comments text box and label for it

        :rtype: None
        :returns: None
        """
        self.comments_text_box_label = tk.Label(self, font=20)
        self.comments_text_box_label['text'] = 'Comments'
        self.comments_text_box_label.pack(side='bottom')
        self.comments_text_box = tk.Entry(self, width=120, font=20)
        self.comments_text_box.pack(side='bottom')
        self.stop_group.append(self.comments_text_box_label)
        self.stop_group.append(self.comments_text_box)

    def start_button_callback(self) -> None:
        """Method for the callback of a start button click

        :rtype: None
        :returns: None
        """
        if len(self.people_text_box.get()) == 0:
            people = []

        else:
            people = self.people_text_box.get().split(',')

        if len(self.description_text_box.get()) > 0:
            self.ett_obj.start_time_record(self.description_text_box.get(), people)

            self.unhide(self.stop_group)
            self.hide(self.start_group)

        else:
            messagebox.showerror(title='MISSING REQUIRED DATA!!', message='A Description is required!')

    def stop_button_callback(self) -> None:
        """Method for the callback of a stop button click

        :rtype: None
        :returns: None
        """
        self.ett_obj.end_time_record(self.comments_text_box.get())
        self.unhide(self.start_group)
        self.hide(self.stop_group)

    @staticmethod
    def hide(group: list) -> None:
        """Static Method to hide a list of widgets

        :rtype: None
        :returns: None
        """
        for item in group:
            item.pack_forget()

    @staticmethod
    def unhide(group: list) -> None:
        """Static Method to unhide a list of widgets

        :rtype: None
        :returns: None
        """
        for item in group:
            item.pack()


def ett_gui() -> None:
    """Function to start the GUI

    :rtype: None
    :returns: None
    """
    root = tk.Tk()
    app = Gui(master=root)
    app.mainloop()
