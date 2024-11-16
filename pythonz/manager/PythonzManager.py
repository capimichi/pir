import os

from jinja2 import Environment

from pythonz.container.DefaultContainer import DefaultContainer


class PythonzManager:
    environment: Environment

    def __init__(self, environment: Environment):
        self.environment = environment

    def generate_class(self, class_name: str, class_type: str):

        default_container: DefaultContainer = DefaultContainer.getInstance()

        handled_types = ['controller', 'service', 'repository', 'entity', 'helper', 'manager', 'command', 'factory', 'model', 'client', 'config', 'exception', 'view', 'variable']

        for handled_type in handled_types:
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

        template = self.environment.get_template(f"default_class.jinja")
        content = template.render(class_name=class_name, parent_type=parent_type)

        with open(path, 'w') as f:
            f.write(content)
