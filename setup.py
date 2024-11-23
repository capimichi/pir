from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="pir",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,  # Include i file extra definiti in MANIFEST.in
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "pir=pir.cli:cli",
        ],
    },
    url="https://github.com/capimichi/pir",
    author="Michele Capicchioni",
    author_email="capimichi@gmail.com",
    description="Pir is a simple CLI tool to generate Python classes",
)
