import os

import click

from pythonz.container.DefaultContainer import DefaultContainer


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

    dir = f"{start_dir}/{package_name}/helper"
    os.makedirs(dir, exist_ok=True)

    path = f"{dir}/{helper_name}.py"
    with open(path, 'w') as f:
        f.write(f"class {helper_name}:\n")
        f.write(f"\tpass\n")

    click.echo('Created helper successfully')
