import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='manager:create'
)
def manager_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    manager_name = click.prompt('Enter the name of the manager es. PostManager')
    pir_manager.generate_class(manager_name, 'manager')
    click.echo('Created manager successfully')
