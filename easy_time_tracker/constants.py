"""
Constants for easy_time_tracker
"""

from pathlib import Path

STRING_NO_SPACES = r"^\S+$"
STRING_NO_SPACES_BEGIN_OR_END = r"^\S.*\S$"
EASY_TIME_TRACKER_DATABASE_PATH = Path.home().resolve().as_posix()
