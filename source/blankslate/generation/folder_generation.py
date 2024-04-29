"""folder_generation.py: Contains functions for generating folders."""

import os
from pathlib import Path

from logs.setup_logging import setup_logging

folder_logger = setup_logging()


def generate_folder(folder: str, path: Path) -> None:
    """
    Generate a folder.
    :param folder: The folder to generate.
    :param path: The path to generate the folder in.
    """
    folder_logger.debug(f"Generating folder: {folder}")
    folder_path = path / folder
    os.makedirs(folder_path, exist_ok=True)
    folder_logger.info(f"Folder generated: {folder_path}")


def generate_folders(folders: list[str], path: Path) -> None:
    """
    Generate multiple folders.
    :param folders: The folders to generate.
    :param path: The path to generate the folders in.
    """
    for folder in folders:
        generate_folder(folder, path)


def generate_folder_structure(
    folder_structure: dict[str, list[str]], path: Path
) -> None:
    """
    Generate a folder structure, limited to one level of subfolders.
    :param folder_structure: The folder structure to generate.
    :param path: The path to generate the folder structure in.
    """
    if not folder_structure:
        folder_logger.warning("No folder structure to generate.")
        return
    elif not path.exists():
        folder_logger.warning(f"Path does not exist, creating: {path}")
        os.makedirs(path)

    folder_logger.debug(f"Generating folder structure: {folder_structure}")

    for folder, subfolders in folder_structure.items():
        current_path = path / folder
        generate_folder(folder, path)
        if isinstance(subfolders, list):
            folder_logger.debug(f"Generating subfolders: {subfolders}")
            generate_folders(subfolders, current_path)
        elif isinstance(subfolders, dict):
            folder_logger.debug(f"Generating subfolders: {subfolders.keys()}")
            generate_folder_structure(subfolders, current_path)
