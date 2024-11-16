import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='model:create'
)
def model_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    model_name = click.prompt('Enter the name of the model es. PostModel')
    pythonz_manager.generate_class(model_name, 'model')
    click.echo('Created model successfully')
