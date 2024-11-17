import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='service:create'
)
@click.option('--entity_name', default='', help='The name of the entity associated with the service')
def service_create_command(entity_name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    service_name = click.prompt('Enter the name of the service es. PostService')
    pythonz_manager.generate_class(
        class_name=service_name,
        class_type='service',
        entity_name=entity_name
    )
    click.echo('Created service successfully')
