import os

import inflection
from injector import inject
from jinja2 import Environment
from redbaron import RedBaron

from pir.container.DefaultContainer import DefaultContainer


class PirManager:
    environment: Environment

    handled_types = ['controller', 'service', 'repository', 'entity', 'helper', 'manager', 'factory', 'model', 'client',
                     'config', 'exception', 'view', 'variable']

    @inject
    def __init__(self, environment: Environment):
        self.environment = environment

    def generate_class(self, class_name: str, class_type: str, entity_name: str = "", env_name: str = ""):

        default_container: DefaultContainer = DefaultContainer.getInstance()

        for handled_type in self.handled_types:
            uc_handled_type = handled_type.capitalize()
            if class_type == handled_type:
                class_name = class_name.replace(uc_handled_type, '').replace(handled_type, '').strip()
                class_name = class_name + uc_handled_type
                break

        if(class_name.endswith('Model')):
            class_name = class_name.replace('Model', '')


        template_name = "default_class.jinja"
        if (class_type == 'variable'):
            template_name = "variable_class.jinja"

        package_name = default_container.get_config('name')
        start_dir = os.getcwd()

        path = f"{start_dir}/{package_name}/{class_type}/{class_name}.py"

        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        init_path = f"{dirname}/__init__.py"
        if not os.path.exists(init_path):
            with open(init_path, 'w') as f:
                f.write('')

        snake_case_entity_name = ""
        if (len(entity_name) == 0):
            entity_name = None

        if (entity_name):
            snake_case_entity_name = inflection.underscore(entity_name)

        template = self.environment.get_template(template_name)
        content = template.render(
            class_name=class_name,
            parent_type=None,
            entity_name=entity_name,
            snake_case_entity_name=snake_case_entity_name
        )

        with open(path, 'w') as f:
            f.write(content)

        if (len(env_name) > 0):

            env_example_path = f"{start_dir}/.env.example"
            if not os.path.exists(env_example_path):
                with open(env_example_path, 'w') as f:
                    f.write('')

            with open(env_example_path, 'r') as f:
                env_example_content = f.read()
            if not env_name in env_example_content:
                with open(env_example_path, 'a') as f:
                    f.write(f"{env_name}=\n")

            default_container_path = f"{start_dir}/{package_name}/container/DefaultContainer.py"
            with open(default_container_path, 'r') as f:
                default_container_content = f.read()

            import_str = f"from {package_name}.variable.{class_name} import {class_name}"
            if import_str not in default_container_content:
                default_container_content = import_str + "\n" + default_container_content

            red = RedBaron(default_container_content)

            # search method _init_environment_variables
            init_environment_variables = red.find("DefNode", name="_init_environment_variables")

            for node in init_environment_variables.value:
                if node.type == "pass":
                    init_environment_variables.value.remove(node)

            env_name = inflection.underscore(env_name).upper()
            env_name = env_name.replace(' ', '_')
            env_name = env_name.replace('-', '_')
            env_name = env_name.replace('.', '_')
            env_name = env_name.replace(':', '_')
            env_name_lower = env_name.lower()
            init_environment_variables.value.append(f"self.{env_name_lower} = os.getenv('{env_name}')\n")

            init_bindings = red.find("DefNode", name="_init_bindings")

            for node in init_bindings.value:
                if node.type == "pass":
                    init_bindings.value.remove(node)

            init_bindings.value.append(f"self.injector.binder.bind({class_name}, {class_name}(self.{env_name_lower}))\n")

            with open(default_container_path, 'w') as f:
                f.write(red.dumps())

    def generate_command(self, command_name, command_alias):
        default_container: DefaultContainer = DefaultContainer.getInstance()
        package_name = default_container.get_config('name')
        start_dir = os.getcwd()

        path = f"{start_dir}/{package_name}/command/{command_name}.py"

        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        init_path = f"{dirname}/__init__.py"
        if not os.path.exists(init_path):
            with open(init_path, 'w') as f:
                f.write('')

        template = self.environment.get_template(f"default_command.jinja")
        content = template.render(command_name=command_name, command_alias=command_alias)

        with open(path, 'w') as f:
            f.write(content)

    def add_dependency(self, source_class_name, target_class_name):
        default_container: DefaultContainer = DefaultContainer.getInstance()
        package_name = default_container.get_config('name')
        start_dir = os.getcwd()

        source_type = ""
        for handled_type in self.handled_types:
            if(source_class_name.lower().endswith(handled_type)):
                source_type = handled_type
                break

        if(source_type == ""):
            source_type = "model"
            if not os.path.exists(f"{start_dir}/{package_name}/{source_type}/{source_class_name}.py"):
                raise Exception(f"Source class {source_class_name} not found")

        target_type = ""
        for handled_type in self.handled_types:
            if(target_class_name.lower().endswith(handled_type)):
                target_type = handled_type
                break

        if(target_type == ""):
            target_type = "model"
            if not os.path.exists(f"{start_dir}/{package_name}/{target_type}/{target_class_name}.py"):
                raise Exception(f"Target class {target_class_name} not found")

        source_path = f"{start_dir}/{package_name}/{source_type}/{source_class_name}.py"
        with open(source_path, 'r') as f:
            content = f.read()
            import_str = f"from {package_name}.{target_type}.{target_class_name} import {target_class_name}"
            if import_str not in content:
                content = import_str + "\n" + content

            property_name = inflection.underscore(target_class_name)

            red = RedBaron(content)
            constructor = red.find("DefNode", name="__init__")

            for node in constructor.value:
                if node.type == "pass":
                    constructor.value.remove(node)

            if(property_name.endswith('_variable')):
                property_name = property_name.replace('_variable', '')

            constructor.arguments.append(property_name + ": " + target_class_name + "\n")
            constructor.value.append("self." + property_name + " = " + property_name)
            constructor.insert_before(property_name + ": " + target_class_name + "\n\n")

            with open(source_path, 'w') as f:
                f.write(red.dumps())

    def init_container(self):
        default_container: DefaultContainer = DefaultContainer.getInstance()
        package_name = default_container.get_config('name')
        start_dir = os.getcwd()

        path = f"{start_dir}/{package_name}/container/DefaultContainer.py"

        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        package_init_path = f"{start_dir}/{package_name}/__init__.py"
        if not os.path.exists(package_init_path):
            with open(package_init_path, 'w') as f:
                f.write('')

        init_path = f"{dirname}/__init__.py"
        if not os.path.exists(init_path):
            with open(init_path, 'w') as f:
                f.write('')

        template = self.environment.get_template(f"default_container.jinja")
        content = template.render()

        with open(path, 'w') as f:
            f.write(content)

    def init_cli(self):
        default_container: DefaultContainer = DefaultContainer.getInstance()
        package_name = default_container.get_config('name')
        start_dir = os.getcwd()

        path = f"{start_dir}/{package_name}/cli.py"

        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        init_path = f"{dirname}/__init__.py"
        if not os.path.exists(init_path):
            with open(init_path, 'w') as f:
                f.write('')

        template = self.environment.get_template(f"default_cli.jinja")
        content = template.render()

        with open(path, 'w') as f:
            f.write(content)

    def init_app(self):
        default_container: DefaultContainer = DefaultContainer.getInstance()
        package_name = default_container.get_config('name')
        start_dir = os.getcwd()

        path = f"{start_dir}/{package_name}/app.py"

        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        init_path = f"{dirname}/__init__.py"
        if not os.path.exists(init_path):
            with open(init_path, 'w') as f:
                f.write('')

        template = self.environment.get_template(f"default_app.jinja")
        content = template.render()

        with open(path, 'w') as f:
            f.write(content)
