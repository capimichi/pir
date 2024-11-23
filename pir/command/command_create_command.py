import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='command:create'
)
def command_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    command_name = click.prompt('Enter the name of the command es. create_post_command')
    command_alias = click.prompt('Enter the alias of the command es. post:create')
    pir_manager.generate_command(command_name, command_alias)
    click.echo('Created command successfully')
