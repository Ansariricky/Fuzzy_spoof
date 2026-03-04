from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path)->List[str]:
    '''
    This function reads the requirements from a file and returns them as a list.
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n', ' ') for req in requirements if req.strip() and not req.startswith('#')]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
    
setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Ricky',
    description='A sample Python package',
)