import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='client:create'
)
def client_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    client_name = click.prompt('Enter the name of the client es. PostClient')
    pythonz_manager.generate_class(client_name, 'client')
    click.echo('Created client successfully')
