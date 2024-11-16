import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper


@click.command(
    name='helper:create'
)
def helper_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()

    helper_name = click.prompt('Enter the name of the helper es. PostHelper')
    helper_name = helper_name.replace('Helper', '').replace('helper', '').strip()
    helper_name = helper_name + 'Helper'

    package_name = default_container.get_config('name')
    start_dir = os.getcwd()

    path = f"{start_dir}/{package_name}/helper/{helper_name}.py"
    ClassHelper.create_class_dir(path)
    ClassHelper.create_class(path, helper_name)

    click.echo('Created helper successfully')
