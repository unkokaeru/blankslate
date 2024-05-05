   Welcome to Blankslate's documentation!
   =======================================

.. image:: https://github.com/unkokaeru/blankslate/actions/workflows/continuous_integration.yml/badge.svg
    :target: https://github.com/unkokaeru/blankslate/actions/workflows/continuous_integration.yml
    :alt: Continuous Integration (CI) Tests

Blankslate automates the creation of Python projects, ensuring that each project adheres to best practices in Python development. It leverages GitHub Actions, NumPy docstrings, and a well-organised directory structure to deliver a project scaffold ready for deployment.

Installation
------------

To install Blankslate, run the following command in your terminal:

.. code-block:: bash

    pip install blankslate-python

Getting Started
---------------

Once installed, you can create a new project by executing:

.. code-block:: bash

    blankslate-python

Follow the prompts to specify your project details. Blankslate will set up the project in your specified directory. Then, you can push this project to GitHub and begin coding in the `source/PROJECT_NAME/` directory.

Features
--------

- **Automatic Project Setup**: Generates a Python project configured with best practices, including a GitHub Actions workflow.
- **Semantic Versioning**: Use `./scripts/release.sh VERSION_NUMBER` to manage versions and generate a changelog. Follow [semantic versioning](https://semver.org). Note that this will automatically build and publish the project to PyPi, too.
- **Angular Commit Style**: Ensure your commits follow the [Angular commit style guidelines](https://gist.github.com/brianclements/841ea7bffdb01346392c#commit-message-header).
- **Documentation Automation**: Automatically generates and updates documentation on GitHub Pages.
- **TODO Issue Tracker**: Converts `# TODO` comments in Python code into GitHub issues. Ensure correct repository settings to enable this feature.

For a full list of features, visit the `features` section.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`