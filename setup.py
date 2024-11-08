##how the opackages are  created
# this setup.py will be responsile in creating my machine learning application as a package
# and deploy in pypy
from setuptools import find_packages,setup
# fort he lsit to be recognised we ewilll be improting below
from typing import List

# condiotn to remove" -e" from the reqioremetn as it will a,so be these
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this functionnwilll return the list of requirements
'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name="mlprojects",
version="0.0.1",
author="tannu",
author_email="guptatannugupta3@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


           # it is not feasible to write all the requirements
           #        



)