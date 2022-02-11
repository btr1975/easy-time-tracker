import pytest
import os
from unittest import mock


@pytest.fixture
def temp_directory(tmp_path):
    d = tmp_path / 'easy_time_tracker-unit-tests'
    d.mkdir()
    return str(d)


@pytest.fixture
def temp_easy_time_tracker_base_path(temp_directory):
    return temp_directory


@pytest.fixture
def temp_easy_time_tracker_current_record_path(temp_directory):
    return os.path.join(temp_directory, 'unit-test-current.json')


@pytest.fixture
def temp_easy_time_tracker_completed_records_path(temp_directory):
    return os.path.join(temp_directory, 'unit-test-completed.json')


@pytest.fixture
def mock_settings_env_vars(temp_easy_time_tracker_completed_records_path, temp_easy_time_tracker_current_record_path):
    with mock.patch.dict(os.environ,
                         {'EASY_TIME_TRACKER_COMPLETED_RECORDS': temp_easy_time_tracker_completed_records_path,
                          'EASY_TIME_TRACKER_CURRENT_RECORD': temp_easy_time_tracker_current_record_path}):
        yield
