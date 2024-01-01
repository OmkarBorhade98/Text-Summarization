import os
from pathlib import Path
import logging

project_name = 'textSummarizer'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

files= [
    ".github/workflows/.gitkeep",
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yml',
    'params.yml',
    'app.py',
    'main.py',
    'setup.py',
    'environment.yml'
    'setup.py'
    'research/trials.ipynb'
]

for file in files:
    file = Path(file)
    filedir, filename = os.path.split(file)

    if (filedir != "") and (not os.path.exists(filedir)):
        os.makedirs(filedir, exist_ok= True)
        logging.info(f'Directory Created {filedir}')

    if(not os.path.exists(file)):
        with open(file, 'w') as f:
            pass
        logging.info(f'{filename} created at {filedir}')

    else:
        logging.info(f'{filename} already exists at {filedir}')