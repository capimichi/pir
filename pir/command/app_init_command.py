import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.manager.PirManager import PirManager


@click.command(
    name='app:init'
)
def cli_init_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)
    pir_manager.init_app()

    click.echo('Initialized app successfully')
