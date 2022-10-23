import re
from setuptools import setup, find_packages

with open('src/pypkgsample/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pypkgsample',
    version=version,
    license='None',
    description='Python Package Sample',
    long_description = long_description,
    author='mkyutani@gmail.com',
    url='http://github.com/mkyutani/python-package-sample',
    packages=find_packages(where='src'),
    package_dir={ '': 'src' },
    install_requires=open('requirements.txt').read().splitlines(),
    keywords='python package sample',
    entry_points={
        'console_scripts': [
            'pypkgsample=pypkgsample:main',
        ],
    },
    zip_safe=False
)
