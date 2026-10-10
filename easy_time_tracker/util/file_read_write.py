"""
Utils for reading and writing files
"""

import os
from typing import Collection, Any
import pandas as pd


def check_if_current_file_exists(path: str) -> bool:
    """Function to check if a file exists

    :param path: The full path to the file name

    :returns: True or False
    """
    return os.path.isfile(path)


def write_text_file(path: str, data: str) -> None:
    """Function to write to text file

    :param path: The full path to the file name
    :param data: The data to write to the file

    :returns: It writes files
    """
    with open(f"{path}", "w", encoding="utf-8", newline="\n") as file:
        file.write(data)


def read_text_file(path: str) -> str:
    """Function to read to text file

    :param path: The full path to the file name

    :returns: The data from the text file
    """
    with open(f"{path}", "r", encoding="utf-8", newline="\n") as file:
        data = file.read()

    return data


def delete_current_file(path: str) -> None:
    """Function to delete a file

    :param path: The full path to the file name

    :returns: It deletes files
    """
    if check_if_current_file_exists(path):
        os.remove(path)


def wrtie_excel_file(path: str, data: Any, headers: Collection) -> None:
    """Function to write to Excel file

    :param path: The full path to the file name
    :param data: The column data
    :param headers: The column headers

    :returns: It creates Excel
    """
    df = pd.DataFrame(data=data, columns=headers)

    df.to_excel(path)
