import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='repository:create'
)
def repository_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)

    repository_name = click.prompt('Enter the name of the repository es. PostRepository')
    pythonz_manager.generate_class(repository_name, 'repository')
    click.echo('Created repository successfully')
