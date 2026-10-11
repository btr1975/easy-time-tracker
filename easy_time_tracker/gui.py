"""
A simple GUI
"""

from typing import Any
import tkinter as tk
from tkinter import messagebox, ttk
from pydantic import BaseModel
from easy_time_tracker.easy_time_tracker import EasyTimeTracker


class ProjectsFrame(tk.Frame):
    """The Projects Frame

    :param master: The master widget
    """

    def __init__(self, master: tk.Misc) -> None:
        self._client = EasyTimeTracker()

        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = ("Courier", 14)

        self.project_dropdown_clicked = None
        self.project_description_text = ""

        projects = self.get_projects_names_list()
        if len(projects) >= 1:
            self.projects_dropdown(projects=projects)

        self.project_description_text_box()

    def get_projects_names_list(self) -> list[str]:
        """Get the project names

        :returns: The project names
        """
        projects = []
        for project in self._client.find_projects():
            projects.append(project.name)

        return projects

    def project_dropdown_callback(self, name: str) -> None:
        """Callback for the project dropdown

        :param name: The name of the project

        :returns: Nothing
        """
        project = self._client.find_projects(name=name)[0]

        self.project_description_text = project.description
        self.project_description_text_box()

        self.create_table(placement_row=2, data=project.people)
        self.create_table(placement_row=3, data=project.tickets)
        self.create_table(placement_row=4, data=project.notes)

    def projects_dropdown(self, projects: list) -> None:
        """The projects dropdown selector

        :param projects: The project names

        :returns: Nothing
        """
        label = tk.Label(self, font=self._font)
        label["text"] = "Project"
        label.grid(row=0, column=0, padx=1, pady=1)

        # datatype of menu text
        self.project_dropdown_clicked = tk.StringVar()
        # initial menu text
        self.project_dropdown_clicked.set("NA")

        dropdown = tk.OptionMenu(self, self.project_dropdown_clicked, *projects, command=self.project_dropdown_callback)
        dropdown.grid(row=0, column=1, padx=1, pady=1)

    def project_description_text_box(self) -> None:
        """The project description text box

        :returns: Nothing
        """
        label = tk.Label(self, font=self._font)
        label["text"] = "Description"
        label.grid(row=1, column=0, padx=1, pady=1)
        text_box = tk.Entry(self, width=120)
        text_box.insert(tk.END, self.project_description_text)
        text_box.grid(row=1, column=1, padx=1, pady=1)

    def create_table(self, placement_row: int, data: list[BaseModel]) -> None:
        """Create a table

        :param placement_row: The placement row of the table
        :param data: The data for the table

        :returns: Nothing
        """
        headers = []
        columns = []
        for index, model in enumerate(data):
            if index == 0:
                headers.extend(list(model.model_dump().keys()))

            columns.append(list(model.model_dump().values()))

        self.table(placement_row=placement_row, headers=headers, columns=columns)

    def table(self, placement_row: int, headers: list[str], columns: list[list[Any]]) -> None:
        """Table GUI object

        :param placement_row: The placement row of the table
        :param headers: The headers of the table
        :param columns: The columns of the table

        :returns: Nothing
        """
        column_span = len(headers) + 1
        table = ttk.Treeview(self, columns=headers, show="headings")

        for col in headers:
            table.heading(col, text=col)
            table.column(col, anchor="center", width=200)

        for row in columns:
            table.insert("", tk.END, values=row)

        table.grid(row=placement_row, columnspan=column_span, padx=1, pady=4)


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


class MainFrame(tk.Frame):
    """The Main application frame

    :param master: The tkinter object
    """

    def __init__(self, master: tk.Tk) -> None:
        self._client = EasyTimeTracker()
        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = ("Courier", 14)

        MainButtons(master=self)


