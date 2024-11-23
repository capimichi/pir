import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='service:create'
)
@click.option('--name', default='', help='The name of the service', prompt="Enter the name of the service. es. PostService")
@click.option('--entity_name', default='', help='The name of the entity associated with the service')
def service_create_command(name: str, entity_name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    pir_manager.generate_class(
        class_name=name,
        class_type='service',
        entity_name=entity_name
    )
    click.echo('Created service successfully')
