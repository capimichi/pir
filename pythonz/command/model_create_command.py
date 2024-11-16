import os

import click

from pythonz.container.DefaultContainer import DefaultContainer
from pythonz.helper.ClassHelper import ClassHelper


@click.command(
    name='model:create'
)
def model_create_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()

    model_name = click.prompt('Enter the name of the model es. PostModel')
    model_name = model_name.replace('Model', '').replace('model', '').strip()
    model_name = model_name + 'Model'

    package_name = default_container.get_config('name')
    start_dir = os.getcwd()

    path = f"{start_dir}/{package_name}/model/{model_name}.py"
    ClassHelper.create_class_dir(path)
    ClassHelper.create_class(path, model_name)

    click.echo('Created model successfully')
