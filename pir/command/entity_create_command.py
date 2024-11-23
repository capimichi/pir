import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='entity:create'
)
def entity_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    entity_name = click.prompt('Enter the name of the entity es. PostEntity')
    pir_manager.generate_class(entity_name, 'entity')
    click.echo('Created entity successfully')
