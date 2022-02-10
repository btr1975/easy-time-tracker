"""
Data schemas
"""
from typing import List
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class StartTimeRecordSchema(BaseModel):  # pylint: disable=too-few-public-methods
    """Class schema to start a record"""
    description: str
    people: list
    time_zone: str
    start_time: str


class EndTimeRecordSchema(StartTimeRecordSchema):  # pylint: disable=too-few-public-methods
    """Class schema to end a record"""
    end_time: str
    total_time_worked: str


class CompletedTimeRecordsSchema(BaseModel):  # pylint: disable=too-few-public-methods
    """Class schema to end a record"""
    records: List[EndTimeRecordSchema]
