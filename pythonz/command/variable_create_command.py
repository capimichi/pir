import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='variable:create'
)
def variable_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    variable_name = click.prompt('Enter the name of the variable es. PostVariable')
    pythonz_manager.generate_class(variable_name, 'variable')
    click.echo('Created variable successfully')
