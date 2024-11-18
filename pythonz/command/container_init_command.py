import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.manager.PythonzManager import PythonzManager


@click.command(
    name='container:init'
)
def container_init_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    pythonz_manager: PythonzManager = default_container.get(PythonzManager)
    pythonz_manager.init_container()