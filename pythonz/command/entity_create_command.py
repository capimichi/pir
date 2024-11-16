import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='entity:create'
)
def entity_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    entity_name = click.prompt('Enter the name of the entity es. PostEntity')
    pythonz_manager.generate_class(entity_name, 'entity')
    click.echo('Created entity successfully')
