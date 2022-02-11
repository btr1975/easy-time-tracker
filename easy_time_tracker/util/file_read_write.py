"""
Utils for reading and writing files
"""
import os


def check_if_current_file_exists(path: str) -> bool:
    """Function to check if a file exists

    :type path: String
    :param path: The full path to the file name

    :rtype: Boolean
    :returns: True or False

    """
    return os.path.isfile(path)


def write_text_file(path: str, data: str) -> None:
    """Function to write to text file

    :type path: String
    :param path: The full path to the file name
    :type data: String
    :param data: The data to write to the file

    :rtype: None
    :returns: It writes files

    """
    with open(f'{path}', 'w', encoding='utf-8', newline='\n') as file:
        file.write(data)


def read_text_file(path: str) -> str:
    """Function to read to text file

    :type path: String
    :param path: The full path to the file name

    :rtype: String
    :returns: The data from the text file

    """
    with open(f'{path}', 'r', encoding='utf-8', newline='\n') as file:
        data = file.read()

    return data


def delete_current_file(path: str) -> None:
    """Function to delete a file

    :type path: String
    :param path: The full path to the file name

    :rtype: None
    :returns: It deletes files

    """
    if check_if_current_file_exists(path):
        os.remove(path)
