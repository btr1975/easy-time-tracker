"""
Data schemas
"""

import datetime
from pydantic import BaseModel, Field, ConfigDict  # pylint: disable=no-name-in-module
from easy_time_tracker.constants import STRING_NO_SPACES, STRING_NO_SPACES_BEGIN_OR_END


def get_current_datetime() -> datetime.datetime:
    """Get current datetime

    :returns: current datetime
    """
    return datetime.datetime.now(datetime.timezone.utc)


class CommonRecord(BaseModel):
    """Common Record Schema meant to be inherited"""

    model_config = ConfigDict(use_enum_values=True)

    created: datetime.datetime = Field(description="Created", default_factory=get_current_datetime)
    modified: datetime.datetime | None = Field(description="Modified", default=None)


class Person(CommonRecord):
    """Person Document Schema"""

    first_name: str = Field(description="First name", pattern=STRING_NO_SPACES)
    middle_name: str | None = Field(description="Middle name", pattern=STRING_NO_SPACES, default=None)
    last_name: str = Field(description="Last name", pattern=STRING_NO_SPACES)
    email: str | None = Field(description="Email", pattern=STRING_NO_SPACES, default=None)


class Note(CommonRecord):
    """Note Document Schema"""

    note: str = Field(description="Note", pattern=STRING_NO_SPACES_BEGIN_OR_END)


class Ticket(CommonRecord):
    """Ticket Document Schema"""

    ticket_id: str = Field(description="Ticket ID", pattern=STRING_NO_SPACES)
    complete: bool = Field(description="Completed", default=False)


class Project(CommonRecord):
    """Project Document Schema"""

    name: str = Field(description="Project name", pattern=STRING_NO_SPACES_BEGIN_OR_END)
    description: str = Field(description="Project description", pattern=STRING_NO_SPACES_BEGIN_OR_END)
    complete: bool = Field(description="Completed", default=False)
    people: list[Person] = Field(description="People", default=[])
    tickets: list[Ticket] = Field(description="Tickets", default=[])
    notes: list[Note] = Field(description="Notes", default=[])


class WeeklyUpdates(CommonRecord):
    """Weekly Updates Schema"""

    worked_on: str = Field(description="Worked on", pattern=STRING_NO_SPACES_BEGIN_OR_END)
    benefit_to_company: str = Field(description="Benefit to company", pattern=STRING_NO_SPACES_BEGIN_OR_END)
