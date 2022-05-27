| BRANCH  | STATUS |
|---------|---|
| main    | [![Unit-Testing, Coverage, Linting](https://github.com/btr1975/easy-time-tracker/actions/workflows/test-coverage-lint.yml/badge.svg?branch=main)](https://github.com/btr1975/easy-time-tracker/actions/workflows/test-coverage-lint.yml) |
| develop | [![Unit-Testing, Coverage, Linting](https://github.com/btr1975/easy-time-tracker/actions/workflows/test-coverage-lint.yml/badge.svg?branch=develop)](https://github.com/btr1975/easy-time-tracker/actions/workflows/test-coverage-lint.yml) |

[![Downloads](https://pepy.tech/badge/easy-time-tracker)](https://pepy.tech/project/easy-time-tracker)
[![Supported Versions](https://img.shields.io/pypi/pyversions/easy-time-tracker.svg)](https://pypi.org/project/easy-time-tracker)

# easy-time-tracker
A simple work time tracker CLI

## Environmental Variables

* Set these variables if you want to save your data somewhere else.

| VARIABLE | USE | DEFAULT-FILE-NAME |
|---|---|---|
| EASY_TIME_TRACKER_CURRENT_RECORD | Set the location of where to store this data | current_record.json |
| EASY_TIME_TRACKER_COMPLETED_RECORDS | Set the location of where to store this data | completed_records.json |

### Notes

* It runs as a linux style cli command use -h, or --help to get help

```text

(venv) user@main-pc:~/some-directory$ ett -h
usage: ett [-h] {start,stop,output,gui} ...

easy-time-tracker

optional arguments:
  -h, --help            show this help message and exit

commands:
  Valid commands: a single command is required

  {start,stop,output,gui}
                        CLI Help
    start               Start the clock
    stop                Stop the clock
    output              Output completed records
    gui                 Start the GUI
```

* Example help for start, people is optional it is to include names of people that were in a meeting.

```text
(venv) user@main-pc:~/some-directory$ ett start -h
usage: ett start [-h] [-d DESCRIPTION] [-p PEOPLE [PEOPLE ...]]

optional arguments:
  -h, --help            show this help message and exit
  -d DESCRIPTION, --description DESCRIPTION
                        Description of the time
  -p PEOPLE [PEOPLE ...], --people PEOPLE [PEOPLE ...]
                        List of people

```
