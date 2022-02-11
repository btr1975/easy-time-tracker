import pytest
import sys
import os
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


def test_constants(mock_settings_env_vars, temp_easy_time_tracker_completed_records_path,
                   temp_easy_time_tracker_current_record_path):
    from easy_time_tracker.constants import EASY_TIME_TRACKER_COMPLETED_RECORDS, EASY_TIME_TRACKER_CURRENT_RECORD
    assert EASY_TIME_TRACKER_COMPLETED_RECORDS == temp_easy_time_tracker_completed_records_path
    assert EASY_TIME_TRACKER_CURRENT_RECORD == temp_easy_time_tracker_current_record_path
