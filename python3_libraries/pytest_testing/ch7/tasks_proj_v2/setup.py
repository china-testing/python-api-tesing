"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='tasks',
    version='0.1.1',
    license='proprietary', 
    description='Minimal Project Task Management',

    author='Brian Okken',
    author_email='Please use pythontesting.net contact form.',
    url='https://pragprog.com/book/bopytest',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['click', 'tinydb', 'six', 'pytest', 'pytest-mock'],
    tests_require=['pytest', 'pytest-mock'],
    extras_require={'mongo': 'pymongo'},

    entry_points={
        'console_scripts': [
            'tasks = tasks.cli:tasks_cli',
        ]
    },
)
