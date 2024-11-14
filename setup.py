from setuptools import find_packages, setup
from typing import List

def get_requirements()->list[str]:
    requirements_list : list[str] = []
    return requirements_list

setup(
    name = 'Air Pressure Live Sensor Detection',
    version = '0.0.1',
    author = 'Sidhi Gupta',
    author_email = 'guptasidhi159@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements(),
)