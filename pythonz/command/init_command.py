import click

from pythonz.container.DefaultContainer import DefaultContainer


@click.command(
    name='init'
)
def init_command():
    default_container: DefaultContainer = DefaultContainer.getInstance()
    package_name = click.prompt('Enter the name of the package')
    default_container.set_config('name', package_name)
    click.echo('Successfully initialized the package')
