import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='manager:create'
)
def manager_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    manager_name = click.prompt('Enter the name of the manager es. PostManager')
    pythonz_manager.generate_class(manager_name, 'manager')
    click.echo('Created manager successfully')
