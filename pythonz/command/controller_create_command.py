import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='controller:create'
)
@click.option('--entity_name', default='', help='The name of the entity associated with the controller')
def controller_create_command(entity_name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    controller_name = click.prompt('Enter the name of the controller es. PostController')
    pythonz_manager.generate_class(
        class_name=controller_name,
        class_type='controller',
        entity_name=entity_name
    )
    click.echo('Created controller successfully')
