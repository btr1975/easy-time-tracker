"""
Project Frame
"""

from typing import Any
import tkinter as tk
from tkinter import ttk, messagebox
from pydantic import BaseModel
from easy_time_tracker.easy_time_tracker import EasyTimeTracker
from easy_time_tracker.gui.notes_frame import NotesFrame


class ProjectsFrame(tk.Frame):
    """The Projects Frame

    :param master: The master widget
    :param font: The font
    """

    def __init__(self, master: tk.Misc, font: tuple[str, int]) -> None:
        self._client = EasyTimeTracker()

        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = font

        self.projects_dropdown_object: tk.OptionMenu | None = None

        # dropdown data type
        self.project_dropdown_clicked = tk.StringVar()

        self.project_description_text_box_label_object = tk.Label(self, font=self._font)
        self.project_description_text_box_object = tk.Entry(self, width=120)

        self.add_note_button_object = tk.Button(self, height=1, width=10, font=self._font)
        self.add_person_button_object = tk.Button(self, height=1, width=10, font=self._font)

        projects = self.get_projects_names_list()
        if len(projects) >= 1:
            self.projects_dropdown(projects=projects)

        self.project_description_text_box()
        self.add_note_button()
        self.add_person_button()

        self.notes_frame: None | NotesFrame = None

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

        self.project_description_text_box_object.delete(0, tk.END)
        self.project_description_text_box_object.insert(tk.END, project.description)

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

        # initial menu text
        self.project_dropdown_clicked.set("NA")

        self.projects_dropdown_object = tk.OptionMenu(
            self, self.project_dropdown_clicked, *projects, command=self.project_dropdown_callback
        )
        self.projects_dropdown_object.grid(row=0, column=1, padx=1, pady=1)

    def project_description_text_box(self) -> None:
        """The project description text box

        :returns: Nothing
        """
        self.project_description_text_box_label_object["text"] = "Description"
        self.project_description_text_box_label_object.grid(row=1, column=0, padx=1, pady=1)

        self.project_description_text_box_object.insert(tk.END, "")
        self.project_description_text_box_object.grid(row=1, column=1, padx=1, pady=1)

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

        if len(columns) == 0:
            table.grid_forget()

    def add_note_button_command_callback(self) -> None:
        """Add a note to the projects

        :returns: Nothing
        """
        if self.project_dropdown_clicked.get() == "NA":
            messagebox.showerror(title="Error", message="You must select a project")
            return

        if self.notes_frame is None:
            description = self.project_description_text_box_object.get()
            project = self.project_dropdown_clicked.get()
            self.destroy()
            self.notes_frame = NotesFrame(
                master=self.master,
                font=self._font,
                project=project,
                description=description,
                on_back=self.master.clear_projects_frame_callback,
            )

    def add_note_button(self) -> None:
        """The button

        :returns: Nothing
        """
        self.add_note_button_object["text"] = "Add Note"
        self.add_note_button_object["command"] = self.add_note_button_command_callback
        self.add_note_button_object.grid(row=5, column=0, padx=1, pady=1)

    def add_person_button(self) -> None:
        """The button

        :returns: Nothing
        """
        self.add_person_button_object["text"] = "Add Person"
        # self.add_person_button_object["command"] = self.delete_person_command_callback
        self.add_person_button_object.grid(row=5, column=1, padx=1, pady=1)
