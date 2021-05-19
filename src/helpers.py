import json
from typing import Any


def base_path(relpath: str = ''):
    """Get the path to the base directory of the project."""
    from pathlib import Path

    path = Path().absolute()

    if 'alkbot' not in str(path):
        EnvironmentError('Project folder not found.')

    while 'alkbot' not in path.name:
        path = path.parent

    return path.joinpath(relpath)


def source_path(relpath: str = ''):
    """Get the path to the src (source) folder."""
    return base_path(f'src/{relpath}')


def get_string(json_path: str, file_path: str = 'resources/strings.json') -> str:
    """Get a string that the bot can reply with."""
    strings = load_strings(file_path)

    if isinstance(strings, dict):
        return strings.get(json_path, '')

    return ''


def load_strings(file_path: str = 'resources/strings.json') -> Any:
    """Load a json file and return its content."""
    with open(source_path(file_path)) as strings_file:
        return json.load(strings_file)
