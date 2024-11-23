import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='helper:create'
)
@click.option('--name', default='', help='The name of the helper',
              prompt="Enter the name of the helper. es. PostHelper")
def helper_create_command(name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    pir_manager.generate_class(
        name,
        'helper'
    )
    click.echo('Created helper successfully')
