import os

import click

from pythonz.container.DefaultContainer import DefaultContainer


@click.command(
    name='container:init'
)
def container_init_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()

    package_name = default_container.get_config('name')
    start_dir = os.getcwd()