import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='entity:create'
)
@click.option('--name', default='', help='The name of the entity',
              prompt="Enter the name of the entity. es. PostEntity")
def entity_create_command(name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    pir_manager.generate_class(
        name,
        'entity'
    )
    click.echo('Created entity successfully')
