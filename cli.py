import click

from pythonz.command.init_command import init_command

@click.group()
def cli():
    pass

cli.add_command(init_command)
# cli.add_command(command2)
# cli.add_command(command3)

if __name__ == '__main__':
    cli()