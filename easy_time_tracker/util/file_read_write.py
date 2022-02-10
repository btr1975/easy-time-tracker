"""
Utils for reading and writing files
"""
from typing import Union
import os


def check_if_current_file_exists(path: str) -> bool:
    return os.path.isfile(path)


def write_text_file(path: str, data: str) -> None:
    with open(f'{path}', 'w', encoding='utf-8', newline='\n') as file:
        file.write(data)


def read_text_file(path: str) -> Union[None, str]:
    data = None
    if not check_if_current_file_exists(path):
        with open(f'{path}', 'r', encoding='utf-8', newline='\n') as file:
            data = file.read()

    return data


def delete_current_file(path: str):
    os.remove(path)
