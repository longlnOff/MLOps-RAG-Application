from setuptools import setup, find_packages


# read the contents of requirements.txt
def read_requirements():
    with open('requirements.txt') as requirements:
        return requirements.read().splitlines()

requirements = read_requirements()

setup(
    name='MLOps-RAG-Chatbot',
    version='1.0',
    packages=find_packages(),
    install_requires=requirements
)