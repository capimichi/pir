import click

from pythonz.command.init_command import init_command
from pythonz.command.controller_create_command import controller_create_command

@click.group()
def cli():
    pass

cli.add_command(init_command)
cli.add_command(controller_create_command)

if __name__ == '__main__':
    cli()