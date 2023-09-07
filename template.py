'''
    Simple template for directory structure
'''
# Path: template.py
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]- %(levelname)s - %(message)s: ')

PROJECT_NAME = 'cnnClassifier'

list_of_files = {
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/compoents/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    ".github/workflows/.gitkeep",
    ".github/workflows/main.yml",
    "config/config.yaml",
    "dvc.yaml",
    "setup.py",
    "requirements.txt",
    "params.yaml",
    "research/trials.ipynb",
    "templates/index.html"
}

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir , filename = os.path.split(filepath)


    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info("Created %s", file_dir)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w', encoding='utf-8') as f:
            pass
        logging.info("Created %s", filepath)
