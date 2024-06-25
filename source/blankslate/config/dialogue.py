"""dialogue.py: Dialogue for the application."""


class Dialogue:
    """
    Dialogue for the application.
    
    Notes
    -----
    This class contains dialogue used throughout the application.
    By storing dialogue in a single location, it is easier to
    manage and update it. Dialogue should be defined as class
    attributes and should be named in uppercase with underscores
    separating words.
    """
    
    # Manual
    MANUAL = """
Now that you've completed setup, you can start creating your project.
You should open the new directory named after your project, located in
your Documents/GitHub directory.
Then, publish your project to GitHub to enable version control and
other features.
Next, run the helper script to publish the project to PyPI, among other
things, using the command `.\scripts\release.sh 0.0.0`, where `0.0.0` is
the version number (using the semantic versioning described in
Blankslate's README.md).

All done!

Whenever you make a change, push it to GitHub then use the helper script
again to publish the changes to PyPI.
"""