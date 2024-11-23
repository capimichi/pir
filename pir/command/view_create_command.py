import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='view:create'
)
@click.option('--name', default='', help='The name of the view', prompt="Enter the name of the view. es. PostView")
def view_create_command(name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    pir_manager.generate_class(
        name,
        'view'
    )
    click.echo('Created view successfully')
