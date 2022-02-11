"""
easy_time_tracker
"""
from datetime import datetime
import json
from .constants import EASY_TIME_TRACKER_CURRENT_RECORD as _EASY_TIME_TRACKER_CURRENT_RECORD
from .constants import EASY_TIME_TRACKER_COMPLETED_RECORDS as _EASY_TIME_TRACKER_COMPLETED_RECORDS
from .util.schemas import StartTimeRecordSchema, EndTimeRecordSchema, CompletedTimeRecordsSchema
from .util.file_read_write import check_if_current_file_exists, write_text_file, read_text_file, delete_current_file


class EasyTimeTracker:
    """Class to create records, and end records"""
    EASY_TIME_TRACKER_CURRENT_RECORD = _EASY_TIME_TRACKER_CURRENT_RECORD
    EASY_TIME_TRACKER_COMPLETED_RECORDS = _EASY_TIME_TRACKER_COMPLETED_RECORDS

    def start_time_record(self, description: str, people: list) -> None:
        """Method to create a record and write the data

        :type description: String
        :param description: The description of the time being recorded
        :type people: List
        :param people: A list of people during the time

        :rtype: None
        :returns: None

        """
        start_time_record = StartTimeRecordSchema(description=description, people=people, time_zone='UTC',
                                                  start_time=str(datetime.utcnow()))

        self._write_current_record(start_time_record)

    def _write_current_record(self, start_time_record: StartTimeRecordSchema) -> None:
        """Protected Method to write the current record

        :type start_time_record: StartTimeRecordSchema
        :param start_time_record: The record to write

        :rtype: None
        :returns: It writes files

        :raises FileExistsError: If a current working record exists already

        """
        if not check_if_current_file_exists(self.EASY_TIME_TRACKER_CURRENT_RECORD):
            write_text_file(self.EASY_TIME_TRACKER_CURRENT_RECORD, start_time_record.json())

        else:
            raise FileExistsError(f'{self.EASY_TIME_TRACKER_CURRENT_RECORD} already exists!!')

    def end_time_record(self) -> None:
        """Method to end a time record

        :rtype: None
        :returns: It ends time records at writes archive

        :raises FileNotFoundError: If a current record is not ongoing

        """
        if check_if_current_file_exists(self.EASY_TIME_TRACKER_CURRENT_RECORD):
            start_time_record = StartTimeRecordSchema(**self._read_current_record())
            current_time = datetime.utcnow()
            total_time_worked = current_time - datetime.strptime(start_time_record.start_time, '%Y-%m-%d %H:%M:%S.%f')
            end_time_record = EndTimeRecordSchema(end_time=str(current_time), total_time_worked=str(total_time_worked),
                                                  **start_time_record.dict())

            self._write_completed_records(end_time_record)

            delete_current_file(self.EASY_TIME_TRACKER_CURRENT_RECORD)

        else:
            raise FileNotFoundError(f'{self.EASY_TIME_TRACKER_CURRENT_RECORD} not found!!')

    def _read_current_record(self) -> dict:
        """Protected Method to read the stored json current record

        :rtype: Dict
        :returns: The json data as a dictionary

        """
        current_record = read_text_file(self.EASY_TIME_TRACKER_CURRENT_RECORD)
        return json.loads(current_record)

    def _read_completed_records(self) -> dict:
        """Protected Method to read the stored json records

        :rtype: Dict
        :returns: The json data as a dictionary

        """
        completed_records = read_text_file(self.EASY_TIME_TRACKER_COMPLETED_RECORDS)
        return json.loads(completed_records)

    def _write_completed_records(self, current_completed_record: EndTimeRecordSchema) -> None:
        """Protected Method to write completed records

        :type current_completed_record: EndTimeRecordSchema
        :param current_completed_record: The current completing record

        :rtype: None
        :returns: It writes files

        """
        if check_if_current_file_exists(self.EASY_TIME_TRACKER_COMPLETED_RECORDS):
            completed_records = CompletedTimeRecordsSchema(**self._read_completed_records())
            completed_records.records.append(current_completed_record)

        else:
            completed_records = CompletedTimeRecordsSchema(records=[current_completed_record])

        write_text_file(self.EASY_TIME_TRACKER_COMPLETED_RECORDS, completed_records.json())
