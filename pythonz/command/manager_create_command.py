import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper


@click.command(
    name='manager:create'
)
def manager_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()

    manager_name = click.prompt('Enter the name of the manager es. PostManager')
    manager_name = manager_name.replace('Manager', '').replace('manager', '').strip()
    manager_name = manager_name + 'Manager'

    package_name = default_container.get_config('name')
    start_dir = os.getcwd()

    path = f"{start_dir}/{package_name}/manager/{manager_name}.py"
    ClassHelper.create_class_dir(path)
    ClassHelper.create_class(path, manager_name)

    click.echo('Created manager successfully')
