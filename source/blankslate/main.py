"""main.py: Enter the application."""

from generation.project_generation import generate_project
from interface.command_line import input_project_details
from logs.setup_logging import setup_logging

main_logger = setup_logging()

"""
To-Do List:
Auto-versioning (python-semantic-release with GitHub actions and angular commit style)
GitHub workflows
Auto docs geneneration (Sphinx)
Tests (pytest)
Automatically import VSCode profile
Input validation
Interface improvements - GUI, progress bar, etc.


Angular Commit Style (reminder):
<type>(<scope>): <short summary>
    │       │             │
    │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
    │       │
    │       └─⫸ Commit Scope: animations|bazel|benchpress|common|compiler|compiler-cli|core|
    │                          elements|forms|http|language-service|localize|platform-browser|
    │                          platform-browser-dynamic|platform-server|router|service-worker|
    │                          upgrade|zone.js|packaging|changelog|docs-infra|migrations|ngcc|ve|
    │                          devtools
    │
    └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test
"""


def run_blankslate() -> None:
    """
    Main entry point of the application.

    Notes
    -----
    This function is the main entry point of the application.
    It is responsible for starting the application, taking in
    user input, and generating the project. It does not return
    anything.
    """
    main_logger.info("Application started.")

    project_details = input_project_details()

    generate_project(project_details)


if __name__ == "__main__":
    try:
        run_blankslate()
    except KeyboardInterrupt:
        print("\n")
        main_logger.info("Exiting application due to user interrupt...")
