"""project_generation.py: Contains the functions for generating a project."""

from pathlib import Path

from logs.setup_logging import setup_logging

from generation.folder_generation import generate_folder_structure
from generation.template_rendering import render_template

project_logger = setup_logging()


def dict_to_tree(file_structure: dict, indent: int = 0, prefix: str = "") -> str:
    """
    Convert a dictionary structure into a tree-like string representation.
    :param file_structure: The dictionary structure to convert.
    :param indent: The current indentation level.
    :param prefix: A string prefix to represent the tree "branches".
    :return: A string representation of the dictionary structure.
    """
    if not file_structure:
        return ""

    keys = list(file_structure.keys())
    last_index = len(keys) - 1
    structure_str = ""

    for index, key in enumerate(keys):
        if index == last_index:
            joint = "└── "
            extension = "    "
        else:
            joint = "├── "
            extension = "│   "

        structure_str += f"{prefix}{joint}{key}\n"

        if isinstance(file_structure[key], dict):
            sub_prefix = prefix + extension
            structure_str += dict_to_tree(file_structure[key], indent + 1, sub_prefix)

    return structure_str


def strip_to_folder_structure(full_structure: dict) -> dict:
    """
    Strip a full structure dictionary to just the folder structure.
    :param full_structure: The full structure dictionary.
    :return: The folder structure dictionary.
    """
    folder_structure = {}
    for key, value in full_structure.items():
        if isinstance(value, dict):
            nested_folders = strip_to_folder_structure(value)
            if nested_folders:
                folder_structure[key] = nested_folders
            elif not nested_folders:
                folder_structure[key] = []
        elif isinstance(value, list):
            folder_structure[key] = []

    return folder_structure


def strip_to_files(full_structure: dict, base_path: str = "") -> list[tuple[str, str]]:
    """
    Strip a full structure dictionary to just the file paths.
    :param full_structure: The full structure dictionary.
    :param base_path: The base path for the current recursive call, used internally.
    :return: A list of tuples containing file names and their paths.
    """
    files_list = []
    for key, value in full_structure.items():
        current_path = f"{base_path}/{key}".strip("/")
        if isinstance(value, dict):
            nested_files = strip_to_files(value, current_path)
            files_list.extend(nested_files)
        elif value is None:
            files_list.append((key, current_path))

    return files_list


def generate_project(project_details: dict[str, str]) -> None:
    """
    Generate a project based on the provided details.
    :param project_details: A dictionary containing the project details.
    """
    project_name = project_details["project_name"]
    project_location = project_details["project_location"]

    full_structure = {
        ".github": {
            "workflows": [],
        },
        "docs": [],
        "source": {
            project_name: {
                "config": {
                    "__init__.py": None,
                    "constants.py": None,
                    "paths.py": None,
                },
                "interface": {
                    "__init__.py": None,
                    "command_line.py": None,
                },
                "logs": {
                    "__init__.py": None,
                    "setup_logging.py": None,
                },
                "main.py": None,
                "VERSION": None,
            },
        },
        "tests": [],
        ".gitignore": None,
        "LICENSE": None,
        "pyproject.toml": None,
        "README.md": None,
        "requirements.txt": None,
    }

    project_logger.info(f"Generating project: {project_name}")
    project_logger.info(f"{project_name}\n{dict_to_tree(full_structure)}")

    folder_structure = strip_to_folder_structure(full_structure)
    file_structure = strip_to_files(full_structure)

    project_logger.debug(f"Folder structure:\n{folder_structure}")
    project_logger.debug(f"File structure:\n{file_structure}")

    generate_folder_structure(folder_structure, Path(project_location))

    for file_name, file_path in file_structure:
        render_template(
            file_name + ".j2", Path(project_location + file_path), project_details
        )  # TODO: fix
