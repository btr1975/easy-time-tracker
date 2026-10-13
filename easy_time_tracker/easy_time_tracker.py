"""
easy_time_tracker
"""

from easy_time_tracker.nqlite_client import NeoSQLiteClient
from neosqlite import UpdateResult, DeleteResult, InsertOneResult
from easy_time_tracker.util.schemas import Person, Project, Note, Ticket, WeeklyUpdate


class EasyTimeTracker:

    def __init__(self):
        self._client = NeoSQLiteClient()

    def create_person(
        self, first_name: str, last_name: str, middle_name: str | None = None, email: str | None = None
    ) -> InsertOneResult:
        """Create a new person

        :param first_name: First name
        :param last_name: Last name
        :param middle_name: Middle name
        :param email: Email

        :returns: Result
        """
        return self._client.create_person(
            document=Person(first_name=first_name, last_name=last_name, middle_name=middle_name, email=email)
        )

    def find_people(self, **kwargs) -> list[Person]:
        """Find people

        :param kwargs: Keyword arguments

        :returns: Result
        """
        return self._client.get_people(data_filter=kwargs)

    def update_person(self, first_name: str, last_name: str, **update) -> UpdateResult:
        """Update a person

        :param first_name: First name
        :param last_name: Last name
        :param update: Update

        :returns: Result
        """
        return self._client.update_person(
            data_filter={"first_name": first_name, "last_name": last_name}, update_data=update
        )

    def delete_person(self, first_name: str, last_name: str) -> DeleteResult:
        """Delete a person

        :param first_name: First name
        :param last_name: Last name

        :returns: Result
        """
        return self._client.delete_person(data_filter={"first_name": first_name, "last_name": last_name})

    def create_project(self, name: str, description: str) -> InsertOneResult:
        """Create a new project

        :param name: The project name
        :param description: The project description

        :returns: Result
        """
        return self._client.create_project(document=Project(name=name, description=description))

    def find_projects(self, **kwargs) -> list[Project]:
        """Find projects

        :param kwargs: Keyword arguments

        :returns: Result
        """
        return self._client.get_projects(data_filter=kwargs)

    def delete_project(self, name: str, description: str) -> DeleteResult:
        """Delete a person

        :param name: The project name
        :param description: The project description

        :returns: Result
        """
        return self._client.delete_project(data_filter={"name": name, "description": description})

    def add_person_to_project(self, name: str, description: str, person: Person) -> UpdateResult:
        """Add a person to a project

        :param name: The project name
        :param description: The project description
        :param person: Person

        :returns: Result
        """
        return self._client.update_project(
            data_filter={"name": name, "description": description}, update_data={"people": person.model_dump()}
        )

    def add_note_to_project(self, name: str, description: str, note: str) -> UpdateResult:
        """Add a note to a project

        :param name: The project name
        :param description: The project description
        :param note: Note

        :returns: Result
        """
        this_note = Note(note=note)
        return self._client.update_project(
            data_filter={"name": name, "description": description}, update_data={"notes": this_note.model_dump()}
        )

    def add_ticket_to_project(self, name: str, description: str, ticket_id: str) -> UpdateResult:
        """Add a ticket to a project

        :param name: The project name
        :param description: The project description
        :param ticket_id: Ticket

        :returns: Result
        """
        this_ticket = Ticket(ticket_id=ticket_id)
        return self._client.update_project(
            data_filter={"name": name, "description": description}, update_data={"tickets": this_ticket.model_dump()}
        )

    def create_weekly_update(self, worked_on: str, benefit_to_company: str) -> InsertOneResult:
        """Create a weekly update entry

        :param worked_on: The document to create
        :param benefit_to_company: The benefit to company

        :returns: Result
        """
        return self._client.create_weekly_update_entry(worked_on=worked_on, benefit_to_company=benefit_to_company)

    def find_weekly_update(self, **kwargs) -> list[WeeklyUpdate]:
        """Find weekly updates

        :param kwargs: Keyword arguments

        :returns: Result
        """
        return self._client.get_weekly_update_entries(data_filter=kwargs)
