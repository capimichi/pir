import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper


@click.command(
    name='controller:create'
)
def controller_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()

    controller_name = click.prompt('Enter the name of the controller es. PostController')
    controller_name = controller_name.replace('Controller', '').replace('controller', '').strip()
    controller_name = controller_name + 'Controller'

    package_name = default_container.get_config('name')
    start_dir = os.getcwd()

    path = f"{start_dir}/{package_name}/controller/{controller_name}.py"
    ClassHelper.create_class_dir(path)
    ClassHelper.create_class(path, controller_name)

    click.echo('Created controller successfully')
