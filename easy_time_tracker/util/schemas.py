"""
Data schemas
"""

import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict  # pylint: disable=no-name-in-module
from easy_time_tracker.constants import STRING_NO_SPACES, STRING_NO_SPACES_BEGIN_OR_END


def get_current_datetime() -> datetime.datetime:
    """Get current datetime

    :returns: current datetime
    """
    return datetime.datetime.now(datetime.timezone.utc)


class CommonRecord(BaseModel):

    model_config = ConfigDict(use_enum_values=True)

    created: datetime.datetime = Field(description="Created", default_factory=get_current_datetime)
    modified: datetime.datetime | None = Field(description="Modified", default=None)


class Person(CommonRecord):
    """Person Document Schema"""

    first_name: str = Field(description="First name", pattern=STRING_NO_SPACES)
    middle_name: str | None = Field(description="Middle name", pattern=STRING_NO_SPACES, default=None)
    last_name: str = Field(description="Last name", pattern=STRING_NO_SPACES)
    email: str | None = Field(description="Email", pattern=STRING_NO_SPACES, default=None)


class Project(CommonRecord):
    """Project Document Schema"""

    name: str = Field(description="Project name", pattern=STRING_NO_SPACES_BEGIN_OR_END)
    description: str = Field(description="Project description", pattern=STRING_NO_SPACES_BEGIN_OR_END)


class StartTimeRecordSchema(BaseModel):  # pylint: disable=too-few-public-methods
    """Class schema to start a record"""

    description: str
    people: list
    project: Optional[str] = Field(default="na")
    time_zone: str
    start_time: str


class EndTimeRecordSchema(StartTimeRecordSchema):  # pylint: disable=too-few-public-methods
    """Class schema to end a record"""

    end_time: str
    ending_comments: Optional[str] = Field(default="no comments added")
    total_time_worked: str


class CompletedTimeRecordsSchema(BaseModel):  # pylint: disable=too-few-public-methods
    """Class schema for records archive"""

    records: List[EndTimeRecordSchema]
