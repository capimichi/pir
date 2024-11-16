import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='service:create'
)
def service_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    service_name = click.prompt('Enter the name of the service es. PostService')
    pythonz_manager.generate_class(service_name, 'service')
    click.echo('Created service successfully')
