from setuptools import setup, find_packages

setup(
    name="pythonz",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "pythonz=pythonz.cli:cli",
        ],
    },
    url="https://github.com/capimichi/pythonz",
    author="Michele Capicchioni",
    author_email="capimichi@gmail.com",
    description="Pythonz is a simple CLI tool to generate Python classes",
)
