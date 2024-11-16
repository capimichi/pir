import os

import click

from pythonz.container.DefaultContainer import DefaultContainer


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

    dir = f"{start_dir}/{package_name}/controller"
    os.makedirs(dir, exist_ok=True)

    path = f"{dir}/{controller_name}.py"
    with open(path, 'w') as f:
        f.write(f"class {controller_name}:\n")
        f.write(f"\tpass\n")

    click.echo('Created controller successfully')
