import os

import inflection
from injector import inject
from jinja2 import Environment
from redbaron import RedBaron

from pythonz.container.DefaultContainer import DefaultContainer


class PythonzManager:
    environment: Environment

    handled_types = ['controller', 'service', 'repository', 'entity', 'helper', 'manager', 'factory', 'model', 'client', 'config', 'exception', 'view', 'variable']

    @inject
    def __init__(self, environment: Environment):
        self.environment = environment

    def generate_class(self, class_name: str, class_type: str):

        default_container: DefaultContainer = DefaultContainer.getInstance()

        for handled_type in self.handled_types:
            uc_handled_type = handled_type.capitalize()
            if class_type == handled_type:
                class_name = class_name.replace(uc_handled_type, '').replace(handled_type, '').strip()
                class_name = class_name + uc_handled_type
                break

        parent_type = ""
        if(class_type == 'variable'):
            parent_type = 'str'


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

        template = self.environment.get_template(f"default_class.jinja.py")
        content = template.render(class_name=class_name, parent_type=parent_type)

        with open(path, 'w') as f:
            f.write(content)

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

        template = self.environment.get_template(f"default_command.jinja.py")
        content = template.render(command_name=command_name, command_alias=command_alias)

        with open(path, 'w') as f:
            f.write(content)

    def add_dependency(self, source_class_name, target_class_name):
        default_container: DefaultContainer = DefaultContainer.getInstance()
        package_name = default_container.get_config('name')
        start_dir = os.getcwd()

        source_type = ""
        for handled_type in self.handled_types:
            if(handled_type in source_class_name.lower()):
                source_type = handled_type
                break

        target_type = ""
        for handled_type in self.handled_types:
            if(handled_type in target_class_name.lower()):
                target_type = handled_type
                break

        source_path = f"{start_dir}/{package_name}/{source_type}/{source_class_name}.py"
        with open(source_path, 'r') as f:
            content = f.read()
            import_str = f"from {package_name}.{target_type}.{target_class_name} import {target_class_name}"
            if import_str not in content:
                content = import_str + "\n" + content

            property_name = inflection.underscore(target_class_name)

            red = RedBaron(content)
            constructor = red.find("DefNode", name="__init__")
            constructor.arguments.append(property_name + ": " + target_class_name + "\n")
            constructor.value.append("self." + property_name + " = " + property_name)
            constructor.insert_before(property_name + ": " + target_class_name + "\n\n")

            with open(source_path, 'w') as f:
                f.write(red.dumps())

