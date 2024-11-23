import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='model:create'
)
@click.option('--name', default='', help='The name of the model', prompt="Enter the name of the model. es. Post")
def model_create_command(name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    pir_manager.generate_class(name, 'model')
    click.echo('Created model successfully')
