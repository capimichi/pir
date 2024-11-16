import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper


@click.command(
    name='variable:create'
)
def variable_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()

    variable_name = click.prompt('Enter the name of the variable es. PostVariable')
    variable_name = variable_name.replace('Variable', '').replace('variable', '').strip()
    variable_name = variable_name + 'Variable'

    package_name = default_container.get_config('name')
    start_dir = os.getcwd()

    path = f"{start_dir}/{package_name}/variable/{variable_name}.py"
    ClassHelper.create_class_dir(path)
    ClassHelper.create_class(path, variable_name, 'str')

    click.echo('Created variable successfully')
