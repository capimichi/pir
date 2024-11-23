import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='command:create'
)
@click.option('--name', default='', help='The name of the command', prompt="Enter the name of the command. es. create_post_command")
@click.option('--command_alias', default='', help='The alias of the command', prompt="Enter the alias of the command. es. create:post")
def command_create_command(name: str, command_alias: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    pir_manager.generate_command(name, command_alias)
    click.echo('Created command successfully')
