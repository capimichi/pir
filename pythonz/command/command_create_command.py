import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='command:create'
)
def command_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    command_name = click.prompt('Enter the name of the command es. create_post_command')
    command_alias = click.prompt('Enter the alias of the command es. post:create')
    pythonz_manager.generate_command(command_name, command_alias)
    click.echo('Created command successfully')
