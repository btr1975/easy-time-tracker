"""
Constants for easy_time_tracker
"""
import os

# The absolute path to the easy-time-tracker directory
EASY_TIME_TRACKER_BASE_PATH = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# The absolute path to the easy-time-tracker static_data directory
EASY_TIME_TRACKER_STATIC_DATA = os.path.join(EASY_TIME_TRACKER_BASE_PATH, 'static_data')
# The name to use for the current record
EASY_TIME_TRACKER_CURRENT_RECORD = os.getenv('EASY_TIME_TRACKER_CURRENT_RECORD') or \
                                   os.path.join(EASY_TIME_TRACKER_STATIC_DATA, 'current_record.json')
# The name to use for the completed records
EASY_TIME_TRACKER_COMPLETED_RECORDS = os.getenv('EASY_TIME_TRACKER_COMPLETED_RECORDS') or \
                                      os.path.join(EASY_TIME_TRACKER_STATIC_DATA, 'completed_records.json')
