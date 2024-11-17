import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='client:create',
)
@click.option('--entity_name', prompt='Enter the name of the entity (optional)', default='',
              help='The name of the entity associated with the client')
def client_create_command(entity_name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    client_name = click.prompt('Enter the name of the client es. PostClient')
    pythonz_manager.generate_class(
        class_name=client_name,
        class_type='client',
        entity_name=entity_name
    )
    click.echo('Created client successfully')
