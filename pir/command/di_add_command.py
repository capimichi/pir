import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='di:add'
)
def di_add_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    source_name = click.prompt('Enter the name of the source class es. PostService')
    target_name = click.prompt('Enter the name of the dependency class es. PostRepository')
    pir_manager.add_dependency(source_name, target_name)
    click.echo('Added dependency successfully')
