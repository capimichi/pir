import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='helper:create'
)
def helper_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    helper_name = click.prompt('Enter the name of the helper es. PostHelper')
    pir_manager.generate_class(helper_name, 'helper')
    click.echo('Created helper successfully')
