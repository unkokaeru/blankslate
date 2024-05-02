"""command_line.py - Command line interface for the application."""

from logs.setup_logging import setup_logging

interface_logger = setup_logging()


def name_to_shorthand(name: str) -> str:
    """
    Convert a name to a shorthand version.

    Parameters
    ----------
    name : str
        The name to convert.

    Returns
    -------
    str
        The shorthand version of the name.

    Examples
    --------
    >>> name_to_shorthand("John Doe")
    'J. Doe'
    >>> name_to_shorthand("Jane Smith")
    'J. Smith'
    >>> name_to_shorthand("Alice")
    'Alice'

    Notes
    -----
    This function converts a name to a shorthand version.
    """
    name_parts = name.split(" ")

    if len(name_parts) == 1:
        return name_parts[0]

    # TODO: Add support for middle names

    first_name = name_parts[0]
    last_name = name_parts[-1]

    return f"{first_name[0]}. {last_name}"


def format_detail(detail: str) -> str:
    """
    Format a detail for user input.
    :param detail: The detail to format, e.g. "project_name".
    :return: The formatted detail, e.g. "project name".
    """
    detail_spaced = detail.replace("_", " ", 1)
    detail_lower = detail_spaced.lower()
    detail_bracketed = detail_lower.replace("_", " (", 1)
    detail_formatted = (
        detail_spaced if detail_spaced == detail_bracketed else detail_bracketed + ")"
    )

    return detail_formatted


def input_project_details() -> dict[str, str]:
    """
    Input the project details from the user.
    :return: A dictionary containing the project details.
    """
    interface_logger.info("First up, let's get some details about your project.")

    project_details = {}

    details_to_input = [
        "project_location",
        "project_name",
        "project_description",
        "project_year",
        "project_author",
        "project_author_shorthand",
        "project_author_email",
        "project_author_username",
    ]

    for detail in details_to_input:
        if detail == "project_author_shorthand":
            project_details[detail] = name_to_shorthand(
                project_details["project_author"]
            )
        else:
            formatted_detail = format_detail(detail)

            project_details[detail] = input(f"What's the {formatted_detail}? ")

    interface_logger.info(
        "Great! We've got all the details we need. Are these correct?"
    )

    for detail, value in project_details.items():
        formatted_detail = format_detail(detail)
        interface_logger.info(f"{formatted_detail.title()}: {value}")

    if input("Type 'y' to confirm: ").lower().strip() != "y":
        interface_logger.info("Let's try that again...")
        return input_project_details()  # TODO: Allow user to re-enter specific details

    interface_logger.info("Thanks! We're all set.")

    interface_logger.debug(f"Project details: {project_details}")

    return project_details