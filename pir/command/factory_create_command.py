import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='factory:create'
)
def factory_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    factory_name = click.prompt('Enter the name of the factory es. PostFactory')
    pir_manager.generate_class(factory_name, 'factory')
    click.echo('Created factory successfully')
