import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "test"

list_of_files = [
    "artifacts/data/.gitkeep",
    "artifacts/chroma/.gitkeep",    
    "artifacts/results/.gitkeep",
    
    "notebooks/trials.ipynb",

    # utils
    "utils/__init__.py",
    "utils/config.py",
    "utils/logger.py",
    "utils/server.py",
    "utils/common.py",
    
    "utils/rag/__init__.py",
    "utils/rag/get_models.py",
    "utils/rag/get_prompt.py",
    "utils/rag/populate.py",

    # main
    # "main.py",
    "app.py",

    # tests
    "tests/__init__.py",

    "params.yaml",
    "dvc.yaml",
]


for filepath in list_of_files:
    filepath = Path(filepath) #to solve the windows path issue
    filedir, filename = os.path.split(filepath) # to handle the project_name folder


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")