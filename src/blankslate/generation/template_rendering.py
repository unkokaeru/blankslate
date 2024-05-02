"""template_rendering.py: Contains functions for rendering templates."""

from jinja2 import Environment, FileSystemLoader, TemplateNotFound

from logs.setup_logging import setup_logging
from config.paths import Paths

template_logger = setup_logging()


def render_template(template: str, output: str, data: dict) -> None:
    """
    Render a template and write the generated content to a file.
    :param template: The template to render.
    :param output: The output file.
    :param data: The data to pass to the template.
    """
    # Initialize Jinja2 environment and load template
    template_logger.debug(f"Rendering template: {template}")
    env = Environment(loader=FileSystemLoader(Paths.TEMPLATES_PATH))
    try:
        template = env.get_template(template)
    except TemplateNotFound:
        template_logger.error(f"Template not found: {template}")
        return
    template_logger.debug(f"Template loaded: {template}")

    # Render the template
    rendered_template = template.render(data)
    template_logger.debug(f"Template rendered: {rendered_template}")

    # Write the rendered template to the output file
    with open(output, "w", encoding="utf-8") as file:
        file.write(rendered_template)

    template_logger.info(f"Template rendered and saved to: {output}")
