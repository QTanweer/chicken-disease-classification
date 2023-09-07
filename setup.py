"""
    creating a custom setup tool 
"""

import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "chicken-disease-classification"
AUTHOR_USER_NAME = "QTanweer"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "qtanweer.mts41ceme@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small cnn package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"www.github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"}
)
