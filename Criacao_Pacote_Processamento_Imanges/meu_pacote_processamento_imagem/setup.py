from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento_de_imagens",
    version="0.0.1",
    author="Thiago",
    author_email="thiago@terra.com.br",
    description="Pacote de processamento de Imagens utilizando Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)