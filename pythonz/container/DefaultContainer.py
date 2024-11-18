import json
import logging
import os

from injector import Injector
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from vyper import v


class DefaultContainer:
    injector = None
    instance = None

    @staticmethod
    def getInstance():
        if DefaultContainer.instance is None:
            DefaultContainer.instance = DefaultContainer()
        return DefaultContainer.instance

    def __init__(self):
        self.injector = Injector()

        load_dotenv()

        self._init_environment_variables()
        self._init_directories()
        self._init_logging()
        self._init_bindings()
        self._init_vyper()

    def get(self, key):
        return self.injector.get(key)

    def get_var(self, key):
        return self.__dict__[key]

    def get_config(self, key):
        return v.get(key)

    def set_config(self, key, value):
        v.set(key, value)
        all_configs = v.all_settings()
        with open(self.config_file_path, 'w') as f:
            f.write(json.dumps(all_configs, indent=4))

    def _init_directories(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.config_file_path = os.path.join(os.getcwd(), 'pythonz.json')

        self.templates_dir = os.path.join(self.root_dir, "pythonz", 'templates')
        os.makedirs(self.templates_dir, exist_ok=True)

        # self.var_dir = os.path.join(self.root_dir, 'var')
        # os.makedirs(self.var_dir, exist_ok=True)
        # self.log_dir = os.path.join(self.var_dir, 'log')
        # os.makedirs(self.log_dir, exist_ok=True)
        # self.post_dir = os.path.join(self.var_dir, 'post')
        # os.makedirs(self.post_dir, exist_ok=True)
        # self.app_log_path = os.path.join(self.log_dir, 'app.log')

    def _init_environment_variables(self):
        self.pandoc_executable = os.environ.get('PANDOC_EXECUTABLE', 'pandoc')

    def _init_logging(self):
        pass
        # logging.basicConfig(filename=self.app_log_path, level=logging.INFO, filemode='a',
        #                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        #                     datefmt='%H:%M:%S')

    def _init_bindings(self):
        # self.injector.binder.bind(PostDirVariable, PostDirVariable(self.post_dir))
        env = Environment(loader=FileSystemLoader(self.templates_dir))
        self.injector.binder.bind(Environment, env)

    def _init_vyper(self):
        config_file_dir = os.path.dirname(self.config_file_path)
        v.add_config_path(config_file_dir)
        v.set_config_name("pythonz")
        v.set_config_type("json")
        if (os.path.exists(self.config_file_path)):
            v.read_in_config()
