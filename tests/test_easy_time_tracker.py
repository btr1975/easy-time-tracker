import pytest
import sys
import os
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


def test_start_time_record(mock_settings_env_vars):
    from easy_time_tracker.easy_time_tracker import EasyTimeTracker
    obj = EasyTimeTracker()
    obj.start_time_record('test description', ['test-person-1', 'test-person-2'])


def test_end_time_record(mock_settings_env_vars):
    from easy_time_tracker.easy_time_tracker import EasyTimeTracker
    obj = EasyTimeTracker()
    obj.end_time_record('test description end comment')


def test_write_completed_records_to_excel(mock_settings_env_vars, temp_directory):
    from easy_time_tracker.easy_time_tracker import EasyTimeTracker
    obj = EasyTimeTracker()
    obj.write_completed_records_to_excel(temp_directory)


def test_full_flow(mock_settings_env_vars, temp_directory):
    from easy_time_tracker.easy_time_tracker import EasyTimeTracker
    obj = EasyTimeTracker()
    with pytest.raises(FileNotFoundError):
        obj.end_time_record('test description end comment 1')

    obj.start_time_record('test description 1', ['test-person-1', 'test-person-2'])

    with pytest.raises(FileExistsError):
        obj.start_time_record('test description 2', ['test-person-3', 'test-person-4'])

    obj.end_time_record('test description end comment 1')
    obj.start_time_record('test description 2', ['test-person-3', 'test-person-4'])
    obj.end_time_record('test description end comment 2')
    obj.write_completed_records_to_excel(temp_directory)

