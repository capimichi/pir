import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='client:create',
)
@click.option('--entity_name', default='', help='The name of the entity associated with the client')
def client_create_command(entity_name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    client_name = click.prompt('Enter the name of the client es. PostClient')
    pir_manager.generate_class(
        class_name=client_name,
        class_type='client',
        entity_name=entity_name
    )
    click.echo('Created client successfully')
