import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='view:create'
)
def view_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    view_name = click.prompt('Enter the name of the view es. PostView')
    pir_manager.generate_class(view_name, 'view')
    click.echo('Created view successfully')
