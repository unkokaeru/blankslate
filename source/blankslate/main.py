"""main.py: Called when the package is run as a script."""

from .generation.project_generation import generate_project
from .interface.command_line import input_project_details, show_manual
from .logs.setup_logging import setup_logging

main_logger = setup_logging()

# TODO: fix badge generation in templates


def main() -> None:
    """
    Main function for the application.

    Notes
    -----
    This function is the entry point for the application.
    """
    try:
        main_logger.info("Application started.")
        project_details = input_project_details()
        generate_project(
            project_details
        )  # TODO: add auto GitHub repo publish and other general first time user stuff
        show_manual()
    except KeyboardInterrupt:
        print("\n")
        main_logger.info("Exiting application due to user interrupt...")


if __name__ == "__main__":
    main()
