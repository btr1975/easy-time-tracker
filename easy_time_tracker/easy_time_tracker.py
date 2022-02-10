"""
easy_time_tracker
"""
from datetime import datetime
import json
from .util.schemas import StartTimeRecordSchema, EndTimeRecordSchema, CompletedTimeRecordsSchema
from .util.file_read_write import check_if_current_file_exists, write_text_file, read_text_file


def create_start_time_record(description: str, people: list) -> StartTimeRecordSchema:
    start_time_record = StartTimeRecordSchema(description=description, people=people, time_zone='UTC',
                                              start_time=str(datetime.utcnow()))
    return start_time_record


def write_current_record(path: str, description: str, people: list):
    if not check_if_current_file_exists(path):
        write_text_file(path, create_start_time_record(description, people).json())

    else:
        raise FileExistsError(f'{path} already exists!!')


def create_end_time_record(start_time_record: StartTimeRecordSchema) -> EndTimeRecordSchema:
    current_time = datetime.utcnow()
    total_time_worked = current_time - datetime.strptime(start_time_record.start_time, '%Y-%m-%d %H:%M:%S.%f')
    end_time_record = EndTimeRecordSchema(end_time=str(current_time), total_time_worked=str(total_time_worked),
                                          **start_time_record.dict())
    return end_time_record


def read_completed_records(path: str):
    completed_records = read_text_file(path)
    print(json.dumps(completed_records))


def write_completed_records(path: str, current_completed_record: EndTimeRecordSchema):
    records = []
    if check_if_current_file_exists(path):
        completed_records = read_text_file(path)
        print(json.dumps(completed_records))

    else:
        records.append(current_completed_record)
        completed_records = CompletedTimeRecordsSchema(records=records)
        write_text_file(path, completed_records.json())
