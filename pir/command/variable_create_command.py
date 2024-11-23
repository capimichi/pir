import os

import click

from pir.container.DefaultContainer import DefaultContainer
from pir.helper.ClassHelper import ClassHelper
from pir.manager.PirManager import PirManager


@click.command(
    name='variable:create'
)
@click.option('--name', default='', help='The name of the variable', prompt="Enter the name of the variable. es. PostVariable")
@click.option('--env_name', default='', help='The name of the environment associated with the variable')
def variable_create_command(name: str, env_name: str):
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pir_manager: PirManager = default_container.get(PirManager)

    pir_manager.generate_class(
        class_name=name,
        class_type='variable',
        env_name=env_name
    )
    click.echo('Created variable successfully')
