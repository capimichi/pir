import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='variable:create'
)
@click.option('--env_name', default='', help='The name of the environment associated with the variable')
def variable_create_command(env_name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    variable_name = click.prompt('Enter the name of the variable es. PostVariable')
    pir_manager.generate_class(
        class_name=variable_name,
        class_type='variable',
        env_name=env_name
    )
    click.echo('Created variable successfully')
