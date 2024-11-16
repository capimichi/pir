import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='helper:create'
)
def helper_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    helper_name = click.prompt('Enter the name of the helper es. PostHelper')
    pythonz_manager.generate_class(helper_name, 'helper')
    click.echo('Created helper successfully')
