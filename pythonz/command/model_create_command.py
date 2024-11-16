import os

import click

from pythonz.container.DefaultContainer import DefaultContainer


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

    dir = f"{start_dir}/{package_name}/model"
    os.makedirs(dir, exist_ok=True)

    path = f"{dir}/{model_name}.py"
    with open(path, 'w') as f:
        f.write(f"class {model_name}:\n")
        f.write(f"\tpass\n")

    click.echo('Created model successfully')
