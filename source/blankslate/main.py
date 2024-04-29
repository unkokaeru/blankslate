"""main.py: The main entry point of the application."""

from generation.project_generation import generate_project
from interface.command_line import input_project_details
from logs.setup_logging import setup_logging

main_logger = setup_logging()

"""
To-Do List:
Auto-versioning
GitHub workflows
Auto docs geneneration
Tests
Automatically import VSCode profile
Input validation
Interface improvements - GUI, progress bar, etc.
"""


def main() -> None:
    """The main function of the application."""
    main_logger.info("Application started.")

    project_details = input_project_details()

    generate_project(project_details)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        main_logger.info("Exiting application due to user interrupt...")
