import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='view:create'
)
def view_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    view_name = click.prompt('Enter the name of the view es. PostView')
    pythonz_manager.generate_class(view_name, 'view')
    click.echo('Created view successfully')
