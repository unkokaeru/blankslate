"""template_rendering.py: Contains functions for rendering templates."""

from jinja2 import Environment, FileSystemLoader, TemplateNotFound

from ..config.paths import Paths
from ..logs.setup_logging import setup_logging

template_logger = setup_logging()


def render_template(template: str, output: str, data: dict) -> None:
    """
    Render a Jinja2 template and save it to a file.

    Parameters
    ----------
    template : str
        The template to render.
    output : str
        The output file to save the rendered template to.
    data : dict
        The data to render the template with.

    Examples
    --------
    >>> render_template("template.md.j2", "template.md", {"name": "Alice"})
    Template rendered and saved to: template.md

    Notes
    -----
    This function renders a Jinja2 template with the provided data
    and saves the rendered template to the output file.
    """
    # Initialize Jinja2 environment and load template
    template_logger.debug(f"Rendering template: {template}")
    env = Environment(loader=FileSystemLoader(Paths.TEMPLATES_PATH))
    try:
        template_obj = env.get_template(template)
    except TemplateNotFound:
        template_logger.error(f"Template not found: {template}")
        return
    template_logger.debug(f"Template loaded: {template_obj}")

    # Render the template
    rendered_template = template_obj.render(data)
    template_logger.debug(f"Template rendered: {rendered_template}")

    # Write the rendered template to the output file
    with open(output, "w", encoding="utf-8") as file:
        file.write(rendered_template)

    template_logger.info(f"Template rendered and saved to: {output}")
