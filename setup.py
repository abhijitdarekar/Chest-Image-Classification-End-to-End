import setuptools
from setuptools import find_packages,setup



def get_packages(filename):
    with open(filename,'r') as f:
        packages = f.readlines()

    return get_packages

__version__ = "0.0.0"

REPO_NAME = 'Chest-Image-Classification-End-to-End'
AUTHOR_NAME = 'abhijitdarekar'
SRC_REPO = "CNN_Classifier"
EMAIL = "darekarabhijit63@gmail.com"

setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=EMAIL,
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=find_packages(where='src')
)