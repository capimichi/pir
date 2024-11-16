import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='di:add'
)
def di_add_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    source_name = click.prompt('Enter the name of the source class es. PostService')
    target_name = click.prompt('Enter the name of the dependency class es. PostRepository')
    pythonz_manager.add_dependency(source_name, target_name)
    click.echo('Added dependency successfully')
