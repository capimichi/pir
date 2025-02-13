# pir
Python helper for my projects

## Why pir
Pir is a simple CLI tool designed to help you generate Python classes quickly and efficiently. It streamlines the process of creating various components such as controllers, clients, repositories, services, views, entities, factories, helpers, managers, models, variables, commands, and dependency injection configurations.

## Installation
To install pir, simply clone the repository and install the required dependencies:
```bash
pip install git+https://github.com/capimichi/pir.git
```

## Usage
The first command to launch is pir:init to create the namespace for the project.
```bash
pir init
```

This will create a file pir.json in the current directory. This file will contain the namespace of the project and the path of the project.

Then you can proceed with the other commands.

## Commands
Pir provides a variety of commands to generate different components. Here are the available commands:

### `init_command`
Initialize a new project.
```bash
pir container:init
```

### `controller_create_command`
Create a new controller.
```bash
pir controller:create --name <controller_name> --entity_name <entity_name>
```
- `--name`: The name of the controller.
- `--entity_name`: The name of the entity associated with the controller.

### `client_create_command`
Create a new client.
```bash
pir client:create --name <client_name> --entity_name <entity_name>
```
- `--name`: The name of the client.
- `--entity_name`: The name of the entity associated with the client.

### `repository_create_command`
Create a new repository.
```bash
pir repository:create --name <repository_name>
```
- `--name`: The name of the repository.

### `service_create_command`
Create a new service.
```bash
pir service:create --name <service_name>
```
- `--name`: The name of the service.

### `view_create_command`
Create a new view.
```bash
pir view:create --name <view_name>
```
- `--name`: The name of the view.

### `entity_create_command`
Create a new entity.
```bash
pir entity:create --name <entity_name>
```
- `--name`: The name of the entity.

### `factory_create_command`
Create a new factory.
```bash
pir factory:create --name <factory_name>
```
- `--name`: The name of the factory.

### `helper_create_command`
Create a new helper.
```bash
pir helper:create --name <helper_name>
```
- `--name`: The name of the helper.

### `manager_create_command`
Create a new manager.
```bash
pir manager:create --name <manager_name>
```
- `--name`: The name of the manager.

### `model_create_command`
Create a new model.
```bash
pir model:create --name <model_name>
```
- `--name`: The name of the model.

### `variable_create_command`
Create a new variable.
```bash
pir variable:create --name <variable_name>
```
- `--name`: The name of the variable.

### `command_create_command`
Create a new command.
```bash
pir command:create --name <command_name> --command_alias <command_alias>
```
- `--name`: The name of the command.
- `--command_alias`: The alias of the command.

### `di_add_command`
Add dependency injection configuration.
```bash
pir di:add
```
- Prompts for the source class name and the dependency class name.

### `container_init_command`
Initialize a new container.
```bash
pir container:init
```

For detailed usage of each command, you can run:
```bash
pir <command> --help
```
