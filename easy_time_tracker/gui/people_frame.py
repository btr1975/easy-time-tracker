"""
The People Frame
"""

import tkinter as tk
from tkinter import messagebox
from easy_time_tracker.easy_time_tracker import EasyTimeTracker


class PeopleFrame(tk.Frame):
    """The People Frame

    :param master: The master widget
    :param font: The font
    """

    def __init__(self, master: tk.Misc, font: tuple[str, int]) -> None:
        self._client = EasyTimeTracker()

        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = font

        self.people_dropdown_object: tk.OptionMenu | None = None

        # The data type of the dropdown
        self.people_dropdown_clicked = tk.StringVar()

        self.person_first_name_text_box_label_object = tk.Label(self, font=self._font)
        self.person_first_name_text_box_object = tk.Entry(self, width=120)

        self.person_middle_name_text_box_label_object = tk.Label(self, font=self._font)
        self.person_middle_name_text_box_object = tk.Entry(self, width=120)

        self.person_last_name_text_box_label_object = tk.Label(self, font=self._font)
        self.person_last_name_text_box_object = tk.Entry(self, width=120)

        self.person_email_address_text_box_label_object = tk.Label(self, font=self._font)
        self.person_email_address_text_box_object = tk.Entry(self, width=120)

        self.clear_person_button_object = tk.Button(self, height=1, width=10, font=self._font)

        self.create_person_button_object = tk.Button(self, height=1, width=10, font=self._font)

        self.update_person_button_object = tk.Button(self, height=1, width=10, font=self._font)

        self.delete_person_button_object = tk.Button(self, height=1, width=10, font=self._font)

        self.load_people_dropdown()
        self.person_first_name_text_box()
        self.person_middle_name_text_box()
        self.person_last_name_text_box()
        self.person_email_address_text_box()
        self.clear_person_button()
        self.create_person_button()
        self.update_person_button()
        self.delete_person_button()

    def load_people_dropdown(self) -> None:
        """Load the people dropdown

        :returns: Nothing
        """
        people = self.get_peoples_names_list()

        if len(people) >= 1:
            self.people_dropdown(people=people)

        else:
            self.people_dropdown(people=[])

    def get_peoples_names_list(self) -> list[str]:
        """Get the people names

        :returns: The people names
        """
        people = []
        for project in self._client.find_people():
            people.append(f"{project.first_name} {project.last_name}")

        return people

    def people_dropdown_callback(self, name: str) -> None:
        """Callback for the people dropdown

        :param name: The name of the people

        :returns: Nothing
        """
        name_split = name.split(" ")
        person = self._client.find_people(first_name=name_split[0], last_name=name_split[1])[0]

        self.person_first_name_text_box_object.insert(tk.END, person.first_name or "")
        self.person_middle_name_text_box_object.insert(tk.END, person.middle_name or "")
        self.person_last_name_text_box_object.insert(tk.END, person.last_name or "")
        self.person_email_address_text_box_object.insert(tk.END, person.email or "")

    def people_dropdown(self, people: list) -> None:
        """The people dropdown selector

        :param people: The people's names

        :returns: Nothing
        """
        label = tk.Label(self, font=self._font)
        label["text"] = "Person"
        label.grid(row=0, column=0, padx=1, pady=1)

        # initial menu text
        self.people_dropdown_clicked.set("NA")

        if self.people_dropdown_object:
            self.people_dropdown_object.destroy()

        if not people:
            self.people_dropdown_object = tk.OptionMenu(self, self.people_dropdown_clicked, value="")

        else:
            self.people_dropdown_object = tk.OptionMenu(
                self, self.people_dropdown_clicked, *people, command=self.people_dropdown_callback
            )

        self.people_dropdown_object.grid(row=0, column=1, padx=1, pady=1)

    def person_first_name_text_box(self) -> None:
        """The person first name text box

        :returns: Nothing
        """
        self.person_first_name_text_box_label_object["text"] = "First Name"
        self.person_first_name_text_box_label_object.grid(row=1, column=0, padx=1, pady=1)

        self.person_first_name_text_box_object.insert(tk.END, "")
        self.person_first_name_text_box_object.grid(row=1, column=1, padx=1, pady=1)

    def person_middle_name_text_box(self) -> None:
        """The person middle name text box

        :returns: Nothing
        """
        self.person_middle_name_text_box_label_object["text"] = "Middle Name"
        self.person_middle_name_text_box_label_object.grid(row=2, column=0, padx=1, pady=1)

        self.person_middle_name_text_box_object.insert(tk.END, "")
        self.person_middle_name_text_box_object.grid(row=2, column=1, padx=1, pady=1)

    def person_last_name_text_box(self) -> None:
        """The person last name text box

        :returns: Nothing
        """
        self.person_last_name_text_box_label_object["text"] = "Last Name"
        self.person_last_name_text_box_label_object.grid(row=3, column=0, padx=1, pady=1)

        self.person_last_name_text_box_object.insert(tk.END, "")
        self.person_last_name_text_box_object.grid(row=3, column=1, padx=1, pady=1)

    def person_email_address_text_box(self) -> None:
        """The person email address text box

        :returns: Nothing
        """
        self.person_email_address_text_box_label_object["text"] = "E-Mail Address"
        self.person_email_address_text_box_label_object.grid(row=4, column=0, padx=1, pady=1)

        self.person_email_address_text_box_object.insert(tk.END, "")
        self.person_email_address_text_box_object.grid(row=4, column=1, padx=1, pady=1)

    def get_data_from_text_boxes(self) -> tuple[str, str | None, str, str | None]:
        """Get the data from the text boxes

        :returns: first_name, middle_name, last_name, email_address
        """
        first_name = self.person_first_name_text_box_object.get()
        middle_name = self.person_middle_name_text_box_object.get()
        last_name = self.person_last_name_text_box_object.get()
        email_address = self.person_email_address_text_box_object.get()

        if not middle_name:
            middle_name = None

        if not email_address:
            email_address = None

        return first_name, middle_name, last_name, email_address

    def create_person_command_callback(self):
        """Callback for creating a person

        :returns: Nothing
        """
        first_name, middle_name, last_name, email_address = self.get_data_from_text_boxes()

        try:
            self._client.create_person(
                first_name=first_name, middle_name=middle_name, last_name=last_name, email=email_address
            )

        except Exception as error:
            messagebox.showerror(title="Error", message=f"{error}")

        self.clear_person_command_callback()
        self.load_people_dropdown()

    def update_person_command_callback(self):
        """Callback for updating a person

        :returns: Nothing
        """
        first_name, middle_name, last_name, email_address = self.get_data_from_text_boxes()

        kwargs = {"middle_name": middle_name, "email": email_address}

        try:
            self._client.update_person(first_name=first_name, last_name=last_name, **kwargs)

        except Exception as error:
            messagebox.showerror(title="Error", message=f"{error}")

        self.clear_person_command_callback()
        self.load_people_dropdown()

    def delete_person_command_callback(self):
        """Callback for deleting a person

        :returns: Nothing
        """
        first_name, middle_name, last_name, email_address = self.get_data_from_text_boxes()

        try:
            self._client.delete_person(first_name=first_name, last_name=last_name)

        except Exception as error:
            messagebox.showerror(title="Error", message=f"{error}")

        self.clear_person_command_callback()
        self.load_people_dropdown()

    def clear_person_command_callback(self):
        """Callback for the clear person button

        :returns: Nothing
        """
        self.person_first_name_text_box_object.delete(0, tk.END)
        self.person_middle_name_text_box_object.delete(0, tk.END)
        self.person_last_name_text_box_object.delete(0, tk.END)
        self.person_email_address_text_box_object.delete(0, tk.END)

    def clear_person_button(self) -> None:
        """The button

        :returns: Nothing
        """
        self.clear_person_button_object["text"] = "Clear"
        self.clear_person_button_object["command"] = self.clear_person_command_callback
        self.clear_person_button_object.grid(row=5, column=0, padx=1, pady=1)

    def create_person_button(self) -> None:
        """The button

        :returns: Nothing
        """
        self.create_person_button_object["text"] = "Create"
        self.create_person_button_object["command"] = self.create_person_command_callback
        self.create_person_button_object.grid(row=5, column=1, padx=1, pady=1)

    def update_person_button(self) -> None:
        """The button

        :returns: Nothing
        """
        self.update_person_button_object["text"] = "Update"
        self.update_person_button_object["command"] = self.update_person_command_callback
        self.update_person_button_object.grid(row=5, column=2, padx=1, pady=1)

    def delete_person_button(self) -> None:
        """The button

        :returns: Nothing
        """
        self.delete_person_button_object["text"] = "Delete"
        self.delete_person_button_object["command"] = self.delete_person_command_callback
        self.delete_person_button_object.grid(row=5, column=3, padx=1, pady=1)
