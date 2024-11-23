import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='model:create'
)
def model_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    model_name = click.prompt('Enter the name of the model es. PostModel')
    pir_manager.generate_class(model_name, 'model')
    click.echo('Created model successfully')
