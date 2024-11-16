import os

import click

from pythonz.container.DefaultContainer import DefaultContainer


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

    dir = f"{start_dir}/{package_name}/manager"
    os.makedirs(dir, exist_ok=True)

    init_path = f"{dir}/__init__.py"
    if (not os.path.exists(init_path)):
        with open(init_path, 'w') as f:
            pass

    path = f"{dir}/{manager_name}.py"
    with open(path, 'w') as f:
        f.write(f"class {manager_name}:\n")
        f.write(f"\tpass\n")

    click.echo('Created manager successfully')
