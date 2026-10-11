"""
The People Frame
"""

import tkinter as tk
from easy_time_tracker.easy_time_tracker import EasyTimeTracker


class PeopleFrame(tk.Frame):
    """The People Frame

    :param master: The master widget
    """

    def __init__(self, master: tk.Misc) -> None:
        self._client = EasyTimeTracker()

        super().__init__(master)
        self.master = master
        self.pack(padx=25, pady=25)
        self._font = ("Courier", 14)

        self.people_dropdown_clicked = None
        self.person_first_name_text = ""
        self.person_middle_name_text = ""
        self.person_last_name_text = ""
        self.person_email_address_text = ""

        people = self.get_peoples_names_list()
        if len(people) >= 1:
            self.people_dropdown(people=people)

        self.person_first_name_text_box()
        self.person_middle_name_text_box()
        self.person_last_name_text_box()
        self.person_email_address_text_box()

    def get_peoples_names_list(self) -> list[str]:
        """Get the people names

        :returns: The people names
        """
        people = []
        for project in self._client.find_people():
            people.append(project.first_name)

        return people

    def people_dropdown_callback(self, name: str) -> None:
        """Callback for the people dropdown

        :param name: The name of the people

        :returns: Nothing
        """
        person = self._client.find_people(first_name=name, last_name=name)[0]

        self.person_first_name_text = person.first_name
        self.person_first_name_text_box()
        self.person_middle_name_text = person.middle_name
        self.person_middle_name_text_box()
        self.person_last_name_text = person.last_name
        self.person_last_name_text_box()
        self.person_email_address_text = person.email
        self.person_email_address_text_box()

    def people_dropdown(self, people: list) -> None:
        """The people dropdown selector

        :param people: The people's names

        :returns: Nothing
        """
        label = tk.Label(self, font=self._font)
        label["text"] = "Person"
        label.grid(row=0, column=0, padx=1, pady=1)

        # datatype of menu text
        self.people_dropdown_clicked = tk.StringVar()
        # initial menu text
        self.people_dropdown_clicked.set("NA")

        dropdown = tk.OptionMenu(self, self.people_dropdown_clicked, *people, command=self.people_dropdown_callback)
        dropdown.grid(row=0, column=1, padx=1, pady=1)

    def person_first_name_text_box(self) -> None:
        """The person first name text box

        :returns: Nothing
        """
        label = tk.Label(self, font=self._font)
        label["text"] = "First Name"
        label.grid(row=1, column=0, padx=1, pady=1)
        text_box = tk.Entry(self, width=120)
        text_box.insert(tk.END, self.person_first_name_text)
        text_box.grid(row=1, column=1, padx=1, pady=1)

    def person_middle_name_text_box(self) -> None:
        """The person middle name text box

        :returns: Nothing
        """
        label = tk.Label(self, font=self._font)
        label["text"] = "Middle Name"
        label.grid(row=2, column=0, padx=1, pady=1)
        text_box = tk.Entry(self, width=120)
        text_box.insert(tk.END, self.person_middle_name_text)
        text_box.grid(row=2, column=1, padx=1, pady=1)

    def person_last_name_text_box(self) -> None:
        """The person last name text box

        :returns: Nothing
        """
        label = tk.Label(self, font=self._font)
        label["text"] = "Last Name"
        label.grid(row=3, column=0, padx=1, pady=1)
        text_box = tk.Entry(self, width=120)
        text_box.insert(tk.END, self.person_last_name_text)
        text_box.grid(row=3, column=1, padx=1, pady=1)

    def person_email_address_text_box(self) -> None:
        """The person email address text box

        :returns: Nothing
        """
        label = tk.Label(self, font=self._font)
        label["text"] = "E-Mail Address"
        label.grid(row=4, column=0, padx=1, pady=1)
        text_box = tk.Entry(self, width=120)
        text_box.insert(tk.END, self.person_email_address_text)
        text_box.grid(row=4, column=1, padx=1, pady=1)
