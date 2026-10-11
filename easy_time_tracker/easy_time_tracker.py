"""
easy_time_tracker
"""

from easy_time_tracker.nqlite_client import NeoSQLiteClient
from neosqlite import UpdateResult, DeleteResult, InsertOneResult
from easy_time_tracker.util.schemas import Person, Project


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
