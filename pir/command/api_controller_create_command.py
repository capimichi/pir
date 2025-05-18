import click

from pir.container.DefaultContainer import DefaultContainer
from pir.manager.PirManager import PirManager


@click.command(
    name='api:controller:create'
)
@click.option('--name', default='', help='The name of the API controller', prompt="Enter the name of the API controller. es. TableApiController")
@click.option('--entity_name', default='', help='The name of the entity associated with the API controller', prompt="Enter the name of the entity. es. Table")
def api_controller_create_command(name: str, entity_name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    pir_manager.generate_class(
        class_name=name,
        class_type='controller',
        entity_name=entity_name,
        template_name="api_controller.jinja"
    )
    click.echo('Created API controller successfully')
