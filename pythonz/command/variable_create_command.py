import os

import click

from pythonz.container.DefaultContainer import DefaultContainer


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

    dir = f"{start_dir}/{package_name}/variable"
    os.makedirs(dir, exist_ok=True)

    init_path = f"{dir}/__init__.py"
    if (not os.path.exists(init_path)):
        with open(init_path, 'w') as f:
            pass

    path = f"{dir}/{variable_name}.py"
    with open(path, 'w') as f:
        f.write(f"class {variable_name}(str):\n")
        f.write(f"\tpass\n")

    click.echo('Created variable successfully')
