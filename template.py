import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s : %(message)s]'
)

PROJECT_NAME = "CNN_Classifier"

listOfFiles=[
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py"
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
]

for path in listOfFiles:
    path = Path(path)
    file_dir,filename = os.path.split(path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Createing File Directory '{file_dir}' for filename '{filename}'.")


    elif (not os.path.exists(path)) or (os.path.getsize(path)==0):
        with open(path,"w") as f :
            pass
            logging.info(f"Creating Empty file {path}.")

    else :
        logging.info(f"{filename} already exists.")
  