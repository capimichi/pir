import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='repository:create'
)
def repository_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    repository_name = click.prompt('Enter the name of the repository es. PostRepository')
    pir_manager.generate_class(repository_name, 'repository')
    click.echo('Created repository successfully')
