from setuptools import find_packages ,setup
from typing import List

const="-e."

def get_requirements(file_path:str)->List[str]:
    """This function takes a file path as input, reads the file and returns a list of requirements"""
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","")for req in requirements]
    if const in requirements:
        requirements.remove(const)
    return requirements



setup(
    name='studentmarksprediction',
    version='0.0.1',
    author="Hansal",
    author_email="bhangalehansal@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)