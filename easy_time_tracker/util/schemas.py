"""
Data schemas
"""

from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict  # pylint: disable=no-name-in-module


class Person(BaseModel):
    """Person Document Schema"""

    model_config = ConfigDict(use_enum_values=True)

    first_name: str = Field(description="First name")
    last_name: str = Field(description="Last name")
    email: str = Field(description="Email")


class Project(BaseModel):
    """Project Document Schema"""

    model_config = ConfigDict(use_enum_values=True)

    name: str = Field(description="Project name")
    description: str = Field(description="Project description")


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
