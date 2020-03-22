from setuptools import setup, find_packages

setup(
    name='solaria',
    version='0.0.3',
    entry_points={
        'console_scripts': [
            'scale = src.writing.environment.scale.cle_main:main',
            # 'solaria = src.reading.storyteller.main' or something
        ],
    },
    packages=find_packages(),  # NOTE what exactly does this do?
    install_requires=['networkx'],

    author='Casey Pancoast',
    description='A whole lot of things at the moment.',
    project_urls={
        'Source code': 'www.github.com/cqpancoast/solaria'
    },
)