class Gui(tk.Frame):  # pylint: disable=too-many-instance-attributes
    """Class to run the Easy Time Tracker GUI

    :param master: The tkinter object

    :returns: Nothing
    """

    start_group = []
    stop_group = []

    def __init__(self, master: tk.Tk) -> None:
        self._client = EasyTimeTracker()

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
        self.project_dropdown_label = None
        self.project_dropdown = None
        self.project_dropdown_clicked = None
        self.create_description_text_box()
        self.create_people_text_box()

        projects = []
        for project in self._client.find_projects():
            projects.append(project.name)

        if len(projects) >= 1:
            self.create_project_dropdown(projects)
        self.create_comments_text_box()
        self.create_stop_button()
        self.create_start_button()

        self.ett_obj = EasyTimeTracker()

    def create_start_button(self) -> None:
        """Method to create the start button and hide the stop group

        :returns: Nothing
        """
        self.start_button = tk.Button(self, height=2, width=80, bg="green")
        self.start_button["text"] = "START"
        self.start_button["command"] = self.start_button_callback
        self.start_button.pack(side="top")
        self.start_group.append((self.start_button, "top"))
        self.hide(self.stop_group)

    def create_stop_button(self) -> None:
        """Method to create the stop button

        :returns: Nothing
        """
        self.stop_button = tk.Button(self, height=2, width=80, bg="red")
        self.stop_button["text"] = "STOP"
        self.stop_button["command"] = self.stop_button_callback
        self.stop_button.pack(side="top")
        self.stop_group.append((self.stop_button, "top"))

    def create_description_text_box(self) -> None:
        """Method to create the description text box and label for it

        :returns: Nothing
        """
        self.description_text_box_label = tk.Label(self, font=20)
        self.description_text_box_label["text"] = "Description"
        self.description_text_box_label.pack(side="bottom")
        self.description_text_box = tk.Entry(self, width=120, font=20)
        self.description_text_box.pack(side="bottom")
        self.start_group.append((self.description_text_box_label, "bottom"))
        self.start_group.append((self.description_text_box, "bottom"))

    def create_people_text_box(self) -> None:
        """Method to create the people text box and label for it

        :returns: Nothing
        """
        self.people_text_box_label = tk.Label(self, font=20)
        self.people_text_box_label["text"] = "People"
        self.people_text_box_label.pack(side="bottom")
        self.people_text_box = tk.Entry(self, width=120, font=20)
        self.people_text_box.pack(side="bottom")
        self.start_group.append((self.people_text_box_label, "bottom"))
        self.start_group.append((self.people_text_box, "bottom"))

    def create_project_dropdown(self, projects: list) -> None:
        """Method to create the project dropdown box

        :param projects: The list of projects

        :returns: Nothing
        """
        self.project_dropdown_label = tk.Label(self, font=20)
        self.project_dropdown_label["text"] = "Project"
        self.project_dropdown_label.pack(side="bottom")
        # datatype of menu text
        self.project_dropdown_clicked = tk.StringVar()
        # initial menu text
        self.project_dropdown_clicked.set("NA")
        self.project_dropdown = tk.OptionMenu(self, self.project_dropdown_clicked, *projects)
        self.project_dropdown.pack(side="bottom")
        self.start_group.append((self.project_dropdown_label, "bottom"))
        self.start_group.append((self.project_dropdown, "bottom"))

    def create_comments_text_box(self) -> None:
        """Method to create the comments text box and label for it

        :returns: Nothing
        """
        self.comments_text_box_label = tk.Label(self, font=20)
        self.comments_text_box_label["text"] = "Comments"
        self.comments_text_box_label.pack(side="bottom")
        self.comments_text_box = tk.Entry(self, width=120, font=20)
        self.comments_text_box.pack(side="bottom")
        self.stop_group.append((self.comments_text_box_label, "bottom"))
        self.stop_group.append((self.comments_text_box, "bottom"))

    def start_button_callback(self) -> None:
        """Method for the callback of a start button click

        :returns: Nothing
        """
        if len(self.people_text_box.get()) == 0:
            people = []

        else:
            people = self.people_text_box.get().split(",")

        if len(self.description_text_box.get()) > 0:
            try:
                if self.project_dropdown_clicked.get() != "NA":
                    self.ett_obj.start_time_record(
                        description=self.description_text_box.get(),
                        people=people,
                        project=self.project_dropdown_clicked.get(),
                    )

                else:
                    self.ett_obj.start_time_record(description=self.description_text_box.get(), people=people)

                self.clear_text_box(self.description_text_box)
                self.clear_text_box(self.people_text_box)

                self.unhide(self.stop_group)
                self.hide(self.start_group)

            except FileExistsError:
                response = messagebox.askquestion(
                    title="RECORD IN PROGRESS", message="Would you like to end the in progress record?"
                )

                if response == "yes":
                    self.stop_button_callback()

                else:
                    messagebox.showinfo(title="RECORD IN PROGRESS", message="Record in progress will keep going.")

        else:
            messagebox.showerror(title="MISSING REQUIRED DATA!!", message="A Description is required!")

    def stop_button_callback(self) -> None:
        """Method for the callback of a stop button click

        :returns: Nothing
        """
        self.ett_obj.end_time_record(self.comments_text_box.get())

        self.clear_text_box(self.comments_text_box)

        self.unhide(self.start_group)
        self.hide(self.stop_group)

    @staticmethod
    def clear_text_box(text_box: tk.Entry):
        """Static Method to clear a text box

        :param text_box: The text box to clear

        :returns: Nothing
        """
        text_box.delete(0, tk.END)

    @staticmethod
    def hide(group: list) -> None:
        """Static Method to hide a list of widgets

        :returns: Nothing
        """
        for item in group:
            item[0].pack_forget()

    @staticmethod
    def unhide(group: list) -> None:
        """Static Method to unhide a list of widgets

        :returns: Nothing
        """
        for item in group:
            item[0].pack(side=item[1])


def ett_gui() -> None:
    """Function to start the GUI

    :returns: Nothing
    """
    root = tk.Tk()
    root.title("Easy Time Tracker")
    # root.geometry("600x400")
    app = MainFrame(master=root)
    app.mainloop()
