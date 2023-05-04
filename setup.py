from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #it helps to read the package name one by one from requirements.txt
        requirements=[req.replace("\n","") for req in requirements]  # it helps to avoid the "/n" comes from readline function 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)   #it automatically remove the "-e." from requirements file because its not needed for "install requires"
    
    return requirements
setup(
    name='Student Performance',
    version='0.0.1',
    author='Biswajit Gochhayat',
    author_email='gochhayatbiswajit253@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)