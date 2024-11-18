import click

from pythonz.command.init_command import init_command
from pythonz.command.controller_create_command import controller_create_command
from pythonz.command.client_create_command import client_create_command
from pythonz.command.repository_create_command import repository_create_command
from pythonz.command.service_create_command import service_create_command
from pythonz.command.view_create_command import view_create_command
from pythonz.command.entity_create_command import entity_create_command
from pythonz.command.factory_create_command import factory_create_command
from pythonz.command.helper_create_command import helper_create_command
from pythonz.command.manager_create_command import manager_create_command
from pythonz.command.model_create_command import model_create_command
from pythonz.command.variable_create_command import variable_create_command
from pythonz.command.command_create_command import command_create_command
from pythonz.command.di_add_command import di_add_command
from pythonz.command.container_init_command import container_init_command

@click.group()
def cli():
    pass

cli.add_command(init_command)
cli.add_command(controller_create_command)
cli.add_command(client_create_command)
cli.add_command(repository_create_command)
cli.add_command(service_create_command)
cli.add_command(view_create_command)
cli.add_command(entity_create_command)
cli.add_command(factory_create_command)
cli.add_command(helper_create_command)
cli.add_command(manager_create_command)
cli.add_command(model_create_command)
cli.add_command(variable_create_command)
cli.add_command(command_create_command)
cli.add_command(di_add_command)
cli.add_command(container_init_command)

if __name__ == '__main__':
    cli()