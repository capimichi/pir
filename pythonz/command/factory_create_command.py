import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='factory:create'
)
def factory_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    factory_name = click.prompt('Enter the name of the factory es. PostFactory')
    pythonz_manager.generate_class(factory_name, 'factory')
    click.echo('Created factory successfully')
