import os
from typing import Optional


class ClassHelper:

    @staticmethod
    def create_class_dir(path: str):
        dirname = os.path.dirname(path)
        os.makedirs(dirname, exist_ok=True)

        init_path = f"{dirname}/__init__.py"
        if (not os.path.exists(init_path)):
            with open(init_path, 'w') as f:
                pass


    @staticmethod
    def create_class(name: str, path: str, class_type: Optional[str] = None):
        class_str = f"class {name}"
        if class_type is not None:
            class_str += f"({class_type})"

        class_str += ":\n"
        class_str += "\tpass\n"

        with open(path, 'w') as f:
            f.write(class_str)